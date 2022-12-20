#!/usr/bin/env python3

def sumasjon(nedre_grense, ovre_grense, funksjon):
    summert = 0
    for i in range(nedre_grense, ovre_grense):
        summert += funksjon(i)
    return summert

def main():
    import numpy as np
    f = lambda x: (((-1)**x) / (2 * x + 1)) * 4

    for i in range(0, 10):
        N = 10**i
        calculated_pi = sumasjon(0, N, f)
        digits = -2
        for j, k in zip(str(calculated_pi), str(np.pi)):
            if j == k:
                digits += 1
            else:
                break
        print(f"10^{i}, {calculated_pi}, accurate digits: {digits}")

if __name__ == "__main__":
    main()