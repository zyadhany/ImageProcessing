import pickle

def file_load(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

def save_as(obj, filename):
    """ save changes into file. """
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)