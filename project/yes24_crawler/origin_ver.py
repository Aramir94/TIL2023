# YES24 들어가서 각 카테고리별 URL 확인 하는 작업 

import requests
from bs4 import BeautifulSoup

# 가져올 페이지의 URL
url = "http://www.yes24.com/24/Category/BestSeller"

# requests를 사용하여 HTML 가져오기
response = requests.get(url)
html = response.content

# BeautifulSoup를 사용하여 파싱하기
soup = BeautifulSoup(html, 'html.parser')

cate_list = soup.select('#category001 > ul > li')
cate_name_list = [i.text.strip() for i in cate_list]

url_list = ["http://www.yes24.com" + i.find('a').get('href') for i in cate_list ]

# 카테고리별로 들어가기 데이터 가져오기

import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome(ChromeDriverManager().install())

result_df = pd.DataFrame()

for i in range(len(cate_list)):
    
    # 카테고리 별로 url 나눠서 크롤링 
    cate_url = url_list[i]
    cate_name = cate_name_list[i]
    
    # top100 가져 와야 하니깐 page 넘버는 5까지
    driver.get(cate_url+'&FetchSize=80')
    time.sleep(0.2)
    title_list = driver.find_elements(By.XPATH,
    '//*[@id="category_layout"]/tbody/tr/td[3]/p[1]/a[1]')    
    page_url_list = [i.get_attribute('href') for i in title_list] # page_url_list 부터
    title_list = [i.text for i in title_list]

    author_list = driver.find_elements(By.XPATH,
    '//*[@id="category_layout"]/tbody/tr/td[3]/div/a[1]')
    author_list = [i.text for i in author_list]

    price_list = driver.find_elements(By.XPATH,
    '//*[@id="category_layout"]/tbody/tr/td[3]/p[2]')
    price_list = [i.text for i in price_list]

    carwler_df = pd.DataFrame()
    carwler_df['title'] = page_url_list
    carwler_df['title'] = title_list
    carwler_df['author_list'] = author_list
    carwler_df['price_list'] = price_list
    carwler_df['category'] = cate_name
    carwler_df['url'] = cate_url
        
      
    # 데이터 프레임화
    result_df = pd.concat([carwler_df, result_df])      
    print(f'======{cate_name} 크롤링 작업 완료======')
print('===== 데이터를 다 다운 받았어 =====')

result_df = result_df.rename_axis('rank').reset_index()
result_df['rank'] = result_df['rank'] + 1
result_df
