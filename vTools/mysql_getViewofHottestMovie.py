import mysql.connector

conn = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommenderSystem")
cursor = conn.cursor()

with open("/Users/vill/Desktop/推荐系统导论/hottestMovie.txt", "r") as f:
    tableName = f.readline()
    i = 1
    while tableName is not "":
        sql = "create view hottest_%s_view as select * from %s order by date ASC" % (tableName[:-1], tableName[:-1])
        cursor.execute(sql)
        conn.commit()
        # print("%d:%s" % (i, tableName))
        print(sql)
        tableName = f.readline()
        i += 1

