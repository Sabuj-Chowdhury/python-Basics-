distance = int(input("Distance: "))

if distance <3:
    transport_mood = "Walk"
elif distance>=3 and distance<=15:
    transport_mood = "Bike"
else:
    transport_mood="Car"
print(transport_mood)