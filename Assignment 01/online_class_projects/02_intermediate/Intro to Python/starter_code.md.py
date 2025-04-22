# Planetary WeightsDownload Project
# """
# Prompts the user for a weight on Earth
# and a planet (in separate inputs). Then 
# prints the equivalent weight on that planet.

# Note that the user should type in a planet with 
# the first letter as uppercase, and you do not need
# to handle the case where a user types in something 
# other than one of the planets (that is not Earth). 
# """


# # Mars Weight

# """
# Prompts the user for a weight on Earth
# and prints the equivalent weight on Mars.
# """

# def main():
#     # Fill this function out!
#     pass

# if __name__ == "__main__":
#     main()




# Gravitational constants (relative to Earth)
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    # Ask for weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Ask for planet name
    planet = input("Enter a planet (capitalize first letter, e.g. Mars): ")

    # Determine gravity constant based on planet
    if planet == "Mercury":
        gravity = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity = VENUS_GRAVITY
    elif planet == "Mars":
        gravity = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity = URANUS_GRAVITY
    elif planet == "Neptune":
        gravity = NEPTUNE_GRAVITY
    else:
        print("Invalid planet. Please enter a valid planet with first letter capitalized.")
        return

    # Calculate equivalent weight
    new_weight = round(earth_weight * gravity, 2)

    # Print result
    print(f"The equivalent weight on {planet}: {new_weight}")

if __name__ == "__main__":
    main()
