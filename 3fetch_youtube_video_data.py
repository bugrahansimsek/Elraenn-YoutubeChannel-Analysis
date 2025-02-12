from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd
import isodate
import time
import os
from dotenv import load_dotenv
from tqdm import tqdm
from datetime import datetime

# 1. API Key Güvenliği
load_dotenv()
api_key = os.getenv('YOUTUBE_API_KEY')  # .env dosyasından oku

# 2. YouTube API Hizmeti
youtube = build('youtube', 'v3', developerKey=api_key)

def get_all_video_ids(playlist_id):
    """Tüm video ID'leri toplar"""
    video_ids = []
    next_page_token = None
    
    with tqdm(desc="Video ID'leri Toplanıyor") as pbar:
        while True:
            try:
                request = youtube.playlistItems().list(
                    part='contentDetails',
                    playlistId=playlist_id,
                    maxResults=50,
                    pageToken=next_page_token
                )
                response = request.execute()
                
                video_ids.extend([
                    item['contentDetails']['videoId'] 
                    for item in response['items']
                ])
                
                next_page_token = response.get('nextPageToken')
                pbar.update(len(response['items']))
                
                if not next_page_token:
                    break
                    
                # API rate limiting
                time.sleep(1)  
                
            except HttpError as e:
                print(f"API Hatası: {e}")
                break
                
    return video_ids

def get_video_details(video_ids):
    """Video detaylarını batch olarak alır"""
    video_data = []
    
    for i in tqdm(range(0, len(video_ids), 50), desc="Video Detayları Alınıyor"):
        batch = video_ids[i:i+50]
        
        try:
            request = youtube.videos().list(
                part='snippet,statistics,contentDetails',
                id=','.join(batch)
            )
            response = request.execute()
            
            for video in response['items']:
                stats = video.get('statistics', {})
                details = video.get('contentDetails', {})
                snippet = video.get('snippet', {})

                # 2. Yayınlanma Tarihini Gün/Ay/Yıl - Saat Formatına Çevir
                published_at = snippet.get('publishedAt', None)
                if published_at:
                    published_at = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")
                    formatted_published_at = published_at.strftime("%d/%m/%Y - %H:%M")
                else:
                    formatted_published_at = "Bilinmiyor"

                # 3. Video Süresi & Türü Belirleme (Shorts/VİDEO)
                duration = details.get('duration', "PT0S")
                duration_seconds = isodate.parse_duration(duration).total_seconds()
                video_type = "SHORTS" if duration_seconds <= 60 else "VİDEO"

                # 4. Video Kategorisini Alma
                category_id = snippet.get('categoryId', "Bilinmiyor")
                category_name = get_video_category(category_id)  # Aşağıda fonksiyonunu ekledik

                video_data.append({
                    'Video_ID': video['id'],
                    'Title': snippet.get('title', "Bilinmiyor"),
                    'Published_At': formatted_published_at,  # Gün/Ay/Yıl - Saat
                    'Views': int(stats.get('viewCount', 0)),
                    'Likes': int(stats.get('likeCount', 0)),
                    'Comments': int(stats.get('commentCount', 0)),
                    'Duration': int(duration_seconds),
                    'Video_Type': video_type,  # Shorts veya Video
                    'Category': category_name,  # Video Kategorisi
                    'Video_URL': f"https://www.youtube.com/watch?v={video['id']}"
                })
                
            time.sleep(1)  # Rate limiting
            
        except HttpError as e:
            print(f"Batch hatası: {e}")
            continue
            
    return video_data

def get_video_category(category_id):
    """Kategori ID'sini kategori adına çevirir"""
    try:
        request = youtube.videoCategories().list(
            part="snippet",
            id=category_id
        )
        response = request.execute()
        
        if 'items' in response and len(response['items']) > 0:
            return response['items'][0]['snippet']['title']
        else:
            return "Bilinmiyor"
    except Exception as e:
        print(f"Kategori çekme hatası: {e}")
        return "Bilinmiyor"

# Ana işlem
if __name__ == "__main__":
    playlist_id = 'UU51-ljNFrvY5ZmV0C_61XcA'
    
    try:
        # Video ID'lerini çek
        all_ids = get_all_video_ids(playlist_id)
        data = get_video_details(all_ids)
        
        # Veri Çerçevesi (DataFrame) oluştur ve kaydet
        df = pd.DataFrame(data)
        df.to_csv('youtube_analytics.csv', index=False, encoding='utf-8-sig')
        
        print(f"\n✅ Toplam {len(df)} video kaydedildi")
        print("📊 Temel İstatistikler:")
        print(df[['Views','Likes','Comments']].describe())
        
    except Exception as e:
        print(f"Kritik hata: {e}")
