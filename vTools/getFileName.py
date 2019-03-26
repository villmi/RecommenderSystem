import os

with open("/Users/vill/Desktop/推荐系统导论/netflix数据集/mv_9383_1.txt", "a+") as f:
    a = []
    for root, dirs, files in os.walk("/Users/vill/Desktop/推荐系统导论/netflix数据集/training_set_Lee"):
        files = sorted(files)
        for file in files:
            f.write("%s\n" % file.split('.')[0])
