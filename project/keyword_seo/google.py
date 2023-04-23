import requests
from xml.etree import ElementTree


def suggestions(keyword):
    url = f'http://suggestqueries.google.com/complete/search?output=toolbar&q={keyword}'
    response = requests.get(url)
    tree = ElementTree.fromstring(response.content)
    suggestions = [suggestion.attrib['data'] for suggestion in tree.findall('*/suggestion')]
    return suggestions

import sqlite3

# SQLite 데이터베이스 연결
conn = sqlite3.connect('database.db')
c = conn.cursor()

# keywords 테이블 생성 (처음에만 실행)
c.execute('''CREATE TABLE IF NOT EXISTS keywords 
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              keyword TEXT)''')
# progress.txt 파일 생성 및 열기
with open('progress.txt', 'w') as f:
    for i in tqdm(range(len(keyword_df))):
        keyword = keyword_df.loc[i, 'keyword']
        keyword_list = [keyword] + suggestions(keyword)
        
        # keyword_list를 SQLite에 추가
        for keyword in keyword_list:
            c.execute("INSERT INTO keywords (keyword) VALUES (?)", (keyword,))
        
        # 진행 상황을 progress.txt 파일에 기록
        f.write(f"{i+1}번째 진행 완료\n")
        conn.commit()
# SQLite 데이터베이스에 변경 사항 저장 및 연결 종료
conn.close()
