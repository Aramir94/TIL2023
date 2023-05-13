import pandas as pd
import requests
from tqdm import tqdm
import time
def bestseller() -> pd.DataFrame:
    """
    교보문고에서 국내 전체 베스트 셀러를 가져 와서 데이터 프레임으로 만들어 줍니다.
    """
    headers = {
        'authority': 'product.kyobobook.co.kr',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ko;q=0.8',
        'cache-control': 'no-cache',
        # 'cookie': '_gcl_aw=GCL.1683985928.CjwKCAjw6vyiBhB_EiwAQJRopvN-zKNdL-Mm_RVD_d_UO1F6JGQUN9BTPSM22lG7GIgIseDdfaCtzhoCB6AQAvD_BwE; _gcl_au=1.1.1694849213.1683985928; RB_PCID=1683985928447337770; _ga=GA1.1.636283117.1683985929; EG_GUID=fe0f85cb-a39a-454e-a0af-288e4959283f; _clck=1wpocrc|2|fbk|0|1228; _fbp=fb.2.1683985929270.1793143721; b5dcbb5e99191a099429032ae16cffe3=f9c3c09f212ff7a8eb01983815465145; order.shipping.addr=03154K//%EC%84%9C%EC%9A%B8%EC%8B%9C%20%EC%A2%85%EB%A1%9C%EA%B5%AC%20%EC%A2%85%EB%A1%9C%201; promo-banner=true; rc-cont=[%22p|KOR|S000200746091%22%2C%22p|KOR|S000201142283%22%2C%22p|KOR|S000001803157%22]; wcs_bt=s_453f4415ebcb:1683988037; RB_SSID=YmxSyi8xYc; _ga_CQHKV7VZV7=GS1.1.1683985928.1.1.1683988041.56.0.0; _clsk=bhyc80|1683988336981|25|1|r.clarity.ms/collect; JSESSIONID=BAA5CF03E08777129D54D906317F79D6',
        'dnt': '1',
        'pragma': 'no-cache',
        'referer': 'https://product.kyobobook.co.kr/bestseller/online?period=002',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    params = {
        'page': '1',
        'per': '110', # 갯수 변경하면 더 가지고 올수 있음
        'period': '002', # 주간 001 일간 002 주간 003 월간
        'dsplDvsnCode': '001',
        'dsplTrgtDvsnCode': '002',
        'saleCmdtDsplDvsnCode': 'TOT',
    }

    response = requests.get(
        'https://product.kyobobook.co.kr/api/gw/pub/pdt/best-seller/online',
        params=params,
        headers=headers,
    )

    data = pd.DataFrame(response.json()['data']['bestSeller'])
    data = data[data['saleCmdtDvsnCode']== 'KOR'] # 광고 상품들 PBC로 들어가있는거 제거 
    data = data.iloc[:100].reset_index(drop=True)
    data = data[['cmdtName', 'chrcName', 'price', 'inbukCntt', 'buyRevwNumc', 'saleCmdtid']]
    # rank 만들기 
    data = data.reset_index()
    data['rank'] = data['index'] + 1 
    
    return data


def review_crawler(product_code: str) ->list: 
    """
    product_code를 이용해서 리뷰를 가져옵니다.
    """
    headers = {
        'authority': 'product.kyobobook.co.kr',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ko;q=0.8',
        'cache-control': 'no-cache',
        'dnt': '1',
        'pragma': 'no-cache',
        'referer': 'https://product.kyobobook.co.kr/detail/S000201142283',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    params = {
        'page': '1',
        'pageLimit': '100', # 갯수 변경하면 더 가지고 올수 있음
        'reviewSort': '002',
        'revwPatrCode': '000',
        'saleCmdtid': product_code,
    }

    response = requests.get('https://product.kyobobook.co.kr/api/review/list', params=params, headers=headers)
    try:
        review_list = pd.DataFrame(response.json()['data']['reviewList'])['revwCntt']
        review_list = review_list.str.replace('\n', ' ').str.strip().to_list() # \n 제거 , 양 옆 공백 제거 
    except:
        review_list = [''] # 리뷰가 없는 경우
    return review_list 


# if __name__ == '__main__': 

data = bestseller() # 베스트 셀러 가져오기

# 각 상품 별로 review 가져 오기 
review_lists = [] 
for product_code in tqdm(data['saleCmdtid']):
    review_list = review_crawler(product_code)
    time.sleep(1)
    review_lists.append(review_list)
data['review'] = review_lists

data.drop(['index', 'saleCmdtid'], 1) # column 후처리 
data = data[['rank', 'cmdtName', 'chrcName', 'price', 'inbukCntt', 'buyRevwNumc', 'review']] # column 순서 변경
data.columns = ['순위', '제목', '저자', '가격', '책소개', '리뷰수', '리뷰내용']
data.insert(0, '사이트', '교보문고') # 사이트 column 추가
data.to_excel('교보문구.xlsx', index=False) # 엑셀로 저장
