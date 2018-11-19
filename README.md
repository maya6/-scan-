# vulnerability-list
一个常见中间件的漏洞检测工具。    
目前支持功能较少，仅作为个人备忘。  
  
  Tomcat：  
  CVE_2017_12615 / CVE_2017_12617  
  example_vulnerability(检测tomcat的examples等目录是否存在)  
  moon.py -u tomcat http://xx.xx.xx.xx:xxxx
  
  Fckeditor:  
  获取版本及常见上传页面检测  
  fck<=2.4版本上传直接上传asa文件getshell  
  moon.py -u fck http://xx.xx.xx.xx/fckxx  
  
  Weblogic：  
  CVE_2017_10271 #利用方法参考：https://vulhub.org  
  moon.py -u weblogic http://xx.xx.xx.xx:xxxx   
  
  IP归属查询：  
  能简单查一下IP的归属地  
  moon.py -u ip http://www.xxx.com  
  
  IIS：  
  短文件名泄露 #来自 lijiejie/IIS_shortname_Scanner  
  moon.py -u iis http://xx.xx.xx.xx  
  
  Docker：  
  docker_daemon_api未授权访问  
  moon.py -u docker http://xx.xx.xx.xx:xxxx  
  
  Redis： 
  redis未授权访问  
  moon.py -u redis http://xx.xx.xx.xx:xxxx or moon.py -u redis xx.xx.xx.xx:xxxx  
  
  Zabbix:  
  zabbix_sql_CVE_2016_10134      #有参考独自等待的脚本  
  moon.py -u zabbix http://xx.xx.xx.xx:xxxx
