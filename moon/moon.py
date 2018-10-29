# -*- coding: utf-8 -*-
import sys
import vulnlist
import tomcat.Main_tomcat

'''
print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])
'''


if __name__ == "__main__":

    #使用说明
    if len(sys.argv) < 3 or sys.argv[1]=="-h":
        print('''
        moon.py -u  tomcat/weblogic http://xx.xx.xx.xx:xx      # attack
        moon.py -vl tomcat/weblogic/apache                     # vulnlist
        ''')

    #漏洞清单
    elif sys.argv[1] == '--vulnlist' or sys.argv[1] == '-vl':
        if sys.argv[2] == 'tomcat':
            vulnlist.tomcat_vulnlist()
        elif sys.argv[2] == 'apache':
            vulnlist.apache_vulnlist()
        elif sys.argv[2] == 'all':
            vulnlist.tomcat_vulnlist()
            vulnlist.apache_vulnlist()

    #漏洞利用
    elif sys.argv[1] == '-u':
        if sys.argv[2] == 'tomcat':
            tomcat.Main_tomcat.exec(sys.argv[3])

    else:
        print('使用的语法说明')
