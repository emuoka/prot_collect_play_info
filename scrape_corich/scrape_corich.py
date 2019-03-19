import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://stage.corich.jp/stage/93493"
responce = requests.get(url)
bs = BeautifulSoup(responce.text, 'html.parser')

#公演名
bs.select("#pcH1 > div.mainTitle > h1 > a")
#団体名
bs.select("#basicData > div.areaRight.box > p.group > a")
#劇場名
bs.select("#basicData > div.areaRight.box > p.theater > a")
#イメージURL
bs.select("#stage_image")

#テーブル解析
table_list = pd.read_html(url)
contents_table = table_list[0]

#期間
contents_table.loc[contents_table[0].str.contains('期間'),1][0]
#出演
contents_table.loc[contents_table[0].str.contains('出演'),1]

#contents_table.loc[contents_table[0].str.contains['期間'],1]