#!/usr/bin/env python3
"""This module define a function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """Python function that lists all documents in a collection"""

    return [document for document in mongo_collection.find()]
