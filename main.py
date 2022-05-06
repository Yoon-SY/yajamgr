# Copyright 2021-2022 Yoon Sung-Yong
# Free use in Daewon Foreign Language High School only
# NIHONGOKA SAIKOU!

import csv
import sys
import copy
from PyQt5 import uic
from PyQt5.QtWidgets import *
import datetime as dt

form_class = uic.loadUiType('panel.ui')[0]

ssint = {0:30,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0}
sslist = {1:[],2:[],3:[],4:[],5:[],6:[], # Jungsi / Ingang / Others / Room / Home / Absent
          7:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]}
maxstdnum = 30 # ssint[0]: actual number of students // maxstdnum: literally the last number
namelist = ['', '', '', '', '', '', '', '', '', '',
            '', '', '', '', '', '', '', '', '', '',
            '', '', '', '', '', '', '', '', '', ''] # Names go here

grade = 3
homeroom = 6

today = dt.date.today()
isotoday = dt.date.isocalendar(today)
korwkday = {1:"월", 2:"화", 3:"수", 4:"목", 5:"금"}

recordmsg = {1:"정시반", 2:"인강실", 3:"기타", 4:"교실", 5:"귀가", 6:"결석", 7:""}

def purify(l):
    ret = []
    for x in l:
        if x <= maxstdnum:
            ret.append(x)
    return ret

# Improved from guipicker
# Returns str with 10 elements in a row
def tenslice(l):
    ret = ''
    if l:
        l = purify(l)
        for i in range(max(0, len(l)//10)+1):
            ret += ', '.join(str(x).rjust(2) for x in l[10*i:10*(i+1)]) + '\n'
    else: ret = '없음'
    return ret

# Reads txt file and returns the content as list
# Each element represents each line of the file
def fileanalyze(f):
    ret = []
    while True:
        s = f.readline()
        if s == '':
            return ret
        ret.append(s)

# Returns appropriate file name according to the classroom info
# and the date info
def getfname(dpt):
    startday = today - dt.timedelta(days=isotoday[2]-1)
    endday = today + dt.timedelta(days=5-isotoday[2])
    return "%d-%d %d주차(%d.%d.~%d.%d.) 야간자율학습 통계.csv" % (
        grade, homeroom, isotoday[1],
        startday.month, startday.day, endday.month, endday.day)

# Initializes a new CSV file
def csv_initialize():
    l = []
    day = today - dt.timedelta(days=isotoday[2]-1)

    # Title
    t = ["번호", "이름"]
    for i in range(5):
        strfday = "%d/%d (%s) " % (day.month, day.day, korwkday[dt.date.isocalendar(day)[2]])
        t.append(strfday + "1교시")
        t.append(strfday + "2교시")
        day += dt.timedelta(days=1)
    l.append(t)

    # Students
    for i in range(1, maxstdnum+1):
        l.append([str(i), namelist[i-1], '', '', '', '', '', '', '', '', '', ''])

    return l

def getschoolstd():
    ret = 0
    for i in range(1, 5):
        ret += len(sslist[i])
    return ret

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Numerous radio buttons
        self.rad_01_1.clicked.connect(self.radpush)
        self.rad_01_2.clicked.connect(self.radpush)
        self.rad_01_3.clicked.connect(self.radpush)
        self.rad_01_4.clicked.connect(self.radpush)
        self.rad_01_5.clicked.connect(self.radpush)
        self.rad_01_6.clicked.connect(self.radpush)
        self.rad_01_7.clicked.connect(self.radpush)
        self.rad_02_1.clicked.connect(self.radpush)
        self.rad_02_2.clicked.connect(self.radpush)
        self.rad_02_3.clicked.connect(self.radpush)
        self.rad_02_4.clicked.connect(self.radpush)
        self.rad_02_5.clicked.connect(self.radpush)
        self.rad_02_6.clicked.connect(self.radpush)
        self.rad_02_7.clicked.connect(self.radpush)
        self.rad_03_1.clicked.connect(self.radpush)
        self.rad_03_2.clicked.connect(self.radpush)
        self.rad_03_3.clicked.connect(self.radpush)
        self.rad_03_4.clicked.connect(self.radpush)
        self.rad_03_5.clicked.connect(self.radpush)
        self.rad_03_6.clicked.connect(self.radpush)
        self.rad_03_7.clicked.connect(self.radpush)
        self.rad_04_1.clicked.connect(self.radpush)
        self.rad_04_2.clicked.connect(self.radpush)
        self.rad_04_3.clicked.connect(self.radpush)
        self.rad_04_4.clicked.connect(self.radpush)
        self.rad_04_5.clicked.connect(self.radpush)
        self.rad_04_6.clicked.connect(self.radpush)
        self.rad_04_7.clicked.connect(self.radpush)
        self.rad_05_1.clicked.connect(self.radpush)
        self.rad_05_2.clicked.connect(self.radpush)
        self.rad_05_3.clicked.connect(self.radpush)
        self.rad_05_4.clicked.connect(self.radpush)
        self.rad_05_5.clicked.connect(self.radpush)
        self.rad_05_6.clicked.connect(self.radpush)
        self.rad_05_7.clicked.connect(self.radpush)
        self.rad_06_1.clicked.connect(self.radpush)
        self.rad_06_2.clicked.connect(self.radpush)
        self.rad_06_3.clicked.connect(self.radpush)
        self.rad_06_4.clicked.connect(self.radpush)
        self.rad_06_5.clicked.connect(self.radpush)
        self.rad_06_6.clicked.connect(self.radpush)
        self.rad_06_7.clicked.connect(self.radpush)
        self.rad_07_1.clicked.connect(self.radpush)
        self.rad_07_2.clicked.connect(self.radpush)
        self.rad_07_3.clicked.connect(self.radpush)
        self.rad_07_4.clicked.connect(self.radpush)
        self.rad_07_5.clicked.connect(self.radpush)
        self.rad_07_6.clicked.connect(self.radpush)
        self.rad_07_7.clicked.connect(self.radpush)
        self.rad_08_1.clicked.connect(self.radpush)
        self.rad_08_2.clicked.connect(self.radpush)
        self.rad_08_3.clicked.connect(self.radpush)
        self.rad_08_4.clicked.connect(self.radpush)
        self.rad_08_5.clicked.connect(self.radpush)
        self.rad_08_6.clicked.connect(self.radpush)
        self.rad_08_7.clicked.connect(self.radpush)
        self.rad_09_1.clicked.connect(self.radpush)
        self.rad_09_2.clicked.connect(self.radpush)
        self.rad_09_3.clicked.connect(self.radpush)
        self.rad_09_4.clicked.connect(self.radpush)
        self.rad_09_5.clicked.connect(self.radpush)
        self.rad_09_6.clicked.connect(self.radpush)
        self.rad_09_7.clicked.connect(self.radpush)
        self.rad_10_1.clicked.connect(self.radpush)
        self.rad_10_2.clicked.connect(self.radpush)
        self.rad_10_3.clicked.connect(self.radpush)
        self.rad_10_4.clicked.connect(self.radpush)
        self.rad_10_5.clicked.connect(self.radpush)
        self.rad_10_6.clicked.connect(self.radpush)
        self.rad_10_7.clicked.connect(self.radpush)
        self.rad_11_1.clicked.connect(self.radpush)
        self.rad_11_2.clicked.connect(self.radpush)
        self.rad_11_3.clicked.connect(self.radpush)
        self.rad_11_4.clicked.connect(self.radpush)
        self.rad_11_5.clicked.connect(self.radpush)
        self.rad_11_6.clicked.connect(self.radpush)
        self.rad_11_7.clicked.connect(self.radpush)
        self.rad_12_1.clicked.connect(self.radpush)
        self.rad_12_2.clicked.connect(self.radpush)
        self.rad_12_3.clicked.connect(self.radpush)
        self.rad_12_4.clicked.connect(self.radpush)
        self.rad_12_5.clicked.connect(self.radpush)
        self.rad_12_6.clicked.connect(self.radpush)
        self.rad_12_7.clicked.connect(self.radpush)
        self.rad_13_1.clicked.connect(self.radpush)
        self.rad_13_2.clicked.connect(self.radpush)
        self.rad_13_3.clicked.connect(self.radpush)
        self.rad_13_4.clicked.connect(self.radpush)
        self.rad_13_5.clicked.connect(self.radpush)
        self.rad_13_6.clicked.connect(self.radpush)
        self.rad_13_7.clicked.connect(self.radpush)
        self.rad_14_1.clicked.connect(self.radpush)
        self.rad_14_2.clicked.connect(self.radpush)
        self.rad_14_3.clicked.connect(self.radpush)
        self.rad_14_4.clicked.connect(self.radpush)
        self.rad_14_5.clicked.connect(self.radpush)
        self.rad_14_6.clicked.connect(self.radpush)
        self.rad_14_7.clicked.connect(self.radpush)
        self.rad_15_1.clicked.connect(self.radpush)
        self.rad_15_2.clicked.connect(self.radpush)
        self.rad_15_3.clicked.connect(self.radpush)
        self.rad_15_4.clicked.connect(self.radpush)
        self.rad_15_5.clicked.connect(self.radpush)
        self.rad_15_6.clicked.connect(self.radpush)
        self.rad_15_7.clicked.connect(self.radpush)
        self.rad_16_1.clicked.connect(self.radpush)
        self.rad_16_2.clicked.connect(self.radpush)
        self.rad_16_3.clicked.connect(self.radpush)
        self.rad_16_4.clicked.connect(self.radpush)
        self.rad_16_5.clicked.connect(self.radpush)
        self.rad_16_6.clicked.connect(self.radpush)
        self.rad_16_7.clicked.connect(self.radpush)
        self.rad_17_1.clicked.connect(self.radpush)
        self.rad_17_2.clicked.connect(self.radpush)
        self.rad_17_3.clicked.connect(self.radpush)
        self.rad_17_4.clicked.connect(self.radpush)
        self.rad_17_5.clicked.connect(self.radpush)
        self.rad_17_6.clicked.connect(self.radpush)
        self.rad_17_7.clicked.connect(self.radpush)
        self.rad_18_1.clicked.connect(self.radpush)
        self.rad_18_2.clicked.connect(self.radpush)
        self.rad_18_3.clicked.connect(self.radpush)
        self.rad_18_4.clicked.connect(self.radpush)
        self.rad_18_5.clicked.connect(self.radpush)
        self.rad_18_6.clicked.connect(self.radpush)
        self.rad_18_7.clicked.connect(self.radpush)
        self.rad_19_1.clicked.connect(self.radpush)
        self.rad_19_2.clicked.connect(self.radpush)
        self.rad_19_3.clicked.connect(self.radpush)
        self.rad_19_4.clicked.connect(self.radpush)
        self.rad_19_5.clicked.connect(self.radpush)
        self.rad_19_6.clicked.connect(self.radpush)
        self.rad_19_7.clicked.connect(self.radpush)
        self.rad_20_1.clicked.connect(self.radpush)
        self.rad_20_2.clicked.connect(self.radpush)
        self.rad_20_3.clicked.connect(self.radpush)
        self.rad_20_4.clicked.connect(self.radpush)
        self.rad_20_5.clicked.connect(self.radpush)
        self.rad_20_6.clicked.connect(self.radpush)
        self.rad_20_7.clicked.connect(self.radpush)
        self.rad_21_1.clicked.connect(self.radpush)
        self.rad_21_2.clicked.connect(self.radpush)
        self.rad_21_3.clicked.connect(self.radpush)
        self.rad_21_4.clicked.connect(self.radpush)
        self.rad_21_5.clicked.connect(self.radpush)
        self.rad_21_6.clicked.connect(self.radpush)
        self.rad_21_7.clicked.connect(self.radpush)
        self.rad_22_1.clicked.connect(self.radpush)
        self.rad_22_2.clicked.connect(self.radpush)
        self.rad_22_3.clicked.connect(self.radpush)
        self.rad_22_4.clicked.connect(self.radpush)
        self.rad_22_5.clicked.connect(self.radpush)
        self.rad_22_6.clicked.connect(self.radpush)
        self.rad_22_7.clicked.connect(self.radpush)
        self.rad_23_1.clicked.connect(self.radpush)
        self.rad_23_2.clicked.connect(self.radpush)
        self.rad_23_3.clicked.connect(self.radpush)
        self.rad_23_4.clicked.connect(self.radpush)
        self.rad_23_5.clicked.connect(self.radpush)
        self.rad_23_6.clicked.connect(self.radpush)
        self.rad_23_7.clicked.connect(self.radpush)
        self.rad_24_1.clicked.connect(self.radpush)
        self.rad_24_2.clicked.connect(self.radpush)
        self.rad_24_3.clicked.connect(self.radpush)
        self.rad_24_4.clicked.connect(self.radpush)
        self.rad_24_5.clicked.connect(self.radpush)
        self.rad_24_6.clicked.connect(self.radpush)
        self.rad_24_7.clicked.connect(self.radpush)
        self.rad_25_1.clicked.connect(self.radpush)
        self.rad_25_2.clicked.connect(self.radpush)
        self.rad_25_3.clicked.connect(self.radpush)
        self.rad_25_4.clicked.connect(self.radpush)
        self.rad_25_5.clicked.connect(self.radpush)
        self.rad_25_6.clicked.connect(self.radpush)
        self.rad_25_7.clicked.connect(self.radpush)
        self.rad_26_1.clicked.connect(self.radpush)
        self.rad_26_2.clicked.connect(self.radpush)
        self.rad_26_3.clicked.connect(self.radpush)
        self.rad_26_4.clicked.connect(self.radpush)
        self.rad_26_5.clicked.connect(self.radpush)
        self.rad_26_6.clicked.connect(self.radpush)
        self.rad_26_7.clicked.connect(self.radpush)
        self.rad_27_1.clicked.connect(self.radpush)
        self.rad_27_2.clicked.connect(self.radpush)
        self.rad_27_3.clicked.connect(self.radpush)
        self.rad_27_4.clicked.connect(self.radpush)
        self.rad_27_5.clicked.connect(self.radpush)
        self.rad_27_6.clicked.connect(self.radpush)
        self.rad_27_7.clicked.connect(self.radpush)
        self.rad_28_1.clicked.connect(self.radpush)
        self.rad_28_2.clicked.connect(self.radpush)
        self.rad_28_3.clicked.connect(self.radpush)
        self.rad_28_4.clicked.connect(self.radpush)
        self.rad_28_5.clicked.connect(self.radpush)
        self.rad_28_6.clicked.connect(self.radpush)
        self.rad_28_7.clicked.connect(self.radpush)
        self.rad_29_1.clicked.connect(self.radpush)
        self.rad_29_2.clicked.connect(self.radpush)
        self.rad_29_3.clicked.connect(self.radpush)
        self.rad_29_4.clicked.connect(self.radpush)
        self.rad_29_5.clicked.connect(self.radpush)
        self.rad_29_6.clicked.connect(self.radpush)
        self.rad_29_7.clicked.connect(self.radpush)
        self.rad_30_1.clicked.connect(self.radpush)
        self.rad_30_2.clicked.connect(self.radpush)
        self.rad_30_3.clicked.connect(self.radpush)
        self.rad_30_4.clicked.connect(self.radpush)
        self.rad_30_5.clicked.connect(self.radpush)
        self.rad_30_6.clicked.connect(self.radpush)
        self.rad_30_7.clicked.connect(self.radpush)

        # Load Button
        self.loadbtn.clicked.connect(self.load)

        # Save Button
        self.savebtn.clicked.connect(self.save)

        # Quit Button
        self.exitbtn.clicked.connect(self.qexit)

    # Relaying rad_clicked and statupdate
    def radpush(self):
        if self.rad_01_1.isChecked(): self.statupdate(1,1)
        elif self.rad_01_2.isChecked(): self.statupdate(1,2)
        elif self.rad_01_3.isChecked(): self.statupdate(1,3)
        elif self.rad_01_4.isChecked(): self.statupdate(1,4)
        elif self.rad_01_5.isChecked(): self.statupdate(1,5)
        elif self.rad_01_6.isChecked(): self.statupdate(1,6)
        elif self.rad_01_7.isChecked(): self.statupdate(1,7)
        if self.rad_02_1.isChecked(): self.statupdate(2,1)
        elif self.rad_02_2.isChecked(): self.statupdate(2,2)
        elif self.rad_02_3.isChecked(): self.statupdate(2,3)
        elif self.rad_02_4.isChecked(): self.statupdate(2,4)
        elif self.rad_02_5.isChecked(): self.statupdate(2,5)
        elif self.rad_02_6.isChecked(): self.statupdate(2,6)
        elif self.rad_02_7.isChecked(): self.statupdate(2,7)
        if self.rad_03_1.isChecked(): self.statupdate(3,1)
        elif self.rad_03_2.isChecked(): self.statupdate(3,2)
        elif self.rad_03_3.isChecked(): self.statupdate(3,3)
        elif self.rad_03_4.isChecked(): self.statupdate(3,4)
        elif self.rad_03_5.isChecked(): self.statupdate(3,5)
        elif self.rad_03_6.isChecked(): self.statupdate(3,6)
        elif self.rad_03_7.isChecked(): self.statupdate(3,7)
        if self.rad_04_1.isChecked(): self.statupdate(4,1)
        elif self.rad_04_2.isChecked(): self.statupdate(4,2)
        elif self.rad_04_3.isChecked(): self.statupdate(4,3)
        elif self.rad_04_4.isChecked(): self.statupdate(4,4)
        elif self.rad_04_5.isChecked(): self.statupdate(4,5)
        elif self.rad_04_6.isChecked(): self.statupdate(4,6)
        elif self.rad_04_7.isChecked(): self.statupdate(4,7)
        if self.rad_05_1.isChecked(): self.statupdate(5,1)
        elif self.rad_05_2.isChecked(): self.statupdate(5,2)
        elif self.rad_05_3.isChecked(): self.statupdate(5,3)
        elif self.rad_05_4.isChecked(): self.statupdate(5,4)
        elif self.rad_05_5.isChecked(): self.statupdate(5,5)
        elif self.rad_05_6.isChecked(): self.statupdate(5,6)
        elif self.rad_05_7.isChecked(): self.statupdate(5,7)
        if self.rad_06_1.isChecked(): self.statupdate(6,1)
        elif self.rad_06_2.isChecked(): self.statupdate(6,2)
        elif self.rad_06_3.isChecked(): self.statupdate(6,3)
        elif self.rad_06_4.isChecked(): self.statupdate(6,4)
        elif self.rad_06_5.isChecked(): self.statupdate(6,5)
        elif self.rad_06_6.isChecked(): self.statupdate(6,6)
        elif self.rad_06_7.isChecked(): self.statupdate(6,7)
        if self.rad_07_1.isChecked(): self.statupdate(7,1)
        elif self.rad_07_2.isChecked(): self.statupdate(7,2)
        elif self.rad_07_3.isChecked(): self.statupdate(7,3)
        elif self.rad_07_4.isChecked(): self.statupdate(7,4)
        elif self.rad_07_5.isChecked(): self.statupdate(7,5)
        elif self.rad_07_6.isChecked(): self.statupdate(7,6)
        elif self.rad_07_7.isChecked(): self.statupdate(7,7)
        if self.rad_08_1.isChecked(): self.statupdate(8,1)
        elif self.rad_08_2.isChecked(): self.statupdate(8,2)
        elif self.rad_08_3.isChecked(): self.statupdate(8,3)
        elif self.rad_08_4.isChecked(): self.statupdate(8,4)
        elif self.rad_08_5.isChecked(): self.statupdate(8,5)
        elif self.rad_08_6.isChecked(): self.statupdate(8,6)
        elif self.rad_08_7.isChecked(): self.statupdate(8,7)
        if self.rad_09_1.isChecked(): self.statupdate(9,1)
        elif self.rad_09_2.isChecked(): self.statupdate(9,2)
        elif self.rad_09_3.isChecked(): self.statupdate(9,3)
        elif self.rad_09_4.isChecked(): self.statupdate(9,4)
        elif self.rad_09_5.isChecked(): self.statupdate(9,5)
        elif self.rad_09_6.isChecked(): self.statupdate(9,6)
        elif self.rad_09_7.isChecked(): self.statupdate(9,7)
        if self.rad_10_1.isChecked(): self.statupdate(10,1)
        elif self.rad_10_2.isChecked(): self.statupdate(10,2)
        elif self.rad_10_3.isChecked(): self.statupdate(10,3)
        elif self.rad_10_4.isChecked(): self.statupdate(10,4)
        elif self.rad_10_5.isChecked(): self.statupdate(10,5)
        elif self.rad_10_6.isChecked(): self.statupdate(10,6)
        elif self.rad_10_7.isChecked(): self.statupdate(10,7)
        if self.rad_11_1.isChecked(): self.statupdate(11,1)
        elif self.rad_11_2.isChecked(): self.statupdate(11,2)
        elif self.rad_11_3.isChecked(): self.statupdate(11,3)
        elif self.rad_11_4.isChecked(): self.statupdate(11,4)
        elif self.rad_11_5.isChecked(): self.statupdate(11,5)
        elif self.rad_11_6.isChecked(): self.statupdate(11,6)
        elif self.rad_11_7.isChecked(): self.statupdate(11,7)
        if self.rad_12_1.isChecked(): self.statupdate(12,1)
        elif self.rad_12_2.isChecked(): self.statupdate(12,2)
        elif self.rad_12_3.isChecked(): self.statupdate(12,3)
        elif self.rad_12_4.isChecked(): self.statupdate(12,4)
        elif self.rad_12_5.isChecked(): self.statupdate(12,5)
        elif self.rad_12_6.isChecked(): self.statupdate(12,6)
        elif self.rad_12_7.isChecked(): self.statupdate(12,7)
        if self.rad_13_1.isChecked(): self.statupdate(13,1)
        elif self.rad_13_2.isChecked(): self.statupdate(13,2)
        elif self.rad_13_3.isChecked(): self.statupdate(13,3)
        elif self.rad_13_4.isChecked(): self.statupdate(13,4)
        elif self.rad_13_5.isChecked(): self.statupdate(13,5)
        elif self.rad_13_6.isChecked(): self.statupdate(13,6)
        elif self.rad_13_7.isChecked(): self.statupdate(13,7)
        if self.rad_14_1.isChecked(): self.statupdate(14,1)
        elif self.rad_14_2.isChecked(): self.statupdate(14,2)
        elif self.rad_14_3.isChecked(): self.statupdate(14,3)
        elif self.rad_14_4.isChecked(): self.statupdate(14,4)
        elif self.rad_14_5.isChecked(): self.statupdate(14,5)
        elif self.rad_14_6.isChecked(): self.statupdate(14,6)
        elif self.rad_14_7.isChecked(): self.statupdate(14,7)
        if self.rad_15_1.isChecked(): self.statupdate(15,1)
        elif self.rad_15_2.isChecked(): self.statupdate(15,2)
        elif self.rad_15_3.isChecked(): self.statupdate(15,3)
        elif self.rad_15_4.isChecked(): self.statupdate(15,4)
        elif self.rad_15_5.isChecked(): self.statupdate(15,5)
        elif self.rad_15_6.isChecked(): self.statupdate(15,6)
        elif self.rad_15_7.isChecked(): self.statupdate(15,7)
        if self.rad_16_1.isChecked(): self.statupdate(16,1)
        elif self.rad_16_2.isChecked(): self.statupdate(16,2)
        elif self.rad_16_3.isChecked(): self.statupdate(16,3)
        elif self.rad_16_4.isChecked(): self.statupdate(16,4)
        elif self.rad_16_5.isChecked(): self.statupdate(16,5)
        elif self.rad_16_6.isChecked(): self.statupdate(16,6)
        elif self.rad_16_7.isChecked(): self.statupdate(16,7)
        if self.rad_17_1.isChecked(): self.statupdate(17,1)
        elif self.rad_17_2.isChecked(): self.statupdate(17,2)
        elif self.rad_17_3.isChecked(): self.statupdate(17,3)
        elif self.rad_17_4.isChecked(): self.statupdate(17,4)
        elif self.rad_17_5.isChecked(): self.statupdate(17,5)
        elif self.rad_17_6.isChecked(): self.statupdate(17,6)
        elif self.rad_17_7.isChecked(): self.statupdate(17,7)
        if self.rad_18_1.isChecked(): self.statupdate(18,1)
        elif self.rad_18_2.isChecked(): self.statupdate(18,2)
        elif self.rad_18_3.isChecked(): self.statupdate(18,3)
        elif self.rad_18_4.isChecked(): self.statupdate(18,4)
        elif self.rad_18_5.isChecked(): self.statupdate(18,5)
        elif self.rad_18_6.isChecked(): self.statupdate(18,6)
        elif self.rad_18_7.isChecked(): self.statupdate(18,7)
        if self.rad_19_1.isChecked(): self.statupdate(19,1)
        elif self.rad_19_2.isChecked(): self.statupdate(19,2)
        elif self.rad_19_3.isChecked(): self.statupdate(19,3)
        elif self.rad_19_4.isChecked(): self.statupdate(19,4)
        elif self.rad_19_5.isChecked(): self.statupdate(19,5)
        elif self.rad_19_6.isChecked(): self.statupdate(19,6)
        elif self.rad_19_7.isChecked(): self.statupdate(19,7)
        if self.rad_20_1.isChecked(): self.statupdate(20,1)
        elif self.rad_20_2.isChecked(): self.statupdate(20,2)
        elif self.rad_20_3.isChecked(): self.statupdate(20,3)
        elif self.rad_20_4.isChecked(): self.statupdate(20,4)
        elif self.rad_20_5.isChecked(): self.statupdate(20,5)
        elif self.rad_20_6.isChecked(): self.statupdate(20,6)
        elif self.rad_20_7.isChecked(): self.statupdate(20,7)
        if self.rad_21_1.isChecked(): self.statupdate(21,1)
        elif self.rad_21_2.isChecked(): self.statupdate(21,2)
        elif self.rad_21_3.isChecked(): self.statupdate(21,3)
        elif self.rad_21_4.isChecked(): self.statupdate(21,4)
        elif self.rad_21_5.isChecked(): self.statupdate(21,5)
        elif self.rad_21_6.isChecked(): self.statupdate(21,6)
        elif self.rad_21_7.isChecked(): self.statupdate(21,7)
        if self.rad_22_1.isChecked(): self.statupdate(22,1)
        elif self.rad_22_2.isChecked(): self.statupdate(22,2)
        elif self.rad_22_3.isChecked(): self.statupdate(22,3)
        elif self.rad_22_4.isChecked(): self.statupdate(22,4)
        elif self.rad_22_5.isChecked(): self.statupdate(22,5)
        elif self.rad_22_6.isChecked(): self.statupdate(22,6)
        elif self.rad_22_7.isChecked(): self.statupdate(22,7)
        if self.rad_23_1.isChecked(): self.statupdate(23,1)
        elif self.rad_23_2.isChecked(): self.statupdate(23,2)
        elif self.rad_23_3.isChecked(): self.statupdate(23,3)
        elif self.rad_23_4.isChecked(): self.statupdate(23,4)
        elif self.rad_23_5.isChecked(): self.statupdate(23,5)
        elif self.rad_23_6.isChecked(): self.statupdate(23,6)
        elif self.rad_23_7.isChecked(): self.statupdate(23,7)
        if self.rad_24_1.isChecked(): self.statupdate(24,1)
        elif self.rad_24_2.isChecked(): self.statupdate(24,2)
        elif self.rad_24_3.isChecked(): self.statupdate(24,3)
        elif self.rad_24_4.isChecked(): self.statupdate(24,4)
        elif self.rad_24_5.isChecked(): self.statupdate(24,5)
        elif self.rad_24_6.isChecked(): self.statupdate(24,6)
        elif self.rad_24_7.isChecked(): self.statupdate(24,7)
        if self.rad_25_1.isChecked(): self.statupdate(25,1)
        elif self.rad_25_2.isChecked(): self.statupdate(25,2)
        elif self.rad_25_3.isChecked(): self.statupdate(25,3)
        elif self.rad_25_4.isChecked(): self.statupdate(25,4)
        elif self.rad_25_5.isChecked(): self.statupdate(25,5)
        elif self.rad_25_6.isChecked(): self.statupdate(25,6)
        elif self.rad_25_7.isChecked(): self.statupdate(25,7)
        if self.rad_26_1.isChecked(): self.statupdate(26,1)
        elif self.rad_26_2.isChecked(): self.statupdate(26,2)
        elif self.rad_26_3.isChecked(): self.statupdate(26,3)
        elif self.rad_26_4.isChecked(): self.statupdate(26,4)
        elif self.rad_26_5.isChecked(): self.statupdate(26,5)
        elif self.rad_26_6.isChecked(): self.statupdate(26,6)
        elif self.rad_26_7.isChecked(): self.statupdate(26,7)
        if self.rad_27_1.isChecked(): self.statupdate(27,1)
        elif self.rad_27_2.isChecked(): self.statupdate(27,2)
        elif self.rad_27_3.isChecked(): self.statupdate(27,3)
        elif self.rad_27_4.isChecked(): self.statupdate(27,4)
        elif self.rad_27_5.isChecked(): self.statupdate(27,5)
        elif self.rad_27_6.isChecked(): self.statupdate(27,6)
        elif self.rad_27_7.isChecked(): self.statupdate(27,7)
        if self.rad_28_1.isChecked(): self.statupdate(28,1)
        elif self.rad_28_2.isChecked(): self.statupdate(28,2)
        elif self.rad_28_3.isChecked(): self.statupdate(28,3)
        elif self.rad_28_4.isChecked(): self.statupdate(28,4)
        elif self.rad_28_5.isChecked(): self.statupdate(28,5)
        elif self.rad_28_6.isChecked(): self.statupdate(28,6)
        elif self.rad_28_7.isChecked(): self.statupdate(28,7)
        if self.rad_29_1.isChecked(): self.statupdate(29,1)
        elif self.rad_29_2.isChecked(): self.statupdate(29,2)
        elif self.rad_29_3.isChecked(): self.statupdate(29,3)
        elif self.rad_29_4.isChecked(): self.statupdate(29,4)
        elif self.rad_29_5.isChecked(): self.statupdate(29,5)
        elif self.rad_29_6.isChecked(): self.statupdate(29,6)
        elif self.rad_29_7.isChecked(): self.statupdate(29,7)
        if self.rad_30_1.isChecked(): self.statupdate(30,1)
        elif self.rad_30_2.isChecked(): self.statupdate(30,2)
        elif self.rad_30_3.isChecked(): self.statupdate(30,3)
        elif self.rad_30_4.isChecked(): self.statupdate(30,4)
        elif self.rad_30_5.isChecked(): self.statupdate(30,5)
        elif self.rad_30_6.isChecked(): self.statupdate(30,6)
        elif self.rad_30_7.isChecked(): self.statupdate(30,7)

    # Updates students status
    def statupdate(self, stdno, option):
        global ssint, sslist
        old = ssint[stdno]; ssint[stdno] = option # Cache old option, then update dict
        sslist[old].remove(stdno); sslist[option].append(stdno) # Update list
        sslist[option].sort() # Sort to pretty-print

        for i in range(1, 7): # Status code 7: No input
            exec(f"self.display_content_{i}.setText(tenslice(sslist[{i}]))")
            exec(f"self.lcd_menu_{i}.display(len(purify(sslist[{i}])))")
        self.lcd_school.display(getschoolstd())
        self.status.setText("정상")

    # Loads students list and updates status panel
    def load(self):
        stage = 0; text = []
        try:
            # Load file
            fname = QFileDialog.getOpenFileName(self, "파일 선택", "", "All Files(*)", "")
            if fname[0]:
                text = fileanalyze(open(fname[0], encoding="utf-8"))
            else:
                raise FileNotFoundError
            stage = 1 # Debug CP
            # FileNotFoundError is exception-handled below

            # Assigns each value
            newgrade = int(text[0][-2:].replace(':',''))
            newhomeroom = int(text[1][-3:].replace(':','')) 
            total = int(text[2][-3:].replace(':',''))
            stage = 2

            absent = [*map(int,text[3][3:].replace(':','').split(', '))]
            name = [*map(str,text[4][3:].replace(':','').lstrip().split(', '))]
            stage = 3
            # IndexError in case of illegal data input, and
            # ValueError in case of indentation problem are exception-handled below

            # Initializing global variants & Radios
            global ssint, sslist, maxstdnum, namelist, grade, homeroom
            namelist = copy.deepcopy(name)
            grade = newgrade
            homeroom = newhomeroom
            maxstdnum = total
            for key in sslist: sslist[key] = []
            stage = 4

            for i in range(1, 31): # Clear ssint & Initialize sslist
                ssint[i] = 7; sslist[7].append(i)
                num = str(i).rjust(2,'0') # Initializing radio buttons
                exec(f"self.rad_{num}_1.setChecked(False)")
                exec(f"self.rad_{num}_2.setChecked(False)")
                exec(f"self.rad_{num}_3.setChecked(False)")
                exec(f"self.rad_{num}_4.setChecked(False)")
                exec(f"self.rad_{num}_5.setChecked(False)")
                exec(f"self.rad_{num}_6.setChecked(False)")
                exec(f"self.rad_{num}_7.setChecked(True)")
            stage = 5

            if absent == [0]:
                ssint[0] = total
            else:
                ssint[0] = total - len(absent)
            # ssint now has the number of present students
            stage = 6

            # Updating display labels
            self.display_title.setText(f"{grade}학년 {homeroom}반 야간자율학습 참가 인원 현황") # Main Title
            for i in range(1, 7): # Status code 7: No input
                exec(f"self.display_content_{i}.setText('없음')")
                exec(f"self.lcd_menu_{i}.display(0)")
            self.lcd_school.display(0)
            self.lcd_total.display(ssint[0])
            stage = 7

            for i in range(1, 31): # Names
                num = str(i).rjust(2,'0')
                if i not in absent and i <= total: # Try un-hide present students and changes name
                    exec(f"self.std_no_{num}.setHidden(False)")
                    exec(f"self.std_name_{num}.setHidden(False)")
                    exec(f"self.std_{num}.setHidden(False)")
                    stdname = name[i-1]
                    if len(stdname) == 2:
                        stdname = stdname[0] + '\u3000' + stdname[1] # U+3000 is a FULL-WIDTH SPACE character
                    exec(f"self.std_name_{num}.setText('{stdname}')")
                else: # Hide absent students
                    exec(f"self.std_no_{num}.setHidden(True)")
                    exec(f"self.std_name_{num}.setHidden(True)")
                    exec(f"self.std_{num}.setHidden(True)")
            stage = 8
            self.status.setText("%d학년 %d반 데이터를 정상적으로 불러왔습니다."
                                % (newgrade, newhomeroom))

        except FileNotFoundError as e:
            self.status.setText("[Errno A1] 파일을 선택하지 않았습니다."); print(e)
        except IndexError as e:
            self.status.setText("[Errno A2] 파일 정보 입력칸에 빈칸이 없는지 확인해 주십시오."); print(e)
        except ValueError as e:
            self.status.setText("[Errno A3] 형식에 맞게 정보를 입력했는지 확인해 주십시오."); print(e)
        except Exception as e:
            self.status.setText("[Errno A9] 알 수 없는 오류 발생. 콘솔창을 확인해주세요."); print(f"A9 {e},\n{stage = },\ntext")

    # Save current students' status as .csv format file
    def save(self):
        stage = 0
        
        fname = getfname(self.display_title.text())
        index = isotoday[2]*2 + int(self.period_combo.currentText()) - 1

        stage = 1
        try:
            try:
                with open(fname, mode='r', newline='') as f:
                    reader = csv.reader(f)
                    content = [i for i in reader]
            except FileNotFoundError: # Pre-initialization needed
                content = csv_initialize()
            stage = 2

            for i in range(1, maxstdnum+1):
                for j in range(1, 8):
                    exec(f"if self.rad_{str(i).rjust(2,'0')}_{j}.isChecked(): content[{i}][{index}] = recordmsg[{j}]")
            stage = 3

            with open(fname, mode='w', newline='') as f:
                writer = csv.writer(f)
                for i in content:
                    writer.writerow(i)
            epoch = dt.datetime.now()
            stage = 4

            print("%s:%s:%s 야자관리 프로그램 폴더에 다음 이름으로 %s교시 기록이 저장되었습니다: %s"
                  % (str(epoch.hour).rjust(2), str(epoch.minute).rjust(2), str(epoch.second).rjust(2),
                     self.period_combo.currentText(), fname))
            self.status.setText("%s교시 기록이 %s시 %s분에 저장되었습니다."
                                % (self.period_combo.currentText(), str(epoch.hour).rjust(2), str(epoch.minute).rjust(2)))

        except Exception as e:
            self.status.setText("[Errno B9] 알 수 없는 오류 발생. 콘솔창을 확인해주세요."); print(f"B9 {e},\n{stage = }")

    # Custom sys.exit() function
    def qexit(self):
        print("프로그램 종료"); sys.exit()

# Run
if __name__ == '__main__':
    print("프로그램 준비 중...")
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    print("프로그램 준비 완료")
    app.exec_()
