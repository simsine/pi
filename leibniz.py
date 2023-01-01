#!/usr/bin/env python3

def sumasjon(nedre_grense, ovre_grense, funksjon):
    summert = 0
    for i in range(nedre_grense, ovre_grense):
        summert += funksjon(i)
    return summert

def main():
    import matplotlib.pyplot as plt
    import numpy as np
    f = lambda x: (((-1)**x) / (2 * x + 1)) * 4
    
    x_values, y_values = [], []

    for i in range(0, 50):
        N = i
        calculated_pi = sumasjon(0, N, f)
        digits = -2
        for j, k in zip(str(calculated_pi), str(np.pi)):
            if j == k:
                digits += 1
            else:
                break
        print(f"10^{i}, {calculated_pi}, accurate digits: {digits}")
        
        x_values.append(N)
        y_values.append(calculated_pi)
    
    plt.axhline(np.pi, color="r")
    plt.plot(x_values, y_values)
    plt.xlabel("N value")
    plt.ylabel("Pi value")
    plt.title("Leibniz method Pi values")
    plt.savefig("Leibniz_piValues.png")

if __name__ == "__main__":
    main()