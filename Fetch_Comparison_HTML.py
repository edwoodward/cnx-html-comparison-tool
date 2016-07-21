import json
import requests
from bs4 import BeautifulSoup


def get_page_json(page_url):
    """
    Retrieves json for the given page id
    :param page_id: page id to fetch json for
    :return: page json
    """
    r = requests.get(page_url)
    return json.loads(r.text)

def get_html(page_url, tag):
    """
    Gets json, extracts HTML and saves page
    :param page_url: URL to fetch
    :param tag: cnx or cte
    """
    json1 = get_page_json(page_url)
    html = json1["content"]
    soup = BeautifulSoup(html, 'html.parser')
    write_file(soup.prettify(), json1["title"] + tag)


def write_file(html, book_title):
    """
    writes given html as given file name (book_title)
    :param html: HTML to save
    :param book_title: name for file
    """
    f = open(book_title + ".html", "w")
    f.write(html)
    f.close()

url1 = "http://archive.cnx.org/contents/fb9f0233-8f5e-45d6-ae68-6ee09d563baa.json"
url2 = "http://archive-cte-cnx-dev.cnx.org/contents/SQ2s9bxF@1.6:3ImooXPD@2.json"

get_html(url1, "-cnx")
get_html(url2, "-cte")


