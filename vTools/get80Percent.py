import mysql.connector

# conn = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommederSystem_Training")
conn = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx")
cursor = conn.cursor()

with open("/Users/vill/Desktop/推荐系统导论/hottestMovie.txt", "r") as f:
    line = f.readline()
    line = line[:-1]
    print(line)
    while line != "":
        sql = "select count(*) from `recommenderSystem`.hottest_%s_view" % line
        cursor.execute(sql)
        s = cursor.fetchone()
        s = int(int(s[0]) * 0.8)
        print(s)
        # sql = "create view hottest_80_%s_view as (select * from hottest_%s_view limit %d) order by consumerId ASC" % (line, line, s)

        sql = "create table `recommenderSystem_Training`.`%s` as select * from `recommenderSystem`.`%s` order by date ASC limit %d" % (line, line, s)
        cursor.execute(sql)
        conn.commit()
        # a = cursor.fetchone()
        # while a is not None:
        # with open("/Users/vill/Desktop/推荐系统导论/netflix数据集/hottest_movie_80%%/hottest_%s_80per.txt" % line, "a+") as ff:
        # ff.write("%s,%s,%s" % (a[1], a[2], a[3]))
        # a = cursor.fetchone()
        line = f.readline()
        line = line[:-1]
        print("%s 80%% is over" % line)
