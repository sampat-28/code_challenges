#Height Calculator
#taking inputs of height
foot,inch=map(int,input("Enter your height in foots and inches").split(" "))
#calculations
meter1=foot*0.3048
meter2=inch*0.0254
meter_height=meter1+meter2
centi_m=meter_height*100
#printing resultant height
print("\n\nYour height in meter is",round(meter_height,3))
print("Youer height in centimetres is",round(centi_m,2))
