# function to calculate kinetic energy
def kinetic_energy(mass, velocity):
    KE = 0.5 * mass * (velocity ** 2)
    return KE

def main():
    # get mass (in kg) and velocity (in meters per second) from the user
    mass = float(input("Enter the mass of the object (in kg): "))
    velocity = float(input("Enter the velocity of the object (in meters per second): "))

    # call the kinetic_energy function to calculate kinetic energy
    KE = kinetic_energy(mass, velocity)

    # display the calculated kinetic energy
    print(f"The kinetic energy of the object is {KE:.2f} joules.")
if __name__ == "__main__":
    main()