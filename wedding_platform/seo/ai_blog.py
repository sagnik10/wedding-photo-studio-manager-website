from openai import OpenAI
from django.conf import settings
from wedding_platform.pages.models import Page

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_blog(topic):
    prompt = f"""
Write a high-quality 1200 word SEO optimized blog on:
"{topic} wedding photography in the UK"

Include:
- H1, H2, H3 headings
- FAQs section
- Local SEO keywords
- Natural human tone
- Call to action
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    content = response.choices[0].message.content

    slug = topic.lower().replace(" ", "-") + "-wedding-photography"

    Page.objects.get_or_create(
        slug=slug,
        defaults={
            "title": f"{topic} Wedding Photography",
            "content": content,
            "meta_title": f"{topic} Wedding Photographer UK",
            "meta_description": content[:160],
        },
    )