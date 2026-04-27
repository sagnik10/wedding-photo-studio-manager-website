import os
import sys
import django
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

from wedding_platform.pages.models import Page
from wedding_platform.gallery.models import Gallery, Photo

BASE = "https://artisticweddingphotos.co.uk"

visited = set()


def crawl(url):

    if url in visited:
        return

    visited.add(url)

    try:
        r = requests.get(url, timeout=10)
    except:
        return

    soup = BeautifulSoup(r.text, "lxml")

    title = soup.title.string if soup.title else "Page"

    text = " ".join([p.get_text() for p in soup.find_all("p")])

    slug = url.replace(BASE, "").replace("/", "") or "home"

    Page.objects.get_or_create(
        title=title,
        slug=slug,
        content=text
    )

    imgs = soup.find_all("img")

    gallery, _ = Gallery.objects.get_or_create(
        title="Imported Gallery",
        slug="imported-gallery"
    )

    for img in imgs:

        src = img.get("src")

        if src:

            img_url = urljoin(BASE, src)

            try:

                img_data = requests.get(img_url).content

                name = img_url.split("/")[-1]

                path = "media/photos/" + name

                os.makedirs("media/photos", exist_ok=True)

                with open(path, "wb") as f:
                    f.write(img_data)

                Photo.objects.create(
                    gallery=gallery,
                    image="photos/" + name
                )

            except:
                pass

    links = soup.find_all("a")

    for link in links:

        href = link.get("href")

        if href and href.startswith("/"):
            crawl(BASE + href)


crawl(BASE)
