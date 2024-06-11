#!/usr/bin/env python3
"""List all docs in Python"""


def list_all(mongo_collection):
    """Listing docs from collection"""
    documents = list(mongo_collection.find())

    return documents
