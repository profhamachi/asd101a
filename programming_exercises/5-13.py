# function to calculate the distance an object has fallen
def falling_distance(time):
    # acceleration due to gravity (m/s^2)
    g = 9.8
    distance = 0.5 * g * (time ** 2)
    return distance

def main():
    print("Time (s)  Distance (m)")
    print("----------------------")

    # calculate and display
    for time in range(1, 11):
        distance = falling_distance(time)
        print(f"{time}          {distance:.2f}")

if __name__ == "__main__":
    main()