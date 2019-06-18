# -*- coding: utf-8 -*-
import sqlite3
def attack(URL):
    conn = sqlite3.connect('F:/anwang.db')
    cursor = conn.cursor()
    #模糊查询
    s = cursor.execute(f"select * from '资产0521' where IP地址 LIKE '%{URL}%' or 所属业务系统 LIKE '%{URL}%' or 负责部门 LIKE '%{URL}%' or 负责人 LIKE '%{URL}%' or 科室 LIKE '%{URL}%';")
    if s.fetchall():
        print('[+]互联网中心 - 发现资产。')
        s = cursor.execute(f"select * from '资21' where IP地址 LIKE '%{URL}%' or 所属业务系统 LIKE '%{URL}%' or 负责部门 LIKE '%{URL}%' or 负责人 LIKE '%{URL}%' or 科室 LIKE '%{URL}%';")
        for ss in s:
            print(ss)
    else:
        print('[-]互联网中心 - 未发现相关资产。')

    conn1 = sqlite3.connect('F:zhgxin.db')
    cursor1 = conn1.cursor()
    #模糊查询
    s = cursor1.execute(f"select * from '19itong' where IP地址 LIKE '%{URL}%' or 所属业务系统 LIKE '%{URL}%' or 负责部门 LIKE '%{URL}%' or 负责人 LIKE '%{URL}%' or 科室 LIKE '%{URL}%';")
    if s.fetchall():
        print('[+]位置中心 - 业务系统发现资产。')
        s = cursor1.execute(f"select * from '190itong' where IP地址 LIKE '%{URL}%' or 所属业务系统 LIKE '%{URL}%' or 负责部门 LIKE '%{URL}%' or 负责人 LIKE '%{URL}%' or 科室 LIKE '%{URL}%';")
        for ss in s:
            print(ss)
    else:
        print('[-]位置中心 - 业务系统未发现相关资产。')

    s = cursor1.execute(f"select * from '1905han' where IP地址 LIKE '%{URL}%' or 所属业务系统 LIKE '%{URL}%' or 负责部门 LIKE '%{URL}%' or 负责人 LIKE '%{URL}%' or 科室 LIKE '%{URL}%';")
    if s.fetchall():
        print('[+]位置中心 - 负责部门负责人发现资产。')
        s = cursor1.execute(f"select * from '19han' where IP地址 LIKE '%{URL}%' or 所属业务系统 LIKE '%{URL}%' or 负责部门 LIKE '%{URL}%' or 负责人 LIKE '%{URL}%' or 科室 LIKE '%{URL}%';")
        for ss in s:
            print(ss)
    else:
        print('[-]位置中心 - 负责部门负责人未发现相关资产。')

if __name__ == "__main__":
    attack()

