#!/usr/bin/env python3
"""This module defines a function that returns the list of
schools having a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Parameters
        mongo_collection: pymongo collection object
        topic: string, the topic to search for
    Returns
        A list of schools having the specified topic
    """
    # Query to find documents where 'topics' field contains the specified topic
    query = {"topics": topic}
    
    # Execute the query and return the list of matching documents
    return list(mongo_collection.find(query))
