import re
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl

app = FastAPI(
    title="Instagram Reel Scraper API",
    description="Extracts basic metadata from an Instagram Reel URL",
    version="1.0.0"
)


class ReelRequest(BaseModel):
    reel_url: HttpUrl


def scrape_reel_info(reel_url: str):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            # "Chrome/151.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(
            reel_url,
            headers=headers,
            timeout=15
        )
    except requests.RequestException as e:
        raise HTTPException(
            status_code=502,
            detail=f"Failed to access Instagram: {str(e)}"
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to load Instagram Reel page"
        )

    soup = BeautifulSoup(response.text, "html.parser")

    og_data = {}

    for meta in soup.find_all("meta"):
        prop = meta.get("property")

        if prop and prop.startswith("og:"):
            og_data[prop] = meta.get("content")


    # 1. Extract thumbnail
    og_image = soup.find("meta", property="og:image")
    thumbnail_url = (
        og_image.get("content")
        if og_image
        else None
    )

    # 2. Extract description
    og_desc = soup.find("meta", property="og:description")

    full_description = (
        og_desc.get("content", "")
        if og_desc
        else ""
    )

    username = "Unknown"
    caption = full_description

    # Try to extract username and caption
    pattern = (
        r"^(?:.*?\s+comments\s+-\s+)?"
        r"([\w.]+)\s+on\s+"
        r"(?:Instagram|[A-Za-z]+\s+\d+,\s+\d{4}):\s*"
        r'["“]?(.*?)["”]?\s*\.?\s*$'
    )

    match = re.match(
        pattern,
        full_description,
        re.DOTALL
    )

    if match:
        username = match.group(1)
        caption = match.group(2)

    else:
        # Fallback
        fallback = re.search(
            r"-\s+([\w.]+)\s+on\s+\w+\s+\d+,",
            full_description
        )

        if fallback:
            username = fallback.group(1)

    # 3. Extract hashtags
    tags = re.findall(r"#\w+", caption)

    return {
        "username": username,
        "caption": caption,
        "tags": tags,
        "thumbnail_url": thumbnail_url,
        "reel_url": reel_url
    }


@app.get("/")
def root():
    return {
        "message": "Instagram Reel Scraper API is running"
    }


@app.post("/scrape-reel")
def scrape_reel(request: ReelRequest):
    return scrape_reel_info(str(request.reel_url))
