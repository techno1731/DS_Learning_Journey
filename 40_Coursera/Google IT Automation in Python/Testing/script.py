#!/usr/bin/env python3
from multiprocessing import Pool
import subprocess

def back_it_up(original, copy):
    subprocess.run(['rsync', original, copy])

if __name__ == "__main__":
    
    p = Pool()
    p.map(back_it_up, original, copy)
