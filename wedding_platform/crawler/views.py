from django.http import JsonResponse
from .models import CrawlTarget, CrawlResult
from .instagram_publish import publish_instagram
from .pinterest_auto import publish_pinterest

import requests
from bs4 import BeautifulSoup


def extract_data(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else ""

        meta = soup.find("meta", attrs={"name": "description"})
        description = meta["content"] if meta else ""

        h1_tags = [h.get_text(strip=True) for h in soup.find_all("h1")]

        images = [
            img.get("src")
            for img in soup.find_all("img")
            if img.get("src")
        ]

        return {
            "title": title,
            "meta_description": description,
            "h1_tags": ", ".join(h1_tags),
            "images": images,
        }

    except Exception as e:
        return {"error": str(e)}


def run_crawler(request):
    results = []

    targets = CrawlTarget.objects.all()

    for target in targets:
        data = extract_data(target.url)

        result = CrawlResult.objects.create(
            target=target,
            title=data.get("title", ""),
            meta_description=data.get("meta_description", ""),
            h1_tags=data.get("h1_tags", ""),
            images=",".join(data.get("images", [])),
        )

        images = data.get("images", [])

        if images:
            first_image = images[0]

            publish_instagram(first_image, result.title)
            publish_pinterest(first_image, result.title, target.url)

        results.append(result.id)

    return JsonResponse({"status": "success", "results": results})