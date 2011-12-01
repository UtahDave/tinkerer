'''
    Tinkerer utility functions
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2011 by Vlad Riscutia
'''
import os
import re
import tinkerer


# create filename from title replacing non-alphanumeric characters with "_"
def filename_from_title(title):
    return re.sub(r"[\W_]", "_", title)


# recursively create path and return it as string
def get_path(*args):
    path = os.path.join(*args)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

