import re
import argparse

# thanks https://www.reddit.com/r/pandoc/comments/17tsijd/render_htmlsyntax_images_in_pdf_from_markdown/

def adjust_content(input_file):
    # Read the contents of the input file
    with open(input_file, 'r') as file:
        content = file.read()

    content = content.replace('$$', '$')

    content = content.replace('{% comment %}', '<!--')
    content = content.replace('{% endcomment %}', '-->')
    content = content.replace('.svg', '.png')

    # Define a regular expression to match the HTML-style image pattern
    pattern = r'<img\s+src="{{ site.baseurl }}(/[^"]+)"\s+alt="([^"]*)"(?:\s+width="([^"]*)")?[^>]*>'

    # Replace the HTML-style image pattern with equivalent Markdown syntax with width attribute
    new_content = re.sub(pattern, lambda m: f'![{m.group(2)}]({m.group(1).lstrip("/")}){{ width={m.group(3)} }}' if m.group(3) else f'![{m.group(2)}]({m.group(1).lstrip("/")})', content)

    # Print the adjusted content to be piped into Pandoc
    print(new_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Adjust HTML-style image syntax in Markdown.')
    parser.add_argument('input_file', help='Path to the input Markdown file')

    args = parser.parse_args()

    adjust_content(args.input_file)