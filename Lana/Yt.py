import yt_dlp

def main():
    query = input("Enter song name to search: ").strip()
    if not query:
        print("Search query cannot be empty.")
        return

    print(f"\nSearching for the top result for: '{query}'...")

    search_opts = {
        'default_search': 'ytsearch1',
        'skip_download': True,
        'quiet': True,
        'remote_components': 'ejs:github',
    }

    try:
        with yt_dlp.YoutubeDL(search_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{query}", download=False)
            entries = info.get('entries', [])

        if not entries:
            print("No songs found.")
            return

        top_entry = entries[0]
        title = top_entry.get('title', 'Unknown Title')
        duration_sec = top_entry.get('duration', 0)
        song_url = top_entry.get('webpage_url')
        
        minutes = duration_sec // 60
        seconds = duration_sec % 60
        duration_str = f"{minutes}:{seconds:02d}" if duration_sec else "N/A"
        
        print("\n--- Top Search Result ---")
        print(f"Title:    {title}")
        print(f"Duration: {duration_str}")
        print(f"URL:      {song_url}")
        
        confirm = input("\nDo you want to download this track as an MP3? (y/n): ").strip().lower()
        
        if confirm == 'y':
            print(f"\nDownloading and converting: '{title}'...")
            
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl':'downloads/%(title)s.%(ext)s',
                'remote_components': 'ejs:github',
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([song_url])
                
            print("\nDownload finished successfully! Check your project folder.")
        else:
            print("Download cancelled.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()