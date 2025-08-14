#!/usr/bin/env python3

'''funcion que espera un tiempo entre 0 y 10'''


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
