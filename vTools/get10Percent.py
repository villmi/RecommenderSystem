import mysql.connector

# conn = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommederSystem_Training")
conn = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx")
cursor = conn.cursor()


def getNum(m, n):
    j = n
    if int(m / 10) != 0:
        j += 1
        j = getNum(int(m/10), j)
    return j


"注释部分用于建立数据库表格"
for i in range(1, 9):
    # print(i)
    # i = int(i)
    # num = int(getNum(i, 1))
    # zero = 7 - num
    # zeros = ""
    # while zero != 0:
    #     zeros = "0%s" % zeros
    #     zero -= 1
    # fileName = "mv_%s%d" % (zeros, i)
    fileName = "mv_0000001"
    # print(fileName)
    # sql = "select count(*) from `recommenderSystem`.`%s`" % fileName
    # cursor.execute(sql)
    # s = cursor.fetchone()
    # s = int(int(s[0]) * 0.2)
    # print(s)
    # # sql = "cre
    # sql = "create table `recommenderSystem_1per_TestSet`.`%s` as select * from `recommenderSystem`.`%s` order by date DESC limit %d" % (fileName, fileName, s)
    # cursor.execute(sql)
    # conn.commit()
    sql = "CREATE TABLE `recommenderSystem_1per_TestSet`.`pre_%s_%d` (`id` INT NOT NULL AUTO_INCREMENT,`consumerId` VARCHAR(45) NULL,`rate` FLOAT NULL,PRIMARY KEY (`id`));" % (fileName,i)
    cursor.execute(sql)
    conn.commit()
"以下部分用于建立文件"
# for i in range(1, 178):
#     with open("/Users/vill/Desktop/推荐系统导论/netflix数据集/1perMovie.txt", "a+") as f:
#         i = int(i)
#         num = int(getNum(i, 1))
#         zero = 7 - num
#         zeros = ""
#         while zero != 0:
#             zeros = "0%s" % zeros
#             zero -= 1
#         fileName = "mv_%s%d" % (zeros, i)
#         f.write("%s\n" % fileName)
