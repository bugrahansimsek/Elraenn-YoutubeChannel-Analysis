# **Elraenn-YouTube-Channel-Analysis**

Bu proje, **Elraenn'in YouTube Kanalı** için veri çekme, düzenleme ve analiz süreçlerini içerir. Projede, kanalın izlenme, beğeni ve yorum verileri analiz edilerek çeşitli içgörüler elde edilmiştir.

## **📌 Proje Süreci**
### **📥 Veri Çekme**
- `get_channel_uploads.py` ile kanalın **video oynatma listesi (playlist) ID’si** bulunur.
- `get_channel_playlists.py` ile kanalın **tüm oynatma listeleri** alınır.
- `fetch_youtube_video_data.py` ile **YouTube API kullanılarak videolara ait veriler çekilir** ve **Elraenn_Youtube_Analytics.csv** dosyasına kaydedilir.

### **🔗 Veri Zenginleştirme**
- `match_steam_game_titles.py` ile **YouTube başlıklarında geçen oyun isimleri**, **Steam API’den çekilen oyun listesi ile eşleştirilir**.

### **📝 Veri Düzenleme**
- Çekilen veriler **Excel'de temizlenir ve analiz için hazırlanır**.

### **📊 Analiz ve Görselleştirme**
- Veriler **Power BI’da analiz edilir ve görselleştirilir** (**Elraenn-Youtube-Channel-Analysis.pbix** dosyasında).

---

## **🛠 Kullanılan Teknolojiler**
- **Python**: Veri çekme işlemi ve veri düzenleme için.
- **YouTube API**: Kanal verilerini almak için.
- **Steam API**: Oyun isimlerini eşleştirmek için.
- **Power BI**: Verileri analiz etmek ve görselleştirmek için.
- **Excel**: Verileri düzenlemek için.
- **GitHub**: Proje dosyalarının ve kodlarının yönetimi için.

---

## **📊 Elde Edilen Sonuçlar**
### **📅 Ay ve Yıla Göre İzlenme Eğilimleri**
- Kanalın yıllık ve aylık izlenme değişimleri analiz edilerek **izleyici ilgisinin zaman içindeki değişimleri incelenmiştir**.

### **🎮 Oyunlara Göre İzlenme**
- Yayınlanan **oyunlara göre izlenme sayıları karşılaştırılmış**, izleyicinin **hangi oyunlara daha fazla ilgi gösterdiği belirlenmiştir**.

### **📆 Haftanın Günlerine Göre İzlenme**
- İzlenme sayılarının **haftanın günlerine göre dağılımı analiz edilerek izleyici alışkanlıkları hakkında fikir edinilmiştir**.

### **📽 Video Türü Dağılımı**
- **Shorts ve standart videoların izlenme performansları karşılaştırılmıştır**.

Bu analiz, **kanalın içerik stratejisini geliştirmek ve izleyici etkileşimini artırmak için faydalı içgörüler sağlamaktadır**.

---

# **Elraenn-YouTube-Channel-Analysis (English)**

This project provides a **data collection, processing, and analysis process** for the **Elraenn YouTube Channel**. The project analyzes the channel's **views, likes, and comments data** to obtain various insights.

## **📌 Project Workflow**
### **📥 Data Collection**
- `get_channel_uploads.py`: **Finds the playlist ID** for the channel’s uploaded videos.
- `get_channel_playlists.py`: **Retrieves all playlists** from the channel.
- `fetch_youtube_video_data.py`: Uses **YouTube API** to **retrieve video data** and save it into **Elraenn_Youtube_Analytics.csv**.

### **🔗 Data Enrichment**
- `match_steam_game_titles.py`: **Matches YouTube video titles with Steam game names** using **Steam API**.

### **📝 Data Cleaning**
- The collected data is **cleaned and prepared in Excel** for further analysis.

### **📊 Analysis and Visualization**
- The data is **analyzed and visualized using Power BI** (**Elraenn-Youtube-Channel-Analysis.pbix** file).

---

## **🛠 Technologies Used**
- **Python**: For data collection and processing.
- **YouTube API**: To fetch channel data.
- **Steam API**: To match game titles.
- **Power BI**: For data analysis and visualization.
- **Excel**: For organizing and preparing data.
- **GitHub**: For managing project files and code.

---

## **📊 Key Insights**
### **📅 Monthly and Yearly View Trends**
- **Analyzes viewer interest over time** based on monthly and yearly view counts.

### **🎮 View Counts by Game**
- Compares view counts **based on games published**, identifying which games attract more interest.

### **📆 View Counts by Day of the Week**
- **Analyzes viewing patterns by the day of the week** to understand viewer habits.

### **📽 Distribution by Video Type**
- **Compares the performance of Shorts and standard videos** in terms of views.

This analysis provides **valuable insights into optimizing content strategy and enhancing audience engagement** for the channel.

---

![Elraenn Analizi Görseli](https://github.com/bugrahansimsek/Elraenn-YoutubeChannel-Analysis/blob/main/ElraennPowerBIGif.gif)
