# -*- coding: utf-8 -*-
from urllib.parse import urlparse
import socket
import requests
import urllib3
from bs4 import BeautifulSoup


def attack(URL):
    # 百度查询模块
    url = URL
    URL = urlparse(URL).netloc
    if URL == '':
        URL = url
    else:
        pass
    try:
        ip = URL
        payload = {'query': ip, 'resource_id': '6006'}
        r = requests.get("https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php", params=payload)

        print('百度结果：',r.json().get('data')[0].get('location'))
    except Exception:
        try:
            ip = socket.gethostbyname(URL)
            print('IP查询目标：' + ip)
            payload = {'query': ip, 'resource_id': '6006'}
            r = requests.get("https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php", params=payload)
            print('百度结果：',r.json().get('data')[0].get('location'))
        except Exception:
            print('获取IP地址错误：'+URL)

    # IPIP查询模块
    print('IPIP结果：')
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url = 'https://www.ipip.net/ip.html'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36'}
    data = {'ip': URL}
    re = requests.post(url,headers=headers,data=data,verify=False,timeout=5)
    soup=BeautifulSoup(re.content,"lxml")

    def information_one(table):
        length = len(table.find_all('td'))
        data2 = table.find_all('td')[2].get_text().strip()
        information2 = table.find_all('span')[3].get_text().strip()
        print(data2, ':', information2)
        m = 5
        x = 4
        while x < length:
            data = table.find_all('td')[x].get_text().strip()
            information = table.find_all('span')[m].get_text().strip()
            print(data, ':', information)
            x = x + 2
            m = m + 1

    def information_two(table):
        data = table.find_all('td')[0].get_text().strip()
        information = table.find_all('span')[1].get_text().strip()
        if '威胁情报' in data:
            print(data, ':', information)
        else:
            pass

    def information_three(table):
        data1 = table.find_all('th')[0].get_text().strip()
        information1 = table.find_all('td')[0].get_text().strip()
        data2 = table.find_all('th')[1].get_text().strip()
        information2 = table.find_all('td')[1].get_text().strip()
        data3 = table.find_all('th')[2].get_text().strip()
        information3 = table.find_all('td')[2].get_text().strip()
        if '纯真IP库数据' in data2:
            print(data1, ':', information1)
            print(data2, ':', information2)
            print(data3, ':', information3)
        else:
            pass
    for x in range(0, 7):
        try:
            table = soup.find_all('div')[6].find_all('table')[x]
        except Exception:
            pass
        try:
            information_one(table)
        except Exception:
            pass
        try:
            information_two(table)
        except Exception:
            pass
        try:
            information_three(table)
        except Exception:
            pass


if __name__ == "__main__":
    attack()
