#!/usr/bin/env python3
'''Funcion que inserta un nuevo documento en una colección usando kwargs'''


def insert_school(mongo_collection, **kwargs):
    '''inserta un nuevo documento en una colección usando kwargs'''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
