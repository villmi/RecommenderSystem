import mysql.connector
import threading


def getNum(m, n):
    j = n
    if int(m / 10) != 0:
        j += 1
        j = getNum(int(m/10), j)
    return j


def run(m, n, name):
    conn = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommenderSystem")
    cursor = conn.cursor()
    # file_path = input("Please input file_path:\n")
    file_path = "E:/recommenderSystem/training_set"
    for i in range(m, n):
        i = int(i)
        num = int(getNum(i, 1))
        zero = 7 - num
        zeros = ""
        while zero != 0:
            zeros = "0%s" % zeros
            zero -= 1
        fileName = "mv_%s%d" % (zeros, i)
        with open("%s/%s.txt" % (file_path, fileName)) as f:
            f.readline()
            second = f.readline()
            while ',' in second:
                second = second.split(",")
                # num = int(getNum(int(second[0]), 1))
                # zero = 7 - num
                # zeros = ""
                # while zero != 0:
                # zeros = "0%s" % zeros
                # zero -= 1
                # fileName = "usr_%s%s" % (zeros, second[0])
                # with open("C:/Users/Administrator/Desktop/netflix数据集/netflix数据集/user_set/%s.txt" % fileName, "a+") as ff:
                # if ff.readline() is not "usr%d:" % second[0]:
                # ff.write("%d,%d,%d\n" % (i, second[1], second[2]))
                # print(second)
                sql = "insert into training_set(`movieId`,`consumerId`,`rate`,`date`) values('%s','%s','%s','%s')" % (
                fileName, second[0], second[1], second[2])
                cursor.execute(sql)
                second = f.readline()
            conn.commit()
            print("%s:table %s completed" % (name, fileName))


if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=(1, 7501, "thread1"))
    t3 = threading.Thread(target=run, args=(7501, 12000, "thread3"))
    t2 = threading.Thread(target=run, args=(12001, 15000, "thread2"))
    t4 = threading.Thread(target=run, args=(15001, 17771, "thread4"))
    # t1.start()
    t2.start()
    t3.start()
    t4.start()