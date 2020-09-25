"""
关于BMI
"""
name = input("请输入你的姓名：")
height = float (input("请输入你的身高（米）："))
weight = float (input("请输入你的体重（千克）："))

BMI =int ( weight/(height*height))

if BMI < 18.5:
    print(name+"你的体重过轻！你的体脂率是："+str(BMI))
elif BMI >=18.5 and BMI <= 25:
    print(name+"你的体重正常！你的体脂率是："+str(BMI))
elif BMI >= 25 and BMI <= 28:
    print(name+"你的体重过重！你的体脂率是："+str(BMI))
elif BMI >= 28 and BMI <= 32:
    print(name+"肥胖！你的体脂率是："+str(BMI))
else:
    print(name+"严重肥胖！你的体脂率是："+str(BMI))