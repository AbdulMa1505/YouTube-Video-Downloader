# YouTube Video Downloader

This Python script allows users to download YouTube videos in the best available quality using the `yt-dlp` library. The script handles SSL certificate verification issues and ensures smooth downloading by setting the required options.

## Prerequisites

Before running the script, ensure you have the following installed:

- **Python 3.x**
- **yt-dlp** library (a fork of `youtube-dl` that supports additional features and fixes)

## Installation

1. **Clone the repository** or create a new Python file with the following code:

```bash
git clone <https://github.com/AbdulMa1505/YouTube-Video-Downloader.git>  # If applicable

2. **creating a virtual env**
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows

3. Install yt_dlp
 - pip install yt-dlp

## Code Explanation
1. - SSL Context Fix: The script modifies the default SSL context to bypass SSL verification issues. This is useful for environments where SSL certificates might not be properly configured.
 ssl._create_default_https_context = ssl._create_unverified_context
2. -yt-dlp Options: The script is set to download videos in the best quality by default using the format: 'best' option.
ydl_opts = {
        'format': 'best',}
3. -Download Video: The video download is handled by the yt-dlp library, which is initialized with the specified options, and the video is downloaded to the current working directory.
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
 ## example usage 
 enter the link here: 
https://www.youtube.com/watch?v=dQw4w9WgXcQ

## Troubleshooting
- SSL Verification Errors
- If you encounter errors related to SSL verification, ensure your Python environment has the required certificates. If necessary, the script disables SSL certificate verification by using an unverified context (ssl._create_unverified_context).
# Missing Dependencies
- If you see errors related to missing modules, install the required dependencies using:
pip install yt-dlp

## License
This project is licensed under the MIT License







