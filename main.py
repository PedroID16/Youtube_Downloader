import yt_dlp
from sys import argv

if len(argv) < 2:
    print("Usage: python main.py <url>")
    exit()

link = argv[1]

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': 'C:/Users/Pedro Miguel/OneDrive/Desktop/YT_Videos/%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(link, download=False)
    print("Title:", info.get('title'))
    print("Views:", info.get('view_count'))
    ydl.download([link])