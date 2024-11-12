import math


def calculate_area(a, b, c):
    s = (a + b + c) / 2
    v1 = s - a
    v2 = s - b
    v3 = s - c
    area = math.sqrt(s * v1 * v2 * v3)
    return area


def main():

    num_floors = int(input("Enter the number of floors (positive integer): "))

    if num_floors <= 0:
        print("Please enter a positive integer for the number of floors.")
        return

    total_floor_area = 0

    for i in range(num_floors):
        floor_area = float(input(f"Enter the area of floor {i + 1} (in square feet): "))
        total_floor_area += floor_area
    print(f"Total floor area: {total_floor_area:.2f} square feet")

    lot_area = float(input("\nEnter the lot area (in square feet): "))

    if lot_area > 0:
        far = total_floor_area / lot_area
        print(f"Floor Area Ratio (FAR): {far:.2f}")

        if 0 <= far <= 3:
            print("FAR is within the acceptable range (0 to 3).")
        else:
            print("FAR is outside the acceptable range (0 to 3).")
            print(
                "Please adjust the floor areas or lot area to achieve an acceptable FAR."
            )
    else:
        print("Lot area must be greater than zero. Cannot calculate FAR.")


if __name__ == "__main__":
    main()
