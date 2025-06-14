import requests
from bs4 import BeautifulSoup
import os
import time

# Create output folder inside data/discourse
output_dir = "../data/discourse"
os.makedirs(output_dir, exist_ok=True)

# Example thread URL you provided
thread_url = "https://discourse.onlinedegree.iitm.ac.in/t/project1-virtual-ta-discussion-thread-tds-may-2025/176077/1"

# Headers (pretend to be a browser)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Scrape the thread
def scrape_thread(url):
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch: {url}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all posts in the thread
    posts = soup.find_all("div", class_="cooked")
    
    thread_text = ""
    for post in posts:
        text = post.get_text(separator="\n").strip()
        thread_text += text + "\n\n"

    return thread_text

# Actually scrape
thread_content = scrape_thread(thread_url)

# Save the scraped text
if thread_content:
    output_file = os.path.join(output_dir, "thread_1.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(thread_content)
    print(f"Saved thread to {output_file}")
else:
    print("Nothing scraped.")
