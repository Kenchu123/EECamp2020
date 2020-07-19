##########################################################################################
# Example 5:
# 
# Write a function that can convert a decimal number to a bianry number.
# 
##########################################################################################


def convert(N):
    s = []
    while N / 2 != 0:
        s.insert(0, N % 2)
        N = N // 2

    return s

n = input("Please enter a decimal number: ")
l = [str(i) for i in convert(int(n))]
print(''.join(l))


