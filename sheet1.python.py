#sheet 1
#question 1




#question 2
print(5**9)

print(3//2)

print(7//3)

print(7/3)

print(6==6)

a=20
a+=30
print(a)
a%=3
print(a)

print(True & False)
print(True * False)
print(True and False)
print((6>3)and (7<4)) or print((18==3)and (9>3))
print(True is False)
#print(False in 'False')
print((True==False) or (False>True)) and (False <= True)

#question 3

s1='Nice to have it'
s2=' here'
print(s1+s2)

#question 4
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])

#question 5
a.insert(0,s1)
a.append(s2)
print(a)

#question 6
Numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]

i=0
while(Numbers[i]!=412):
    if Numbers[i]%2==0:
        print(Numbers[i])
    i=i+1

#question 7
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
color_list_1-=color_list_2
print(color_list_1)

#question 8
#PANGRAM ?????

#question 9
a=eval(input('enter the number:'))
a1=str(a)*2
a2=str(a)*3
a3=int(a+int(a1)+int(a2))
print(a3)

#question 10
#question 11
print("Enter a string: ")
s=input().split(',')
print(s)
s.sort()
print(s)


#question 12
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]}
d1=d['Marks']
large=max(d['Marks'])
j=0
for i in range(len(d1)):
    if(d1[i]==large):
        j=i

d2=d['Student']
print(d2[j])


#question 13
#s='hello world! 123'
s=input("Enter a string:")
letter=0
digit=0
for i in s:
    if i.isalpha():
        letter=letter+1
    if i.isdigit():
        digit=digit+1
print("LETTERS ",letter)
print("DIGITS ",digit)
#question 14
#question 16

