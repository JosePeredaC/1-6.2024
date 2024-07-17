#!/usr/bin/env python
#_*_ coding: utf8 _*_
from pytube import YouTube
import argparse as ag
import requests
import json
parser = ag.ArgumentParser(description="Descargar videos de Youtube")
parser.add_argument('-l','--link',help="Link",required=False)
parser.add_argument('-f','--format',help="Formato del video [1]Audio [2]Video", required=True, type=int)
parser = parser.parse_args()
opcion = parser.format
def download_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path)
def download_audio(url, output_path):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path)
def buscar_videos(nombre_video):
    url="https://www.youtube.com/youtubei/v1/search"
    data = {
        "context": {
            "client": {
                "clientName": "WEB",
                "clientVersion": "2.20240313.01.00"
            }
        },
        "query": f"{nombre_video}"
    }

    json_data = json.dumps(data)


    response = requests.post(url, data=json_data)

    contents = response.json().get("contents").get("twoColumnSearchResultsRenderer").get("primaryContents").get("sectionListRenderer").get("contents")[0].get("itemSectionRenderer").get("contents")
    videos = [obj.get("videoRenderer") for obj in contents if "videoRenderer" in obj]
    urls_videos = []
    num = 0
    for vid in videos:
        try:
            print("----------------------------------------------------------------------------")
            print(f"Opcion [{num}]")
            print("Titulo:", vid.get("title",{}).get("runs",{})[0].get("text",{}))
            print("Canal:", vid.get("longBylineText",{}).get("runs",{})[0].get("text",{}))
            print("Duración:", vid.get("lengthText",{}).get("simpleText",{}))
            print("Visualizaciones:", vid.get("viewCountText",{}).get("simpleText",{}))
            print("Publicado:", vid.get("publishedTimeText",{}).get("simpleText",{}))
            print("----------------------------------------------------------------------------")
        except: 
            continue
        try:
            query = vid.get("inlinePlaybackEndpoint").get("commandMetadata").get("webCommandMetadata").get("url")
            url = f"https://www.youtube.com{query}"
            urls_videos.append(url)
            num += 1
        except:
            continue
    elegir = int(input("\nElige el video que deseas descargar: "))
    video_url = urls_videos[elegir]
    return(video_url)
def audio_video(opcion):
    if(opcion == 1):
        if parser.link:
            video_url = parser.link    
        else:
            nombre_video = str(input("Introduce el nombre del video: "))
            video_url = buscar_videos(nombre_video)
        download_audio(video_url, r"C:\Users\USER\Videos\OpenBoard")
        print("El video ha sido descargado con exito!")
    elif (opcion == 2):
        if parser.link:
            video_url = parser.link
        else:
            nombre_video = str(input("Introduce el nombre del video: "))
            video_url = buscar_videos(nombre_video)
        download_video(video_url, r"C:\Users\USER\Videos\OpenBoard")
        print("El video ha sido descargado con exito!")
def main():
    audio_video(opcion)  
    
    
if __name__ == '__main__': 
    try:
        main()
    except:
        print("\nSe ha salido del programa")