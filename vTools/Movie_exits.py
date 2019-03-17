import os.path


def getNum(m, n):
    j = n
    if int(m / 10) != 0:
        j += 1
        j = getNum(int(m / 10), j)
    return j


for i in range(1, 17771):
    print(i)
    num = int(getNum(i, 1))
    zero = 7 - num
    zeros = ""
    while zero != 0:
        zeros = "0%s" % zeros
        zero -= 1
        fileName = "mv_%s%d" % (zeros, i)
    fileName = "mv_%s%d" % (zeros, i)
    if os.path.exists("/Users/vill/Desktop/推荐系统导论/netflix数据集/0.1M_movie/%s.txt" % fileName):
        with open("/Users/vill/Desktop/推荐系统导论/hottestMovie.txt", "a+") as f:
            f.write("%s\r\n" % fileName)
