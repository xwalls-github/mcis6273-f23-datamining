import re
import csv
from collections import Counter
from urllib import request

# URL of the text file
url = "https://www.gutenberg.org/cache/epub/5827/pg5827.txt"

# Function to download the text from the URL
def download_text(url):
    response = request.urlopen(url)
    return response.read().decode("utf-8")

# Download the text file from the web
text = download_text(url)

# Tokenize the text and filter out words starting with an uppercase letter
tokens = re.findall(r"\b[A-Z][A-Za-z']*\b", text)

# Count the frequency of each word
word_counts = Counter(tokens)

# Sort the words by frequency in descending order
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Write the results to a CSV file named all_words_starting_with_uppercase.csv
with open("all_words_starting_with_uppercase.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(sorted_words)
