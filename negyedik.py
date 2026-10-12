def osszeadas(a, b, s=1):
    return (a + b) / s


# Főprogram
if __name__ == "__main__":
    x = 4
    y = 6
    s = 1
    print(osszeadas(x, y, s))

    sorozat = [1, 5, 9, 6, 8, 7]
    for elem in sorozat:
        if elem == 5:
            continue
        print(elem)
        if elem == 6:
            break
    else:
        print("vége")
    print()

    for elem in range(1, 6, 2):
        print(elem)

    for elem in "Jó reggelt!":
        print(elem)

    # hibás futás

    s = 1
    x =  76
    try:
        eredmeny = x / s
    except ZeroDivisionError:
        eredmeny = 0
        print("Hiba - nullával való osztás")
    except TypeError:
        eredmeny = 1
        print("Az egyik érték hibás")
    else:
        print(eredmeny)
    finally:
        print("program vége")