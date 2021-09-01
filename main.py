# Copyright 2021 Yoon Sung-Yong
# Free use in Daewon Foreign Language High School only
# NIHONGOKA SAIKOU!

import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

form_class = uic.loadUiType('panel.ui')[0]

ssint = {0:30,1:5,2:5,3:5,4:5,5:5,6:5,7:5,8:5,9:5,10:5,11:5,12:5,13:5,14:5,15:5,16:5,17:5,18:5,19:5,20:5,21:5,22:5,23:5,24:5,25:5,26:5,27:5,28:5,29:5,30:5}
sslist = {1:[],2:[],3:[],4:[],5:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]}

# Imported from guipicker
# Returns str with 10 elements in a row
def tenslice(l):
    ret = ''
    if l:
        for i in range(max(0, len(l)//10)+1):
            t = []
            for x in l[10*i:10*(i+1)]: t.append(x)
            ret += ', '.join(str(x).rjust(2) for x in t) + '\n'
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
        self.rad_02_1.clicked.connect(self.radpush)
        self.rad_02_2.clicked.connect(self.radpush)
        self.rad_02_3.clicked.connect(self.radpush)
        self.rad_02_4.clicked.connect(self.radpush)
        self.rad_02_5.clicked.connect(self.radpush)
        self.rad_03_1.clicked.connect(self.radpush)
        self.rad_03_2.clicked.connect(self.radpush)
        self.rad_03_3.clicked.connect(self.radpush)
        self.rad_03_4.clicked.connect(self.radpush)
        self.rad_03_5.clicked.connect(self.radpush)
        self.rad_04_1.clicked.connect(self.radpush)
        self.rad_04_2.clicked.connect(self.radpush)
        self.rad_04_3.clicked.connect(self.radpush)
        self.rad_04_4.clicked.connect(self.radpush)
        self.rad_04_5.clicked.connect(self.radpush)
        self.rad_05_1.clicked.connect(self.radpush)
        self.rad_05_2.clicked.connect(self.radpush)
        self.rad_05_3.clicked.connect(self.radpush)
        self.rad_05_4.clicked.connect(self.radpush)
        self.rad_05_5.clicked.connect(self.radpush)
        self.rad_06_1.clicked.connect(self.radpush)
        self.rad_06_2.clicked.connect(self.radpush)
        self.rad_06_3.clicked.connect(self.radpush)
        self.rad_06_4.clicked.connect(self.radpush)
        self.rad_06_5.clicked.connect(self.radpush)
        self.rad_07_1.clicked.connect(self.radpush)
        self.rad_07_2.clicked.connect(self.radpush)
        self.rad_07_3.clicked.connect(self.radpush)
        self.rad_07_4.clicked.connect(self.radpush)
        self.rad_07_5.clicked.connect(self.radpush)
        self.rad_08_1.clicked.connect(self.radpush)
        self.rad_08_2.clicked.connect(self.radpush)
        self.rad_08_3.clicked.connect(self.radpush)
        self.rad_08_4.clicked.connect(self.radpush)
        self.rad_08_5.clicked.connect(self.radpush)
        self.rad_09_1.clicked.connect(self.radpush)
        self.rad_09_2.clicked.connect(self.radpush)
        self.rad_09_3.clicked.connect(self.radpush)
        self.rad_09_4.clicked.connect(self.radpush)
        self.rad_09_5.clicked.connect(self.radpush)
        self.rad_10_1.clicked.connect(self.radpush)
        self.rad_10_2.clicked.connect(self.radpush)
        self.rad_10_3.clicked.connect(self.radpush)
        self.rad_10_4.clicked.connect(self.radpush)
        self.rad_10_5.clicked.connect(self.radpush)
        self.rad_11_1.clicked.connect(self.radpush)
        self.rad_11_2.clicked.connect(self.radpush)
        self.rad_11_3.clicked.connect(self.radpush)
        self.rad_11_4.clicked.connect(self.radpush)
        self.rad_11_5.clicked.connect(self.radpush)
        self.rad_12_1.clicked.connect(self.radpush)
        self.rad_12_2.clicked.connect(self.radpush)
        self.rad_12_3.clicked.connect(self.radpush)
        self.rad_12_4.clicked.connect(self.radpush)
        self.rad_12_5.clicked.connect(self.radpush)
        self.rad_13_1.clicked.connect(self.radpush)
        self.rad_13_2.clicked.connect(self.radpush)
        self.rad_13_3.clicked.connect(self.radpush)
        self.rad_13_4.clicked.connect(self.radpush)
        self.rad_13_5.clicked.connect(self.radpush)
        self.rad_14_1.clicked.connect(self.radpush)
        self.rad_14_2.clicked.connect(self.radpush)
        self.rad_14_3.clicked.connect(self.radpush)
        self.rad_14_4.clicked.connect(self.radpush)
        self.rad_14_5.clicked.connect(self.radpush)
        self.rad_15_1.clicked.connect(self.radpush)
        self.rad_15_2.clicked.connect(self.radpush)
        self.rad_15_3.clicked.connect(self.radpush)
        self.rad_15_4.clicked.connect(self.radpush)
        self.rad_15_5.clicked.connect(self.radpush)
        self.rad_16_1.clicked.connect(self.radpush)
        self.rad_16_2.clicked.connect(self.radpush)
        self.rad_16_3.clicked.connect(self.radpush)
        self.rad_16_4.clicked.connect(self.radpush)
        self.rad_16_5.clicked.connect(self.radpush)
        self.rad_17_1.clicked.connect(self.radpush)
        self.rad_17_2.clicked.connect(self.radpush)
        self.rad_17_3.clicked.connect(self.radpush)
        self.rad_17_4.clicked.connect(self.radpush)
        self.rad_17_5.clicked.connect(self.radpush)
        self.rad_18_1.clicked.connect(self.radpush)
        self.rad_18_2.clicked.connect(self.radpush)
        self.rad_18_3.clicked.connect(self.radpush)
        self.rad_18_4.clicked.connect(self.radpush)
        self.rad_18_5.clicked.connect(self.radpush)
        self.rad_19_1.clicked.connect(self.radpush)
        self.rad_19_2.clicked.connect(self.radpush)
        self.rad_19_3.clicked.connect(self.radpush)
        self.rad_19_4.clicked.connect(self.radpush)
        self.rad_19_5.clicked.connect(self.radpush)
        self.rad_20_1.clicked.connect(self.radpush)
        self.rad_20_2.clicked.connect(self.radpush)
        self.rad_20_3.clicked.connect(self.radpush)
        self.rad_20_4.clicked.connect(self.radpush)
        self.rad_20_5.clicked.connect(self.radpush)
        self.rad_21_1.clicked.connect(self.radpush)
        self.rad_21_2.clicked.connect(self.radpush)
        self.rad_21_3.clicked.connect(self.radpush)
        self.rad_21_4.clicked.connect(self.radpush)
        self.rad_21_5.clicked.connect(self.radpush)
        self.rad_22_1.clicked.connect(self.radpush)
        self.rad_22_2.clicked.connect(self.radpush)
        self.rad_22_3.clicked.connect(self.radpush)
        self.rad_22_4.clicked.connect(self.radpush)
        self.rad_22_5.clicked.connect(self.radpush)
        self.rad_23_1.clicked.connect(self.radpush)
        self.rad_23_2.clicked.connect(self.radpush)
        self.rad_23_3.clicked.connect(self.radpush)
        self.rad_23_4.clicked.connect(self.radpush)
        self.rad_23_5.clicked.connect(self.radpush)
        self.rad_24_1.clicked.connect(self.radpush)
        self.rad_24_2.clicked.connect(self.radpush)
        self.rad_24_3.clicked.connect(self.radpush)
        self.rad_24_4.clicked.connect(self.radpush)
        self.rad_24_5.clicked.connect(self.radpush)
        self.rad_25_1.clicked.connect(self.radpush)
        self.rad_25_2.clicked.connect(self.radpush)
        self.rad_25_3.clicked.connect(self.radpush)
        self.rad_25_4.clicked.connect(self.radpush)
        self.rad_25_5.clicked.connect(self.radpush)
        self.rad_26_1.clicked.connect(self.radpush)
        self.rad_26_2.clicked.connect(self.radpush)
        self.rad_26_3.clicked.connect(self.radpush)
        self.rad_26_4.clicked.connect(self.radpush)
        self.rad_26_5.clicked.connect(self.radpush)
        self.rad_27_1.clicked.connect(self.radpush)
        self.rad_27_2.clicked.connect(self.radpush)
        self.rad_27_3.clicked.connect(self.radpush)
        self.rad_27_4.clicked.connect(self.radpush)
        self.rad_27_5.clicked.connect(self.radpush)
        self.rad_28_1.clicked.connect(self.radpush)
        self.rad_28_2.clicked.connect(self.radpush)
        self.rad_28_3.clicked.connect(self.radpush)
        self.rad_28_4.clicked.connect(self.radpush)
        self.rad_28_5.clicked.connect(self.radpush)
        self.rad_29_1.clicked.connect(self.radpush)
        self.rad_29_2.clicked.connect(self.radpush)
        self.rad_29_3.clicked.connect(self.radpush)
        self.rad_29_4.clicked.connect(self.radpush)
        self.rad_29_5.clicked.connect(self.radpush)
        self.rad_30_1.clicked.connect(self.radpush)
        self.rad_30_2.clicked.connect(self.radpush)
        self.rad_30_3.clicked.connect(self.radpush)
        self.rad_30_4.clicked.connect(self.radpush)
        self.rad_30_5.clicked.connect(self.radpush)

        # Load Button
        self.loadbtn.clicked.connect(self.load)

        # Quit Button
        self.exitbtn.clicked.connect(self.qexit)

    # Relaying rad_clicked and statupdate
    def radpush(self):
        if self.rad_01_1.isChecked(): self.statupdate(1,1)
        elif self.rad_01_2.isChecked(): self.statupdate(1,2)
        elif self.rad_01_3.isChecked(): self.statupdate(1,3)
        elif self.rad_01_4.isChecked(): self.statupdate(1,4)
        elif self.rad_01_5.isChecked(): self.statupdate(1,5)
        if self.rad_02_1.isChecked(): self.statupdate(2,1)
        elif self.rad_02_2.isChecked(): self.statupdate(2,2)
        elif self.rad_02_3.isChecked(): self.statupdate(2,3)
        elif self.rad_02_4.isChecked(): self.statupdate(2,4)
        elif self.rad_02_5.isChecked(): self.statupdate(2,5)
        if self.rad_03_1.isChecked(): self.statupdate(3,1)
        elif self.rad_03_2.isChecked(): self.statupdate(3,2)
        elif self.rad_03_3.isChecked(): self.statupdate(3,3)
        elif self.rad_03_4.isChecked(): self.statupdate(3,4)
        elif self.rad_03_5.isChecked(): self.statupdate(3,5)
        if self.rad_04_1.isChecked(): self.statupdate(4,1)
        elif self.rad_04_2.isChecked(): self.statupdate(4,2)
        elif self.rad_04_3.isChecked(): self.statupdate(4,3)
        elif self.rad_04_4.isChecked(): self.statupdate(4,4)
        elif self.rad_04_5.isChecked(): self.statupdate(4,5)
        if self.rad_05_1.isChecked(): self.statupdate(5,1)
        elif self.rad_05_2.isChecked(): self.statupdate(5,2)
        elif self.rad_05_3.isChecked(): self.statupdate(5,3)
        elif self.rad_05_4.isChecked(): self.statupdate(5,4)
        elif self.rad_05_5.isChecked(): self.statupdate(5,5)
        if self.rad_06_1.isChecked(): self.statupdate(6,1)
        elif self.rad_06_2.isChecked(): self.statupdate(6,2)
        elif self.rad_06_3.isChecked(): self.statupdate(6,3)
        elif self.rad_06_4.isChecked(): self.statupdate(6,4)
        elif self.rad_06_5.isChecked(): self.statupdate(6,5)
        if self.rad_07_1.isChecked(): self.statupdate(7,1)
        elif self.rad_07_2.isChecked(): self.statupdate(7,2)
        elif self.rad_07_3.isChecked(): self.statupdate(7,3)
        elif self.rad_07_4.isChecked(): self.statupdate(7,4)
        elif self.rad_07_5.isChecked(): self.statupdate(7,5)
        if self.rad_08_1.isChecked(): self.statupdate(8,1)
        elif self.rad_08_2.isChecked(): self.statupdate(8,2)
        elif self.rad_08_3.isChecked(): self.statupdate(8,3)
        elif self.rad_08_4.isChecked(): self.statupdate(8,4)
        elif self.rad_08_5.isChecked(): self.statupdate(8,5)
        if self.rad_09_1.isChecked(): self.statupdate(9,1)
        elif self.rad_09_2.isChecked(): self.statupdate(9,2)
        elif self.rad_09_3.isChecked(): self.statupdate(9,3)
        elif self.rad_09_4.isChecked(): self.statupdate(9,4)
        elif self.rad_09_5.isChecked(): self.statupdate(9,5)
        if self.rad_10_1.isChecked(): self.statupdate(10,1)
        elif self.rad_10_2.isChecked(): self.statupdate(10,2)
        elif self.rad_10_3.isChecked(): self.statupdate(10,3)
        elif self.rad_10_4.isChecked(): self.statupdate(10,4)
        elif self.rad_10_5.isChecked(): self.statupdate(10,5)
        if self.rad_11_1.isChecked(): self.statupdate(11,1)
        elif self.rad_11_2.isChecked(): self.statupdate(11,2)
        elif self.rad_11_3.isChecked(): self.statupdate(11,3)
        elif self.rad_11_4.isChecked(): self.statupdate(11,4)
        elif self.rad_11_5.isChecked(): self.statupdate(11,5)
        if self.rad_12_1.isChecked(): self.statupdate(12,1)
        elif self.rad_12_2.isChecked(): self.statupdate(12,2)
        elif self.rad_12_3.isChecked(): self.statupdate(12,3)
        elif self.rad_12_4.isChecked(): self.statupdate(12,4)
        elif self.rad_12_5.isChecked(): self.statupdate(12,5)
        if self.rad_13_1.isChecked(): self.statupdate(13,1)
        elif self.rad_13_2.isChecked(): self.statupdate(13,2)
        elif self.rad_13_3.isChecked(): self.statupdate(13,3)
        elif self.rad_13_4.isChecked(): self.statupdate(13,4)
        elif self.rad_13_5.isChecked(): self.statupdate(13,5)
        if self.rad_14_1.isChecked(): self.statupdate(14,1)
        elif self.rad_14_2.isChecked(): self.statupdate(14,2)
        elif self.rad_14_3.isChecked(): self.statupdate(14,3)
        elif self.rad_14_4.isChecked(): self.statupdate(14,4)
        elif self.rad_14_5.isChecked(): self.statupdate(14,5)
        if self.rad_15_1.isChecked(): self.statupdate(15,1)
        elif self.rad_15_2.isChecked(): self.statupdate(15,2)
        elif self.rad_15_3.isChecked(): self.statupdate(15,3)
        elif self.rad_15_4.isChecked(): self.statupdate(15,4)
        elif self.rad_15_5.isChecked(): self.statupdate(15,5)
        if self.rad_16_1.isChecked(): self.statupdate(16,1)
        elif self.rad_16_2.isChecked(): self.statupdate(16,2)
        elif self.rad_16_3.isChecked(): self.statupdate(16,3)
        elif self.rad_16_4.isChecked(): self.statupdate(16,4)
        elif self.rad_16_5.isChecked(): self.statupdate(16,5)
        if self.rad_17_1.isChecked(): self.statupdate(17,1)
        elif self.rad_17_2.isChecked(): self.statupdate(17,2)
        elif self.rad_17_3.isChecked(): self.statupdate(17,3)
        elif self.rad_17_4.isChecked(): self.statupdate(17,4)
        elif self.rad_17_5.isChecked(): self.statupdate(17,5)
        if self.rad_18_1.isChecked(): self.statupdate(18,1)
        elif self.rad_18_2.isChecked(): self.statupdate(18,2)
        elif self.rad_18_3.isChecked(): self.statupdate(18,3)
        elif self.rad_18_4.isChecked(): self.statupdate(18,4)
        elif self.rad_18_5.isChecked(): self.statupdate(18,5)
        if self.rad_19_1.isChecked(): self.statupdate(19,1)
        elif self.rad_19_2.isChecked(): self.statupdate(19,2)
        elif self.rad_19_3.isChecked(): self.statupdate(19,3)
        elif self.rad_19_4.isChecked(): self.statupdate(19,4)
        elif self.rad_19_5.isChecked(): self.statupdate(19,5)
        if self.rad_20_1.isChecked(): self.statupdate(20,1)
        elif self.rad_20_2.isChecked(): self.statupdate(20,2)
        elif self.rad_20_3.isChecked(): self.statupdate(20,3)
        elif self.rad_20_4.isChecked(): self.statupdate(20,4)
        elif self.rad_20_5.isChecked(): self.statupdate(20,5)
        if self.rad_21_1.isChecked(): self.statupdate(21,1)
        elif self.rad_21_2.isChecked(): self.statupdate(21,2)
        elif self.rad_21_3.isChecked(): self.statupdate(21,3)
        elif self.rad_21_4.isChecked(): self.statupdate(21,4)
        elif self.rad_21_5.isChecked(): self.statupdate(21,5)
        if self.rad_22_1.isChecked(): self.statupdate(22,1)
        elif self.rad_22_2.isChecked(): self.statupdate(22,2)
        elif self.rad_22_3.isChecked(): self.statupdate(22,3)
        elif self.rad_22_4.isChecked(): self.statupdate(22,4)
        elif self.rad_22_5.isChecked(): self.statupdate(22,5)
        if self.rad_23_1.isChecked(): self.statupdate(23,1)
        elif self.rad_23_2.isChecked(): self.statupdate(23,2)
        elif self.rad_23_3.isChecked(): self.statupdate(23,3)
        elif self.rad_23_4.isChecked(): self.statupdate(23,4)
        elif self.rad_23_5.isChecked(): self.statupdate(23,5)
        if self.rad_24_1.isChecked(): self.statupdate(24,1)
        elif self.rad_24_2.isChecked(): self.statupdate(24,2)
        elif self.rad_24_3.isChecked(): self.statupdate(24,3)
        elif self.rad_24_4.isChecked(): self.statupdate(24,4)
        elif self.rad_24_5.isChecked(): self.statupdate(24,5)
        if self.rad_25_1.isChecked(): self.statupdate(25,1)
        elif self.rad_25_2.isChecked(): self.statupdate(25,2)
        elif self.rad_25_3.isChecked(): self.statupdate(25,3)
        elif self.rad_25_4.isChecked(): self.statupdate(25,4)
        elif self.rad_25_5.isChecked(): self.statupdate(25,5)
        if self.rad_26_1.isChecked(): self.statupdate(26,1)
        elif self.rad_26_2.isChecked(): self.statupdate(26,2)
        elif self.rad_26_3.isChecked(): self.statupdate(26,3)
        elif self.rad_26_4.isChecked(): self.statupdate(26,4)
        elif self.rad_26_5.isChecked(): self.statupdate(26,5)
        if self.rad_27_1.isChecked(): self.statupdate(27,1)
        elif self.rad_27_2.isChecked(): self.statupdate(27,2)
        elif self.rad_27_3.isChecked(): self.statupdate(27,3)
        elif self.rad_27_4.isChecked(): self.statupdate(27,4)
        elif self.rad_27_5.isChecked(): self.statupdate(27,5)
        if self.rad_28_1.isChecked(): self.statupdate(28,1)
        elif self.rad_28_2.isChecked(): self.statupdate(28,2)
        elif self.rad_28_3.isChecked(): self.statupdate(28,3)
        elif self.rad_28_4.isChecked(): self.statupdate(28,4)
        elif self.rad_28_5.isChecked(): self.statupdate(28,5)
        if self.rad_29_1.isChecked(): self.statupdate(29,1)
        elif self.rad_29_2.isChecked(): self.statupdate(29,2)
        elif self.rad_29_3.isChecked(): self.statupdate(29,3)
        elif self.rad_29_4.isChecked(): self.statupdate(29,4)
        elif self.rad_29_5.isChecked(): self.statupdate(29,5)
        if self.rad_30_1.isChecked(): self.statupdate(30,1)
        elif self.rad_30_2.isChecked(): self.statupdate(30,2)
        elif self.rad_30_3.isChecked(): self.statupdate(30,3)
        elif self.rad_30_4.isChecked(): self.statupdate(30,4)
        elif self.rad_30_5.isChecked(): self.statupdate(30,5)

    # Updates students status
    def statupdate(self, stdno, option):
        global ssint, sslist
        old = ssint[stdno]; ssint[stdno] = option # Cache old option, then update dict
        sslist[old].remove(stdno); sslist[option].append(stdno) # Update list
        sslist[option].sort() # Sort to pretty-print
        self.labelupdate(old, option, len(sslist[1])+len(sslist[2])+len(sslist[3])+len(sslist[4]))

    # Updates display texts
    def labelupdate(self, old, new, remain):
        if old != 5: exec(f"self.display_content_{old}.setText(tenslice(sslist[old]))")
        if new != 5: exec(f"self.display_content_{new}.setText(tenslice(sslist[new]))")
        exec(f"self.display_total.display({remain})")

    # Loads students list and updates status panel
    def load(self):
        stage = 0; text = []
        try:
            # Load file
            fname = QFileDialog.getOpenFileName(self, "파일 선택", "", "All Files(*)", '')
            if fname[0]:
                text = fileanalyze(open(fname[0], encoding='utf-8'))
            else:
                raise FileNotFoundError
            stage = 1 # Debug CP
            # FileNotFoundError is exception-handled below

            # Assigns each value
            grade = int(text[0][-2:].replace(':',''))
            homeroom = int(text[1][-3:].replace(':','')) 
            total = int(text[2][-3:].replace(':',''))
            stage = 2

            absent = [*map(int,text[3][3:].replace(':','').split(', '))]
            name = [*map(str,text[4][3:].replace(':','').lstrip().split(', '))]
            stage = 3
            # IndexError in case of illegal data input, and
            # ValueError in case of indentation problem are exception-handled below

            # Initializing global variants & Radios
            global ssint, sslist
            for key in sslist: sslist[key] = []
            stage = 4

            for i in range(1, 31): # Clear ssint & Initialize sslist
                ssint[i] = 5; sslist[5].append(i)
                num = str(i).rjust(2,'0') # Initializing radio buttons
                exec(f"self.rad_{num}_1.setChecked(False)")
                exec(f"self.rad_{num}_2.setChecked(False)")
                exec(f"self.rad_{num}_3.setChecked(False)")
                exec(f"self.rad_{num}_4.setChecked(False)")
                exec(f"self.rad_{num}_5.setChecked(True)")
            stage = 5

            ssint[0] = total - len(absent) # ssint now has the number of present students
            stage = 6

            # Updating display labels
            self.display_title_1.setText(f"{grade}학년 {homeroom}반 야간자율학습 참가 인원 현황") # Main Title
            self.display_content_1.setText("없음") # Status section
            self.display_content_2.setText("없음")
            self.display_content_3.setText("없음")
            self.display_content_4.setText("없음")
            self.display_total.display(0) # Total number section
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
            self.loadstatus.setText("정상")

        except FileNotFoundError as e:
            self.loadstatus.setText("[Errno 1] 파일을 선택하지 않았습니다."); print(e)
        except IndexError as e:
            self.loadstatus.setText("[Errno 2] 파일 정보 입력칸에 빈칸이 없는지 확인해 주십시오."); print(e)
        except ValueError as e:
            self.loadstatus.setText("[Errno 3] 형식에 맞게 정보를 입력했는지 확인해 주십시오."); print(e)
        except Exception as e:
            self.loadstatus.setText("[Errno 0] 알 수 없는 오류 발생. 콘솔창을 확인해주세요."); print(e, stage, text, sep='\n')

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
