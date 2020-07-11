##########################################################################################
# Example 5:
# 
# Write a function that can convert a decimal number to a bianry number.
# 
##########################################################################################


def convert(N):
    pass
    ### TODO:

    ###

n = input("Please enter a decimal number: ")
print(convert(int(n)))


'''
Answer:
def convert(N):
    s = ''
    while N / 2 != 0:
        s = str(N % 2) + s
        N = N // 2

    return s

'''







