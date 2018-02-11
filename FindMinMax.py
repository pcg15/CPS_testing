def FindMinMax(list1):
    try: 
        list1 = list(list1)
    except TypeError:
        print("Give a list please!")
    for x in list1:
		try:
            x = float(x)
		except ValueError:
        print("Give a list with numbers!")
    try:
        print(list1[1])
    except:
        print("You need more than one number in the list!")       
    Minimum = min(list1)
    Maximum = max(list1)
    tup = (Minimum, Maximum)
    return tup
