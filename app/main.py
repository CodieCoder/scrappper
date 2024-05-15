from bs4 import BeautifulSoup
import requests
import csv

def get_children_text_only(element):
  """
  Extracts text content from all children of an element recursively.
  """
  text = ""
  for child in element.children:
    if isinstance(child, str):  # Check if child is a string (text content)
      text += child.strip()  # Add text content with leading/trailing whitespace removed
    elif child.name is not None:  # Check if child is a tag (not comment, etc.)
      text += get_children_text_only(child)  # Recursively call for child elements
  return text


page_to_scrape = requests.get("http://quotes.toscrape.com")

soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# title = soup.findAll("span", attrs={"id":"clean_title"})
title = soup.findAll("span", attrs={"class":"text"})
# authors = soup.findAll("p", attrs={"id":"body"})
authors = soup.findAll("small", attrs={"class":"author"})

# sosls = soup.

file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)

writer.writerow(["QUOTES", "AUTHORS"])

print(page_to_scrape)
for quote, author in zip(title, authors):
    print(quote.text + " - ", author.text)
    writer.writerow([quote.text, author.text])
file.close()

