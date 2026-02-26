width = int(input("\nWidth: "))
height = int(input("Height: "))

def calculate_area(width, height):
    area = width * height
    return area

result = calculate_area(width, height)
print(f"\nArea is: {result}")
