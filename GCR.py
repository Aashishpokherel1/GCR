import math


def calculate_area(a, b, c):
    s = (a + b + c) / 2
    v1 = s - a
    v2 = s - b
    v3 = s - c
    area = math.sqrt(s * v1 * v2 * v3)
    return area


def main():
    num_triangles = int(input("Enter the number of triangles: "))
    total_area = 0

    for i in range(num_triangles):
        print(f"\nTriangle {i + 1}:")
        a = float(input("Enter side a (in meters): "))
        b = float(input("Enter side b (in meters): "))
        c = float(input("Enter side c (in meters): "))

        if a + b > c and a + c > b and b + c > a:
            area = calculate_area(a, b, c)
            total_area += area
            print(f"The area of triangle {i + 1} is: {area:.2f} square feet")
        else:
            print("Invalid triangle sides. Please enter valid values.")

    print(f"\nTotal area of all triangles: {total_area:.2f} square feet")

    # GCR Calculation
    footprint_area = float(
        input("\nEnter the footprint area of the building (in square feet): ")
    )
    if total_area > 0:
        gcr = footprint_area / total_area
        gcr_percentage = gcr * 100
        print(f"GCR: {gcr_percentage:.2f}%")

        if gcr_percentage < 1:
            print("Your house cannot pass (GCR > 0).")
        else:
            print("Your house passes (GCR <= 0).")
    else:
        print("Total area is zero. Cannot calculate GCR.")


if __name__ == "__main__":
    main()
