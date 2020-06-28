_world = {}
starting_position = (0, 0)
import os
import sys

import pkgutil

def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname('map.txt')

    return os.path.join(datadir, filename)


def tile_exists(x, y):
        return _world.get((x, y))


def load_tiles():
    with open(find_data_file('map.txt')) as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')
            if tile_name == 'SpawnRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = '' if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)
