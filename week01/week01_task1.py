# 使用BeautifulSoup解析网页
# bs4是第三方库需要使用pip命令安装

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'


cookie = '__mta=250908985.1595604024524.1596005478333.1596005516705.15; uuid_n_v=v1; uuid=3AF63E60CDC111EAAACFDFD33042EC971557D6A60401471B9B8D5626B03F758F; _csrf=25f6b2324d9f9ccc9e0092c5b098ba29bcf11b092a3de5d19604c89b942f3b6e; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595604020; _lxsdk_cuid=17381692b35c8-0e2b6056395c9f-b7a1334-100200-17381692b35c8; _lxsdk=3AF63E60CDC111EAAACFDFD33042EC971557D6A60401471B9B8D5626B03F758F; mojo-uuid=65514a681aa839c0037c7cc9a26093cc; __mta=250908985.1595604024524.1595837250071.1596000688959.10; mojo-session-id={"id":"852fc66b145ea33a5df16bce500bfa9d","time":1596005377313}; mojo-trace-id=9; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1596005517; _lxsdk_s=173994acaba-0ee-8ab-4e9%7C%7C14'


header = {'user-agent': user_agent, 'Cookie': cookie}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl, headers=header)

bs_info = bs(response.text, 'html.parser')

movie_list = []
for tag in bs_info.find_all('div', attrs={'class': 'movie-hover-info'})[:10]:
    if tag.find_all('span',attrs={'class':'name noscore'}):
        movie_name = tag.text.split()[0]
        movie_type = tag.text.split()[2]
        movie_date = tag.text.split()[6]
        movie_list.append({
                    "name": movie_name,
                    "type": movie_type,
                    "time": movie_date,
                })
    else:
        movie_name = tag.text.split()[0]
        movie_type = tag.text.split()[3]
        movie_date = tag.text.split()[7]
        movie_list.append({
                    "name": movie_name,
                    "type": movie_type,
                    "time": movie_date,
                })



movie = pd.DataFrame(data = movie_list)
movie.to_csv('C:/Users/Administrator/Desktop/movie.csv', encoding='gbk', index=False, header=False)




