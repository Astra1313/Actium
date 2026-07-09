import math
print("---Distance Calculator between Two Points---")
active = True

while active:
# Getting coordinates from user
    x1 = float(input("enter x1:  "))
    y1 = float(input("enter y1:  "))
    x2 = float(input("enter x2:  "))
    y2 = float(input("enter y2:  "))  


    delta_x= x2-x1
    delta_y= y2-y1




    squared_distance = delta_x**2 + delta_y**2


    distance = math.sqrt(squared_distance)



    print("-" * 30)
    print(f"squared distance (d2): {squared_distance}")
    print(f"distance: {math.hypot(delta_x, delta_y)}")
    print("-" * 30)

choice = input("Devam mı? (y/n): ").lower()
            
if choice != 'y':
        active = False  
print("Closing...")

# Bu satır döngü bittikten sonra çalışır (Hizası en başta)
print("Güle güle!")
