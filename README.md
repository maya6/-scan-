# vulnerability-list
一个的漏洞检测工具。     
  
  ## Tomcat：  
  CVE_2017_12615 / CVE_2017_12617  
  tomcat_weakpassword  
  example_vulnerability(检测tomcat的examples等目录是否存在)  
  > moon.py -u tomcat http://xx.xx.xx.xx:xxxx
  
  ## Fckeditor:  
  获取版本及常见上传页面检测  
  fck<=2.4版本上传直接上传asa文件getshell  
  > moon.py -u fck http://xx.xx.xx.xx/fckxx  
  
  ## Weblogic：  
  CVE_2017_10271 #利用方法参考：https://vulhub.org  
  weblogic_ssrf_cve-2014-4210  
  weblogic_weakpassword  
  > moon.py -u weblogic http://xx.xx.xx.xx:xxxx   
  
  ## IP归属查询：  
  能简单查一下IP的归属地  
  > moon.py -u ip http://www.xxx.com  
  
  ## IIS：  
  短文件名泄露 #来自 lijiejie/IIS_shortname_Scanner  
  > moon.py -u iis http://xx.xx.xx.xx  
  
  ## Docker：  
  docker_daemon_api未授权访问  
  > moon.py -u docker http://xx.xx.xx.xx:xxxx  
  
  ## Redis： 
  redis未授权访问  
  > moon.py -u redis http://xx.xx.xx.xx:xxxx or moon.py -u redis xx.xx.xx.xx:xxxx  
  
  ## Zabbix:  
  zabbix_sql_CVE_2016_10134      #有参考独自等待的脚本  
  > moon.py -u zabbix http://xx.xx.xx.xx:xxxx  
  
  ## Navigate:  
  navigate_Unauthenticated_Remote_Code_Execution  #利用方法参考  https://www.exploit-db.com/exploits/45561/  
  > moon.py -u navigate http://xx.xx.xx.xx:xxxx  
  
  ## Gatepass:  
  Gate Pass Management System 2.1 - 'login' SQL Injection      #参考  https://www.exploit-db.com/exploits/45766/  
  > moon.py -u gatepass http://xx.xx.xx.xx:xxxx
  
