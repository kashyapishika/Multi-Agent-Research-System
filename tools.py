import re
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
from langchain.tools import tool

@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information on a topic.
    Returns titles, URLs and snippets."""
    try:
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=5):
                results.append(
                    f"Title: {r['title']}\nURL: {r['href']}\nSnippet: {r['body'][:300]}\n"
                )
        return "\n----\n".join(results) if results else "No results found."
    except Exception as e:
        return f"Search failed: {str(e)}"

@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                                   "Chrome/120.0.0.0 Safari/537.36"},
        )
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()
        text = soup.get_text(separator=" ", strip=True)
        text = re.sub(r"\s{3,}", "\n\n", text)
        return text[:4000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"
