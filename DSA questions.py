# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:21:45 2020

@author: parva
"""

'''1. Reversal of array'''

# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}

# Input :  arr[] = {4, 5, 1, 2}
# Output : arr[] = {2, 1, 5, 4}

def rev_rec(a,start,end):
    if start >= end:
        return 
    
    a[start],a[end] = a[end],a[start]
    rev_rec(a, start+1, end-1)    
    
A = [2,4,5,2,6,3,1]
rev_rec(A,0,5)
A


'''2. Maximum and minimum of an array using minimum number of comparisons'''

def getMinMax(low, high, arr): 
    arr_max = arr[low] 
    arr_min = arr[low] 
      
    if low == high: 
        arr_max = arr[low] 
        arr_min = arr[low] 
        return (arr_max, arr_min) 
          
    elif high == low + 1: 
        if arr[low] > arr[high]: 
            arr_max = arr[low] 
            arr_min = arr[high] 
        else: 
            arr_max = arr[high] 
            arr_min = arr[low] 
        return (arr_max, arr_min) 
    else: 
          
        # If there are more than 2 elements 
        mid = int((low + high) / 2) 
        arr_max1, arr_min1 = getMinMax(low, mid, arr) 
        arr_max2, arr_min2 = getMinMax(mid + 1, high, arr) 
  
    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2)) 
            
A = [1000, 11, 445, 1, 330, 3000]    
getMinMax(0,5,A)


'''3. Find the kth max and min element from an array'''
#not the optimized solution
def KMinMax(K,a):
    a.sort()
    return a[K-1],a[-K]

A = [1000, 11, 445, 1, 330, 3000] 
KMinMax(2,A)


'''4. Sort an array of 0s, 1s and 2s without any sorting algorithm'''
A = [1,2,0,0,0,2,1,1,1,2,0,2,0,1]

def A012(A):
    zeros,ones,twos = 0,0,0
    for i in range(len(A)):
        if A[i] == 0:
            zeros+=1
        elif A[i] == 1:
            ones+=1
        else:
            twos+=1
            
    for i in range(zeros):
        A[i] = 0
    for i in range(zeros,zeros+ones):
        A[i] = 1
    for i in range(zeros+ones,zeros+ones+twos):
        A[i] = 2
    
    return A

A012(A)

'''5. Move all negative numbers to beginning and positive to end with constant extra space'''
B = [12,32,-11,-6,0,19,-1,-37,0,22,-45]

def negpos(a):
    n = len(a)
    left = 0
    right = n-1
    while left < right:
        if a[left] >= 0 and a[right] < 0:
            a[left],a[right] = a[right],a[left]
            left += 1
            right -= 1
            
        if a[left] < 0 and a[right] < 0:
            left +=1
            
        if a[left] < 0 and a[right] >= 0:
            left +=1
            right -= 1
            
        if a[left] >= 0 and a[right] >= 0:
            right -= 1
            
    return a
            
negpos(B)


'''6. Union and Intersection of two Sorted Arrays'''
A = [1,3,4,17,23,57,61]
B = [2,4,13,17,29,35,51,57,72]

def UIS(a,b):
    inter = []
    for ele in a:
        if ele in b:
            inter.append(ele)
    union = list(set(a + b))
    return union,inter
    
UIS(A,B) 


'''7. Cyclically rotate an array by one'''

def array_rot(a):
    n = len(a)
    movable = a[0]
    for i in range(n):
        if i != (n-1):
            a[i+1],movable = movable,a[i+1]
            
        else:
            a[0] = movable
            
    return a

array_rot([1,3,2,6,4,3,4])


'''8. Given an array arr of N integers. Find the contiguous sub-array with maximum sum. '''
        
A = [-7,2,-4,3,5,-4,2,0,-1,8,-5,-7,3,6]
B = [-7,2,-4,3,5,-4,2,0,-1,2,-5,-7,3,-6]
def max_subarray(a):
    final_max = 0
    current_max = 0
    for ele in a:
        current_max += ele
        if current_max < 0:
            current_max = 0
        elif current_max > final_max:
            final_max = current_max
            
    return final_max

max_subarray(A)
max_subarray(B)


'''9. Minimize and Maximize the maximum difference between Heights.'''

def Mini_MaxHeights(arr,n,k):
    
    if n == 1:
        return 0
    else:
        arr.sort()
        ans = arr[n-1] - arr[0]
        small = arr[0] + k
        big = arr[n-1] - k
        
        if small > big:
            small,big = big,small
        
        for i in range(1,n-1):
            add = arr[i]+k
            subtract = arr[i]-k
            
            if subtract>=small and add<=big:
                continue
            
            if big - subtract >= add - small:
                big = add
                
            else:
                small = subtract
                
        return min(ans,big - small)
    
arr = [7, 4, 8, 8, 8, 9]
Mini_MaxHeights(arr, len(arr), 5)
            

'''10. Minimum number of jumps to reach the end of an array.'''

def minJumps(arr, n): 
  if (n <= 1): 
    return 0
   
  if (arr[0] == 0): 
    return -1
   
  maxReach = arr[0]   
  step = arr[0] 
  jump = 1 
  print('maxReach = ',maxReach)
  print('step = ',step)
  print('jumps = ',jump) 
  for i in range(1, n): 
    # Check if we have reached the end of the array 
    print('i = ',i)

    if (i == n-1): 
      return jump 
   
    # updating maxReach 
    maxReach = max(maxReach, i + arr[i]) 
    print('maxReach = ',maxReach)
    # we use a step to get to the current index 
    step -= 1; 
    print('step = ',step)
    # If no further steps left 
    if (step == 0): 
      # we must have used a jump 
      jump += 1
      print('jumps = ',jump)
      # Check if the current index / position or lesser index 
      # is the maximum reach point from the previous indexes 
      if(i >= maxReach): 
        return -1
   
      # re-initialize the steps to the amount 
      # of steps to reach maxReach from position i. 
      step = maxReach - i; 
  return -1
        
A = [1,4,3,2,6,7]
minJumps(A,len(A))
                        
                
B = [3,1,5,0,9,2,6,7,6,8,9]
minJumps(B,len(B))     
        
    
'''11. Find Duplicate in an array of N+1 Integers.'''


def dup(arr):
    a = list(set(arr))
    for ele in a:
        arr.remove(ele)
            
    return arr[0]

dup([3,1,3,4,2])


'''12. Merge two sorted arrays without using extra space.'''


# Python program to merge 
# two sorted arrays 
# with O(1) extra space. 
  
# Merge ar1[] and ar2[] 
# with O(1) extra space 
def merge(ar1, ar2, m, n): 
  
    # Iterate through all 
    # elements of ar2[] starting from 
    # the last element 
    for i in range(n-1, -1, -1): 
      
        # Find the smallest element 
        # greater than ar2[i]. Move all 
        # elements one position ahead 
        # till the smallest greater 
        # element is not found  
        last = ar1[m-1] 
        j=m-2
        while(j >= 0 and ar1[j] > ar2[i]): 
            ar1[j+1] = ar1[j] 
            j-=1
   
        # If there was a greater element 
        if (j != m-2 or last > ar2[i]): 
          
            ar1[j+1] = ar2[i] 
            ar2[i] = last 
    return ar1,ar2


ar1 = [1, 5, 9, 10, 15, 20] 
ar2 = [2, 3, 8, 13] 
m = len(ar1) 
n = len(ar2)     

merge(ar1, ar2, m, n)


'''13. kadane's algo. '''

#returns maximum sum of contiguous subarray

def kadane_algo(arr,n):
    current_sum = arr[0]
    final_sum = arr[0]
    for i in range(1,n):
        current_sum += arr[i]
        if current_sum < 0:
            current_sum = 0
        elif current_sum > final_sum:
            final_sum = current_sum
        
    return final_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
kadane_algo(arr, len(arr))



'''14. Merge Intervals'''

#Given a collection of intervals, merge all overlapping intervals.

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

def merge_intervals(intervals):
    intervals.sort(key = lambda x:x[0])
    stack = []
    stack.append(intervals[0])
    for i in range(1,len(intervals)):
        if intervals[i][0] >= stack[-1][0] and intervals[i][0] <= stack[-1][1]:
            if intervals[i][1] > stack[-1][1]:
                
                stack[-1][1] = intervals[i][1]
            
        else:
            stack.append(intervals[i])
            
    return stack

intervals = [[1,3],[2,6],[8,10],[15,18]]      
merge_intervals(intervals)       

