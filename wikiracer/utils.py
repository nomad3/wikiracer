import logging
import re
from urllib.parse import urlparse, unquote
from typing import Set
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

WIKIPEDIA_BASE_URL = 'https://en.wikipedia.org'

def extract_title(url: str) -> str:
    """
    Extracts the Wikipedia page title from a URL.
    """
    parsed_url = urlparse(url)
    title = unquote(parsed_url.path.split('/wiki/')[-1])
    logger.debug(f"Extracted title '{title}' from URL '{url}'")
    return title

def is_valid_link(href: str) -> bool:
    """
    Checks if an href is a valid Wikipedia article link.
    """
    invalid_patterns = (
        re.compile(r'^#'),             # Fragments
        re.compile(r'^/wiki/(Help|File|Portal|Special|Talk|Category|Template|Template_talk|Wikipedia):'),  # Namespaces
        re.compile(r'\.ogg$|\.jpg$|\.jpeg$|\.png$'),  # File types
    )
    if not href.startswith('/wiki/'):
        return False
    for pattern in invalid_patterns:
        if pattern.search(href):
            return False
    return True

def extract_links(content: BeautifulSoup) -> Set[str]:
    """
    Extracts all valid Wikipedia links from the page content.
    """
    links = set()
    for link in content.find_all('a', href=True):
        href = link['href']
        if is_valid_link(href):
            full_url = WIKIPEDIA_BASE_URL + href
            links.add(full_url)
    logger.debug(f"Extracted {len(links)} links")
    return links
