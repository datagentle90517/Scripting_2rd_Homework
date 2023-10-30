student=dict()
student["sid"]=input("請輸入您的學號：")
student["sname"]=input("請輸入您的姓名：")
student["fchina"]=float(input("請輸入您的國文成績："))
student["fmath"]=float(input("請輸入您的數學成績："))
student["finfo"]=float(input("請輸入您的電腦成績："))
allScore=student["fchina"]+student["fmath"]+student["finfo"]
avg=round((allScore/3),2)
print("-"*30)
print(f"{student['sname']}({student['sid']})同學您好:")
print("以下是您的各科成績與分數評定\n")
print(f"國文:{student['fchina']} / 數學:{student['fmath']} / 電腦:{student['finfo']}")
print(f"總分:{allScore} / 平均:{avg}")
print("-"*30)
if avg<60:
    print("成績判定：不合格")
else:
    print("成績判定：合格")    
