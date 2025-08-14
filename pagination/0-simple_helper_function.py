#!/usr/bin/env python3

'''funcion que para calcular el rango de índices para paginación'''


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Calcula el índice inicial y final para obtener una página de elementos
    de una lista'''
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
