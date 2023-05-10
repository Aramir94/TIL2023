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

from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import pandas as pd

# Initialize the driver
driver = webdriver.Chrome()

def fetch_data(cate_url, cate_name):
    # Navigate to url
    driver.get(cate_url+'&FetchSize=80')
    sleep(0.2)

    # Fetch data
    title_elements = driver.find_elements(By.XPATH, '//*[@id="category_layout"]/tbody/tr/td[3]/p[1]/a[1]')
    author_elements = driver.find_elements(By.XPATH, '//*[@id="category_layout"]/tbody/tr/td[3]/div/a[1]')
    price_elements = driver.find_elements(By.XPATH, '//*[@id="category_layout"]/tbody/tr/td[3]/p[2]')

    # Prepare data for DataFrame
    data = {
        'title': [elem.text for elem in title_elements],
        'url': [elem.get_attribute('href') for elem in title_elements],
        'author_list': [elem.text for elem in author_elements],
        'price_list': [elem.text for elem in price_elements],
        'category': [cate_name] * len(title_elements),
        'cate_url': [cate_url] * len(title_elements)
    }

    # Create DataFrame
    df = pd.DataFrame(data)
    return df

# Initialize an empty DataFrame
result_df = pd.DataFrame()

for url, name in zip(url_list, cate_name_list):
    df = fetch_data(url, name)
    result_df = pd.concat([result_df, df])
    print(f'======{name} 크롤링 작업 완료======')

print('=====  데이터를 다 다운 받았어 =====')

# Close the driver
driver.close()

