#!/usr/bin/env python3

'''funcion que mide el tiempo de ejecucion'''


import asyncio
import time
import importlib
wait = importlib.import_module('1-concurrent_coroutines').wait


def measure_time(n: int, max_delay: int) -> float:
    '''usa time para medir el intervalo de ejecucion usando
    el reloj de alta resolucion'''
    start = time.perf_counter()
    asyncio.run(wait(n, max_delay))
    end = time.perf_counter()
    total = start - end
    return total / n
