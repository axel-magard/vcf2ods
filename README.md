# vCard to ODS Converter

This script converts vcf (Virtaul Contacts File) files to ods (Open Document Spreadsheet) files.

## Features

1. **Fix vCard files**: The script handles vCard files that split long lines across multiple lines with an equals sign (`=`). It combines these lines into a single line in a new vCard file.

2. **Convert vCard to ODS**: The script reads the fixed vCard file and writes the contact information into a ODS file. The ODS file includes columns for the contact's 

- name
- address
- max. 2 telephone numbers
- max. 2 email addresses
- notes

## How to Run

1. Make sure you have the required Python packages installed by running:  
   `pip install vobject pyexcel_ods3 optparse`
2. Run the script in a Python environment:  
   `python vcf2ods.py VCF_FILE `
