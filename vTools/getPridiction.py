import mysql.connector

conn1 = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommenderSystem_1per_Training")
cursor1 = conn1.cursor()
conn2 = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommenderSystem_1per_TestSet")
cursor2 = conn2.cursor()
conn3 = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommenderSystem_1per_Training")
cursor3 = conn3.cursor()
conn4 = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommenderSystem_1per_TestSet")
cursor4 = conn4.cursor()


def vFilter(result_similarity):
    list1 = []
    list2 = []
    while len(result_similarity) != 0:
        a = result_similarity.pop()
        if a[4] > 10:
            list1.append(a)
        else:
            list2.append(a)
    return list2 + list1


with open("/Users/vill/Desktop/推荐系统导论/netflix数据集/1perMovie.txt") as f:
    movieName = f.readline()[:-1]
    while movieName is not "":
        sql = "select * from similarity where movie1='%s' or movie2='%s' order by similarity desc, count desc" % (movieName,movieName)
        cursor1.execute(sql)
        result_similarity = cursor1.fetchall()
        result_similarity = vFilter(result_similarity)
        # for i in range(1, 176):
        #     print(result_similarity[i])
        sql = "select consumerId from %s" % movieName
        cursor2.execute(sql)
        consumerId = cursor2.fetchone()
        while consumerId is not None:
            consumerId = consumerId[0]
            count = 0
            up = 0
            down = 0
            rs = result_similarity[:]
            while count != 4 and len(rs) != 0:
                r = rs.pop()
                sql = "select * from %s where consumerId='%s'" % (r[2], consumerId)
                print(sql)
                # try:
                cursor3.execute(sql)
                result = cursor3.fetchone()
                if result is not None:
                    rate = float(result[2])
                    up += float(rate * r[4])
                    down += float(r[4])
                    count += 1
                    print("%f,%f" % (up, down))
                # except:
                    # continue
            prediction = 0
            try:
                prediction = float(up/down)
            except:
                prediction = -1.0
            sql = "insert into pre_%s(consumerId,rate) values('%s','%f')" % (movieName, consumerId, prediction)
            # print(sql)
            cursor4.execute(sql)
            conn4.commit()
            # print(movie2)
            consumerId = cursor2.fetchone()
            print(len(result_similarity))
        # movieName = f.readline()[:-1]
        movieName = f.readline()[:-1]

        # sql = "select consumerId from %s" % movieName
        # cursor2.execute(sql)
        # consumerId = cursor2.fetchone()[0]
        # while consumerId is not None:
        #     sql = "select * from si"

