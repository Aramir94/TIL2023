# Python3 샘플 코드 #
api = ''

import requests

url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?_wadl&type=xml'
params ={'serviceKey' : apikey, 'LAWD_CD' : '11110', 'DEAL_YMD' : '201512' }

response = requests.get(url, params=params)
print(response.content.decode('utf-8'))
