#!/usr/bin/python3
"""
Python function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """schools_by_topic"""
    if mongo_collection is None:
        return None
    return mongo_collection.find({"topics": topic})
