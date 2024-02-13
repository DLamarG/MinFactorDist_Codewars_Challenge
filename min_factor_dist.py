def min_distance(n):
    factors = []
    min_dist = n
    for num in range(1,(n+1)):
        if n % num == 0:
            factors.append(num)
    for i in range(len(factors)-1):
        if factors[i+1] - factors[i] < min_dist:
            min_dist = factors[i+1] - factors[i]
    return(min_dist)


print(min_distance(8))
print(min_distance(25))
print(min_distance(13013))