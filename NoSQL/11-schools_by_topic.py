#!/usr/bin/env python3
"""Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """Returns list of school having a specific topic"""
    docs = mongo_collection.find({"topics": topic})
    return docs