##########################################################################################
# Example 3:
# 
# Given a list contains "ADVENTURE", please transform it into "NTUEE" using list manipulation
# 
##########################################################################################

camp = ["N", "A", "T", "U", "R", "E"]

camp.pop(4)
camp.pop(1)
camp.append("E")

result = ''.join(camp)
print(f'result = {result}')


