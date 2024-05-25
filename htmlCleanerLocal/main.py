import re
import html
# to copy the whole HTML page use this command on dev console => copy(document.documentElement.outerHTML);
def clean_html(html_content):
    # Decode HTML entities
    decoded_text = html.unescape(html_content)
    # Remove all HTML tags
    clean_text = re.sub(r'<[^>]*>', '', decoded_text)
    # Remove extra spaces and newlines
    clean_text = re.sub(r'\n\s*\n', '\n', clean_text)
    return clean_text.strip()

def clean_html_file(input_file, output_file):
    # Read HTML content from input file
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Clean the HTML content
    cleaned_text = clean_html(html_content)
    
    # Write cleaned text to output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

# Input and output file paths
input_file_path = 'input.html'
output_file_path = 'output.txt'

# Clean HTML content from input file and write to output file
clean_html_file(input_file_path, output_file_path)
