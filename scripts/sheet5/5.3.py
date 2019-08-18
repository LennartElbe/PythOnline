def gcd(m, n):
    while n != 0:
        h = m % n

        m = n
        n = h
    return m


def cli_gcd():

    print("Calculate GCD from the input natural numbers.")
    current_list = []
    n = int(input("Input nat. number (or 0 to quit): "))
    while n != 0:  # takes in user input and puts it into a list
        current_list.append(n)
        n = int(input("Input nat. number (or 0 to quit): "))

    if len(current_list) == 0:  # if the list is empty print nothing and terminate program
        print("")
        return
    x = current_list[0]  # test for gcd(60,60) first
    for i in range(len(current_list)):
        #z in a loop check with next element 60,50 etc.
        x = gcd(x, current_list[i])
    print("GCD: %d" % x)


print(gcd(60, 60))

cli_gcd()
