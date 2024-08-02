import os
import pytube
import tkinter as tk
from tkinter import messagebox

def get_desktop_path():
    home = os.path.expanduser("~")
    return os.path.join(home, "Desktop")

def download_video(url, path):
    pytube.YouTube(url).streams.get_highest_resolution().download(path)
    print(f"Video downloaded to {path}")

def download_audio(url, path):
    pytube.YouTube(url).streams.filter(only_audio=True).first().download(path)
    print(f"Audio downloaded to {path}")


def on_download():
    url = url_entry.get()
    download_path = get_desktop_path()

    if video_var.get() and audio_var.get():
        messagebox.showerror("Error", "Select either video or audio not both.")
        return

    if not video_var.get() and not audio_var.get():
        messagebox.showerror("Error", "Select video or audio.")
        return

    try:
        if video_var.get():
            download_video(url, download_path)
        elif audio_var.get():
            download_audio(url, download_path)
        messagebox.showinfo("Success", f"Download complete! File saved to {download_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# interface
root = tk.Tk()
root.title("YouTube Downloader")

tk.Label(root, text="YouTube URL:").pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

video_var = tk.BooleanVar()
audio_var = tk.BooleanVar()

tk.Checkbutton(root, text="Download Video", variable=video_var).pack(pady=5)
tk.Checkbutton(root, text="Download Audio", variable=audio_var).pack(pady=5)

tk.Button(root, text="Download", command=on_download).pack(pady=20)

root.mainloop()
