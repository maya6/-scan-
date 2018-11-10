# -*- coding: utf-8 -*-
import sys
import vulnlist
import tomcat.Main_tomcat
import fckeditor.Main_fckeditor
import ipquery.Main_ipquery
import weblogic.Main_weblogic
import iis.Main_iis
import docker_vuln.Main_docker
import  redis_vuln.Main_redis



if __name__ == "__main__":

    #使用说明
    if len(sys.argv) < 3 or sys.argv[1]=="-h":
        print('''
        moon.py -u  tomcat/fck/ip/all http://xx.xx.xx.xx:xx      # attack
        ''')

    #漏洞清单
    # elif sys.argv[1] == '--vulnlist' or sys.argv[1] == '-vl':
    #     if sys.argv[2] == 'tomcat':
    #         vulnlist.tomcat_vulnlist()
    #     elif sys.argv[2] == 'apache':
    #         vulnlist.apache_vulnlist()
    #     elif sys.argv[2] == 'fck':
    #         vulnlist.fck_vulnlist()
    #     elif sys.argv[2] == 'all':
    #         vulnlist.tomcat_vulnlist()
    #         vulnlist.apache_vulnlist()
    #     else:
    #         print('[-]参数错误！')

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
        elif sys.argv[2] == 'ip':
            ipquery.Main_ipquery.exec(sys.argv[3])
        elif sys.argv[2] == 'weblogic':
            weblogic.Main_weblogic.exec(sys.argv[3])
        elif sys.argv[2] == 'iis':
            iis.Main_iis.exec(sys.argv[3])
        elif sys.argv[2] == 'docker':
            docker_vuln.Main_docker.exec(sys.argv[3])
        elif sys.argv[2] == 'redis':
            redis_vuln.Main_redis.exec(sys.argv[3])
        elif sys.argv[2] == 'all':
            tomcat.Main_tomcat.exec(sys.argv[3])
            fckeditor.Main_fckeditor.exec(sys.argv[3])
        else:
            print('[-]参数错误！')
    else:
        print('使用的语法说明')
