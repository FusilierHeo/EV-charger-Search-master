
#-*- coding: utf-8 -*-
import urllib.request

from xml.dom.minidom import parse,parseString
from xml.etree import ElementTree


server='http://openapi.kepco.co.kr/service/evInfoService/getEvSearchList'
serviceKey="4lmWp814ERUDuydXPhoe%2FcCMA8%2BAdBGDoCEnTrCRixmHXdNe63pJDHI9NJueNefS729hoLtHk67YiFbm6rOzEw%3D%3D"


def urlBuilder(server, key):
    data='?'+'serviceKey='+key+'&numOfRows='+str(600)+'&pageNo='+str(1) +'&addr='
    request=server+data

    print(request)
    return request


def LoadPoint(item):
    dic = {}
    dic["충전소 명"] = item.find("csNm").text
    dic["주소"]=item.find("addr").text
    dic["충전기 타입"]=item.find("chargeTp").text
    #dic["cpName"]=item.find("cpNm").text
    dic["현재 상태"]=item.find("cpStat").text
    #dic["type2"]=item.find("cpTp").text
    dic["위도"]=item.find("lat").text
    dic["경도"]=item.find("longi").text
    dic["시간"]=item.find("statUpdateDatetime").text
    return dic


class ChargingStation:
    def __init__(self, station):
        url = urlBuilder(server, serviceKey)
        data = urllib.request.urlopen(url).read()
        tree = ElementTree.fromstring(data)
        itemElement = list(tree.iter("item"))

        for item in itemElement:
            item.find("addr").text
            tmp = LoadPoint(item)
            station.append(tmp)


    def printList(self, station):
        for i in station:
            print(i)

    def searchList(self, station, add, list):
        list.clear()
        for i in station:
            if add in i["주소"]:
                list.append(i)
    '''
    def CreateJSON(self, station):
        f=open('pos.json','w')
        f.write('{\n"position": [\n')

        for i in station:
            f.write('{\n')
            f.write('"lat": {0},\n'.format(i["위도"]))
            f.write('"lng": {0}\n'.format(i["경도"]))

            f.write('},\n')

        f.write(']\n}')
        f.close()
    '''

def start_Deco(func):
    def func_wrapper(*args, **kwargs):
        return "<!DOCTYPE html>\n{0}\n".format(func(*args, **kwargs))
    return func_wrapper

def html_deco(func):
    def func_wrapper(*args, **kwargs):
        return "<html>\n{0}\n</html>\n".format(func(*args, **kwargs))
    return func_wrapper

def head_deco(func):
    def func_wrapper(*args, **kwargs):
        return "<head>\n{0}\n</head>\n".format(func(*args, **kwargs))
    return func_wrapper

def body_deco(func):
    def func_wrapper(*args, **kwargs):
        return "<body>\n{0}\n</body>\n".format(func(*args, **kwargs))
    return func_wrapper

def div_deco(func):
    def func_wrapper(*args, **kwargs):
        return "<div>{0}</div>\n".format(func(*args, **kwargs))
    return func_wrapper

def script_deco(func):
    def func_wrapper(*args, **kwargs):
        return "<script>\n{0}\n</script>".format(func(*args, **kwargs))
    return func_wrapper