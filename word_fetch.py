from urllib.request import urlopen
import re



def url_to_list(url):
    """Write one word per line to to a list

    Args:
        url: A URL of any kind that to create a list of all page elements

    Returns:
        web_page_contents: A list of all elements on the page
    """
    with urlopen(url) as web_page:
        web_page_contents = []
        for line in web_page:
            line_contents = line.decode('utf-8').split()
            for element in line_contents:
                web_page_contents.append(element)
        return web_page_contents


def remove_duplicate_elements(items):
    """Remove all elements that are the same text. A dictionary is unable to hold duplicate keys. To remove duplicate
    values from the list we create a dictionary from the list values using the fromkeys function and wrap it in a list
    constructor. This allows a list to be returned without duplicate values.

    Args:
        items: a list of items
    Returns:
        A list of items without duplicate values
    """
    return list(dict.fromkeys(items))


def clean_url(items):
    """Remove unwanted elements from the URL list.

    A string is made from the list of items.
    Four regex patterns are created to pass into the re.sub() method to clean the URL string.
    These specify Javascript code and tags; style tags and enclosed HTML; Special characters; and all HTML tags.
    The cleaned string is split into a list of elements once again and returned.

    Args:
        items: A list.
    Returns:
        clean_list: A list of items with removed elements.
    """

    url_string = ' '.join(items)

    paragraphs = re.findall(r'<p>(.*?)</p>', url_string)
    h_tags = re.findall(r'<h.*?>(.*?)</.*?h.*?>', url_string)

    url_string = ' '.join(paragraphs + h_tags)

    heads = re.compile(r'<he.*?>(.*?)</.*?he.*?>')
    scripts = re.compile(r'<script.*?/script>*.')
    style = re.compile(r'<style.*?/style>')
    specials = re.compile(r'[^A-Za-z0-9]+')
    remove_tags = re.compile(r'<.*?>')
    remove_numbers = re.compile(r'(?<!\S)[+-]?\d+(?!\S)')

    clean_string = re.sub(heads, '', url_string)
    clean_string = re.sub(scripts, '', clean_string)
    clean_string = re.sub(style, '', clean_string)
    clean_string = re.sub(remove_tags, '', clean_string)
    clean_string = re.sub(specials, ' ', clean_string)
    clean_string = re.sub(remove_numbers, '', clean_string)

    clean_list = list(clean_string.split())
    return clean_list


def check_against_exclusion_lists(items, exclusions):
    """Check the list of URL words against a list of words to exclude from keyword list. Iterate through items and
    check if word in items exists in exclusions. If so, remove the word from list.

    Args:
        items: a list of all remaining words from the URL to create a keyword list from.
        exclusions: a list of words that should be excluded from the keyword list.
    Returns:
        items: the update list of URL words excluding any words found in the exlucsion list.

    """
    for word in items:
        if word in exclusions:
            items.remove(word)
    return items


def check_against_keyword_lists(items, keywords):
    """Check a list of words against a list of words to include (such as nouns, verbs, keywords). Iterate through items
    and if word in items is in keywords then append this word to a new list stored_words.

    Args:
        items: A list of words from the URL
        keywords: A list of words to check the URL words against
    Returns:
        stored_words: A list of keywords to store as a separate list.
    """
    stored_words = []
    for word in items:
        if word in keywords:
            stored_words.append(word)
    return stored_words
