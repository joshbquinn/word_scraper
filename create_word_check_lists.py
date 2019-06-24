import word_fetch as wf


def write_to_file(items, file_name):

    f = open(file_name, 'w')
    a_list = open(file_name, 'r')
    a_list = a_list.read().split()

    for item in items:
        if item not in a_list:
            f.write(item + '\n')
    f.close()


def main():

    # List Creations

    # Keywords list creation
    verbs = wf.url_to_list('https://www.scrapmaker.com/data/wordlists/language/Verbs(4,874).txt')
    nouns = wf.url_to_list('https://www.scrapmaker.com/data/wordlists/language/Nouns(5,449).txt')

    # Exclusion word list creation
    common = wf.url_to_list('https://www.scrapmaker.com/data/wordlists/language/Transitionalwords(72).txt')
    adjectives = wf.url_to_list('https://gitgud.malvager.net/zed/WaaS/raw/master/src/adjectives1.txt')
    prepositions = wf.url_to_list('https://www.scrapmaker.com/data/wordlists/language/prepositions.txt')
    # conjunctions = url_to_list()
    # pronouns = url_to_list()
    # determiners = url_to_list()

    # Write word lists to file in project directory
    write_to_file(verbs, 'verbs')
    write_to_file(nouns, 'nouns')

    # Write exclusion word lists to same file in project directory
    write_to_file(wf.remove_duplicate_elements(common), 'common')
    write_to_file(wf.remove_duplicate_elements(adjectives), 'common')
    write_to_file(wf.remove_duplicate_elements(prepositions), 'common')


if __name__ == '__main__':
    main()
