import mysql.connector


def getNum(m, n):
    j = n
    if int(m / 10) != 0:
        j += 1
        j = getNum(int(m/10), j)
    return j


conn = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommenderSystem")
cursor = conn.cursor()

filePath = input("Please input filePath:\n")
for i in range(2781, 17771):
    i = int(i)
    num = int(getNum(i, 1))
    zero = 7 - num
    zeros = ""
    while zero != 0:
        zeros = "0%s" % zeros
        zero -= 1
    fileName = "mv_%s%d" % (zeros, i)
    with open("%s/%s.txt" % (filePath, fileName)) as f:
        sql = "create table `%s`(" \
              "`id` INT NOT NULL AUTO_INCREMENT," \
              "`consumerId` VARCHAR(50) NULL," \
              "`rate` INT NULL," \
              "`date` VARCHAR(45) NULL," \
              "PRIMARY KEY (`id`));" % fileName
        cursor.execute(sql)
        conn.commit()
        first = f.readline()
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
        print("table %s completed" % fileName)






