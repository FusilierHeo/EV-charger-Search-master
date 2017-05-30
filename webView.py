from PyQt5.QtWidgets import *
from PyQt5.QtCore import * #table 쓰기위한 import 형식
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *

import Data

station=[]
charging=Data.ChargingStation(station)


@Data.head_deco
def Head():
    return '\t<meta charset="utf-8">\n\t<title>지도 생성하기</title>'

def scale():
    return '<div id="map" style="width:100%;height:700px;"></div>\n'

def api():
    return '<script type="text/javascript" src="http://apis.daum.net/maps/maps3.js?apikey=86b3d296fd406d6de445c8b66d2479c8"></script>\n'

@Data.script_deco
def drawMap():
    map = "var map = new daum.maps.Map(document.getElementById('map'), {\n" \
          "center : new daum.maps.LatLng(36.2683, 127.6358),\n" \
          "level : 14\n" \
          "});\n"

    cluster="var clusterer = new daum.maps.MarkerClusterer({\n" \
            "map: map,\n" \
            "averageCenter: true,\n" \
            "minLevel: 10\n" \
            " });\n"

    #array="var foo = new Array()"
    num=0
    marker="var markerPosition  = new daum.maps.LatLng(33.450701, 126.570667); " \
           "var marker = new daum.maps.Marker({" \
           "position: markerPosition" \
           "});"

    '''
    for i in station:
        marker+="foo[{0}] = new daum.maps.Marker({position : new daum.maps.LatLng({1}, {2})});\n".format(num, i["위도"], i["경도"])
        num+=1

    
    mark="for(var i=0; i<{0}; i++)\n" \
         "clusterer.addMarkers(foo[i]);".format(len(station))

'''
    mark="clusterer.addMarkers(marker);"
    return map+cluster+marker+mark

@Data.body_deco
def body():
    return scale()+api()+drawMap()

@Data.start_Deco
@Data.html_deco
def all():
    return Head()+body()

maphtml=all()
'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>지도 생성하기</title>

</head>
<body>
<!-- 지도를 표시할 div 입니다 -->
<div id="map" style="width:100%;height:700px;"></div>

<script type="text/javascript" src="http://apis.daum.net/maps/maps3.js?apikey=86b3d296fd406d6de445c8b66d2479c8"></script>
<script>
  var map = new daum.maps.Map(document.getElementById('map'), { // 지도를 표시할 div
        center : new daum.maps.LatLng(36.2683, 127.6358), // 지도의 중심좌표
        level : 14 // 지도의 확대 레벨
    });

    // 마커 클러스터러를 생성합니다
    var clusterer = new daum.maps.MarkerClusterer({
        map: map, // 마커들을 클러스터로 관리하고 표시할 지도 객체
        averageCenter: true, // 클러스터에 포함된 마커들의 평균 위치를 클러스터 마커 위치로 설정
        minLevel: 10 // 클러스터 할 최소 지도 레벨
    });

    // 데이터를 가져오기 위해 jQuery를 사용합니다
    // 데이터를 가져와 마커를 생성하고 클러스터러 객체에 넘겨줍니다
    $.get("pos2.json", function(data) {
        // 데이터에서 좌표 값을 가지고 마커를 표시합니다
        // 마커 클러스터러로 관리할 마커 객체는 생성할 때 지도 객체를 설정하지 않습니다
        var markers = $(data.positions).map(function(i, position) {
            return new daum.maps.Marker({
                position : new daum.maps.LatLng(position.lat, position.lng)
            });
        });

        // 클러스터러에 마커들을 추가합니다
        clusterer.addMarkers(markers);
    });
</script>
</body>
</html>
'''



class Browser(QApplication):
    def __init__(self):
        QApplication.__init__(self, [])
        self.window = QWidget()
        self.window.setWindowTitle("Daum Map Api");

        self.web = QWebView(self.window)
        self.web.setMinimumSize(800,800)
        self.web.page().mainFrame().addToJavaScriptWindowObject('self', self)
        self.web.setHtml(maphtml)

        self.text = QTextEdit(self.window)

        self.layout = QVBoxLayout(self.window)
        self.layout.addWidget(self.web)
        self.layout.addWidget(self.text)

        self.window.show()
        self.exec_()

    @pyqtSlot(float, float, int)
    def polygoncomplete(self, lat, lng, i):
        if i == 0:
            self.text.clear()
        self.text.append("Point #{} ({}, {})".format(i, lat, lng))

Browser()