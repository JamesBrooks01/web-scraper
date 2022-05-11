import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
  URL = url
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  citations = soup.find_all(class_='Template-Fact')
  print(len(citations))
  return len(citations)


def get_citations_needed_report(url):
  URL = url
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  citations = soup.find_all(class_='Template-Fact')
  for cite in citations:
    print(cite.parent.text)
    return cite.parent.text
