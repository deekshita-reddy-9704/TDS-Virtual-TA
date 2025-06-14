import os
import fitz  # PyMuPDF

# Input and output folders
input_dir = "../data/course_content"
output_dir = "../data/course_content_extracted/pdf"
os.makedirs(output_dir, exist_ok=True)

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def process_all_pdfs():
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                rel_path = os.path.relpath(pdf_path, input_dir)
                output_path = os.path.join(output_dir, rel_path.replace('.pdf', '.txt'))

                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                print(f"Extracting: {pdf_path}")
                text = extract_text_from_pdf(pdf_path)

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(text)

                print(f"✅ Saved: {output_path}")

if __name__ == "__main__":
    process_all_pdfs()
