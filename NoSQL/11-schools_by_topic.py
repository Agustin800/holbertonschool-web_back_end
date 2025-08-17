#!/usr/bin/env python3
'''Funcion que devuelve la lista de escuelas que tienen un tema específico'''


def schools_by_topic(mongo_collection, topic):
    '''devuelve la lista de escuelas que tienen un tema específico'''
    return list(mongo_collection.find({"topics": topic}))
