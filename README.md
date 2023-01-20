# YQScan
语言雀敏感信息泄露搜索
        
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
    使用方法: 
            python3 YQScan.py -key 测试 -p 1
            -key:指定关键词
            -p:指定搜索页数（推荐10页）
    环境配置

    安装工具所需的python库
    pip install -r requirements.txt

    代码第14行添加自己的语雀cookie
    'cookie': 'xxxxxxxxxx'

    添加完就可以愉快的使用了。

    python3 YQScan.py -key 关键词 -p 搜索页数

    例：
    python3 YQScan.py -key 员工 -p 1
