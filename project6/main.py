import re
import shutil
import requests
import setting as se
import XIMALAY as xi
from lxml import html
import os

if os.path.exists('mirbase'):
    shutil.rmtree('mirbase')

albumId = input('请输入要下载的专辑url的编号(如夜的命名术————"https://www.ximalaya.com/album/55045267"中的55045267):')

max_page = se.make(albumId)

xi.download(max_page)


print('已完成')
