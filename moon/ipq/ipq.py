# -*- coding: utf-8 -*-
import sqlite3
def attack(URL):
    URL = '\''+URL+'\''
    conn = sqlite3.connect('E:/python/归属查询/hulianwang.db')
    cursor = conn.cursor()
    s = cursor.execute(f"select * from '资产表-181120' where IP地址 = {URL} or 所属业务系统 = {URL} or 负责部门 = {URL} or 负责人 = {URL} or 科室 = {URL};")
    if s.fetchall():
        print('[+]发现资产。')
        s = cursor.execute(f"select * from '资产表-181120' where IP地址 = {URL} or 所属业务系统 = {URL} or 负责部门 = {URL} or 负责人 = {URL} or 科室 = {URL};")
        for ss in s:
            print(ss)
    else:
        print('[-]未发现相关资产。')


if __name__ == "__main__":
    attack()

