import os
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

USERNAME = "ariazi"  # Replace with your actual username
YEAR = "2026"
URL = f"https://app.thestorygraph.com/stats/{USERNAME}?year={YEAR}"

# Scrape StoryGraph Stats Page
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # StoryGraph stores genre info in chart blocks/labels
    # Extract top genres and counts (Example parsing logic)
    genres = []
    counts = []
    
    # Target genre elements from the rendered stats page
    genre_section = soup.find("div", id="genres-stats")
    if genre_section:
        for row in genre_section.find_all("div", class_="stat-row")[:6]: # Top 6 genres
            name = row.find("span", class_="genre-name").text.strip()
            count = int(row.find("span", class_="count").text.strip())
            genres.append(name)
            counts.append(count)

    # Plot Bar Chart
    plt.figure(figsize=(8, 4))
    plt.barh(genres, counts, color="#3776AB")
    plt.xlabel("Books Read")
    plt.title(f"Reading Genres ({YEAR})")
    plt.gca().invert_yaxis()  # Top genre at the top
    plt.tight_layout()
    
    # Save chart as SVG
    os.makedirs("assets", exist_ok=True)
    plt.savefig("assets/genre_stats.svg", format="svg", transparent=True)
