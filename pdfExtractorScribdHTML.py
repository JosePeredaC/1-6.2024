import re
from bs4 import BeautifulSoup
import requests

url = "https://es.scribd.com/embeds/580838553/content"
response = requests.get(url)    
soup = BeautifulSoup(response.text, 'html.parser')
script_tags = soup.find_all(type="text/javascript")

my_script_tag = script_tags[17].text

urls = re.findall(r'contentUrl:\s*"(.*?)"', my_script_tag)

num_pages = len(urls)
print("Número total de páginas (URLs):", num_pages)

output_html = ""

for i, url in enumerate(urls):
    print(f"Generando HTML para la página {i + 1} de {num_pages}...")
    response = requests.get(url)
    html_text = re.search(r'window\.page\d+_callback\(\["(.*?)"\]\);', response.text, re.DOTALL)

    if html_text:
        formatted_html = html_text.group(1).replace('\\"', '"').replace('\n','')

        soup_page = BeautifulSoup(formatted_html, 'html.parser')

        for div_ff0 in soup_page.find_all('div', class_='ff0'):
            div_ff0.decompose()

        output_html += str(soup_page).replace('\\n','').replace('orig=','src=')
    else:
        print("No se encontró HTML entre paréntesis.")

output_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .outer_page.book_view{display:inline-block}.outer_page.blurred_page{-webkit-user-drag:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.newpage{margin: 30px auto;box-shadow: 1px 1px 10px;white-space:nowrap;position:relative;top:0;left:0;text-rendering:auto;color:#000}.image_layer,.link_layer,.text_layer{width:0;height:0;position:absolute;top:0;left:0}.image_layer .absimg{position:absolute;border:none;left:0;-webkit-user-drag:none}.image_layer .absimg::selection{background-color:transparent}.text_layer{transform:scale(.2);transform-origin:top left}.text_layer div,.text_layer span{white-space:nowrap;padding:0;margin:0;border:none;line-height:1}.text_layer span{height:1px}.text_layer span.a,.text_layer span.g{position:absolute;border:none;left:0}.text_layer span.w,.text_layer span.w1,.text_layer span.w10,.text_layer span.w11,.text_layer span.w12,.text_layer span.w2,.text_layer span.w3,.text_layer span.w4,.text_layer span.w5,.text_layer span.w6,.text_layer span.w7,.text_layer span.w8,.text_layer span.w9{white-space:nowrap;padding:0;margin:0;border:none;height:1px;line-height:1;display:inline-block}.text_layer a.ll{position:absolute;display:block;color:inherit;text-decoration:none}.text_layer span.l,.text_layer span.l1,.text_layer span.l10,.text_layer span.l11,.text_layer span.l12,.text_layer span.l2,.text_layer span.l3,.text_layer span.l4,.text_layer span.l5,.text_layer span.l6,.text_layer span.l7,.text_layer span.l8,.text_layer span.l9{white-space:nowrap;padding:0;border:none;height:1px;line-height:1;display:inline}.text_layer span.l{margin:0}.text_layer span.l1{margin:0 0 0 -1px}.text_layer span.l2{margin:0 0 0 -2px}.text_layer span.l3{margin:0 0 0 -3px}.text_layer span.l4{margin:0 0 0 -4px}.text_layer span.l5{margin:0 0 0 -5px}.text_layer span.l6{margin:0 0 0 -6px}.text_layer span.l7{margin:0 0 0 -7px}.text_layer span.l8{margin:0 0 0 -8px}.text_layer span.l9{margin:0 0 0 -9px}.text_layer span.l10{margin:0 0 0 -10px}.text_layer span.l11{margin:0 0 0 -11px}.text_layer span.l12{margin:0 0 0 -12px}.text_layer span.w1{width:1px}.text_layer span.w2{width:2px}.text_layer span.w3{width:3px}.text_layer span.w4{width:4px}.text_layer span.w5{width:5px}.text_layer span.w6{width:6px}.text_layer span.w7{width:7px}.text_layer span.w8{width:8px}.text_layer span.w9{width:9px}.text_layer span.w10{width:10px}.text_layer span.w11{width:11px}.text_layer span.w12{width:12px}
    </style>
</head>
<body>
""" + output_html + """
</body>
</html>
"""


with open("output.html", "w", encoding="utf-8") as file:
    file.write(output_html)

print("Se ha generado el archivo HTML 'output.html' con todo el contenido.")

