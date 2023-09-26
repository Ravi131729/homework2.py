
def gen_and_print_dict():
    num_dict = {}
    for num in range(1, 21):
        num_dict[num] = num ** 2
    
    for value in num_dict.values():
        print(value)

gen_and_print_dict()
