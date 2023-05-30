import os
import csv
import markdown

# Define the headings you want to extract
headings_to_extract = ['High Risk Findings', 'Medium Risk Findings']

# Create a list to store the extracted data
data = []

# Loop through each markdown file in the folder
for file in os.listdir():
    # Check if the item in the directory is a file and ends with .md extension
    if os.path.isfile(file) and file.endswith('.md'):
        # Parse the markdown file
        with open(file, 'r') as f:
            md = f.read()
            html = markdown.markdown(md)
        
        # Extract the headings and associated links
        for line in html.split('\n'):
            for heading in headings_to_extract:
                if heading in line:
                    start_index = line.index('[')
                    end_index = line.index(']', start_index)
                    link = line[start_index+1:end_index]
                    text = line[end_index+1:].strip()
                    data.append({'File': file, 'Heading': text, 'Link': link})

# Write the data to a CSV file
with open('report_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['File', 'Heading', 'Link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in data:
        writer.writerow(item)
