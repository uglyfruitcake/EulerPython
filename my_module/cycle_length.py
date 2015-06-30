def cycle_length(n):
    for i in range(1, n + 1):
        if ((10 ** i)-1) % n == 0:
            return(i)
            break
        else:
            if i == n:
                return(0)
