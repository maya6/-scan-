# -*- coding: utf-8 -*-

def tomcat_vulnlist():

    print('''
    Tomcat_vuln_list:
    
    [+]CVE-2017-12615[+]
    应用：上传文件
    影响范围：Linux/Windows  Tomcat: 7.0.0 to 7.0.79 - 官网数据
    成因：Tomcat配置了可写（readonly=false），导致我们可以往服务器写文件
    修复：将 conf/web.xml 中对于 DefaultServlet 的 readonly 设置为 true
    
    [+]CVE-2017-12617[+]
    与CVE-2017-12615类似
    
    [+]example_vulnerability[+]
    影响范围：Tomcat: 全版本
    session操纵漏洞：Apache Tomcat默认安装包含”/examples”目录，里面存着众多的样例，
                    其中session样例(/examples/servlets/servlet/SessionExample)允许用户对session进行操纵。
                    因为session是全局通用的，所以用户可以通过操纵session获取管理员权限。
                    (不一定都是全局的，如果path只在examples下，那就无法利用)。
                    利用此漏洞需要知道相关后台登录后的session键值对，然后写入到session中，利用条件苛刻。
                    https://cloud.tencent.com/info/2e03f26090fe592b6c7aa933dd6c0f94.html
    解决办法：安装完tomcat后，删除$CATALINA_HOME/webapps下默认的所有目录文件* rm -rf /srv/apache-tomcat/webapps/*
    ''')


def apache_vulnlist():
    print('''
    
    ''')

if __name__ == "__main__":
    tomcat_vulnlist()
    apache_vulnlist()