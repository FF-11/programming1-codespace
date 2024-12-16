for i in [0, 1, 2, 3, 4, 3, 2, 1, 0]:
    if i % 2:
        output = [" "] * 12
        for j in range((i // 2)+1):
            output[2*j] = output[-1-2*j] = "@"
    else:
        output = ["@"] * 12
        for j in range(i // 2):
            output[(2*j)-2] = output[-2*j+1] = " "
    print(*output, sep='')
