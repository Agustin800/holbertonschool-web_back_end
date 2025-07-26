#!/usr/bin/env python3

'''funcion que lanzar múltiples esperas en paralelo y devolver
los tiempos ordenados.'''


import asyncio
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''retorna la lista con todas las esperas dentro'''
    delays = []
    tasks = [wait_random(max_delay) for a in range(n)]

    for task in asyncio.as_completed(task):
        delay = await task
        delays.append(delay)
    
    return delays
