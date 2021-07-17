#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'predictAnswer' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stockData
#  2. INTEGER_ARRAY queries
#

def predictAnswer(stockData, queries):
    # Write your code here
    #print(stockData)
    #print(queries)
    print("now it is the query list through this n value")
    print(stockData[:queries[0]-1])
    index = 0
    for query in queries:
        regular_stock_prince = stockData[query-1]
        day_index = 1
        for price in stockData[:query-2]:
            if price < regular_stock_prince:
                queries[index] = price_index 
                break
            
        index += 2
    print(queries)
    return (queries)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stockData_count = int(input().strip())

    stockData = []

    for _ in range(stockData_count):
        stockData_item = int(input().strip())
        stockData.append(stockData_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = predictAnswer(stockData, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

