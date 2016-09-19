#-*- coding: UTF-8 -*-
'''
Created on 2016年8月2日

@author: li_min
'''
import unittest
from src.CommonFunctions.CommonFunctions import CommonFunctions
from src.CommonFunctions.DataOperations import DataOperations
#from src.CommonFunctions.DataOperations import DataOperations

class logintest(unittest.TestCase):
    
    def setUp(self):
        CommonFunctions().setup()
    
    def test_login(self):
        db=DataOperations("login.xml")
        
        CommonFunctions().Login(db.readxml("login","username"),db.readxml("login", "password"))
        self.assertEqual(db.readxml("login", "keywordvalue"), CommonFunctions().gettest(db.readxml("login", "keyword")))
        #db=DataOperations("login.xml")
        #CommonFunctions().Login(db.readxml("login", "username"),db.readxml("login", "password"))
        #self.assertEqual(db.readxml("login", "keywordvalue"), CommonFunctions().gettest(db.readxml("login", "keyword")))
        
        
if __name__ == '__main__':
        unittest.main()
