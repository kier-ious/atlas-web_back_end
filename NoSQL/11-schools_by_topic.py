#!/usr/bin/env python3
"""Where can I learn Python?????"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic"""
    query = {"topics": topic}
    return mongo_collection.find(query)
