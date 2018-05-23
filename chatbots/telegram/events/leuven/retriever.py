import requests

from lxml import etree

def getEvents(url):
    r = requests.get(url)
    parser = etree.XMLParser(recover=True)
    rss_tree = etree.fromstring(r.content, parser)

    titles = rss_tree.xpath('/rss/channel/item/title')
    hyperlinks = rss_tree.xpath('/rss/channel/item/link')

    events_list = (titles, hyperlinks)
    response_message = "Here are today's events:\n\n\n"

    i = 0
    while i < len(events_list[0]) and i < 5:
        title = events_list[0][i].text
        hyperlink = events_list[1][i].text
        response_message = response_message + "Event Title: " + title + "\n\nEvent Link: " + hyperlink + '\n\n\n'
        i = i + 1

    return response_message

def getCategories():
    return "/free_concerts /free_fitness"

def getSearch(message):
    search_term = message[8:len(message)]
    url = 'https://www.uitinvlaanderen.be/agenda/search/rss?search=' + search_term + '&facet%5Bdatetype%5D%5B0%5D=today&facet%5Bcategory_flandersregion_id%5D%5B0%5D=reg.16'
    return getEvents(url)