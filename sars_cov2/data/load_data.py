def str_to_int(s):
    """Convert a given string s to integer if possible.

    If the conversion fails, return the string.

    :param s: A string to convert.
    :return: An integer or the string.
    """
    try:
        return int(s)
    except ValueError:
        return s


def load_data(dataset):
    """Loads the given data sets and returns a dictionary.

    :param dataset: The path to the data set to load.
    :return: A dictionary containing the data set.
    """
    header = None
    data = dict()
    with open(dataset) as fp:
        for row in fp:
            row = row.strip('\n')
            if len(data) == 0:
                header = row.split(' ')
                for h in header:
                    data[h] = []
            else:
                r = row.split(' ')
                for idx, h in enumerate(header):
                    data[h].append(str_to_int(r[idx]))
    return data
