# -*- coding: utf-8 -*-
import os
import nmap_br.nmap_n


def exec(IP,PORT):
    try:
        nmap_br.nmap_n.attack(IP,PORT)
    except:
        print('userage: moon.py -u nmap port IP     port,IP为nmap格式。端口可为空 ''')



if __name__ == "__main__":
    exec()
