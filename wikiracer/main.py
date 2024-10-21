import logging
import sys
from wikiracer.racer import WikiRacer

def main():
    logging.basicConfig(level=logging.INFO)
    if len(sys.argv) != 3:
        print("Usage: python -m wikiracer.main <start_url> <end_url>")
        sys.exit(1)

    start_url = sys.argv[1].strip()
    end_url = sys.argv[2].strip()

    racer = WikiRacer()
    path = racer.find_path(start_url, end_url)
    if path:
        print("\nPath found:")
        for idx, url in enumerate(path, 1):
            print(f"{idx}. {url}")
    else:
        print("No path found between the given pages.")

if __name__ == "__main__":
    main()
