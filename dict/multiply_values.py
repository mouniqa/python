d={
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5
}

mult_result = 1
add_result = 0
for key in d.keys():
    mult_result *= d[key]
    add_result += d[key]

print(mult_result)
print(add_result)
