from wedding_platform.pages.models import Page


def generate_city_pages():
    cities = [
        "London", "Manchester", "Birmingham", "Leeds",
        "Liverpool", "Bristol", "Nottingham", "Sheffield",
        "Leicester", "Coventry", "Oxford", "Cambridge",
        "Newcastle", "Derby", "York", "Bath",
        "Brighton", "Reading", "Luton", "Milton Keynes"
    ]

    for city in cities:
        title = f"Wedding Photographer in {city}"
        slug = f"{city.lower().replace(' ', '-')}-wedding-photographer"

        content = f"""
<h1>{title}</h1>

<p>Looking for a professional wedding photographer in {city}? We capture timeless wedding moments with elegance.</p>

<h2>Why Choose Us in {city}</h2>
<ul>
<li>Experienced photographers</li>
<li>Affordable packages</li>
<li>Fast delivery</li>
</ul>

<h2>Book Your Wedding Photographer in {city}</h2>
<p>Contact us today to secure your date.</p>
"""

        Page.objects.get_or_create(
            slug=slug,
            defaults={
                "title": title,
                "content": content,
                "meta_title": f"{city} Wedding Photographer | Danarus",
                "meta_description": f"Top wedding photographer in {city}. Book now.",
            },
        )