# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    'lang' : 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.6',
    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept_encoding' : 'gzip, deflate',
    'cache_control' : 'max-age=0'
}

def folder_name(year,month):
    if (month >= 1 and month <= 3 ):
        return year+"_0103"
    elif (month >= 4 and month <= 6 ):
        return year+"_0406"
    elif (month >= 7 and month <= 9 ):
        return year+"_0709"
    elif (month >= 10 and month <= 12 ):
        return year+"_1012"
    else:
        return year+"other"

def sn_list(text_payload,page_num):
    _json = []
    payload={}
    for pageNumber in range(1,page_num):
        url = 'https://ani.gamer.com.tw/animeList.php?page='+ str(pageNumber)+'&c=0&sort=1'
        r = requests.get(url, headers=headers)
        sp = BeautifulSoup(r.text, 'html.parser')
        meta = sp.find('div',{'class': "theme-list-block"})
        
        # from meta data extract each anime infomation
        for item in meta.find_all('a',{'class':'theme-list-main'}):

            # get anime info
            
            title = item.find('p',{'class':'theme-name'}).text
            date = item.find('p',{'class':'theme-time'}).text.split('年份：')[1]
            year = date.split('/')[0]
            month = int(date.split('/')[1])
            folder = folder_name(year,month)

            # get anime sn
            
            req_page = requests.get("https://ani.gamer.com.tw/"+str(item['href']), headers=headers)
            
            # delay 0.5s.
            time.sleep(0.5)
            
            sn = req_page.url.split("?sn=")[1]
            
            print(title + " : " + sn)
            data = {
                "sn":sn,
                "title":title,
                "folder_name":folder,
            }
            
            if data['folder_name'] not in payload.keys():
                _json = []

            if text_payload != []:
                if title not in text_payload:
                    _json.append(data)
                    payload[folder] = _json
            else:
                _json.append(data)
                payload[folder] = _json

    return payload

def write_list(payload):
    content = ''
    for folder in payload:
        # print(folder)
        content += '@' + folder + "\n"
        for info in payload[folder]:
            # print(info)
            content += "{sn} all #{title}\n".format(sn=info['sn'], title=info['title'])

    with open('sn_list.txt', "a+",encoding='utf8') as f:
        f.write(content)


def read_list():
    text_payload = []
    try:
        with open('sn_list.txt', "r", encoding='utf8') as f:
            text_str = f.read()
            
            matches = re.finditer(r"#(.+)", text_str, re.MULTILINE)

            for matchNum, match in enumerate(matches, start=1):
                text_payload.append(match.group(1))
        return text_payload
    except:
        print("sn_list is empty. Create a new file now.\n")
        return text_payload


# Main function
if __name__ == '__main__':
    print("\nSTART FETCH!\n")
    
    # set the page num for search
    page_num = 3

    # read sn_list
    text_payload = read_list()
    
    # get new sn number
    payload = sn_list(text_payload,page_num)
    
    # write new data to sn_list
    write_list(payload)

    print("done")
        
