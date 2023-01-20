# !/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import pandas as pd
from urllib import parse
import requests
import time


def YQsearch(pages, query):
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/109.0.0.0 Safari/537.36 ",
        'cookie': 'xxxxxxxxxx'
    }
    URL = f'https://www.yuque.com/api/zsearch?p={pages}&q={parse.quote(query)}&scope=%2F&sence=searchPage&tab=public&type=content'
    response = requests.get(url=URL, headers=headers)
    print('[+]当前检索关键词:', query, '[+]当前正在检索第:', pages, '页')
    return response.json()


# 以时间为文件名避免文件名重复^^
def time_filename():
    t = time.localtime()
    # 年月日
    year = t.tm_year
    mon = t.tm_mon
    day = t.tm_mday
    # 时分秒
    hour = t.tm_hour
    min = t.tm_min
    sec = t.tm_sec
    times = str(year) + '_' + str(mon) + '_' + str(day) + '_' + str(hour) + '_' + str(min) + '_' + str(sec)
    return times


def clears(data):
    title_list = []
    url_list = []
    book_name_list = []
    group_name_list = []
    id_list = []
    abstract_list = []
    for i in range(len(data['data']['hits'])):
        # time.sleep(1)
        response_yuque_data = data['data']['hits'][i]
        book_name = response_yuque_data['book_name']
        group_name = response_yuque_data['group_name']
        id = response_yuque_data['id']
        title = response_yuque_data['title'].replace('<em>', '').replace('</em>', '')
        url = 'https://www.yuque.com' + response_yuque_data['url']
        abstract = response_yuque_data['abstract'].replace('<em>', '').replace('</em>', '')
        title_list.append(title)
        url_list.append(url)
        abstract_list.append(abstract)
        book_name_list.append(book_name)
        group_name_list.append(group_name)
        id_list.append(id)
        print('---------------------{0}----------------------'.format(i + 1))
        print('[+]Title:', title)
        print('[+]Link:', url)
        print('[+]abstract:\n', abstract)
        print('[+]知识库名称:', book_name)
        print('[+]知识库归属:', group_name)
        print('[+]id:', id)
        print('---------------------分割线----------------------\n')
        # 字典中的key值即为csv中列名
    return title_list, url_list, abstract_list, book_name_list, group_name_list, id_list


def run(query, pages):
    title_list = []
    url_list = []
    book_name_list = []
    group_name_list = []
    id_list = []
    abstract_list = []
    # 验证搜索是否为空
    data = YQsearch(query=query, pages=1)
    if len(data['data']['hits']) == 0:
        print('[-]当前关键词检索失败请替换其他关键词搜素尝试！')
        pass
    else:
        # 搜索页数这里用了循环，这里循环次数就是搜索的页数
        for i in range(pages):
            data = YQsearch(query=query, pages=i + 1)
            time.sleep(3)
            data = clears(data=data)
            # 写入列表
            title_list += data[0]
            url_list += (data[1])
            abstract_list += (data[2])
            book_name_list += (data[3])
            group_name_list += (data[4])
            id_list += (data[5])
    # 字典中的key值即为csv中列名
    dataframe = pd.DataFrame(
        {'Title': title_list, 'Link': url_list, 'abstract': abstract_list, '知识库名称': book_name_list,
         '知识库归属': group_name_list, 'id': id_list})
    # 将DataFrame存储为csv,index表示是否显示行名，default=True
    # 设置mode='a'使数据连续写入
    # 设置encoding="utf-8"避免出现乱码的情况
    filename = time_filename() + '.csv'
    dataframe.to_csv(filename, encoding="utf-8", mode='a', index=False, sep=',')


if __name__ == '__main__':
    banner = '''

    __   _______ _____                 
    \ \ / /  _  /  ___|                
     \ V /| | | \ `--.  ___ __ _ _ __  
      \ / | | | |`--. \/ __/ _` | '_ \ 
      | | \ \/' /\__/ / (_| (_| | | | |
      \_/  \_/\_\____/ \___\__,_|_| |_|

    by &nOnExiaoyu
    https://github.com/nOnExiaoyu
    YQScan仅用于安全人员测试请勿做非法用途
    tips:默认会将搜索结合保存csv文件输出
    '''
    print(banner)
    try:
        if sys.argv[1] == '-h':
            help = '''
            使用方法: 
            python3 YQScan.py -key 测试 -p 1
            -key:指定关键词
            -p:指定搜索页数（推荐10页）
            '''
            print(help)
        else:
            run(query=sys.argv[2], pages=int(sys.argv[4]))
    except:
        print('-h查看帮助')
