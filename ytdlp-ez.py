import os
import tkinter as tk
from tkinter import filedialog

def main():
    # start by updating ytdlp
    os.system("yt-dlp --update");
    
    # Hide root window
    root = tk.Tk()
    root.withdraw()

    print("Select a folder where downloads will be saved...")
    download_dir = filedialog.askdirectory(title="Choose Download Folder")

    if not download_dir:
        print("No folder selected, exiting...")
        return

    print("Selected Directory: " + download_dir)

    while True:
        print("\nChoose download type:")
        print("1. Audio only (mp3)")
        print("2. Video only (mp4, up to 1080p, H.264)")
        print("3. Audio + Video (mp4, up to 1080p, H.264)")
        print("4. Quit")

        choice = input("Enter choice (1/2/3/4): ").strip()

        if choice == "4":
            print("Exiting...")
            break

        url = input("Enter video URL: ").strip()

        if choice == "1":
            # Audio only
            cmd = f'yt-dlp -f bestaudio -x --audio-format mp3 -o "{download_dir}/%(title)s.%(ext)s" "{url}"'
        elif choice == "2":
            # Video only
            cmd = f'yt-dlp -f "bestvideo[height<=1080][vcodec^=avc1]" --merge-output-format mp4 -o "{download_dir}/%(title)s.%(ext)s" "{url}"'
        elif choice == "3":
            # Both audio + video
            cmd = f'yt-dlp -f "bestvideo[ext=mp4][vcodec^=avc1][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4][vcodec^=avc1][height<=1080]" -o "{download_dir}/%(title)s.%(ext)s" "{url}"'
        else:
            print("Invalid choice, try again.")
            continue

        print(f"\nRunning command:\n{cmd}\n")
        os.system(cmd)

if __name__ == "__main__":
    main()
