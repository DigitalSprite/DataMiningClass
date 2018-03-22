import pandas as pd
import numpy as np
from lshash.lshash import LSHash
import random as rand

# csv_reader = csv.reader(open('../reco_data/trade.csv', encoding='utf-8'))
# log = []
# #用于计算行和列的总数
# vips = []
# commodities = []
# i = True
# for row in csv_reader:
#     if(i == True):
#         i = False
#         continue
#     log.append([row[4], row[6], row[16]])
#     if(row[4] not in vips):
#         vips.append(row[4])
#     if(row[6] not in commodities):
#         commodities.append(row[6])
# df = pd.DataFrame(np.zeros((commodities.__len__(), vips.__len__()), dtype=np.int), index=np.array(commodities), columns=np.array(vips))
# for row in log:
#     df[row[0]][row[1]] += float(row[2])
# #得到了矩阵：行表示物品id，列表示vip的id
# print(df)

def getMatrix(file_name):
    df = pd.read_csv(file_name)
    line_index = set(df.iloc[:,4])
    row_index = set(df.iloc[:,6])
    new_df = pd.DataFrame(np.zeros((row_index.__len__(), line_index.__len__()), dtype=np.int), index=row_index, columns=line_index)
    temp = df.loc[:,['vipno','pluno','amt']]
    for i in range(temp.shape[0]):
        if i == 0:
            continue
        new_df.loc[temp.iloc[i, 1], temp.iloc[i, 0]] += int(temp.iloc[i, 2])
        if (temp.iloc[i, 2] - int(temp.iloc[i, 2]) == 0.5):
            new_df.loc[temp.iloc[i, 1], temp.iloc[i, 0]] += 1
    return new_df

def getLSHashOutput(filename, hash_size, k):
    matrix = getMatrix(filename)
    total_num = len(matrix.iloc[0])
    lsh = LSHash(hash_size=int(hash_size * total_num), input_dim=len(matrix.iloc[:,0]))
    for i in range(total_num):
        lsh.index(input_point=matrix.iloc[:,i], extra_data=matrix.columns[i])
    out_num = rand.randint(0, total_num - 1)
    #有多种lshash函数，默认是euclidean
    print(lsh.query(query_point=matrix.iloc[:, out_num], num_results=k + 1, distance_func='euclidean'))


if __name__ == '__main__':
    hash_size = [0.01, 0.05, 0.1, 0.2, 0.3, 0.5]
    k = [1,2,3,4,5]
    r1 = rand.randint(0, 5)
    r2 = rand.randint(0,4)
    getLSHashOutput('../reco_data/trade.csv', hash_size[r1], k[r2])
