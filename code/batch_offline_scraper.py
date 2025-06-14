from bs4 import BeautifulSoup
import os

# Input & output folders
input_dir = "../data/discourse"
output_dir = "../data/discourse"
os.makedirs(output_dir, exist_ok=True)

# Loop over all HTML files
for filename in os.listdir(input_dir):
    if filename.endswith(".html"):
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, filename.replace(".html", ".txt"))

        # Read HTML content
        with open(input_file, "r", encoding="utf-8") as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, "html.parser")
        posts = soup.find_all("div", class_="cooked")

        thread_text = ""
        for post in posts:
            text = post.get_text(separator="\n").strip()
            thread_text += text + "\n\n"

        # Save extracted text
        if thread_text:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(thread_text)
            print(f"✅ Extracted {filename} -> {output_file}")
        else:
            print(f"⚠️ No content extracted from {filename}")
