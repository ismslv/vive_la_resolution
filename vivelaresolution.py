from ctypes import sizeof
from os.path import realpath,join,dirname,exists,abspath

from funcs import get_file_path, get_resource_path
from screen import ScreenRes, get_current_resolution, get_resolution, set_resolution

# parameters
application_path = ''

# get current resolution
res_current = get_current_resolution()

#check if resolutions file exists
file_path = get_file_path('res.txt')
file_exists = exists(file_path)
if not file_exists:
    # get possible resolutions
    res_possible = get_resolution()

    with open(file_path, 'a') as res_file:
        for r in res_possible:
            res_file.write('%sx%s\n'%(r.w, r.h))
else:
    # read file with resolutions list
    with open(file_path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    # parse resolutions list
    res = []
    for line in lines:
        line_split = line.split('x')
        res.append(ScreenRes(int(line_split[0]), int(line_split[1])))

    # compare resolutions with current
    # -1 if no match
    m_current = -1
    for r in res:
        if r == res_current:
            m_current = res.index(r)
            break

    # select next resolution
    # if -1 select first
    res_new = res[0]
    if -1 < m_current < len(res) - 1:
        res_new = res[m_current + 1]

    # set new resolution
    set_resolution(res_new)