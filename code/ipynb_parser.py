import os
import json

# Input and output folders
input_dir = "../data/course_content"
output_dir = "../data/course_content_extracted/ipynb"
os.makedirs(output_dir, exist_ok=True)

def extract_text_from_ipynb(ipynb_path):
    text = ""
    try:
        with open(ipynb_path, "r", encoding="utf-8") as f:
            notebook = json.load(f)

        for cell in notebook.get("cells", []):
            if cell.get("cell_type") in ["markdown", "code"]:
                cell_text = ''.join(cell.get("source", []))
                text += cell_text + "\n\n"
    except Exception as e:
        print(f"Error reading {ipynb_path}: {e}")
    return text

def process_all_ipynb():
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".ipynb"):
                ipynb_path = os.path.join(root, file)
                rel_path = os.path.relpath(ipynb_path, input_dir)
                output_path = os.path.join(output_dir, rel_path.replace('.ipynb', '.txt'))

                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                print(f"Extracting: {ipynb_path}")
                text = extract_text_from_ipynb(ipynb_path)

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(text)

                print(f"✅ Saved: {output_path}")

if __name__ == "__main__":
    process_all_ipynb()
