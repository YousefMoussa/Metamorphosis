import PyPDF2

def extract_text_from_pdf(pdf_file, output_file='output.txt'):
    try:
        # Open the PDF file
        with open(pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            
            # Read each page and append its text to a list
            text = [page.extract_text() for page in reader.pages]

        # Join all text and save to a file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('\n'.join(text))

    except Exception as e:
        print(f"An error occurred: {e}")
 
    return output_file
def clean_file(input_filename):
    try:
        cleaned_lines = []

        with open(input_filename, 'r') as input_file:
            for line in input_file:
                # Replace non-alphabetic and non-digit characters with spaces
                cleaned_line = ''.join(char if char.isalpha() or char.isdigit() else ' ' for char in line)
                cleaned_lines.append(cleaned_line)

     

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    return(cleaned_lines)


if __name__ == "__main__":
    PDF_FILE = input("Enter the path to the PDF file: ")
    OUTPUT_FILE = 'output.txt'
    extract_text_from_pdf(PDF_FILE, OUTPUT_FILE)

