import tbl_robo_motion

#csvファイルのテーブルを開いて、通し番号に対応するデータを持ってくる
class GetRobotActionDataOfMotion:

        def __init__(self):
                #robot_action_data_of_motion = (0,0)
                self.robot_action_data_of_motion = tbl_robo_motion.tblRobotSRV()
        def getRobotMotion(self,motion_tbl_no):
		#ここで、csvなどのテーブルファイルを開き、motion_tbl_noに対応するコメントを返り値の変数に入れる
                return self.robot_action_data_of_motion.DATA[motion_tbl_no]
