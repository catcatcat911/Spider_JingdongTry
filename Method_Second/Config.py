"""
Config.py
配置文件
"""

settings = {
    #登陆时等待的时间
    'loginWait' : 60 ,
    #一天申请的限制个数
    'maxApplyNum' : 300 ,
    #试用类型
    #家用电器737 手机数码652 电脑办公670 家居家装1620 服饰鞋包1315 生鲜美食12218 钟表奢品5025 家庭清洁15901 食品饮料1320
    'cids' : ['737', '652' ,'670', '1620', '1315', '12218' ,'5025' , '15901' ,'1320' ,] ,
    #申请商品价格下限 单位 元
    'goodPrice' : 30 ,
    #浏览器button最长等待时间 单位秒
    'waitTime' : 10 ,
}
