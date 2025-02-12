from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
from dotenv import load_dotenv

# .env dosyasını yükle (Eğer kullanıyorsan)
load_dotenv()
api_key = os.getenv('YOUTUBE_API_KEY')  # .env içinden API anahtarını al

# Eğer .env dosyan yoksa, doğrudan API anahtarını kullanabilirsin:
if not api_key:
    api_key = ""  # API anahtarını buraya yazabilirsin

# YouTube API'yi başlat
youtube = build('youtube', 'v3', developerKey=api_key)

# Kanal ID'si (Elraenn için güncellenmiş)
channel_id = "UC51-ljNFrvY5ZmV0C_61XcA"

def get_uploads_playlist_id(channel_id):
    """Belirtilen kanalın yükleme oynatma listesinin ID'sini döndürür."""
    try:
        # API isteği yap
        request = youtube.channels().list(
            part="contentDetails",
            id=channel_id
        )
        response = request.execute()

        # Kanalın yükleme oynatma listesini al
        playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        print(f"✅ Yükleme oynatma listesi ID'si: {playlist_id}")
        return playlist_id

    except HttpError as e:
        print(f"❌ YouTube API Hatası: {e}")
        return None
    except KeyError:
        print("❌ Geçersiz kanal ID veya kanalın yüklemeleri bulunamadı.")
        return None
    except Exception as e:
        print(f"❌ Beklenmedik bir hata oluştu: {e}")
        return None

# Playlist ID'yi alma işlemini gerçekleştir
playlist_id = get_uploads_playlist_id(channel_id)

if not playlist_id:
    print("⚠️ Playlist ID bulunamadı. Lütfen kanal ID'yi kontrol edin!")
