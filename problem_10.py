

input_seq = input()
words = input_seq.split()
sorted_words = sorted(set(words))
print(' '.join(sorted_words))