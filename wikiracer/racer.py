import logging
import requests
from bs4 import BeautifulSoup
from collections import deque
from typing import List, Optional, Set, Tuple
from wikiracer.utils import extract_title, extract_links

logger = logging.getLogger(__name__)

class WikiRacer:
    def __init__(self):
        self.session = requests.Session()

    def get_page_content(self, url: str) -> Optional[BeautifulSoup]:
        """
        Fetches the page content and returns a BeautifulSoup object.
        """
        try:
            response = self.session.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            content = soup.find(id='bodyContent')
            return content
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch '{url}': {e}")
            return None

    def bfs(self, start_url: str, end_url: str) -> Optional[List[str]]:
        """
        Performs BFS to find the shortest path from start_url to end_url.
        """
        start_title = extract_title(start_url)
        end_title = extract_title(end_url)
        visited: Set[str] = set()
        queue: deque[Tuple[str, List[str]]] = deque()
        queue.append((start_url, [start_url]))

        while queue:
            current_url, path = queue.popleft()
            current_title = extract_title(current_url)

            if current_title in visited:
                continue

            logger.info(f"Visiting '{current_title}'")
            visited.add(current_title)

            if current_title == end_title:
                logger.info("End page found!")
                return path

            content = self.get_page_content(current_url)
            if not content:
                continue

            links = extract_links(content)
            for link in links:
                link_title = extract_title(link)
                if link_title not in visited:
                    queue.append((link, path + [link]))

        logger.warning("No path found")
        return None

    def find_path(self, start_url: str, end_url: str) -> Optional[List[str]]:
        return self.bfs(start_url, end_url)
