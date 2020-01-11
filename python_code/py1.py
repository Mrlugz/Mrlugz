import pymysql
print("================测试是否连通====================")
try:
    conn = pymysql.connect(host='192.168.1.128', user='root', passwd='', db='test', port=3306, charset='utf8')
    cur = conn.cursor()
    cur.execute('select * from runoob_tbl')
    version = cur.fetchone()
    print(version)
    cur.close()
    conn.close()
except  Exception:
    print("发生异常")