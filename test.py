import mysql.connector

# conn = mysql.connector.connect(host='localhost',user='root',passwd='zxk123456',db='recommender_db')
# cursor = conn.cursor()

def Predict():
    #连接数据库
    conn = mysql.connector.connect(host='localhost', user='vill', passwd='hao5jx', db='recommenderSystem_MVLENS')
    cursor = conn.cursor()

    for i in range(1, 943):
        #获取uerId对应的电影ID
        sql = 'select movieId from ratings where userId=%d' % i
        cursor.execute(sql)
        movies = cursor.fetchall()
        print(movies)

        #获取相似度大于0用户
        sql = 'select * from similarity where (user1=%d or user2=%d) and similarity>0 order by similarity desc' % (i,i)
        cursor.execute(sql)
        sim = cursor.fetchall()
        similar = []

        #获取评分平均值
        sql = 'select avg(rate) from ratings where userId=%d' % i
        cursor.execute(sql)
        avg = cursor.fetchall()
        avg = avg[0]
        for j in sim:
            if int(j[1]) == i:
                similar.append((j[2],j[3]))
            elif int(j[2]) == i:
                similar.append(j[1],j[3])
        print(similar)
        for movie in movies:

            down = 0
            up = 0
            for similarity in similar:
                sql = 'select rate from ratings where userId=%d and movieId=%d'% (int(similarity[0]),int(movie[0]))
                cursor.execute(sql)
                rate = cursor.fetchall()
                if rate is not None:
                    print('%s :%s: %s' % (similarity[0],similarity[1],rate[0]))

                    sql = 'select avg(rate) from ratings where userId=%d' % int(similarity[0])
                    cursor.execute(sql)
                    avg1 = cursor.fetchall()
                    avg1 = avg1[0]
                    up += similarity[1]*float(rate[0]-avg1)
                    down += float(similarity[1])

            if down != 0:
                predict = float(avg)+up/down
                print(predict)
                # sql = 'update ratings set prodiction=%f where userId=%d and movieId=%d'% (predict,i,movie[0])
                # cursor.execute(sql)
                # conn.commit()
        break




if __name__ == '__main__':
    Predict()
