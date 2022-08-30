from dataclasses import dataclass
import string
import itertools
import re
from screeninfo import get_monitors
import subprocess

from funcs import get_resource_path

@dataclass
class ScreenRes:
    w: int = 0
    h: int = 0
    hz: int = 60
    pos: string = "default"

    def __eq__(self, other):
        return self.w==other.w and self.h==other.h

    def __hash__(self):
        return hash((self.w, self.h))

# get current resolution
def get_current_resolution():
    monitors = get_monitors()
    return ScreenRes(monitors[0].width, monitors[0].height)

# set screen resolution
# width, height, monitor index
def set_resolution(res, d = 0):
    subprocess.run([get_resource_path('ChangeScreenResolution.exe'), '/w=%s'%res.w, '/h=%s'%res.h, '/d=%s'%d], creationflags=0x08000000)

def get_resolution(d = 0):
    res_raw = subprocess.run([get_resource_path('ChangeScreenResolution.exe'), '/m', '/d=%s'%d], creationflags=0x08000000, capture_output = True, stdin=subprocess.DEVNULL).stdout.decode()
    res = []

    # parse possible resolutions
    # line format 640x480 32bit @60Hz default
    for match in re.finditer("(\d+)x(\d+)\s\d\dbit\s\@(\d+)Hz\s(\w+)", res_raw):
        res.append(ScreenRes(int(match.groups()[0]), int(match.groups()[1]), match.groups()[2], match.groups()[3]))

    # sort and remove duplicates
    # TODO: set Hz and stretch
    # for the moment find duplicates by resolution only
    res.sort(key=lambda r: r.w, reverse=True)
    res = list(res_possible for res_possible,_ in itertools.groupby(res))
    return res