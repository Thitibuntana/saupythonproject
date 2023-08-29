roomWidth = float(input("Room width (CM): "))
roomLenght = float(input("Room lenght (CM): "))
roomHeight = float(input("Room height (CM): "))
print("----------------------------------------")
totalArea = ((roomWidth * roomLenght)*2) + ((roomWidth * roomHeight)*2) + ((roomHeight * roomLenght)*2) 
gallonAmount = round(totalArea/5)

print("For a room that is " + str(roomWidth) + " cm wide, " + str(roomLenght) + " cm long, and " + str(roomHeight) + " cm tall, you will need " + str(gallonAmount) + " gallons of paint.")
print("For a room that is", roomWidth, "cm wide,", roomLenght, "cm long, and", roomHeight, "cm tall, you will need", gallonAmount, "gallons of paint.")
print(f"For a room that is {roomWidth} cm wide, {roomLenght} cm long, and {roomHeight} cm tall, you will need {gallonAmount} gallons of paint.")
print("For a room that is {} cm wide, {} cm long, and {} cm tall, you will need {} gallons of paint.".format(roomWidth ,roomLenght ,roomHeight ,gallonAmount))


