# Wikiracer

## Description

Wikiracer is a program that finds the shortest path between two Wikipedia pages by following links within the article bodies.

## Features

- Uses BFS to find the shortest path.
- Dockerized for consistent deployment.
- CI/CD pipeline with GitHub Actions.
- Unit tests included.

## Requirements

- Python 3.9 or higher
- `requests` library
- `beautifulsoup4` library

## Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/yourusername/wikiracer.git
cd wikiracer
pip install -r requirements.txt
