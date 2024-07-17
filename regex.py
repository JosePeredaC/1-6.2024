import re
import argparse as ag

parser = ag.ArgumentParser(description="Descargar archivos Scribd")
parser.add_argument('-l','--link',help="Link",required=True)
parser = parser.parse_args()

url = parser.link
regex = r"\d"
findall = re.findall(regex, url)
id = ''.join(findall)
nurl = f"https://es.scribd.com/embeds/{id}/content"
