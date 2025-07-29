#!/usr/bin/env python3

'''funcion que genera 10 números aleatorios entre 0 y 10 con una pausa de 1 segundo.'''


import random
import asyncio


async def async_generator():
    '''genera 10 números aleatorios entre 0 y 10
    con una pausa de 1 segundo.'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
