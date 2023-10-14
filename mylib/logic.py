import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """This is a wikipedia fetcher"""

    result = wikipedia.summary(name, length)
    return result


def search_wiki(name):
    """Search Wikipedia"""

    results = wikipedia.search(name)
    return results


def phrase(name):
    """Returns phases from wikipedia"""
    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
