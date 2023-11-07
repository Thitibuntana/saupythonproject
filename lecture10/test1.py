try :
    n1 = int(input("Input number 1: "))
    n2 = int(input("Input number 2: "))

    result1 = n1 * n2
    result2 = n1 / n2

    print(f"{n1} x {n2} = {result1}")
    print(f"{n1} / {n2} = {result2}")
except ValueError :
    print("Input invalid.")
except ZeroDivisionError :
    print("2nd number mustn't be zero.")
except Exception :
    print("Exception found. Restart.")
finally :
    print("s")