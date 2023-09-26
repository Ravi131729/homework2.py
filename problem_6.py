

import math

C = 50
H = 30

def cal_value(D):
    Q = math.sqrt((2 * C * D) / H)
    return round(Q)
input_seq = input("Enter a comma-separated sequence of values for D: ")
values_for_D = input_seq.split(',')
results = [str(cal_value(float(value))) for value in values_for_D]
print(','.join(results))

