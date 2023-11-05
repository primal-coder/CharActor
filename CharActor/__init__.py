from typing import Union as _Union
from .__log__ import logger, log
from ._charactor import dicts as _dicts
from ._charactor import create, BaseCharacters as _BaseCharacters, character_bank
from ._objects._items import _Armory, _Goods

log('Initializing CharActor.')
log('Initializing character bank.')

class _Catalogues:
    log('Initializing catalogues.')
    Armory = None
    Goods = None
    def __init__(self):
        self.Armory = _Armory()
        self.Goods = _Goods()
        
    def get(self, item_name: str = None, grid = None, cell = None):
        if item_name is None:
            return
        if None not in [grid, cell] and isinstance(cell, str):
            cell = grid[cell]
        item_name = item_name
        if item_name in self.Armory:
            return self.Armory.get(item_name, grid, cell)
        elif item_name in self.Goods:
            return self.Goods.get(item_name, grid, cell)
        else:
            print(f'Item {item_name} not found in catalogues.')
            return None

log('Creating catalogue instance.')
        
Catalogues = _Catalogues()

del log, logger