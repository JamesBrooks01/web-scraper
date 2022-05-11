from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report

def test_satalite_url_count():
  actual = get_citations_needed_count("https://en.wikipedia.org/wiki/$50SAT")
  expected = 1
  assert actual == expected

def test_mexico_url_count():
  actual = get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")
  expected = 5
  assert actual == expected