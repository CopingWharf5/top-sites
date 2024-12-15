from numpy import random
import numpy as np
import sys, csv

def Zipf(a: np.float64, min: np.uint64, max: np.uint64, size=None):
    """
    Generate Zipf-like random variables,
    but in inclusive [min...max] interval
    """
    if min == 0:
        raise ZeroDivisionError("")

    v = np.arange(min, max+1) # values to sample
    p = 1.0 / np.power(v, a)  # probabilities
    p /= np.sum(p)            # normalized

    return np.random.choice(v, size=size, replace=True, p=p)

generate_zipf = False

zipf_size = int(sys.argv[1])
zipf_parameter = float(sys.argv[2])
in_path = sys.argv[3]
out_path = sys.argv[4]

with open(in_path, 'r') as f1:
    text_list = f1.readlines()
#print(text_list)

if generate_zipf:
    random_list = Zipf(zipf_parameter, 1, len(text_list)+1, zipf_size)
else:
    random_list = random.randint(0, len(text_list), size=zipf_size)

text_list_zipf = [(text_list[j] ) for j in random_list]
with open(out_path, 'w') as f2:
    f2.writelines(text_list_zipf)
