import requests
from bs4 import BeautifulSoup

def extract_direct_link(terabox_url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(terabox_url, headers=headers)

    if res.status_code != 200:
        return None

    soup = BeautifulSoup(res.text, "html.parser")
    for script in soup.find_all("script"):
        if 'downloadLink' in script.text:
            text = script.text
            start = text.find("downloadLink") + len("downloadLink\":\"")
            end = text.find("\"", start)
            link = text[start:end]
            return link.replace("\\u002F", "/")
    return None
