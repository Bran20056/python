import json
import os
import requests
i = 1
max_page = 10000
albumId=0
headers = {
    # 浏览器的身份标识 - 伪装
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'

}
cookie = {
    'cookies' : f'_xmLog=h5&c82b78fd-4bd4-48e8-8e14-fbdefa3bdeb7&process.env.sdkVersion; wfp=ACNlMjAzM2UxODEwNTY2NWRlfc8INKZlWt94bXdlYl93d3c; 1&remember_me=y; 1&_token=163135182&62ED8640140N379590DB8B071B64F3E8024E3A5AB19C7E7ADE6BA3D43ED53EBE81E8D12872C67MDE95CA8EFFA4025_; xm-page-viewid=ximalaya-web; impl=www.ximalaya.com.login; x_xmly_traffic=utm_source%253A%2526utm_medium%253A%2526utm_campaign%253A%2526utm_content%253A%2526utm_term%253A%2526utm_from%253A; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1708151133,1708152866,1708153288,1708168350; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1708186221; web_login=1708186439882'
}

filepath = 'mirbase/'


def make(albumId):
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    i = 1
    while True:
        
        id = i
        url = f'https://www.ximalaya.com/revision/album/v1/getTracksList?albumId={albumId}&pageNum={id}&sort=0&pageSize=30'
        # print(url)
        resp = requests.get(url,headers=headers)
        data = resp.text
        
        with open('mirbase/mirbase'+str(i)+'.json','a',encoding='utf-8') as f:
            f.write(data)
        i = i+1
        data_dict = json.loads(data)
        if data_dict["data"]["tracks"] == []:
            break
    # print(i)
    return i-3
            
# make(55045267)