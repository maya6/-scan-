# -*- coding: utf-8 -*-
import sqlite3
def attack(URL):
    conn = sqlite3.connect('F:/OneDrive/工作/数据库备份/190205-hulianwang.db')
    cursor = conn.cursor()
    #模糊查询
    s = cursor.execute(f"select * from '资产表-190205' where IP地址 LIKE '%{URL}%' or 所属业务系统 LIKE '%{URL}%' or 负责部门 LIKE '%{URL}%' or 负责人 LIKE '%{URL}%' or 科室 LIKE '%{URL}%';")
    if s.fetchall():
        print('[+]发现资产。')
        s = cursor.execute(f"select * from '资产表-190205' where IP地址 LIKE '%{URL}%' or 所属业务系统 LIKE '%{URL}%' or 负责部门 LIKE '%{URL}%' or 负责人 LIKE '%{URL}%' or 科室 LIKE '%{URL}%';")
        for ss in s:
            print(ss)
    else:
        print('[-]未发现相关资产。')


if __name__ == "__main__":
    attack()

