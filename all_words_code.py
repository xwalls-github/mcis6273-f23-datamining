# Xavier Walls
# MCIS-6273-F2 Data Mining

import csv
import re
import urllib.request
from collections import Counter

# Function to tokenize text and count word frequencies
def tokenize_text(text):
    # Split the text into words while preserving contractions (e.g., can't)
    words = re.findall(r'\b[\w\']+\b', text.lower())
    return words

# URL of the text file
url = "https://www.gutenberg.org/cache/epub/5827/pg5827.txt"

# Download the text file
response = urllib.request.urlopen(url)
text = response.read().decode('utf-8')

# Tokenize the text and count word frequencies
word_list = tokenize_text(text)
word_counts = Counter(word_list)

# Write the results to a CSV file
with open("mcis6273-f23-datamining/all_words.csv", "w", newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header
    csv_writer.writerow(["Word", "Frequency"])
    
    # Write word frequencies
    for word, frequency in word_counts.items():
        csv_writer.writerow([word, frequency])

print("Word frequencies saved to 'all_words.csv'.")