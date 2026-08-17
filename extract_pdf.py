
import sys
import re

def extract_text(file_path):
    try:
        # Try importing pypdf (common library)
        try:
            from pypdf import PdfReader
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        except ImportError:
            pass
        
        # Fallback: simple string extraction for uncompressed PDFs (very basic)
        with open(file_path, 'rb') as f:
            content = f.read()
            # Find streams of text between brackets (basic PDF structure)
            # This is very rough and might not work for compressed streams
            text_content = re.findall(b'\((.*?)\)', content)
            return "\n".join([t.decode('utf-8', errors='ignore') for t in text_content])

    except Exception as e:
        return f"Error reading PDF: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf.py <file_path>")
        sys.exit(1)
    
    print(extract_text(sys.argv[1]))
