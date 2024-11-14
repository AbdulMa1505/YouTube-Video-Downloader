import ssl
import yt_dlp
ssl._create_default_https_context = ssl._create_unverified_context
url=input("enter the link here: \n")
ydl_opts={
    'format':'best',
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url]) 