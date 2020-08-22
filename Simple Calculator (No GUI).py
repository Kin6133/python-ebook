#กำหนดให้ a เป็น input ในการกรอกเครื่องหมาย
a = input("Choose your operand (+,-,*,/) : ")
#กำหนดให้ b เป็น float ของ input ในการกรอกตัวเลขตัวที่หนึ่ง
b = float(input("Type your first number : "))
#กำหนดให้ c เป็น float ของ input ในการกรอกตัวเลขตัวที่สอง
c = float(input("Type your second number : "))
#ถ้า a เท่ากับ +
if a == "+":
    print("The sum of {0} and {1} is {2}." .format  (b,c,b+c))
#ถ้า a เท่ากับ -
if a == "-":
    print("{0} – {1} = {2}".format(b,c,b-c))
#ถ้า a เท่ากับ *
if a == "*":
    print("{0} * {1} = {2}".format(b,c,b*c))
#ถ้า a เท่ากับ /
if a == "/":
    print("{0} / {1} = {2}".format(b,c,b/c))
#ถ้า a ไม่เท่ากับ +,-,* หรือ /
if a != "+" and a != "-" and a != "*" and a != "/" :
	print("Unknown Operands.")
#จบการใช้
print("Calculator Ended.")
