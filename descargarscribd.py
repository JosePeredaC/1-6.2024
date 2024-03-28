from bs4 import BeautifulSoup
import requests

url = "https://es.scribd.com/embeds/413993612/content"
data={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'

}
response = requests.get(url , data=data)    
soup = BeautifulSoup(response.text,'html.parser' )
img = soup.find_all(class_="newpage")
for i in img:
    print(i)
