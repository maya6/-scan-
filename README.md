# vulnerability-list
一个常见中间件的漏洞检测工具。  
包含的脚本有参考国内外前辈代码。  
目前支持功能较少，仅作为个人备忘。  
  
  Tomcat：  
  CVE_2017_12615 / CVE_2017_12617  
  example_vulnerability(检测tomcat的examples等目录是否存在)
  moon.py -u tomcat http://xx.xx.xx.xx:8080
  
  Fckeditor:  
  获取版本及常见上传页面检测  
  fck<=2.4版本上传直接上传asa文件getshell
  moon.py -u fck http://xx.xx.xx.xx/fck
  
  IP归属查询：  
  能简单查一下IP的归属地  
  moon.py -u ip http://www.xxx.com
