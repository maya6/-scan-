# -*- coding: utf-8 -*-
import sys
import requests
import time

'''
Usage:
    moon.py -u  fckeditor http://127.0.0.1:8080
    
'''

def attack(URL):
    urls = (
        '/FCKeditor/_samples/default.html',
        '/FCKeditor/_samples/asp/sample01.asp',
        '/FCKeditor/_samples/asp/sample02.asp',
        '/FCKeditor/_samples/asp/sample03.asp',
        '/FCKeditor/_samples/asp/sample04.asp',
        '/fckeditor/editor/filemanager/connectors/test.html',
        '/_samples/default.html',
        '/_samples/asp/sample01.asp',
        '/_samples/asp/sample02.asp',
        '/_samples/asp/sample03.asp',
        '/_samples/asp/sample04.asp',
        '/editor/filemanager/connectors/test.html',
        '/FCKeditor/editor/filemanager/upload/test.html',
        '/FCKeditor/editor/filemanager/browser/default/connectors/test.html',
        '/FCKeditor/editor/filemanager/browser/default/browser.html?Type=Image&Connector=connectors/jsp/connector',
        '/FCKeditor/editor/filemanager/connectors/test.html',
        '/FCKeditor/editor/filemanager/connectors/uploadtest.html'
        '/editor/filemanager/upload/test.html',
        '/editor/filemanager/browser/default/connectors/test.html',
        '/editor/filemanager/browser/default/browser.html?Type=Image&Connector=connectors/jsp/connector',
        '/editor/filemanager/connectors/test.html',
        '/editor/filemanager/connectors/uploadtest.html'

    )

    print('[+]开始检测-Fckeditor敏感目录。[+]')
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers={"User-Agent":user_agent}
    for url in urls:
        url = URL + url
        try:
            verify_response = requests.get(url, headers=headers)

            if verify_response.status_code == 200:
                print('存在此页面：'+url)
            else :
                continue
        except :
            print("Someerror!")
    print('[+]检测结束-Fckeditor敏感目录。[+]')
    print('\n')

if __name__ == "__main__":
    attack()


