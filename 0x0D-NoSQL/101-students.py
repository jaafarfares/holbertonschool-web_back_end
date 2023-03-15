#!/usr/bin/env python3
"""
Python function that returns all students sorted by average score.
"""


def top_students(mongo_collection):
    """top_students"""
    top = [
        {"$unwind": "$topics"},
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "scores": {"$push": "$topics.score"}
            }
        },
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "averageScore": {"$avg": "$scores"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(top))
