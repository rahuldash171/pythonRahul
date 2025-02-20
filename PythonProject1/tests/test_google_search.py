from pages.base_page  import GooglePage

def test_google_search(browser):
    google = GooglePage(browser)
    google.open_google()
    google.search("Selenium Python")
    assert "Selenium Python - Google Search" in browser.title
