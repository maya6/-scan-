# -*- coding: utf-8 -*-

def tomcat_vulnlist():

    print('''
    Tomcat_vuln_list:
    
    CVE-2017-12615
    应用：上传文件
    影响范围：Linux/Windows  Tomcat: 7.0.0 to 7.0.79 - 官网数据
    成因：Tomcat配置了可写（readonly=false），导致我们可以往服务器写文件
    修复：将 conf/web.xml 中对于 DefaultServlet 的 readonly 设置为 true
    ''')


def apache_vulnlist():
    print('''
    Apache_vuln_list:

    Apache HTTPD 换行解析漏洞（CVE-2017-15715）
    应用：饶过文件名黑名单上传策略，导致绕过一些服务器的安全策略。将上传的 1.php 修改为 /1.php%0a 饶过上传，且可正常解析
    影响范围：Apache HTTPD 2.4.0~2.4.29
    成因：在解析PHP时，1.php\\x0A 将被按照PHP后缀进行解析
    修复：补丁升级？
    
    Apache HTTPD 未知后缀解析漏洞
    应用：饶过文件名黑名单上传策略，导致绕过一些服务器的安全策略。利用解析漏洞上传getshell
    影响范围：Apache、php版本无关，配置不当
    成因：http://your-ip/index.php中是一个白名单检查文件后缀的上传组件，上传完成后并未重命名。我们可以通过上传文件名为xxx.php.jpg或xxx.php.jpeg的文件，利用Apache解析漏洞进行getshell。
    修复：配置？
    
    
    ''')

if __name__ == "__main__":
    tomcat_vulnlist()
    apache_vulnlist()