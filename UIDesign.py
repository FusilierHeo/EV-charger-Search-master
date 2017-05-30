# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import subprocess
import Data

stationList=[]
searchList=[]
station=Data.ChargingStation(stationList)

qtCreatorFile = "UIDesign.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.search.clicked.connect(self.Search)
        self.comboBox.currentIndexChanged.connect(self.printInfo)

    def Search(self):
        add = self.lineEdit.text()
        station.searchList(stationList, add, searchList)
        # station.printList(searchList)
        self.setComboBox()
        self.printInfo()

    def setComboBox(self):
        self.comboBox.clear()
        for item in searchList:
            self.comboBox.addItem(item["충전소 명"])

    def printInfo(self):
        index = self.comboBox.currentIndex()
        if index is -1:
            return
        tmpData = searchList[index]
        stationData = "충전소 명 : {0}\n" \
                      "주소 : {1}\n" \
                      "충전기 타입 : {2}\n" \
                      "위도 : {3}\n" \
                      "경도 : {4}\n" \
                      "현재상태 : {5}\n" \
                      "갱신시간 : {6}\n".format(tmpData["충전소 명"], tmpData["주소"], tmpData["충전기 타입"],
                                            tmpData["위도"], tmpData["경도"], tmpData["현재 상태"], tmpData["시간"])
        print(stationData)
        self.textEdit.setText(stationData)

    def sendmail(self):
        import smtplib
        import string

        index = self.comboBox.currentIndex()
        tmpData = searchList[index]
        stationData = "충전소 명 : {0}\n" \
                      "주소 : {1}\n" \
                      "충전기 타입 : {2}\n" \
                      "위도 : {3}\n" \
                      "경도 : {4}\n" \
                      "현재상태 : {5}\n" \
                      "갱신시간 : {6}\n".format(tmpData["충전소 명"], tmpData["주소"], tmpData["충전기 타입"],
                                            tmpData["위도"], tmpData["경도"], tmpData["현재 상태"], tmpData["시간"])

        USER = 'sjhur1991'
        PASS = 'skhur3319'
        TO = 'footman5@naver.com'
        SUBJECT = 'EV 충전소 위치 안내'
        ip = subprocess.check_output("hostname-I", shell=True)
        TEXT = ''
        print(TEXT)
        FROM = USER
        HOST = 'smtp.naver.com:465'
        BODY = string.join((
            'From: %s' % FROM,
            'To: %s' % TO,
            'Subject: %s' % SUBJECT,
            '\r\n',
            TEXT,
        ), '\r\n')

        server = smtplib.SMTP(HOST)
        server.starttls()
        server.login(USER, PASS)
        server.sendmail(FROM, TO, BODY)
        server.quit()

        print('%s 님, 이메일이 성공적으로 전송되었습니다.' % TO)

    if __name__ == "__main+__":
        sendmail()

app = QApplication(sys.argv)
xwin = MyApp()
app.exec()

