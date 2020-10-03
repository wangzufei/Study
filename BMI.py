"""
关于BMI的问题！
"""
name = input("请输入你的姓名：")
height = float(input("请输入你的身高："))
weight = float(input("请输入你的体重："))
bmi = weight/(height*height)

if bmi <= 18.5:
   print (name+"过轻！\n你的体脂率："+str(int(bmi))+"%")
elif bmi >18.5 and bmi <= 25:
   print (name+"正常！\n你的体脂率："+str(int(bmi))+"%")
elif bmi > 25 and bmi <= 28:
   print (name+"过重！\n你的体脂率："+ str(int(bmi))+"%")
elif bmi > 28 and bmi <= 29:
    print (name+"肥胖！\n你的体脂率："+str(int(bmi))+"%")
else:
   print (name+"严重肥胖！\n你的体脂率："+str(int(bmi))+"%")
