

def gen_and_print_even_tuple():
    given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    even_tuple = tuple(x for x in given_tuple if x % 2 == 0)
    print(even_tuple)

gen_and_print_even_tuple()
