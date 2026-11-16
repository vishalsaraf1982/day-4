num=int(input ("Enter your withdrawal amount "))
note1=num//100
note2=(num%100)//50
note3=((num%100)%50)//10

print("number of 100 rs note ",note1)
print("number of 50 rs note ",note2)
print("number of 10 rs note ",note3)