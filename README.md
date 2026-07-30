# Backend AI Scraper

A lightweight educational web scraper that collects structured book data from **Books to Scrape**, a practice website designed for web-scraping exercises.

The project demonstrates the complete data-gathering pipeline:

**Fetch → Parse → Extract → Clean → Structure → Save**

It also includes responsible scraping practices such as `robots.txt` handling, rate limiting, and scraper identification through a custom User-Agent.

## Project Goal

The goal of this project is to build a scraper that:

- Collects pages from a practice website
- Extracts useful fields from HTML
- Cleans and normalizes the extracted data
- Saves structured records as JSON
- Follows responsible scraping practices
- Produces a clean dataset suitable for future RAG workflows

## Tech Stack

- Python
- Requests
- BeautifulSoup
- lxml
- `urllib.robotparser`
- JSON

## Project Structure

```text
backend-ai-scraper/
│
├── cleaner.py
├── extractor.py
├── fetcher.py
├── parser.py
├── saver.py
├── scraper.py
├── requirements.txt
├── .gitignore
│
└── data/
    └── books.json
