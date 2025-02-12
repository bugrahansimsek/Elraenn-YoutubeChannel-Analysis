import requests
import json
import os
import pandas as pd
import re
from rapidfuzz import process

# ✅ Steam API ve Dosya Yolu Tanımları
steam_games_file = ""  # Steam API'den çekilen oyun listesinin saklanacağı JSON dosyası
youtube_csv_file = ""  # YouTube videolarının analiz edilmek üzere saklandığı CSV dosyası
output_csv_file = ""  # Eşleşmiş oyun isimlerinin kaydedileceği güncellenmiş CSV dosyası
steam_api_url = ""  # Steam API'nin kullanacağı URL


# ✅ Steam API'den oyun listesini çek ve JSON dosyasına kaydet
def fetch_and_save_steam_games():
    """Steam API'den oyun listesini çeker ve JSON dosyasına kaydeder."""
    print("🔄 Steam API'ye istek yapılıyor...")
    response = requests.get(steam_api_url, timeout=15)  # 15 saniye timeout
    
    if response.status_code == 200:
        print("✅ Steam API başarıyla cevap verdi.")
        app_list = response.json()["applist"]["apps"]
        print(f"🔹 Toplam {len(app_list)} oyun çekildi.")

        # JSON dosyasına kaydet
        with open(steam_games_file, "w", encoding="utf-8") as f:
            json.dump(app_list, f, ensure_ascii=False, indent=4)

        print(f"✅ Oyun listesi kaydedildi: {steam_games_file}")
    else:
        print(f"❌ Steam API Hatası! HTTP Kod: {response.status_code}")

# ✅ Eğer JSON dosyası yoksa Steam API'den veri çek, varsa direkt oku
if not os.path.exists(steam_games_file):
    print("📂 Steam oyun listesi bulunamadı, API'den çekiliyor...")
    fetch_and_save_steam_games()
else:
    print("✅ Steam oyun listesi zaten mevcut, API'ye istek yapılmadı.")

# ✅ JSON dosyasından oyun isimlerini yükle
with open(steam_games_file, "r", encoding="utf-8") as f:
    steam_games = json.load(f)

# ✅ Steam oyun isimlerini temizleyelim
steam_game_names = {re.sub(r'[^a-zA-Z0-9 ]', '', game["name"].lower()).strip(): game["appid"] for game in steam_games}

# ✅ YouTube başlıklarındaki oyun isimlerini en yakın eşleşme ile bulalım (Hızlı!)
def fast_fuzzy_match(title):
    """Başlıktan en yakın oyun adını Steam veritabanı ile eşleştirir."""
    if pd.isna(title):
        return "Diğer"
    
    # Başlığı temizle (özel karakterleri kaldır, küçük harfe çevir)
    clean_title = re.sub(r'[^a-zA-Z0-9 ]', '', title.lower()).strip()

    # En yakın eşleşmeyi bul (%85 eşleşme eşiği, hızlı modda çalıştır)
    match_result = process.extractOne(clean_title, steam_game_names.keys(), score_cutoff=85)
    
    # Eğer eşleşme bulunamazsa "Diğer" olarak işaretle
    if match_result is None:
        print(f"❌ Eşleşme bulunamadı: {title}")
        return "Diğer"

    match, score = match_result[0], match_result[1]

    # Log ekleyelim (ilk 10 eşleşmeyi görmek için)
    print(f"🎯 Başlık: {title} | Eşleşme: {match} | Skor: {score}")
    
    return match if match else "Diğer"  # %85 üzeri eşleşmeler oyun kabul edilir

# ✅ CSV dosyasını oku ve oyun isimlerini eşleştir
print("📂 YouTube verileri yükleniyor...")
df = pd.read_csv(youtube_csv_file)

# Eğer "Title" sütunu yoksa hata vermemesi için kontrol ekleyelim
if "Title" not in df.columns:
    print("❌ Hata: 'Title' sütunu bulunamadı! CSV dosyanı kontrol et.")
    exit()

df["Game_Name"] = df["Title"].apply(fast_fuzzy_match)

# ✅ Güncellenmiş CSV'yi tekrar kaydet
df.to_csv(output_csv_file, index=False, encoding="utf-8-sig")

print(f"✅ Güncellenmiş dosya kaydedildi: {output_csv_file}")
