"""This modules defines a function that returns the list of
school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Parameter
        mongo_collection: pymongo collection object
        topic: will be topic searched
    """

    return mongo_collection.schools_by_topic.find({topic: "topic"})
