import mysql.connector

conn = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommenderSystem_Training")
# conn = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx")
cursor = conn.cursor()

with open("/Users/vill/Desktop/推荐系统导论/hottestMovie.txt") as f:
    name = f.readline()[:-1]
    while name is not "":
        sql = "select avg(rate) from %s" % name
        cursor.execute(sql)
        avg = float(cursor.fetchone()[0])
        sql = "insert into averageRate(movieId, averageRate) values('%s', %f)" % (name, avg)
        cursor.execute(sql)
        conn.commit()
        name = f.readline()[:-1]
