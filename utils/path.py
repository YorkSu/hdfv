# -*- coding: utf-8 -*-
"""Path
======

Functions that handles the path of hdf5
"""


import h5py


def is_group(h5, path: str) -> int:
    """Determine if the hdf5 path is Group
    
    Returns:
        code: int
        - 200, Successful
        - 404, Not Found
        - 403, Permission denied 
    """
    try:
        temp = h5[path]
        if not isinstance(temp, h5py.Group):
            return 403
    except Exception:
        return 404
    return 200


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

