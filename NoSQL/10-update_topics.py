#!/usr/bin/env python3
"""Change school topics"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on name"""
    document = mongo_collection.update({'name': name, '$set': {'topics': topics}}, {'many': True})
    return document