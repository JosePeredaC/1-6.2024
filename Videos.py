#!/usr/bin/env python
#_*_ coding: utf8 _*_
from pytube import YouTube
import ffmpeg
def download_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path)
def download_audio(url, output_path):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_path = audio_stream.download(output_path)
    mp3_path = output_path + "/audio.mp3"  
    (
        ffmpeg.input(audio_path)
        .output(mp3_path, format='mp3', acodec='libmp3lame', ar='44100', audio_bitrate='192k')
        .overwrite_output()
        .run()
    )
    return mp3_path
def main():
    print("Dinos que deseas descargar:\n[1]Audio\n[2]Video\n")
    opcion=int(input("Opcion: ")) 
    if(opcion == 1):
        video_url = str(input("Introduce el link del video: "))
        download_audio(video_url, r"/storage/emulated/0/Download/")
    elif (opcion == 2):
        video_url = str(input("Introduce el link del video:"))
        download_video(video_url, r"/storage/emulated/0/Download/")
if __name__ == '__main__': 
    main()