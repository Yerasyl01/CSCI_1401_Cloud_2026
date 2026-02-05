from pypdf import PdfReader
import sys

def extract_text(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        pdf_path = r"C:\Users\byabz\.gemini\antigravity\brain\68718b3f-8c56-4ce5-925a-7ea2e408a7e4\.tempmediaStorage\12beaee423783ade.pdf"
    
    content = extract_text(pdf_path)
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(content)
