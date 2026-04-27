import requests
from django.conf import settings


def publish_instagram(image_url, caption):
    url = "https://graph.facebook.com/v18.0/me/media"

    response = requests.post(
        url,
        data={
            "image_url": image_url,
            "caption": caption,
        },
        params={"access_token": settings.INSTAGRAM_TOKEN},
        timeout=10,
    )

    return response.json()