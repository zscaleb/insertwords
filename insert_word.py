"""
将单词本存入数据库
1.创建数据库dict utf8
2.创建数据表words 将单词和单词解释分别存入不同的字段
reate table words(id int primary key anto_increment,word char(32），mean text);
3.将单词存入worlds单词表
"""

import pymysql
import re
f = open('dict.txt')
# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')
# 获取游标（操作数据库，执行sql语句
cur = db.cursor()

# data = f.readline()
# tmp = data.split(' ')
# word = tmp[0]
# mean = ' '.join(tmp[1:]).strip()
# print(word)
# print(mean)

sql = "insert into words(word,mean) values(%s,%s)"
for line in f:
    tup = re.findall(r"(\S+)\s+(.*)",line)[0]
    try:
        cur.execute(sql,tup)
        db.commit()
    except:
        db.rollback()

f.close()

# 关闭数据库
cur.close()
db.close()
