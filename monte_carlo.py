#!/usr/bin/env python3

from matplotlib import pyplot as plt
import random
import numpy as np

def monte_carlo_method(x):
    points = []
    point_count = 0
    circle_count = 0

    for i in range(1, x):
        # generating random points
        x = random.random()
        y = random.random()

        # adding the point to the list of points
        points.append((x, y))
        point_count += 1
        
        # checking if the point is inside the circle using pythagoras
        if (x ** 2 + y ** 2) ** 0.5 <= 1:
            circle_count += 1

    # returning the ratio of points inside the circle to all points
    # since we're using a quarter circle, we must multiply by 4
    return 4 * (circle_count / point_count), points

def main():
    x = 1000000
    calculated_pi, points = monte_carlo_method(x)
    
    # Calculate accurate digits
    digits = -2 
    for i, j in zip(str(calculated_pi), str(np.pi)):
        if i == j:
            digits += 1
        else:
            break
    print(f"{np.pi}\n{calculated_pi}\n accurate digits: {digits}")

    # plotting the points, green for points inside the circle, red for points outside the circle
    limit = 0
    for point in points:
        # using modulo of x / 1000 to plot only 1000 points
        if limit % (x / 1000) == 0:
            # using pythagoras to determine if the point is inside the circle
            if (point[0] ** 2 + point[1] ** 2) ** 0.5 <= 1:
                # plotting the point as a green circle
                plt.plot(point[0], point[1], 'go')
            else:
                # plotting the point as a red circle
                plt.plot(point[0], point[1], 'ro')

        # incrementing lim
        limit += 1

    # plotting the quarter circle
    circle = plt.Circle((0, 0), 1, color='b', fill=False, linewidth=2)

    # plotting the square
    square = plt.Rectangle((-1, -1), 2, 2, color='b', fill=False)

    # plotting the circle and the square
    plt.gca().add_patch(circle)
    plt.gca().add_patch(square)

    # adding a title and axis labels
    plt.title(f'Calculated pi = {str(calculated_pi)}, accurate digits = {digits}')
    plt.xlabel('X')
    plt.ylabel('Y')
    # plt.text(0.5, 1.1, 'pi = ' + str(calculated_pi))

    # limiting the view to the square
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # plt.show()
    plt.savefig("test.png", dpi=100)
    
if __name__ == "__main__":
    main()
