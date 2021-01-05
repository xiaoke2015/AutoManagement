#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os   #Python的标准库中的os模块包含普遍的操作系统功能
import sys
from PIL import Image


def exportIcons(pro):

    im = Image.open("icon.png")
    im120 = im.resize((120,120))
    im180 = im.resize((180,180))
    os.system('mkdir ' + pro + 'Icon')
    im120.save( pro + 'Icon/' + 'icon60@2x.png')
    im180.save(pro + 'Icon/' +  'icon60@3x.png')
    im.save(pro + 'Icon/' +  'icon1024.png')

exportIcons('BostonDigital')