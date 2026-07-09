import math
print("---Distance Calculator between Two Points---")
active = True

while active:
# Getting coordinates from user
    x1 = float(input("enter x1:  "))
    y1 = float(input("enter y1:  "))
    x2 = float(input("enter x2:  "))
    y2 = float(input("enter y2:  "))  

#Calculating the difference(the 'legs' of our triangle)
    delta_x= x2-x1
    delta_y= y2-y1

#Applying the Phytagorean theorem
#this calculates the distance correctly distance= math.sqrt(delta_x**2+ delta_y**2)

#1. Calculate the squared distance
    squared_distance = delta_x**2 + delta_y**2

# 2. Calculate the actual distance (Pass the value into the function)
    distance = math.sqrt(squared_distance)


# 3. Displaying everything (Ensure 'distance' matches the case above)
    print("-" * 30)
    print(f"squared distance (d2): {squared_distance}")
    print(f"distance: {math.hypot(delta_x, delta_y)}")
    print("-" * 30)

choice = input("Devam mı? (y/n): ").lower()
            
if choice != 'y':
        active = False  # Bu satır if'in içinde (8 boşluk içerde)
print("Program kapatılıyor...")

# Bu satır döngü bittikten sonra çalışır (Hizası en başta)
print("Güle güle!")
