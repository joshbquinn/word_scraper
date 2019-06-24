
def write_to_file(items, file_name, url_string):
    """Write items from a list to a specified file if the items do not already exist in the file.
    Add the url string to the top of the file for source address.

    Args:
        items: A list to write to a file
        file_name: The specified file name to write the list to.
        url_string: The URL the list of words has been created from.

    """
    f = open(file_name, 'w')
    a_list = open(file_name, 'r')
    a_list = a_list.read().split()

    f.write('URL Source: ' + url_string + '\n\n')

    for item in items:
        if item not in a_list:
            f.write(item + '\n')

    f.close()


def create_list_from_file(file_path):
    """Write word one per line to text file.

    Args:
        file_path: A file path to return a list of items from.

    Returns:
        a_list: a list of all items as strings from the specified file path
    """

    f = open(file_path)
    a_list = set(f.read().split())
    f.close()
    return a_list
