#!/usr/bin/env python3
"""Func that inserts a new doc in a collection"""


def insert_school(mongo_collection, **kwargs):
    """Inserting that info!"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
