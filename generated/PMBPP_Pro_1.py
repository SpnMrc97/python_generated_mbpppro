import re

def filter_lowercase_underscore_strings(strings):
    """
    Filters a list of strings, returning only those which contain
    sequences of lowercase letters joined with underscores.

    :param strings: List of strings to be filtered
    :return: A list of strings that match the pattern
    """
    pattern = re.compile(r'^[a-z]+(_[a-z]+)*$')
    return [s for s in strings if pattern.match(s)]
