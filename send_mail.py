# sudo nano /home/pi/ip_mailer.py


# -*- coding: utf-8 -*-

import subprocess
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Data import LoadPoint
import UIDesign
from UIDesign import MyApp

#index = self.comboBox.currentIndex()
#stationList = []
#searchList = []


def sendmail():
    import  smtplib
    import string



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
    ip = subprocess.check_output("hostname-I", shell = True)
    TEXT = ''
    print(TEXT)
    FROM = USER
    HOST = 'smtp.naver.com:465'
    BODY = string.join((
        'From: %s'%FROM,
        'To: %s'%TO,
        'Subject: %s'%SUBJECT,
        '\r\n',
        TEXT,
    ),'\r\n')

    server = smtplib.SMTP(HOST)
    server.starttls()
    server.login(USER, PASS)
    server.sendmail(FROM, TO, BODY)
    server.quit()

    print('%s 님, 이메일이 성공적으로 전송되었습니다.'%TO)

if __name__=="__main+__":
    sendmail()


