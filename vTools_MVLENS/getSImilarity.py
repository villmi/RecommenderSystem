import mysql.connector
import time


def getAvg(rate):
    sum = 0
    for i in rate:
        sum += int(i[1])
    return float(sum / len(rate))


def getSimilarity(r1, r2):
    if len(r1) != 0:
        if r1 == r2:
            return 1, len(r1)  # 两个用户评分完全相同，定义为相似度为1
        else:
            avg1 = getAvg(r1)
            avg2 = getAvg(r2)
            up = 0.0
            down1 = 0.0
            down2 = 0.0
            for x in range(len(r1)):
                up += (float(r1[x][1]) - avg1) * (float(r2[x][1]) - avg2)
                down1 += (float(r1[x][1]) - avg1) ** 2
                down2 += (float(r2[x][1]) - avg2) ** 2
            if (down1 == 0 or down2 == 0) and len(r1) == 1:
                return -2, len(r1)  # 2表示两个用户仅对一部电影打过分
            elif (down1 == 0 or down2 == 0) and len(r1) != 0:
                return -3, len(r1)  # 3表示有一个用户每次打分可能都一样
            else:
                return up / ((down1 * down2) ** 0.5), len(r1)
    else:
        return -4, 0  # 两个用户没有对同一部电影打过分


def runSimilarity(fCount):
    conn = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommenderSystem_MVLENS")
    cursor = conn.cursor()
    fCount += 1
    for i in range(1, fCount):
        sql = "select movieId, rate from u1_base where userId=%d" % i     # 获取用户i已经进行的评分，可以得到一组格式为（电影id，评分的集合）
        cursor.execute(sql)
        user1 = cursor.fetchall()
        for j in range(i + 1, fCount):
            sql = "select movieId, rate from u1_base where userId=%d" % j
            cursor.execute(sql)
            user2 = cursor.fetchall()
            n = 0
            m = 0
            rate1 = []
            rate2 = []
            while (m <= len(user1) - 1) and (n <= len(user2) - 1):  # 筛选出两个用户共同进行过评分的电影id以及评分
                if user1[m][0] == user2[n][0]:
                    rate1.append(user1[m])
                    rate2.append(user2[n])
                    m += 1
                    n += 1
                elif user1[m][0] < user2[n][0]:
                    m += 1
                else:
                    n += 1
            similarity, count = getSimilarity(rate1, rate2)
            # sql = "insert into similarity(userId1, userId2, similarity, count) values(%d,%d,%f,%d)" % (i, j, similarity, count)  # 将两两用户之间的相似度导入数据库
            cursor.execute(sql)
            print("similarity between user%d and user%d is: %f " % (i, j, similarity))
        conn.commit()


def getPredict():
    conn = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommenderSystem_MVLENS")
    cursor = conn.cursor()
    for i in range(10, 11):
        sql = "select movieID from u1_test where userId=%d" % i  # 选出测试集中，id为i的用户，以及需要进行预测的电影id
        cursor.execute(sql)
        movies = cursor.fetchall()
        print(movies)
        sql = "select * from similarity where (userId1=%d or userId2=%d) and count >= 10 and similarity>0 order by similarity desc" % (i, i)
        "这边导出与用户i与其他用户的相似度，筛选条件是：他们都进行评分的电影超过10部，且相似度大于0，并以相似度进行降序排列"
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
                "筛选出观看过正在进行预测电影的用户的评分"
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
                if count == 5:  # "用于限制：如果相似用户过多，只取相似度最相近的5名用户的评分"
                    break
            print(down)
            # if down != 0:
            #     predict = float(avg) + up / down
            #     print(predict)
            #     sql = "update u1_test set prodiction=%f where userId=%d and movieId=%d" % (predict, i, movie[0])
            #     cursor.execute(sql)
            #     conn.commit()


if __name__ == '__main__':
    # sTime = time.time()
    # runSimilarity(943)
    # fTime = time.time()
    # print("timeCost is :%f" % float(sTime-fTime))
    # sTime = time.time()
    # getPredict()
    # fTime = time.time()
    # print("timeCost is :%f" % float(sTime-fTime))
    # getPredict()
    t = time.time()
    runSimilarity(943)
    print(time.time() - t)
    "一个看数据时的考虑：" \
    "就结果而言，如果一个用户测试集中的实际评分与预测评分差距较大，比如实际5分，预测2分，这个用户的这个高分是否被电影整体评分以及评分时间段影响" \
    "比如可以考虑用户被影响的概率？？？（只是猜想，可忽略不计）"
