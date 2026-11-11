import math 
import random 
# print(math.factorial(11))

# def sum_target(arr,target):
#     left = 0 
#     right = len(arr) - 1 
#     total = arr[left] + arr[right]
#     result = 0 
#     if total == target : 
#         result +=1
#         left +=1 
#         right -=1
#     return result 
# numbers = [1,2,3,4,5,6,7,8,9]    
# print(sum_target(numbers,10))


# def two_sum(arr,target):
#     left = 0
#     right = len(arr) - 1
#     result = 0 
#     while left < right :
#         total = arr[left] + arr[right]
#         if total == target :
#             result +=1
#             left +=1 
#             right -=1
#         elif total < target :
#             left +=1
#         else:
#             right -= 1 
#     return result 
# numbers = [1,2,3,4,6,7,8,9]         
# print(two_sum(numbers,10))


# arr = [1,5,8,2,6,6,5]
# prefix =  [0] * (len(arr)+1)
# for i in range(len(arr)):
#     prefix[i+1] = prefix[i] + arr[i]
# print(f"Original array : {arr}")    
# print(f"Sum array : {prefix}")
# N = int(input('Enter the N : '))
# print(prefix[N])

# arr = [2, 4, 1, 7, 3, 5, 8]  


# prefix = [0] * (len(arr) + 1)
# for i in range(len(arr)):
#     prefix[i + 1] = prefix[i] + arr[i]

# print("Original array:", arr)
# print("Prefix array:  ", prefix)


# N = 6
# sum_till_n = prefix[N]
# print(f"Sum of elements till N={N}: {sum_till_n}")



# # L, R = 1, 4
# # range_sum = prefix[R + 1] - prefix[L]
# # print(f"Sum of elements in range [{L}, {R}]: {range_sum}")

# arr = [random.randint(1,100) for _ in range(7)]
# prefix =[0] * (len(arr)+1)
# for x in range(len(arr)):
#     prefix[x+1]=prefix[x] + arr[x]
# N = int(input('Enter the N to know sum of N elements : '))   
# print(prefix[N])

# arr = [1,2,4,7,9,10]
# prefix =[0] *(len(arr)+1)
# for x in range(len(arr)):
#     prefix[x+1] = prefix[x] + arr[x]
# # print(arr)
# # print(prefix)    
# N = int(input())
# # print(prefix[N])
# result = 0
# for i in range(1,N+1): 
#     result +=x 
# print(x)    

# arr = [1,2,4,7,9,10]
# result = 0 
# N = int(input())
# for x in range(1,N):
#     result += arr[x]
# print(result )    

# arr = [1,2,3,4,5,6,7,8,9]
# prefix = [0] * (len(arr)+1)
# for i in range(len(arr)):
#     prefix[i+1] = prefix[i] + arr[i]
# N = int(input())
# print(prefix[N+1])   

# numbers = [1,2,3,4,5,6,7,8,9]
# prefix = [0] * (len(numbers) + 1 )
# for x in range(len(numbers)):
#     prefix[x+1] = prefix[x] + numbers[x]
# L,R = map(int,input().split())
# answer = prefix[R+1] - prefix[L]    
# print(numbers)
# print(answer)

# N = int(input())
# temp = N
# reverse = 0 
# while temp>0:
#     digit = temp%10
#     reverse = reverse*10+digit 
#     temp//=10
# if N == reverse :
#     print('Palindrome')
# else:
#     print('Not Palindrome')    
# class Solution:
#     def IsPalindrome(self,x:int) -> bool:
#         if x < 0 :
#             return False 
#         temp = x 
#         reverse = 0 
#         while temp>0:
#             digit = temp%10
#             reverse = reverse*10 +digit 
#             temp //= 10 
#         return x == reverse     
# solver = Solution()
# print(solver.IsPalindrome(121))        


# number = int(input())
# digits = len(str(number))
# temp = number 
# total = 0
# while temp > 0 :
#     digit = temp%10
#     total += digit**digits 
#     temp//=10
# if total == number:
#     print('Armstrong')
# else:
#     print('Not Armstrong')


# class Solution:
#     def IsArmstrong(self,x:int)->bool:
#         temp = x
#         digits = len(str(x))
#         total = 0 
#         while temp>0:
#             digit = temp%10
#             total += digit**digits
#             temp//=10
#         return x == total    

# n = int(input())
# total =  0 
# for x in range(1,n):
#     if n % x == 0:
#         total +=x
# if total == n :
#     print('Perfect Number ')
# else:
#     print('Not Perfect')

class Perfect:
    def IsPerfect(self,x:int):
        total = 0
        for i in range(1,x):
            if x%i==0:
                total +=i
        if x == total :
            print('Perfect')
        else:
            print('Not')        
perfect = Perfect()
perfect.IsPerfect(28)









