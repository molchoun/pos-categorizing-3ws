import requests
from bs4 import BeautifulSoup


def fetch_article_text(url):
    # headers = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
    #     }
    response = requests.get(url)
    code = response.status_code
    if code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        text = ' '.join([elem.text for elem in soup.select('p , .hdg1')])
        return text
    else:
        print(f"Couldn't fetch address: {url}.\nStatus code: {code}")

