import requests
import time
import re
import json

def get_one_page(url):

    try:
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6821.400 QQBrowser/10.3.3040.400'}
        repondes=requests.get(url,headers=headers)
        if repondes.status_code==200:
            return repondes.text
        else:
            return None
    except ResourceWarning:
        return None

def parse_one_page(html):
    patten=re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items=re.findall(patten,html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip(),
            'time':item[4].strip(),
            'score':item[5]+item[6]
        }
def write_to_page(connet):
    with open('novie.txt','a',encoding='utf-8')as p:
        p.write(json.dumps(connet,ensure_ascii=False)+'\n')

def main(offset):

    url='http://maoyan.com/board/4?offset='+str(offset)
    html=get_one_page(url)
    connet=parse_one_page(html)
    for item in connet:
        print(item)
        write_to_page(item)

if __name__=='__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)
