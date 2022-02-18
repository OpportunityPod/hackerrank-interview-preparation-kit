#!/bin/python3
import math
import os
import random
import re
import sys

def dfs(s,arr,visited):
    visited[s]=True
    cost=0
    for i in arr[s]:
        if(not visited[i]):
            cost+=1
            cost+=dfs(i,arr,visited)
    return cost
  
def roadsAndLibraries(n,m, c_lib, c_road, cities):
    if(c_lib<c_road):
        return c_lib*n
    if(m==0):
        return n*c_lib
    arr=[[0] for i in range(n+1)]
    visited=[False for i in range(n+1)]
    for i in range(1,n+1):
        arr[i][0]=i
    for i in range(m):
        arr[cities[i][0]].append(cities[i][1])
        arr[cities[i][1]].append(cities[i][0])
    vis=0
    for i in range(1,n+1):
        if(not visited[i]):
            vis+=dfs(i,arr,visited)
    cost=(((vis)*c_road)+((n-vis)*c_lib))
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, m, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
