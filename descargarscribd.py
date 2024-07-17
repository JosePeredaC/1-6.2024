from bs4 import BeautifulSoup
import requests
import re
import argparse as ag

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from io import BytesIO

parser = ag.ArgumentParser(description="Descargar archivos Scribd")
parser.add_argument('-l','--link',help="Link",required=True)
parser = parser.parse_args()

def create_pdf_from_images(image_urls, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter

    for index, url in enumerate(image_urls[0:900]):
        print('Image', index)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                image_data = BytesIO(response.content)
                img = ImageReader(image_data)
                c.drawImage(img, 0, 0, width=width, height=height, preserveAspectRatio=True)
                c.showPage()
            else:
                print(f"Failed to retrieve image from URL: {url}")
        except Exception as e:
            print(f"Error processing image from URL {url}: {str(e)}")

    c.save()

aurl = parser.link
regex = r"\d"
findall = re.findall(regex, aurl)
id = ''.join(findall)
url = f"https://es.scribd.com/embeds/{id}/content"

response = requests.get(url)    
soup = BeautifulSoup(response.text,'html.parser' )
script_tags = soup.find_all(type="text/javascript")


my_script_tag = script_tags[17].text


urls = re.findall(r'contentUrl:\s*"(.*?)"', my_script_tag)
img_urls = list(map(lambda x: x.replace('pages','images').replace('jsonp','jpg'), urls))

# print(img_urls)

output_pdf = "output.pdf"

# Call the function to create the PDF
create_pdf_from_images(img_urls, output_pdf)