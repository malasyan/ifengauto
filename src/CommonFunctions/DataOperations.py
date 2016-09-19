#-*- coding: UTF-8 -*-

#import os
from xml.dom import minidom
global DOC #获取Xml文件句柄

class DataOperations(object):
    '''
       读取xml操作
    '''


    def __init__(self, filename):
        '''
        Constructor
        '''
        global DOC
        #DOC=minidom.parse(os.getcwd()+"/src/TestData/"+filename)
        DOC = minidom.parse("../TestData/"+filename) 
        
    def readxml(self,tagnamefirst,tagNamesecond): 
        '''
        从指定的文件中中读取指定节点的值
        @param tagnamefirst:起始节点的名称，如：project 
    
        @param tagNamesecond: 起始节点下的二级节点
        @return: 返回二级节点的值
        '''           
        root = DOC.documentElement
        message=root.getElementsByTagName(tagnamefirst)[0]
        return message.getElementsByTagName(tagNamesecond)[0].childNodes[0].nodeValue
     
    