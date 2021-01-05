#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python的标准库中的os模块包含普遍的操作系统功能
import os   
import sys
import json
import time

class AutoInstall :
    name = ''
    def __init__(self, name):
        self.name = name

    def podInstall(self):

        pods = [
        "  pod 'Masonry'\n",
        "  pod 'YYModel'\n",
        "  pod 'YYText'\n",
        "  pod 'YYImage'\n",
        "  pod 'SDWebImage'\n",
        "  pod 'MJRefresh'\n",
        "  pod 'FMDB'\n",
        "  pod 'SDCycleScrollView'\n",
        "  pod 'MBProgressHUD'\n",
        "  pod 'AVOSCloud' \n"
        "  pod 'AFNetworking'\n"
        ]

        lines = []

        os.system("pod init")

        path = './Podfile'

        with open(path, 'r') as file:
            filelines = file.readlines()
            lines.extend(filelines[:9])
            lines.extend(pods)
            lines.extend(filelines[9:])
        
        with open(path, 'w') as file:
            file.writelines(lines)
        print (lines)

        os.system("pod install")        

    def editPlist(self):

        plistPath = "./" + self.name +  "/info.plist"

        # 设置网络请求
        os.system("/usr/libexec/PlistBuddy -c 'Add :NSAppTransportSecurity:NSAllowsArbitraryLoads bool true' " + plistPath)
        # 设置暗黑模式
        os.system("/usr/libexec/PlistBuddy -c 'Add :Appearance string  Light' " + plistPath)
        # 删除 UIApplicationSceneManifest
        os.system("/usr/libexec/PlistBuddy -c 'Delete :UIApplicationSceneManifest' " + plistPath)
        # 删除 UISupportedInterfaceOrientations~ipad
        os.system("/usr/libexec/PlistBuddy -c 'Delete :UISupportedInterfaceOrientations~ipad' " + plistPath)

        # 设置权限描述
        os.system("/usr/libexec/PlistBuddy -c 'Add :NSCameraUsageDescription string  camera' " + plistPath)
        os.system("/usr/libexec/PlistBuddy -c 'Add :NSLocationWhenInUseUsageDescription string  location' " + plistPath)
        os.system("/usr/libexec/PlistBuddy -c 'Add :NSPhotoLibraryAddUsageDescription string  location' " + plistPath)
        os.system("/usr/libexec/PlistBuddy -c 'Add :NSPhotoLibraryUsageDescription string  Photo' " + plistPath)
        os.system("/usr/libexec/PlistBuddy -c 'Add :NSLocationAlwaysUsageDescription string  Location' " + plistPath)

    def updateClass(self):
        
        pbxproj = "./project.pbxproj"

        os.system("/usr/libexec/PlistBuddy -c 'print' " + pbxproj)


    def test(self):
        member = ['a','b','c','1','2','3','4','5','6','7','8','9']
        member1 = ['one','two','three']
        member.insert(1,member1)
        print(member[:4])
        print(member[4:])


linefeed = '\n'
linefeed2 = '\n\n'
linefeed3 = '\n\n\n'

NS_BEGIN = 'NS_ASSUME_NONNULL_BEGIN' + linefeed2
NS_END = 'NS_ASSUME_NONNULL_END' + linefeed2

class ObjcFilesCreator:
    
    projectname = ''
    prefixname = ''
    srcname = 'src'
    homeDir = 'Classes'

    def __init__(self ,projectname , prefixname):
        self.projectname = projectname
        self.prefixname = prefixname

    # def __init__(self):
    #     print(self)

    def writelinestofile(self, filename , lines):
        path = './' + self.homeDir + '/' + filename
        with open(path, 'wr') as file:
            file.writelines(lines)

    def note(self, vcName):
        
        today = time.strftime("%Y/%m/%d", time.localtime())
        text = '//\n//    ' + vcName + '\n//    ' + self.projectname + '\n//\n//   Created by alibaba on ' + today + '.\n//\n\n'

        return text
    
    # 创建 ViewController
    def creatVC(self,vcName):

        filename = vcName + 'ViewController'

        mlines = []
        mlines.append(self.note(filename + '.m'))
        mlines.append('#import "' + filename + '.h"' + linefeed2)
        mlines.append('@interface ' + filename + ' ()' + linefeed2)
        mlines.append('@end' + linefeed2)
        mlines.append('@implementation ' + filename + '' + linefeed2)
        mlines.append('- (void)viewDidLoad {' + linefeed)
        mlines.append('    [super viewDidLoad];' + linefeed2)
        mlines.append('}' + linefeed2)
        mlines.append('@end' + linefeed2)
        # print lines
        mfilenamewrite = filename + '.m'
        self.writelinestofile(mfilenamewrite,mlines)

        hlines = []
        hlines.append(self.note(filename + '.h'))
        hlines.append('#import <UIKit/UIKit.h>' + linefeed2)
        hlines.append(NS_BEGIN)
        hlines.append('@interface ' + filename + ' : UIViewController' + linefeed3)
        hlines.append('@end' + linefeed2)
        hlines.append(NS_END)
        # print lines
        hfilenamewrite = filename + '.h'
        self.writelinestofile(hfilenamewrite,hlines)

    # 创建 TableViewCell
    def creatTableViewCell(self ,vcName):
        
        filename = vcName + 'TableViewCell'

        mlines = []
        mlines.append(self.note(filename + '.m'))
        mlines.append('#import "' + filename + '.h"' + linefeed2)
        mlines.append('@interface ' + filename + ' ()' + linefeed2)
        mlines.append('@end' + linefeed2)
        mlines.append('@implementation ' + filename + '' + linefeed2)

        mlines.append('- (void)awakeFromNib {' + linefeed)
        mlines.append('    [super awakeFromNib];' + linefeed)
        mlines.append('    // Initialization code' + linefeed)
        mlines.append('}' + linefeed2)

        mlines.append('- (void)setSelected:(BOOL)selected animated:(BOOL)animated {' + linefeed)
        mlines.append('    [super setSelected:selected animated:animated];' + linefeed2)
        mlines.append('    // Configure the view for the selected state' + linefeed)
        mlines.append('}' + linefeed2)

        mlines.append('- (instancetype)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier {' + linefeed)
        mlines.append('    self = [super initWithStyle:style reuseIdentifier:reuseIdentifier];' + linefeed)
        mlines.append('    if(self){' + linefeed)
        mlines.append('        [self creatUIs];' + linefeed)
        mlines.append('    }' + linefeed)
        mlines.append('    return self;' + linefeed)
        mlines.append('}' + linefeed2)

        mlines.append('- (void)creatUIs {' + linefeed2)
        mlines.append('}' + linefeed2)

        mlines.append('@end' + linefeed2)
        # print lines
        mfilenamewrite = filename + '.m'
        self.writelinestofile(mfilenamewrite,mlines)

        hlines = []
        hlines.append(self.note(filename + '.h'))
        hlines.append('#import <UIKit/UIKit.h>' + linefeed2)
        hlines.append(NS_BEGIN)
        hlines.append('@interface ' + filename + ' : UITableViewCell' + linefeed3)
        hlines.append('@end' + linefeed2)
        hlines.append(NS_END)
        # print lines
        hfilenamewrite = filename + '.h'
        self.writelinestofile(hfilenamewrite,hlines)

    # 创建 ViewController
    def creatModel(self,vcName): 

        filename = vcName + 'Model'

        mlines = []
        mlines.append(self.note(filename + '.m'))
        mlines.append('#import "' + filename + '.h"' + linefeed2)
        mlines.append('@implementation ' + filename + '' + linefeed2)
        mlines.append('@end' + linefeed2)
        # print lines
        mfilenamewrite = filename + '.m'
        self.writelinestofile(mfilenamewrite,mlines)

        hlines = []
        hlines.append(self.note(filename + '.h'))
        hlines.append('#import <Foundation/Foundation.h>' + linefeed2)
        hlines.append(NS_BEGIN)
        hlines.append('@interface ' + filename + ' : NSObject' + linefeed3)
        hlines.append('@end' + linefeed2)
        hlines.append(NS_END)
        # print lines
        hfilenamewrite = filename + '.h'
        self.writelinestofile(hfilenamewrite,hlines)

    # 创建 TabBarController
    def creatTabBarVC(self,vcName):

        filename = vcName + 'TabBarController'

        mlines = []
        mlines.append(self.note(filename + '.m'))
        mlines.append('#import "' + filename + '.h"' + linefeed2)
        mlines.append('@interface ' + filename + ' ()' + linefeed2)
        mlines.append('@end' + linefeed2)
        mlines.append('@implementation ' + filename + '' + linefeed2)
        mlines.append('- (void)viewDidLoad {' + linefeed)
        mlines.append('    [super viewDidLoad];' + linefeed)
        mlines.append('    // Do any additional setup after loading the view.' + linefeed)
        mlines.append('    self.view.backgroundColor = [UIColor whiteColor];' + linefeed)
        mlines.append('    [UINavigationBar appearance].backgroundColor = [UIColor whiteColor];' + linefeed)
        mlines.append('    [UINavigationBar appearance].translucent = NO;' + linefeed2)
        mlines.append('}' + linefeed2)
        mlines.append('@end' + linefeed2)
        
    
        # print lines
        mfilenamewrite = filename + '.m'
        self.writelinestofile(mfilenamewrite,mlines)

        hlines = []
        hlines.append(self.note(filename + '.h'))
        hlines.append('#import <UIKit/UIKit.h>' + linefeed2)
        hlines.append(NS_BEGIN)
        hlines.append('@interface ' + filename + ' : UITabBarController' + linefeed3)
        hlines.append('@end' + linefeed2)
        hlines.append(NS_END)
        # print lines
        hfilenamewrite = filename + '.h'
        self.writelinestofile(hfilenamewrite,hlines)


    def addLazyTableView(self):
        
        lines = []
        lines.append('- (UITableView*)tablebView {' + linefeed)
        lines.append('    if(_tablebView == nil){' + linefeed)
        lines.append('        _tablebView = [[UITableView alloc]initWithFrame:CGRectMake(0, KNBLBar, SCREEM_WIDTH, SCREEM_HEIGHT - KNBLBar)];' + linefeed)
        lines.append('        _tablebView.dataSource = self;' + linefeed)
        lines.append('        _tablebView.delegate = self;' + linefeed)
        lines.append('        _tablebView.tableFooterView = [[UIView alloc]init];' + linefeed)
        lines.append('    }' + linefeed)
        lines.append('    return _tablebView;' + linefeed)
        lines.append('}' + linefeed2)

        return lines

    def addLazyDataArray(self):
        
        lines = []

        lines.append('- (NSMutableArray*)dataArray {' + linefeed)
        lines.append('    if(_dataArray == nil){' + linefeed)
        lines.append('        _dataArray = [NSMutableArray array];' + linefeed)
        lines.append('    }' + linefeed)
        lines.append('    return _dataArray;' + linefeed)
        lines.append('}' + linefeed2)

        return lines


    def addTableViewDataSource(self):
        
        lines = []

        lines.append('- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {' + linefeed2)
        lines.append('    return self.dataArray.count;' + linefeed)
        lines.append('}' + linefeed2)

        lines.append('- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath {' + linefeed2)
        lines.append('    return 60;' + linefeed)
        lines.append('}' + linefeed2)

        lines.append('- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {' + linefeed2)
        lines.append('    UITableViewCell * cell = [tableView dequeueReusableCellWithIdentifier:@"UITableViewCell"];' + linefeed2)
        lines.append('    return cell;' + linefeed)
        lines.append('}' + linefeed2)

        return lines


    def creatTableViewVC(self,vcName):

        filename = vcName + 'ViewController'

        mlines = []
        mlines.append(self.note(filename + '.m'))
        mlines.append('#import "' + filename + '.h"' + linefeed2)
        mlines.append('@interface ' + filename + ' ()' + linefeed2)
        mlines.append('<UITableViewDataSource,UITableViewDelegate>' + linefeed)
        mlines.append('@property (nonatomic ,strong)UITableView * tablebView;' + linefeed)
        mlines.append('@property (nonatomic ,strong)NSMutableArray * dataArray;' + linefeed2)
        mlines.append('@end' + linefeed2)
        mlines.append('@implementation ' + filename + '' + linefeed2)
        mlines.append('- (void)viewDidLoad {' + linefeed)
        mlines.append('    [super viewDidLoad];' + linefeed)
        mlines.append('    // Do any additional setup after loading the view.' + linefeed)
        mlines.append('    self.view.backgroundColor = [UIColor whiteColor];' + linefeed2)
        mlines.append('}' + linefeed2)

        for line in self.addTableViewDataSource():
            mlines.append(line)
        for line in self.addLazyTableView():
            mlines.append(line)
        for line in self.addLazyDataArray():
            mlines.append(line)

        mlines.append('@end' + linefeed2)
        # print lines
        mfilenamewrite = filename + '.m'
        self.writelinestofile(mfilenamewrite,mlines)

        hlines = []
        hlines.append(self.note(filename + '.h'))
        hlines.append('#import <UIKit/UIKit.h>' + linefeed2)
        hlines.append(NS_BEGIN)
        hlines.append('@interface ' + filename + ' : ViewController' + linefeed3)
        hlines.append('@end' + linefeed2)
        hlines.append(NS_END)
        # print lines
        hfilenamewrite = filename + '.h'
        self.writelinestofile(hfilenamewrite,hlines)


    def creatVCs(self):
        
        os.system('rm -rf ./'+ self.homeDir + '')
        os.system('mkdir '+ self.homeDir + '')

        prefix = self.prefixname

        self.creatTabBarVC(prefix)
        self.creatVC(prefix + 'Login')
        self.creatVC(prefix + 'Register')
        self.creatTableViewVC(prefix + 'Home')
        self.creatTableViewVC(prefix + 'News')
        self.creatTableViewVC(prefix + 'Profile')
        self.creatTableViewVC(prefix + 'Settings')
        self.creatVC(prefix + 'Feedback')
        self.creatVC(prefix + 'Privacy')
        self.creatVC(prefix + 'About')
        self.creatVC(prefix + 'Collection')

        self.creatTableViewVC(prefix + 'NewsDetail')
        self.creatTableViewVC(prefix + 'Detail')


#        self.creatTableViewCell(prefix + 'Articles')
#        self.creatTableViewCell(prefix + 'Announcements')
#        self.creatTableViewCell(prefix + 'Briefs')

        self.creatModel(prefix + 'Home')
        self.creatModel(prefix + 'News')
        self.creatModel(prefix + 'Collection')


class PBXProjectHelper:
    path = ''
    def __init__(self, path):
        self.path = path


    def update_bit_code(self):
        
        pbxproj = "./PhoenixDigitalCurrency.xcodeproj/project.pbxproj"

        with open(pbxproj, 'r') as file:
            text = file.read()
            json1 = json.dumps(text)
            print (json1)
            

        # os.system("/usr/libexec/PlistBuddy -c 'Set :objects:3769478825A2B74700FE1BAF:buildSettings:ENABLE_BITCODE bool YES' " + pbxproj)
        # os.system("/usr/libexec/PlistBuddy -c 'Set :objects:3769478925A2B74700FE1BAF:buildSettings:ENABLE_BITCODE bool YES' " + pbxproj)



# auto = AutoInstall("PhoenixDigitalCurrency")
# auto.editPlist()
# auto.podInstall()
# auto.updateClass()
# auto.test()

helper = PBXProjectHelper('./project.pbxproj')
helper.update_bit_code()

# objc = ObjcFilesCreator('PhoenixDigitalCurrency','PDC')
# objc.creatVCs()



