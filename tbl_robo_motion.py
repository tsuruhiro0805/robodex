#tbl_robo_motion.csv
#csvならコメントアウト消さないといけない？
#速度と時間の２つずつのセット　角度より扱いやすそうなので速度にした
#時間の単位は暫定でmsとする
#速度が0で時間が0でないセットは、その場で指定時間停止することを意味する
#速度の単位は未定　動かしてみてから考える

#0,0,0#動作しない
#1,50,500,0,500,-50,1000,50,500#いやいや首振り
#2,50,1000,0,1000,-50,2000,50,1000#いやいや首振り2倍ストローク
#3,100,500,0,500,-100,1000,100,500#いやいや首振り2倍速度

class tblRobotSRV:
    def __init__(self):
        self.DATA = [
            [0,0,0],            #動作しない
            [1,30,200,-30,200,0,0],     #いやいや首振り
            [2,60,200,-60,200,0,0],     #いやいや首振り2倍ストローク
            [3,90,200,-90,200,0,0]      #いやいや首振り2倍ストローク
        ]

#角度と停止時間(ms)の3セットにする

#0,0,0,0,0,0,0#動作しない
#1,30,200,-30,200,0,0#いやいや首振り
#2,60,200,-60,200,0,0#いやいや首振り2倍ストローク
