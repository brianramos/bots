import requests

from lxml import etree

def getEvents(url):
    print("\nsomeone used the bot\n")
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