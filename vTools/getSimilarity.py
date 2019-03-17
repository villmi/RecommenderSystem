import mysql.connector
import math
import time

conn1 = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommenderSystem_1per_Training")
conn2 = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommenderSystem_1per_Training")
# conn = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx")
cursor1 = conn1.cursor()
cursor2 = conn2.cursor()


index1 = 1
with open("/Users/vill/Desktop/推荐系统导论/netflix数据集/1perMovie.txt", "r") as f:
        movieName = f.readline()
        movieName = movieName[:-1]
        index2 = index1   # 后面这个数字可以控制比较的表，例如，+1 为第二张表
        while movieName is not "":
            print("-----%s is calculating" % movieName)
            with open("/Users/vill/Desktop/推荐系统导论/netflix数据集/1perMovie.txt", "r") as ff:
                index2 += 1
                count = 0
                for i in range(1, index2):
                    a = ff.readline()[:-1]
                    # print("skip:%s" % a)
                movie2Name = ff.readline()[:-1]
                print("---calculating %s and %s....." % (movieName, movie2Name))
                timeBegin = time.time()
                while movie2Name is not "":
                    if movie2Name != movieName:
                        # print(movieName)
                        # print(movie2Name)
                        sql = "select `%s`.rate,`%s`.rate from `%s`,`%s` where `%s`.consumerId=`%s`.consumerId" % (movieName, movie2Name, movieName, movie2Name, movieName, movie2Name)
                        # print(sql)
                        cursor1.execute(sql)
                        result = cursor1.fetchone()
                        # print(result)
                        list1 = []
                        list2 = []
                        sum1 = 0
                        sum2 = 0
                        up = 0.0
                        down1 = 0.0
                        down2 = 0.0
                        while result is not None:
                            list1.append(int(result[0]))
                            list2.append(int(result[1]))
                            # print(list1)
                            # print(list2)
                            sum1 += int(result[0])
                            sum2 += int(result[1])
                            count += 1
                            result = cursor1.fetchone()
                            print("counting...%d" % count)
                            # print(result)
                        sql = "insert into similarity(movie1,movie2,count) values('%s','%s',%d)" % (movieName, movie2Name, count)
                        cursor2.execute(sql)
                        conn2.commit()
                        try:
                            avg1 = float(sum1 / count)
                            avg2 = float(sum2 / count)
                            while len(list1) and len(list2) is not 0:
                                a = list1.pop()
                                b = list2.pop()
                                # if movieName == "item2" and movie2Name == "item5":
                                #      print(a)
                                #      print(b)
                                #      print(avg1)
                                #      print(avg2)
                                #      print("******************")
                                up += float(a - avg1) * float(b - avg2)
                                down1 += float(a - avg1) ** 2
                                down2 += float(b - avg2) ** 2
                                # print(a)
                                # print(b)
                                print("poping..%d" % count)
                                count -= 1
                        except:
                            similarity = -2.0
                            down1 = 0
                            down2 = 0
                    count = 0
                    try:
                        similarity = float(up / math.sqrt(float(down1 * down2)))
                    except:
                        similarity = -3.0
                    sql = "update similarity set similarity='%s' where movie1='%s' and movie2= '%s'" % (similarity, movieName, movie2Name)
                    cursor2.execute(sql)
                    conn2.commit()
                    print("---%s and %s is over!time costs: %s" % (movieName, movie2Name, str(time.time() - timeBegin)))
                    movie2Name = ff.readline()[:-1]
                    # movie2Name = None
            print("-----%s is over" % movieName)
            print()
            movieName = f.readline()[:-1]
