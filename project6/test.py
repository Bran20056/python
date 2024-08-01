import requests
from bs4 import BeautifulSoup

# 目标网站的URL
url = 'https://www.51earth.com'

# 发送GET请求
response = requests.get(url)

# 确保请求成功
if response.status_code == 200:
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取并打印页面的主体文本，或进行其他处理
    # 这里只是一个简单的示例，实际上你可能需要根据页面结构进行更复杂的处理
    text = soup.get_text()
    print(text)

    # 将抓取到的文本保存到文件中
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(text)
else:
    print(f"Failed to retrieve content, status code: {response.status_code}")

