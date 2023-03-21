# This script converts Microsoft Word files into Markdown.
# How to use: python doc_to_md.py input.docx output.md.

import os
import sys
import argparse
from docx import Document
import markdown

def convert_docx_to_md(input_path, output_path):
    document = Document(input_path)
    text = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])
    md = markdown.markdown(text)
    with open(output_path, 'w') as f:
        f.write(md)

def main():
    parser = argparse.ArgumentParser(description='Convert .docx files to Markdown.')
    parser.add_argument('input_path', help='path to input .docx file')
    parser.add_argument('output_path', help='path to output .md file')
    args = parser.parse_args()

    if not os.path.isfile(args.input_path):
        print('Error: input file does not exist.')
        sys.exit(1)

    if os.path.splitext(args.input_path)[1] not in ('.doc', '.docx'):
        print('Error: input file must be a .doc or .docx file.')
        sys.exit(1)

    convert_docx_to_md(args.input_path, args.output_path)
    print(f'Successfully converted {args.input_path} to {args.output_path}.')

if __name__ == '__main__':
    main()
