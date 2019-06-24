import directory_management as dm
import file_management as fm
import word_fetch as wf
import create_word_check_lists as create_words
import sys
import re


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
    url_words = wf.url_to_list(url)  # Fetch web page url and create list of all elements

    found_nouns = wf.check_against_keyword_lists(url_words, nouns)  # Return a list of matched nouns from URL list
    found_verbs = wf.check_against_keyword_lists(url_words, verbs)  # Return a list of matched verbs from URL list

    # Write the matched nouns and verbs to file before Clean
    fm.write_to_file(wf.remove_duplicate_elements(found_nouns), nouns_before, url)
    fm.write_to_file(wf.remove_duplicate_elements(found_verbs), verbs_before, url)

    url_words = wf.clean_url(url_words)  # Remove HTML, JavaScript, Unwanted Elements
    url_words = wf.remove_duplicate_elements(url_words)  # Remove all duplicated elements

    keywords_remaining = wf.check_against_exclusion_lists(url_words, exclusion_list)  # Remove common words
    found_nouns = wf.check_against_keyword_lists(keywords_remaining, nouns)  # Return a list of matched nouns
    found_verbs = wf.check_against_keyword_lists(keywords_remaining, verbs)  # Return a list of matched verbs

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
    create_words.main()

    default_url = 'https://www.bbc.com/news/world-middle-east-48742972'
    try:
        user_url = sys.argv[1]
        main(user_url)
    except IndexError as e:
        main(default_url)
        print("No URL was specified in the command line. Default URL was used instead."
              "\n sys.argv[] Index Error: {}".format(str(e)), file=sys.stderr)

