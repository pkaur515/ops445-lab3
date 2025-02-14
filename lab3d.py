#!/usr/bin/env python3
'''Lab 3 disk space check'''
# Author ID: pkaur515

import subprocess

def free_space():
    p = subprocess.Popen(['df', '-h', '|', 'grep', '/$', '|', 'awk', '{print $4}'], 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE, 
                         shell=True)
    output = p.communicate()
    stdout = output[0].decode('utf-8').strip()
    return stdout

if __name__ == '__main__':
    print(free_space())  # Should print the available disk space
