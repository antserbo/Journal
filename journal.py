import os


def load(name):
    """
    This method creates and loads a new journal.

    :param name: This base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    filename = get_full_pathname(name)
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readline():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    """
    This method saves (writes) entries to our journal.

    :param name: This base name of the journal to be written in.
    :param journal_data: This is the journal data structure where entries are being written to.
    :return:
    """
    filename = get_full_pathname(name)
    print('..... saving to: {}'.format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    """
    This method returns the absolute path of the file (os-independent).

    :param name: File base name without path.
    :return: Absolute path of the file.
    """
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    """
    This method adds our entry the the journal data structure for further processing.

    :param text: This our entry, simple sentences our words we want to write down.
    :param journal_data: This is the journal data structure where text is saved.
    :return:
    """
    journal_data.append(text)
