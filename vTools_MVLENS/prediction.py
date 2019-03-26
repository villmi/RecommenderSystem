import mysql.connector


conn = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommenderSystem_MVLENS")
cursor = conn.cursor()


if __name__ == '__main__':
    for i in range(1, 943):
        sql = "select movieID from u1_test where userId=%d" % i
        cursor.execute(sql)
        movies = cursor.fetchall()
        print(movies)
        sql = "select * from similarity where (userId1=%d or userId2=%d) and count >= 10 and similarity>0 order by similarity desc" % (i, i)
        cursor.execute(sql)
        ss = cursor.fetchall()
        similarities = []
        sql = "select avg(rate) from u1_base where userId=%d" % i
        cursor.execute(sql)
        avg = cursor.fetchone()
        avg = avg[0]
        for s in ss:
            if int(s[1]) == i:
                similarities.append((s[2], s[3]))
            elif int(s[2]) == i:
                similarities.append((s[1], s[3]))
        print(similarities)
        for movie in movies:
            count = 0
            down = 0
            up = 0
            for similarity in similarities:
                sql = "select rate from u1_base where userId=%d and movieId=%d" % (int(similarity[0]), int(movie[0]))
                cursor.execute(sql)
                rate = cursor.fetchone()
                if rate is not None:
                    print("%s :%s: %s " % (similarity[0], similarity[1], rate[0]))
                    count += 1
                    sql = "select avg(rate) from u1_base where userId=%d" % int(similarity[0])
                    cursor.execute(sql)
                    avg1 = cursor.fetchone()
                    avg1 = avg1[0]
                    up += similarity[1]*float(rate[0]-avg1)
                    down += float(similarity[1])
                if count == 10:
                    break
            predict = float(avg) + up / down
            print(predict)


        #     print(len(similarities))
        #     for similarity in similarities:
        #         sql = "select rate from u1_base where userId=%d and movieId=%d" % (int(similarity[0]), int(similarity[1]))
        #         # print(sql)
        #         cursor.execute(sql)
        #         rate = cursor.fetchone()
        #         if rate is not None:
        #             print(rate)








