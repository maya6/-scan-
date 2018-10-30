# -*- coding: utf-8 -*-
import sys
import vulnlist
import tomcat.Main_tomcat
import fckeditor.Main_fckeditor
'''
print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])
'''


if __name__ == "__main__":



    #使用说明
    if len(sys.argv) < 3 or sys.argv[1]=="-h":
        print('''
        moon.py -u  tomcat/fck/all http://xx.xx.xx.xx:xx      # attack
        moon.py -vl tomcat                   # vulnlist
        ''')

    #漏洞清单
    elif sys.argv[1] == '--vulnlist' or sys.argv[1] == '-vl':
        if sys.argv[2] == 'tomcat':
            vulnlist.tomcat_vulnlist()
        elif sys.argv[2] == 'apache':
            vulnlist.apache_vulnlist()
        elif sys.argv[2] == 'fck':
            vulnlist.fck_vulnlist()
        elif sys.argv[2] == 'all':
            vulnlist.tomcat_vulnlist()
            vulnlist.apache_vulnlist()
        else:
            print('[-]参数错误！')

    #漏洞利用
    elif sys.argv[1] == '-u':

        # 处理url末尾可能存在的/
        if sys.argv[3][-1] != '/':
            pass
        else:
            sys.argv[3] = sys.argv[3][0:-1]
        print('[+]检测地址:'+sys.argv[3])


        if sys.argv[2] == 'tomcat':
            tomcat.Main_tomcat.exec(sys.argv[3])
        elif sys.argv[2] == 'fck':
            fckeditor.Main_fckeditor.exec(sys.argv[3])
        elif sys.argv[2] == 'all':
            tomcat.Main_tomcat.exec(sys.argv[3])
            fckeditor.Main_fckeditor.exec(sys.argv[3])
        else:
            print('[-]参数错误！')


    else:
        print('使用的语法说明')
