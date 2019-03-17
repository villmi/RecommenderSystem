import mysql.connector


def getNum(m, n):
    j = n
    if int(m / 10) != 0:
        j += 1
        j = getNum(int(m/10), j)
    return j


# filePath = input("Please input filePath:\n")
filePath = "/Users/vill/Desktop/推荐系统导论/netflix数据集/training_set"
for i in range(2, 17771):
    i = int(i)
    num = int(getNum(i, 1))
    zero = 7 - num
    zeros = ""
    while zero != 0:
        zeros = "0%s" % zeros
        zero -= 1
    fileName = "mv_%s%d" % (zeros, i)
    with open("%s/%s.txt" % (filePath, fileName)) as f:
        first = f.readline()
        second = f.readline()
        while ',' in second:
            second = second.split(",")
            num = int(getNum(int(second[0]), 1))
            zero = 7 - num
            zeros = ""
            while zero != 0:
                zeros = "0%s" % zeros
                zero -= 1
            fileName1 = "usr_%s%s" % (zeros, second[0])
            with open("/Users/vill/Desktop/推荐系统导论/netflix数据集/user_set/%s.txt" % fileName1, "a+") as ff:
                if ff.readline() is not "usr%s:" % second[0]:
                    ff.write("%s:\n" % fileName1)
                    ff.write("%s,%s,%s\n" % (i, second[1], second[2]))
                else:
                    ff.write("%s,%s,%s\n" % (i, second[1], second[2]))
            # print(second)
            second = f.readline()
        print("file %s completed" % fileName)






