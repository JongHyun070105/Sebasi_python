while True:
    a,b,c = map(int, input().split())


    if a == 0 & b == 0 & c == 0:
        print("wrong")
        break
    else:
        if((a * a) + (b * b) == (c * c) or
                (b * b) + (c * c) == (a * a) or
                    (a * a) +(c * c) == (b * b)):
            print("right")
        else:
            print("wrong")

