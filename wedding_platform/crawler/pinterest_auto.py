import requests
from django.conf import settings


def publish_pinterest(image_url, title, link):
    url = "https://api.pinterest.com/v5/pins"

    headers = {
        "Authorization": f"Bearer {settings.PINTEREST_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "title": title,
        "link": link,
        "media_source": {
            "source_type": "image_url",
            "url": image_url,
        },
    }

    response = requests.post(url, json=payload, headers=headers, timeout=10)

    return response.json()