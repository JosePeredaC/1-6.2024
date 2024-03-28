import requests
import json
import re

from bs4 import BeautifulSoup
nombre_video = str(input("nombre: "))
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
num = 0
for vid in videos:
    print("----------------------------------------------------------------------------")
    print(f"Opcion [{num}]")
    print("Titulo:", vid.get("title").get("runs")[0].get("text"))
    print("Canal:", vid.get("longBylineText").get("runs")[0].get("text"))
    print("Duración:", vid.get("lengthText").get("simpleText"))
    print("Visualizaciones:", vid.get("viewCountText").get("simpleText"))
    print("Publicado:", vid.get("publishedTimeText").get("simpleText"))
    print("----------------------------------------------------------------------------")
    num += 1
    query = vid.get("inlinePlaybackEndpoint").get("commandMetadata").get("webCommandMetadata").get("url")
    url = f"https://www.youtube.com{query}"
    videos[num] = url
elegir = int(input("\nElige el video que deseas descargar: "))
video_url = videos[elegir]
return(video_url)