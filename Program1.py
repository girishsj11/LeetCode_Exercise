# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 22:17:57 2020

@author: giri
"""

def twoSum(num_array, target):
    if(target in num_array):
        return (num_array.index(target))
    else:
        temp = dict()
        for index, value in enumerate(num_array):
            remaining = target - value
            if remaining in temp:
                return [temp[remaining], index]
            temp[value] = index
        return (list(temp.values()))


if __name__ == "__main__":
    print("Enter the list of elements separated by spaces : ")
    num_array = list(map(int,input().split(' ')))
    print("user input array is : ",num_array)
    target = int(input("Enter the target number you can get it from the entered list : "))
    print("output index '{}' values which equals to target '{}' ".format(twoSum(num_array, target),target))
