from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
from dotenv import load_dotenv

# 📌 .env dosyasını yükle
load_dotenv()
api_key = os.getenv('YOUTUBE_API_KEY')  # .env dosyasından API anahtarını oku

# 📌 Eğer .env içinde API anahtarı yoksa uyarı ver ve programı kapat
if not api_key:
    print("❌ HATA: API anahtarı bulunamadı! .env dosyanı kontrol et.")
    exit()  # Programı durdur

# 📌 YouTube API'yi başlat
youtube = build('youtube', 'v3', developerKey=api_key)

# 📌 Kanal ID'si (Elraenn için)
channel_id = "UC51-ljNFrvY5ZmV0C_61XcA"

def get_uploads_playlist_id(channel_id):
    """Belirtilen kanalın yükleme oynatma listesinin ID'sini döndürür."""
    try:
        # 📌 API isteği yap
        request = youtube.channels().list(
            part="contentDetails",
            id=channel_id
        )
        response = request.execute()

        # 📌 Eğer kanalın yükleme oynatma listesi bulunamazsa
        if 'items' not in response or len(response['items']) == 0:
            print("❌ HATA: Kanal ID geçersiz veya kanalın yüklemeleri yok.")
            return None

        # 📌 Kanalın yükleme oynatma listesini al
        playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        print(f"✅ Yükleme oynatma listesi ID'si: {playlist_id}")
        return playlist_id

    except HttpError as e:
        print(f"❌ YouTube API Hatası: {e}")
        return None
    except KeyError:
        print("❌ HATA: Geçersiz kanal ID veya kanalın yüklemeleri bulunamadı.")
        return None
    except Exception as e:
        print(f"❌ Beklenmedik bir hata oluştu: {e}")
        return None

# 📌 Playlist ID'yi alma işlemini gerçekleştir
playlist_id = get_uploads_playlist_id(channel_id)

# 📌 Eğer playlist ID bulunamazsa programı durdur
if not playlist_id:
    print("⚠️ HATA: Playlist ID bulunamadı. Lütfen kanal ID'yi kontrol edin!")
    exit()
