def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = (weight/(height*height))

    if (bmi <18.5):
        print("your bmi is " + str(bmi) + ", underweight")

    if (18.5 <= bmi <= 25):
        print("your bmi is " + str(bmi) + ", normal weight")

    if ( bmi > 25 ):
        print ("your bmi is " + str(bmi) +", over weight")

calculate_bmi(weight=80,height=1.73)