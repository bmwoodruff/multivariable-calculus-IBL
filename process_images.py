# -*- coding: utf-8 -*-
"""
Karl Schmitt

This script processes all the PTX files for the multivariable-calculus-IBL
text to create the images and cross-references required.

It can be run in either the main folder, or the PTX folder. 

It outputs images create to a sub-folder labeled 'html-images'
"""

import os, subprocess

mbxfilepath = './../mathbook/script/mbx'

args = ['./../mathbook/script/mbx', "-v","-c", "latex-image", "-f", "svg", "-d", "./html/images"]

for dirpath, dirnames, filenames in os.walk('./ptx'):
    for name in filenames:
        file = os.path.join(dirpath, name)
        subprocess.call(['python', args, file])