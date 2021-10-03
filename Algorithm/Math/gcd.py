def GCD(a, b):
    if a == b:
	    return a

    while b:
	    a, b = b, a % b

    return a

if __name__ == '__main__':
	
    a, b = map(int, input().split())
    print("GCD: ", GCD(a, b))
