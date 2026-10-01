height= float(input())
m = int(input())
index= m/(height*height)
if index < 18.5:
    print("Your body mass index is:",round(index, 2),"that is underweight")
elif 18.5<=index<=24.9:
    print("Your body mass index is:",round(index, 2),"that is normal weight")
elif index > 24.9:
    print("Your body mass index is:",round(index, 2),"that is overweight")
