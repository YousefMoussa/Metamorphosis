import PyPDF2

def extract_text_from_pdf(pdf_file, output_file):
    try:
        # Open the PDF file
        with open(pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            
            # Read each page and append its text to a list
            text = [page.extract_text() for page in reader.pages]

        # Join all text and save to a file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('\n'.join(text))

        print(f"Text extracted and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    PDF_FILE = input("Enter the path to the PDF file: ")
    OUTPUT_FILE = 'output.txt'
    extract_text_from_pdf(PDF_FILE, OUTPUT_FILE)
