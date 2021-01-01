# -*- coding: utf-8 -*-
"""Path
======

Functions that handles the path of hdf5
"""


import h5py


def get_type(h5, path: str) -> int:
    """Get the type of hdf5 path
    
    Returns:
        code: int
        - 100, Hdf5 File
        - 101, Hdf5 Group
        - 102, Hdf5 Dataset
        - 400, Unknown Error
        - 404, Not Found
    """
    try:
        temp = h5[path]
        if isinstance(temp, h5py.File):
            return 100
        if isinstance(temp, h5py.Group):
            return 101
        if isinstance(temp, h5py.Dataset):
            return 102
    except Exception:
        return 404
    return 400


def is_win_abs(path: str) -> bool:
    return len(path) > 1 and path[1] == ':'


def is_abs(path: str) -> bool:
    return is_win_abs(path) or path[0] == '/'


def next(path: str) -> str:
    if path != '/':  # Ignore root
        path = '/' + '/'.join(path.split('/')[1:-1])
    return path


def add(pwd: str, path: str) -> str:
    path = path.strip()
    if not path:
        return pwd
    if pwd == '/':  # root directory
        pwd += path
    else:
        pwd += '/' + path
    return pwd


def relative(pwd: str, path: str) -> str:
    if path == '.':  # this directary
        pass
    elif path == '..':  # next directory
        pwd = next(pwd)
    else:
        pwd = add(pwd, path)
    return pwd


def change(pwd: str, path: str) -> str:
    if is_win_abs(path):  # win absolute path
        return path
    if is_abs(path):  # absolute path
        pwd = '/'
    for p in path.split('/'):
        pwd = relative(pwd, p)
    return pwd


def to_related(path: str) -> str:
    if is_win_abs(path):
        return path
    if is_abs(path):
        return '.' + path
    return './' + path


if __name__ == '__main__':
    _pwd = '/foo/bar'
    print(next(_pwd))
    print(add(_pwd, 'bar'))
    print(relative(_pwd, '.'))
    print(relative(_pwd, '..'))
    print(relative(_pwd, 'bar'))
    print(change(_pwd, '/'))
    print(change(_pwd, '..'))
    print(change(_pwd, '../..'))
    print(change(_pwd, 'abc'))
    print(change(_pwd, '/abc'))
    print(change(_pwd, '../abc'))

