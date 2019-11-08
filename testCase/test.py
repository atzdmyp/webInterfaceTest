import unittest
from common import configDB
import readConfig as readConfig
import pymysql
import os

localReadConfig = readConfig.ReadConfig()
local_db = configDB.MyDB()
# romwe抽奖活动相关操作


class TestDB(unittest.TestCase):

    def setUp(self):
        self.select_member = None
        self.select_list = {}
        self.cursor = None
        host = localReadConfig.get_db("host")
        username = localReadConfig.get_db("username")
        password = localReadConfig.get_db("password")
        port = localReadConfig.get_db("port")
        database = localReadConfig.get_db("database")
        config = {
            'host': str(host),
            'user': username,
            'passwd': password,
            'port': int(port),
            'db': database
        }
        # execute jmeter case
        result = os.popen(r'E:\JMeter\apache-jmeter-3.0\apache-jmeter-3.0\bin\jmeter.bat -n -t F:\JMeterworkspace\天降礼包.jmx -l f:\result.jtl')
        print(result.read())
        # connect to DB
        self.db = pymysql.connect(**config)
        # create cursor
        self.cursor = self.db.cursor()
        if self.cursor:
            print("Connect DB successfully!")

    def testDB(self):
        # mysql1 = """SELECT activity_type, COUNT(activity_type), is_show FROM `tablename` WHERE email='xxxxxxx' AND is_show=0 GROUP BY activity_type"""
        mysql2 = """SELECT activity_type, COUNT(activity_type), is_show FROM `tablename` WHERE email='xxxxxxx' AND is_show=0 GROUP BY activity_type"""
        file = "F:/result.txt"

        # self.cursor.execute(mysql1)
        # count_num = self.cursor.fetchall()
        # for n in count_num:
        #    with open(file, "a") as f:
        #        f.write("****************天降礼包****************\n抽奖总数：%d \n" % n[0])

        self.cursor.execute(mysql2)
        list = self.cursor.fetchall()
        self.num = 0
        # get result list
        for i in list:
            # if i[0] < 6:
            #    self.num += i[1]
            self.num += i[1]
            with open(file, "a") as f:
                f.write("奖项：%d  出现次数：%d  是否展示：%d \n" % (i[0], i[1], i[2]))
        with open(file, "a") as f:
            f.write("中奖次数：%d \n ********************************\n" % self.num)

        # sumget = """SELECT COUNT(*) FROM tablename WHERE member_id IN (SELECT member_id FROM rs_member WHERE email='xxxxxxx')"""
        # self.cursor.execute(sumget)
        # a = self.cursor.fetchall()
        # for i in a:
        #     print("查询到%d条积分中奖记录。" % i[0])
        #     print("计算到%d条积分中奖记录。" % self.num)
        # coupon_num = """SELECT COUNT(*) FROM tablename WHERE email = 'xxxxxxxx'"""
        # self.cursor.execute(coupon_num)
        # b = self.cursor.fetchall()
        # for n in b:
        #     print("优惠券绑定记录%d条" % n[0])

    def tearDown(self):
        # delsql = """DELETE FROM tablename WHERE email='xxxxxx'"""
        # delsql2 = """DELETE FROM tablename WHERE member_id IN (SELECT member_id FROM tablename WHERE email='xxxxxx') AND last_update_time > '2017-11-07 00:00:00'"""
        # delsql3 = """DELETE FROM tablename WHERE email = 'xxxxxx'"""
        # self.cursor.execute(delsql)
        # self.db.commit()
        # self.cursor.execute(delsql2)
        # self.db.commit()
        # self.cursor.execute(delsql3)
        # self.db.commit()

        # close database
        self.db.close()
