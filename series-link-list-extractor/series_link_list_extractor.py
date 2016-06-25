import urllib.request
from bs4 import BeautifulSoup

def get_title_of(result_container):
    return result_container['title']

def get_link_of(result_container):
    for c in result_container.contents[0].contents:
        if c.name == 'a':
            return c['href']

########
# Main #
########
req = urllib.request.Request('http://indavideo.hu/search/text/csillagkapu?channel_constraint=undefined')
with urllib.request.urlopen(req) as response:
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    search_result_containers = soup.find_all('div', 'item TYPE_8   ')
    result = [(get_title_of(c), get_link_of(c)) for c in search_result_containers]

    print(result)
    print('{} results found'.format(len(result)))