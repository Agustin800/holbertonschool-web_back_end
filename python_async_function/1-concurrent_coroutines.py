#!/usr/bin/env python3

'''funcion que lanzar múltiples esperas en paralelo y devolver
los tiempos ordenados.'''


import asyncio
from typing import List
from 0-basic_async_syntax.py import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''c+retorna la lista con todas las esperas dentro'''
    delays = []
    task = [wait_random(max_delay) for a in range(n)]

    for task in asyncio.as_completed(task):
        delay = await task
        delays.append(delay)
    
    return delays
