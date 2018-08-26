"""
A simple script to help locate research articles on the Internet. Works only on Windows for now.
Operation:
1) First, copy a text reference to the article to the clipboard. The text should contain one or more of the following:
  Title, author names, DOI number, journal name, issue and page numbers, abstract.
2) Activate the script. It reads the Windows clipboard contents.
3) The script then queries the CrossRef API to find the article best matching the textual reference.
    If the reference is deficient or the article is very new and not yet in the database,
    a wrong article may be identified.
3) The script then opens the article's web page in the default browser.

Author: Joona Rissanen
"""

import win32clipboard
import webbrowser
import urllib
import requests
import json

API_URL = r'https://api.crossref.org/works?query='
CONFIG_FILE = 'config.json'
AUTHOR_EMAIL = 'thequickplotter@gmail.com'


def find_best_matching_doi_url(query_string):
    assert query_string
    total_url = API_URL + urllib.parse.quote_plus(query_string)
    headers = make_headers()
    response_text = requests.get(total_url, headers=headers).text
    match_dict = json.loads(response_text)
    assert match_dict['status'] == 'ok'
    first_match = match_dict['message']['items'][0]
    return first_match['URL']

    
def read_windows_clipboard_contents():
    win32clipboard.OpenClipboard()
    clipboard_contents = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return clipboard_contents


def get_user_email_from_config():
    try:
        with open(CONFIG_FILE, 'r') as config_file:
            text = config_file.read()
            config_dict = json.loads(text)
            email = config_dict.get('email', AUTHOR_EMAIL)
            return email
    except FileNotFoundError:
        print('Configuration file config.json not found. Defaulting to author email, but please restore config.json '
              'with your email address.')
        return AUTHOR_EMAIL


def make_headers():
    return {
        'User-Agent':
            'Article Finder script, (https://github.com/Jomiri/article-finder, mailto:{email})'
            .format(email=get_user_email_from_config())
    }


def open_in_new_browser_tab(url):
    webbrowser.open(url, 2)


def main():
    try:
        query_string = read_windows_clipboard_contents()
        article_doi_url = find_best_matching_doi_url(query_string)
        open_in_new_browser_tab(article_doi_url)
    except Exception:
        return


if __name__ == '__main__':
    main()
