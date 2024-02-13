def shortest_intance(n):
    factors = []
    shortest_int = n
    for num in range(1,(n+1)):
        if n % num == 0:
            factors.append(num)
    for i in range(len(factors)-1):
        if factors[i+1] - factors[i] < shortest_int:
            shortest_int = factors[i+1] - factors[i]
    return(shortest_int)


print(shortest_intance(8))
print(shortest_intance(25))
print(shortest_intance(13013))