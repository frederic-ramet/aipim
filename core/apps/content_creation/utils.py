
import requests
from bs4 import BeautifulSoup
import json


def extract_description_details(soup):
    description_details = {}
    accordion_content = soup.find("div", class_="accordion__content js-accordion-content")
    if accordion_content:
        # Handling for norms and other details
        norms = accordion_content.find("ul", class_="list-standards")
        if norms:
            description_details['norms'] = [{item.find("div", class_="heading-5").get_text(strip=True): item.find("div", class_="text-current").get_text(strip=True)} for item in norms.find_all("li", class_="list-standards__item")]

        # Handle rich text details
        rich_texts = accordion_content.find_all("div", class_="text-current rich-text")
        for rich_text in rich_texts:
            headings = rich_text.find_all("h2")
            for heading in headings:
                description_details[heading.get_text(strip=True)] = heading.find_next_sibling('p').get_text(strip=True) if heading.find_next_sibling('p') else "Detail not available"
    return description_details

def extract_characteristics(content_div):
    characteristics = {}
    rows = content_div.find_all("div", class_="list-characteristics__row")
    for row in rows:
        title = row.find("span", class_="list-characteristics__title").get_text(strip=True)
        desc = row.find("span", class_="list-characteristics__desc").get_text(strip=True)
        characteristics[title] = desc
    return characteristics

def extract_resources(content_div):
    resources = []
    document_rows = content_div.find_all("div", class_="list-documents-news__row")
    for row in document_rows:
        title = row.find("a", class_="list-documents-news__title").get_text(strip=True)
        link = row.find("a", class_="link link--icons list-documents-news__link")['href']
        file_info = row.find("span", class_="list-documents-news__file").get_text(strip=True)
        resources.append({
            "title": title,
            "link": f"https://www.nexans.fr{link}",
            "file_info": file_info
        })
    return resources


def extract_variants(soup):
    variants = []
    product_list = soup.find("div", class_="product__list filter-list")
    if product_list:
        for item in product_list.find_all("div", class_="product__list__item filter-element"):
            specs = {attr.replace('data-', '').replace('COLORSH', 'sheath_color').lower(): item[attr] for attr in item.attrs if attr.startswith('data-')}
            downloads = [f"https://www.nexans.fr{li.find('a')['href']}" for li in item.find_all("li", class_="product__downloads__file")]
            variants.append({
                "title": item.find("h3", class_="product__list__item__title").get_text(strip=True),
                "reference": item.find("p", class_="product__list__item__ref").get_text(strip=True),
                "specs": specs,
                "downloads": downloads
            })
    return variants


def get_product_from_nexans_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the product title
    title_tag = soup.find("p", class_="product__title heading-3")
    title = title_tag.get_text(strip=True) if title_tag else "Title not found"

    # Extract the product description
    description_tag = soup.find("div", class_="product__desc truncate js-truncate")
    description = description_tag.find("p").get_text(strip=True) if description_tag else "Description not found"

    # Extract all images from the gallery
    gallery_div = soup.find("div", class_="row product__gallery js-gallery")
    images = [img['src'] for img in gallery_div.find_all("img")] if gallery_div else ["No images found"]

    # Extract links to documents
    downloads = []
    downloads_list = soup.find("ul", class_="product__downloads")
    if downloads_list:
        for file in downloads_list.find_all("li", class_="product__downloads__file"):
            link_tag = file.find("a", class_="product__downloads__file__link")
            if link_tag:
                downloads.append({
                    "title": link_tag.find(class_="product__downloads__file__title").get_text(strip=True),
                    "data": link_tag.find(class_="product__downloads__file__data").get_text(strip=True),
                    "link": f"https://www.nexans.fr{link_tag['href']}"
                })

    # Extract variants
    variants = extract_variants(soup)

    # Extract detailed descriptions and characteristics
    description_details = extract_description_details(soup)

    # Extract characteristics
    characteristics = extract_characteristics(soup.find("div", id="product-characteristics"))

    # Extract resources
    resources = extract_resources(soup.find("div", id="product-ressources"))

    product_info = {
        "title": title,
        "url":url,
        "description": description,
        "images": images,
        "downloads": downloads,
        "description_details": description_details,
        "characteristics": characteristics,
        "resources": resources,
        "variants": variants,
    }

    # Convert the dictionary to a JSON string for output or further use
    return json.dumps(product_info, indent=4)

