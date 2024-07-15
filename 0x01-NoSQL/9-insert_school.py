#!/usr/bin/env python3
""" This module define a function that inserts a new document in a
collection based on kwargs
"""


def list_all(mongo_collection, **kwargs):
    """
    Parameters
        mongo_collection: pymongo collectionobject
        kwargs: dictionary with data to insert

    Return
        _id of the new document
    """

    return mongo_collection.insert_one(kwargs).inserted_id
