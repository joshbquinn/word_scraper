from urllib.request import urlopen
import re
import directory_management as dm
import file_management as fm


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

    # scripts = re.compile(r'<script\s.*?/script>*.' or r'<noscript.*?/noscript>')
    scripts = re.compile(r'<script.*?/script>*.')
    style = re.compile(r'<style.*?/style>')
    specials = re.compile(r'[^A-Za-z0-9]+')
    clean = re.compile(r'<.*?>')

    clean_string = re.sub(scripts, '', url_string)
    clean_string = re.sub(style, '', clean_string)
    clean_string = re.sub(clean, '', clean_string)
    clean_string = re.sub(specials, ' ', clean_string)

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


def main(url):

    directory = re.sub(r'[^a-zA-Z0-9 \n\.]', '_', url)  # Strip special chars from URL to create correct directory name
    directory_name = dm.unique_directory(directory) # Create a unique directory name with time stamp
    dm.create_directory(directory_name)  # Create a unique directory for each word scrape

    # Create file names
    nouns_before = f'before_matched_nouns_{directory_name}'
    verbs_before = f'before_matched_verbs_{directory_name}'
    nouns_after = f'after_matched_nouns_{directory_name}'
    verbs_after = f'after_matched_verbs_{directory_name}'
    keywords = f'matched_keywords_{directory_name}'

    # Create word lists from text files
    exclusion_list = fm.create_list_from_file('common')
    nouns = fm.create_list_from_file('nouns')
    verbs = fm.create_list_from_file('verbs')
    url_words = url_to_list(url)  # Fetch web page url and create list of all elements

    found_nouns = check_against_keyword_lists(url_words, nouns)  # Return a list of matched nouns from URL list
    found_verbs = check_against_keyword_lists(url_words, verbs)  # Return a list of matched verbs from URL list

    # Write the matched nouns and verbs to file before Clean
    fm.write_to_file(remove_duplicate_elements(found_nouns), nouns_before, url)
    fm.write_to_file(remove_duplicate_elements(found_verbs), verbs_before, url)

    url_words = clean_url(url_words)  # Remove HTML, JavaScript, Unwanted Elements
    url_words = remove_duplicate_elements(url_words)  # Remove all duplicated elements

    keywords_remaining = check_against_exclusion_lists(url_words, exclusion_list)  # Remove common words
    found_nouns = check_against_keyword_lists(keywords_remaining, nouns)  # Return a list of matched nouns
    found_verbs = check_against_keyword_lists(keywords_remaining, verbs)  # Return a list of matched verbs

    # Write all matched words to a file if they don't already exist there

    fm.write_to_file(found_nouns, nouns_after, url)
    fm.write_to_file(found_verbs, verbs_after, url)

    # Write the remaining words from the website to the keywords file
    fm.write_to_file(keywords_remaining, keywords, url)

    # Write files to directory
    dm.write_to_directory(nouns_before, directory_name)
    dm.write_to_directory(verbs_before, directory_name)
    dm.write_to_directory(nouns_after, directory_name)
    dm.write_to_directory(verbs_after, directory_name)
    dm.write_to_directory(keywords, directory_name)


if __name__ == '__main__':
    url = 'https://www.rte.ie/news/2019/0621/1056733-iceland-rockall/'
    main(url)
