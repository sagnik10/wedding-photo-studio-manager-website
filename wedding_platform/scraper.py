import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

url="https://artisticweddingphotos.co.uk"

r=requests.get(url)

soup=BeautifulSoup(r.text,"lxml")

imgs=soup.find_all("img")

os.makedirs("scraped_images",exist_ok=True)

for img in imgs:

 src=img.get("src")

 if src:

  img_url=urljoin(url,src)

  data=requests.get(img_url).content

  name=img_url.split("/")[-1]

  with open("scraped_images/"+name,"wb") as f:

   f.write(data)

  print("saved",name)
