import moviepy
import moviepy.editor
video = moviepy.editor.VideoFileClip(r"C:\Users\vijay\OneDrive\Desktop\short projects\mp4-mp3\video.mp4")
audio = video.audio
audio.write_audiofile(r"C:\Users\vijay\OneDrive\Desktop\short projects\mp4-mp3\audiovideo.mp3")