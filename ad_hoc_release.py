#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os   #Python的标准库中的os模块包含普遍的操作系统功能
import sys

# import requests
from time import time


class AutomatedPackaging:

    xcworkspace = '/Users/lijiajian/Desktop/BILU_PRO/hash_ios/BL_Society.xcworkspace'
    xcarchive = '/Users/lijiajian/Desktop/archive1.xcarchive'
    scheme = 'BL_Society'
    exportOptions = '/Users/lijiajian/Desktop/HashPod/ExportOptions.plist'
    exportIpa = '/Users/lijiajian/Desktop/HashPod/BL_Society'

    def xcodebuild_archive(self):
        ''' 导出 archive 文件'''
        command = 'xcodebuild archive -workspace ' + self.xcworkspace + ' -scheme ' + self.scheme + ' -archivePath ' + self.xcarchive
        if os.path.exists(self.xcworkspace):
            os.system(command)


    def xcodebuild_exportArchive(self):
        ''' 导出 IPA包组 文件'''
        command = 'xcodebuild -exportArchive -archivePath ' + self.xcarchive + ' -exportPath ' + self.exportIpa + ' -exportOptionsPlist ' + self.exportOptions
        if os.path.exists(self.xcarchive):
            os.system(command)

    
    def remove_archive(self):
        ''' 删除导出的 archive 文件'''
        if os.path.exists(self.xcarchive):
            command = 'rm ' + self.xcarchive
            os.system(command)

    



    def uploadPugongying(self):
        print("uploadPugongying")

    def uploadAppstore(self):
        
        print("uploadAppstore")



a = AutomatedPackaging()

a.xcodebuild_archive()

