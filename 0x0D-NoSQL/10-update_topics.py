#!/usr/bin/env python3
""" mongodb
Python function that inserts a new document in a collection based on kwargs
"""


def update_topics(mongo_collection, name, topics):
    """
    update_topics
    """
    if mongo_collection is None:
        return None
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
