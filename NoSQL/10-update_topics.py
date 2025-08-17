#!/usr/bin/env python3
'''Funcion que cambia todos los temas (topics) de un
documento de la colección school según el nombre'''


def update_topics(mongo_collection, name, topics):
    '''cambia todos los temas (topics) de un
    documento de la colección school según el nombre'''
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
