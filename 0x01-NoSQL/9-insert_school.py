""" This module define a function that inserts a new document in a
collection based on kwargs
"""


def list_all(mongo_collection):
    """Python function that inserts a new document in a 
    collection based on kwargs:
    """

    return mongo_collection.insert_one(kwargs).insert_id