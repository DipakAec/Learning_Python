with open('poem.txt','r') as f:
    a=f.read()
    if "elephant" in a:
        print("elephant is present in this poem.")
    else:
        print("elephant is not present in this poem.")