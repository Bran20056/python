import random
import re
import time
import requests
import json
import os  # 操作系统

# \: 转义符
# filepath = 'E:/夜的命名术丨年度都市异能霸榜神作丨紫襟领衔有声剧/'
# filepath = input('请输入存储路径（类似E:/夜的命名术丨年度都市异能霸榜神作丨紫襟领衔有声剧/）：')
# if not os.path.exists(filepath):
#     os.makedirs(filepath)

# 获取数据
mulu_dizhi = f'https://www.ximalaya.com/revision/album/v1/getTracksList?albumId=55045267&pageNum=1&pageSize=30'

# 反爬虫 - 请求头
headers = {
    # 浏览器的身份标识 - 伪装
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
cookie = {
    'cookie':f'_xmLog=h5&c82b78fd-4bd4-48e8-8e14-fbdefa3bdeb7&process.env.sdkVersion; wfp=ACNlMjAzM2UxODEwNTY2NWRlfc8INKZlWt94bXdlYl93d3c; 1&remember_me=y; 1&_token=163135182&62ED8640140N379590DB8B071B64F3E8024E3A5AB19C7E7ADE6BA3D43ED53EBE81E8D12872C67MDE95CA8EFFA4025_; xm-page-viewid=ximalaya-web; impl=www.ximalaya.com.login; x_xmly_traffic=utm_source%253A%2526utm_medium%253A%2526utm_campaign%253A%2526utm_content%253A%2526utm_term%253A%2526utm_from%253A; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1708151133,1708152866,1708153288,1708168350; web_login=1708172015163; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1708172015'
}
# max_page = 10000
# text: 文本数据 / 源代码
# json: json
# resp = requests.get(mulu_dizhi, headers=headers)
# print(resp.text)
# mulu_xinxi = resp.json()
def download(max_page):
    with open('mirbase/mirbase'+str(1)+'.json','r',encoding='utf-8') as f:
        data = json.load(f)
    file = input('请输入存储路径（类似E:/）：')
    filepath = file+data["data"]["tracks"][0]["albumTitle"]+'/'
    safe_filepath = re.sub(r'[\*?"<>|]', ' ', filepath)
    if not os.path.exists(safe_filepath):
        os.makedirs(safe_filepath)
    
    
    
    
    for i in range(max_page):
        # i = 64
        with open('mirbase/mirbase'+str(i+1)+'.json','r',encoding='utf-8') as f:
            data = json.load(f)
        mulu_xinxi = data
        # 2. 拿取全部音频的id 以及标题
        # 字典取值
        mulu_xinxi = mulu_xinxi['data']['tracks']
        # print(mulu_xinxi)
        # for循环: 从列表中 一条条的拿取数据
        for yinpin_xinxi in mulu_xinxi:
            # print(yinpin_xinxi)
            yinpin_title = yinpin_xinxi["title"]
            print(yinpin_title)
            # 替换地址 拿取音频信息
            # f_string ： 字符串 变量传入
            play_dizhi = f'http://mobile.ximalaya.com/mobile/redirect/free/play/{yinpin_xinxi["trackId"]}/1'
            # {yinpin_xinxi["trackId"]}
            yinpin = requests.get(play_dizhi, headers=headers,cookies=cookie)
            # print(yinpin.content)
            # yinpin_dizhi = yinpin_data['data']['src']  # 1    2
            # print(yinpin_dizhi)

            # 打开文件 / 读写形式
            # 二进制 ： 图片 音频 视频 : content
            yinpin_title = yinpin_title.replace(':', '_')
            with open(safe_filepath+yinpin_title+'.m4a','wb') as f:
                f.write(yinpin.content)
            # random_number = random.randint(1, 10)
            time.sleep(random.randint(1, 10))
            # yinpin = open(filename + yinpin_title + '.m4a', mode='wb')
            # # 写入数据
            # yinpin.write(requests.get(yinpin_dizhi, headers=headers).content)
            # # 关闭文件
            # yinpin.close()