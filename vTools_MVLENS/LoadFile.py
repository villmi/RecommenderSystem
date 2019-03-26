import mysql.connector
import math


with open("/Users/vill/Desktop/推荐系统导论/ml-100k/u1.test", "r") as f:
    conn = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommenderSystem_MVLENS")
    cursor = conn.cursor()
    sql = "create table if not exists u1_test(" \
          "`id` int not null auto_increment," \
          "`userId` int null," \
          "`movieID` INT NULL," \
          "`rate` int null," \
          "`time` float null," \
          "primary key(`id`));"
    cursor.execute(sql)
    conn.commit()
    line = f.readline()[:-1]
    count = 1
    while line is not "":
        line = line.split("\t")
        sql = "insert into u1_test(userId, movieId, rate, time) values(%d, %d, %d, %f)" % (int(line[0]), int(line[1]), int(line[2]), float(line[3]))
        cursor.execute(sql)
        conn.commit()
        line = f.readline()[:-1]
        print("line %d" % count)
        count += 1

"代码以u1.data为例，其他改改名字就好了"
