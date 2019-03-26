import mysql.connector

conn = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommenderSystem_MVLENS")
cursor = conn.cursor()


def getMAE():
    sql = "select count(*) from u1_test"
    cursor.execute(sql)
    count = cursor.fetchone()
    count = int(count[0])
    print(count)
    total = 0
    a = 0
    for i in range(1, count + 1):
        print(i)
        sql = "select rate,prodiction from u1_test where id=%d" % i
        cursor.execute(sql)
        result = cursor.fetchone()
        if result[1] is not None:
            a += 1
            predict = float(result[1])
            rate = float(result[0])
            total += abs(predict - rate)
    MAE = total / a
    print(MAE)
    print(total)
    print(a)


if __name__ == '__main__':
    getMAE()
