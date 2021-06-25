def fun(l):
    list_len = len(l)
    for i in range(list_len):
        if i < list_len - 1:
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                fun(l)
    return l

