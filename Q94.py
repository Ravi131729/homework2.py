

input_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

req_list = []
for item in input_list:
    if item not in req_list:
        req_list.append(item)

print(req_list)
