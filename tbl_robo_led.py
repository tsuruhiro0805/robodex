#tbl_robo_led.csv
#フルカラーLEDを暫定3つ取り付ける
#1つのLEDで、各色0から100で設定できる
#10個のデータで1セットとする　点灯時間(ms)、向かって右LEDのRGB、中央LEDのRGB、左LEDのRGB

#.pyにして、ここでタプルを定義した方が良さそう。
#まずは固定長で考える。(id+時間+RGB*3の11数字)

class tblRobotLED:
    def __init__(self):
        self.DATA = [
            [0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0],   #初期値
            [1,3000,100,  0,  0,  0,100,  0,  0,  0,100]    #3秒点灯
        ]
#1秒毎に色を変えていく
#2,1000,100,0,0,0,100,0,0,0,100,1000,0,100,0,0,0,100,100,0,0,1000,0,0,100,100,0,0,0,100,0
#1秒インターバルの点滅
#3,1000,100,100,100,100,100,100,100,100,100,1000,0,0,0,0,0,0,0,0,0,1000,100,100,100,100,100,100,100,100,100
