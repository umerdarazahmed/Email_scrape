import requests
import re
import csv

# Define the URL to scrape
url = "https://www.geeksforgeeks.org/python-programming-language/"

# Send a GET request to the URL
response = requests.get(url)

# Extract the HTML content from the response
html_content = response.text

# Find all email addresses using regular expression
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', html_content)

# Create a CSV file and write the emails to it
with open('emails.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Email'])

    for email in emails:
        writer.writerow([email])

print("Emails scraped and saved to emails.csv file.")
