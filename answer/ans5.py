##########################################################################################
# Example 5:
# 
# Write a function that can convert a bill to change.(找零機)
# 
##########################################################################################


def convert(N):
    num_50 = 0
    num_10 = 0
    num_5 = 0
    num_1 = 0

    num_50 = N // 50
    N = N % 50

    num_10 = N // 10
    N = N % 10

    num_5 = N // 5
    N = N % 5

    num_1 = N // 1
    N = N % 1
    
    print(f"50: {num_50}")
    print(f"10: {num_10}")
    print(f"5: {num_5}")
    print(f"1: {num_1}")

def convert_list(N):
    num = [0, 0, 0, 0]
    coin = [50, 10, 5, 1]

    for index, val in enumerate(coin):
        num[index] = N // val
        N = N % val
    
    print(f"50: {num[0]}")
    print(f"10: {num[1]}")
    print(f"5: {num[2]}")
    print(f"1: {num[3]}")

def convert_dict(N):
    num = {50: 0, 10: 0, 5: 0, 1:0}
    coin = [50, 10, 5, 1]

    for i in coin:
        num[i] = N // i
        N = N % i

    print(f"50: {num[50]}")
    print(f"10: {num[10]}")
    print(f"5: {num[5]}")
    print(f"1: {num[1]}")


n = input("Please enter a number: ")
# convert(int(n))
# convert_list(int(n))
convert_dict(int(n))





