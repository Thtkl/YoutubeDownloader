import os
import pytube

def get_desktop_path():
    # Get the user's home directory
    home = os.path.expanduser("~")
    return os.path.join(home, "Desktop")

def download_video(url, path):
    # for video
    pytube.YouTube(url).streams.get_highest_resolution().download(path)
    print(f"Video downloaded to {path}")

def download_audio(url, path):
    # for audio stream
    pytube.YouTube(url).streams.filter(only_audio=True).first().download(path)
    print(f"Audio downloaded to {path}")

def main():
    choice = input("Enter 1 for Video // Enter 2 for Audio\n: ")

    if choice in ['1', '2']:
        url = input("Enter YouTube URL: ")
        desktop_path = get_desktop_path()

        if choice == '1':
            download_video(url, desktop_path)
        elif choice == '2':
            download_audio(url, desktop_path)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
