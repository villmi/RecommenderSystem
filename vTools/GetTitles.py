import mysql.connector

conn = mysql.connector.connect(host="localhost", user="vill", passwd="hao5jx", database="recommenderSystem")
cursor = conn.cursor()

filePath = input("Please input filePath:\n")

with open(filePath, 'r') as f:
    line = f.readline()
    i = 1
    while line is not None:
        line = line.split(",")
        if ('\'' or '\"') in line[2]:
            if '\'' in line[2]:
                line[2] = line[2].replace('\'', '\\\'')
                print("a")
            else:
                line[2] = line[2].replace('\"', '\\\"')
                print("b")
        sql = "insert into `movie`(`id`,`year`,`movieName`) values(%d,'%s','%s')" % (int(line[0]), line[1], line[2])
        print(sql)
        cursor.execute(sql)
        conn.commit()
        print(i)
        i = i + 1
        line = f.readline()
