#!/usr/bin/env python3
""" This module defines a function that inserts a new document in a
collection based on kwargs
"""

def insert_new(mongo_collection, **kwargs):
    """
    Parameters
        mongo_collection: pymongo collection object
        kwargs: dictionary with data to insert

    Returns
        _id of the new document
    """
    return mongo_collection.insert_one(kwargs).inserted_id