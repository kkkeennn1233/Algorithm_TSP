import random, time
import matplotlib.pyplot as plt
import numpy as np


def SetCostMatrix(num):  # 建立一個距離矩陣
    cmatrix = {}
    for i in range(0, num):
        for j in range(0, num):
            if i == j:
                cmatrix[(i, j)] = 0
            else:
                if j > i:
                    cmatrix[(i, j)] = random.randint(1, 30)  # 每條邊權重包含(1-30)
                else:
                    cmatrix[(i, j)] = cmatrix[(j, i)]  # 同樣的點到同樣的點距離改成0
    print(cmatrix)
    return cmatrix


def GetCostVal(row, col):
    return cities_matrix[(row, col)]  # 查距離***查字典值的


def TSPGetMinDistance(start, cities):
    D = []
    if len(cities) == 0:
        minDis = GetCostVal(start, 0)
        return minDis
    else:
        for i in range(len(cities)):
            dcities = cities[:]
            dcities.remove(cities[i])
            D.append(GetCostVal(start, cities[i]) + TSPGetMinDistance(cities[i], dcities))
    return (min(D))


def average():
    TSP_round_time = []  # 存取5次時間差
    for i in range(1):
        start_time = time.time()  # 起始時間
        main()
        end_time = time.time()  # 結束時間
        # print(end_time-start_time)
        TSP_round_time.append(end_time - start_time)  # 時間差
    avg_time = (np.mean(TSP_round_time))  # 平均時間
    TSP_time.append(np.mean(avg_time))
    print(TSP_time)


def main():
    TSP_DP_Min = TSPGetMinDistance(start_point, cities_name)
    # print(TSP_DP_Min)#最短路徑


TSP_time = []
for i in range(4, 21):
    random_points = i  # 有幾座城市
    cities_matrix = SetCostMatrix(random_points)  # 城市距離字典
    start_point = 0  # 從0出發
    cities_name = [i for i in range(1, random_points)]  # 除了起點0的城市的points
    average()

print(TSP_time)
xpt = [i for i in range(4, 21)]
ypt = TSP_time
plt.plot(xpt, ypt)  # 畫線
plt.title("TSP_DP_Time", fontsize=20)  # 圖表標題
plt.xlabel("Number_Of_City", fontsize=12)  # x軸標題
plt.ylabel("AVG_Time", fontsize=12)  # y軸標題
plt.show()  # 顯示繪製的圖形
