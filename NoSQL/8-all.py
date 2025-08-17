#!/usr/bin/env python3
'''Funcion que lista todos los documentos en una colección'''


def list_all(mongo_collection):
    '''lista todos los documentos en una colección'''
    return list(mongo_collection.find())
