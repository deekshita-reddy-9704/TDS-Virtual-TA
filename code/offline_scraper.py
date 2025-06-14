from bs4 import BeautifulSoup
import os

# Input HTML file path
input_file = "../data/discourse/thread1.html"

# Output text file path
output_dir = "../data/discourse"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "thread_1.txt")

# Read the saved HTML file
with open(input_file, "r", encoding="utf-8") as f:
    html_content = f.read()

# Parse with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extract all posts (same cooked divs as in Discourse)
posts = soup.find_all("div", class_="cooked")

# Combine text
thread_text = ""
for post in posts:
    text = post.get_text(separator="\n").strip()
    thread_text += text + "\n\n"

# Save extracted content
if thread_text:
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(thread_text)
    print(f"✅ Extracted and saved thread content to {output_file}")
else:
    print("⚠️ No content extracted.")
