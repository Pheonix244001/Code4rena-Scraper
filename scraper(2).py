import os
import csv
import markdown

# Step 1: Import packages

# Packages required: os, csv, markdown

# Step 2: Loop through markdown files in folder

# Define folder path
folder_path = './'

# Define headings to extract
headings_to_extract = ['High Risk Findings', 'Medium Risk Findings']

# Create a list to store extracted data
data = []

# Loop through each markdown file in folder
for file_name in os.listdir(folder_path):
    # Check if file is a markdown file
    if file_name.endswith('.md'):
        # Read markdown file
        with open(os.path.join(folder_path, file_name), 'r') as f:
            md = f.read()
            # Convert markdown to HTML
            html = markdown.markdown(md)
        # Loop through each line of HTML
        current_heading = ''
        for line in html.split('\n'):
            # Check if line is a heading and in the list of headings to extract
            if line.startswith('<h2>') and any(heading in line for heading in headings_to_extract):
                current_heading = line.replace('<h2>', '').replace('</h2>', '')
            # Check if line contains a link with [H- or [M- in it
            elif current_heading and '[[' in line and ('[H-' in line or '[M-' in line):
                link = line[line.index('[[')+2:line.index(']]')]
                text = line[line.index(']]')+2:].strip()
                # Add data to list
                data.append({'File': file_name, 'Heading': current_heading, 'Link': link, 'Text': text})

# Step 3: Extract headings with [H- or [M- and check for associated links

# Step 4: Create and write to CSV file

# Create CSV file
with open('data.csv', mode='w', newline='') as file:
    # Define CSV writer and headers
    writer = csv.DictWriter(file, fieldnames=['File', 'Heading', 'Link', 'Text'])
    writer.writeheader()
    # Write data to CSV file
    for row in data:
        writer.writerow(row)
