import threading
import mysql.connector


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
    file_path = "/Users/vill/Desktop/推荐系统导论/netflix数据集/training_set"
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
            sql = "create table `%s`(" \
                "`id` INT NOT NULL AUTO_INCREMENT," \
                "`consumerId` VARCHAR(50) NULL," \
                "`rate` INT NULL," \
                "`date` VARCHAR(45) NULL," \
                "PRIMARY KEY (`id`));" % fileName
            cursor.execute(sql)
            conn.commit()
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
                sql = "insert into %s(`consumerId`,`rate`,`date`) values('%s','%s','%s')" % (fileName, second[0], second[1], second[2])
                cursor.execute(sql)
                second = f.readline()
            conn.commit()
            print("%s:table %s completed" % (name, fileName))


if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=(5614, 7501, "thread1"))
    t3 = threading.Thread(target=run, args=(8911, 10986, "thread3"))
    t2 = threading.Thread(target=run, args=(16153, 16960, "thread2"))
    t4 = threading.Thread(target=run, args=(16960, 17771, "thread4"))
    # t1.start()
    t2.start()
    # t3.start()
    t4.start()
