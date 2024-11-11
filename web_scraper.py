import requests
from bs4 import BeautifulSoup


def web_scraper(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Debugging output
        print(f"Status Code: {response.status_code}")
        print(f"Response Length: {len(response.text)}")

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <h2> tags
        articles = soup.find_all('h2')

        if not articles:
            print("No articles found.")

        # Extract and print titles and links
        for article in articles:
            # Get the title text
            title = article.get_text(strip=True)
            # Attempt to find the first <a> tag within the <h2>
            link_tag = article.find('a')

            # If the link tag is not found, check for any <a> in the next sibling
            if not link_tag:
                link_tag = article.find_next('a')  # Check the next <a> tag in the document

            link = link_tag['href'] if link_tag and 'href' in link_tag.attrs else 'No link available'

            # Complete link if necessary
            if link and not link.startswith('http'):
                link = 'https://www.bbc.com' + link

            print(f"Title: {title}")
            print(f"Link: {link}\n")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


# Example URL to scrape
url = 'https://www.bbc.com/news'  # Ensure the URL is accessible
web_scraper(url)
