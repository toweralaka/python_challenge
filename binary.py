def thestringrepeat(arr):
    result_list = []
    bin_dict = {}
    cur_elem = arr[0]
    cur_count = 0
    for elem in arr:
        if elem == cur_elem:
            cur_count += 1
        else:
            result_list.append((cur_elem, cur_count))
            try:
                bin_dict[cur_elem].append(cur_count)
            except KeyError:
                bin_dict[cur_elem] = [cur_count,]
            cur_elem = elem
            cur_count = 1
    result_list.append((cur_elem, cur_count))
    try:
        bin_dict[cur_elem].append(cur_count)
    except KeyError:
        bin_dict[cur_elem] = [cur_count,]
    return bin_dict

def binarylength(num):
    mybin = (f'{num:08b}').lstrip('0')
    bin_list = thestringrepeat(str(mybin))
    # bin_dict = {}
    # sorted_list = sorted(nested_list, key=lambda x: x[1])
    return max(bin_list['1'])

print(binarylength(51))