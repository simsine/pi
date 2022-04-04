#!/usr/bin/env python3

def pi(x):
    sum = 0
    n = 1
    positive = True

    while True:
        if positive:
            sum += 1 / n
        else:
            sum -= 1 / n
        
        n += 2
        positive = not positive

        if n > x:
            break
    
    return sum * 4

def main():
    print(pi(10000000))

if __name__ == "__main__":
    main()
