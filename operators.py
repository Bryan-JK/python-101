'''
Write a simple script that demonstrate your understanding of Operators,operands and operator precedence
'''
#OPERATORS
a = 40
b = 10
print(a+b)
#substraction
print(a-b)
#multiplication
print(a*b)
#division 
print(a/b)
#the % means modulus in which it extraxts and displays the reminder after division
print(a%b)
#exponentation
print(a**b)
#floor division
c= 23
d= 2 
print(c//d)

#operand - is the value that operations are done onto it 

#comparison operators 
# ==  if two operands  are equal it then prints true 
e = 'fish'
f = 'fish'
print(e==f)
# != if operands  are not equal prints true which is the opposite of ==
print(e!=f)
#<> if operands are not equal prints true which is the opposite of == and similar to !=

#> prints true when the left operand is greater than the right operand 
print(a>b)
# < prints true if the right operand is greater than the left operand 
print(b<a)
 # >= prints true when the left operand is greater than or equal to the right operand
print(a>=b)
 # <= prints true if the right operand is greater than  or equal tothe left operand 
print(b<=a)

# Python Assignment Operators 
k = 20
y = 10

# '=' assigns values of k and y to z 
z = k + y 
print(z)

# Add AND opreator (+=) adds the left Operand 'k' and right operand 'y' and assigns them to the left operand k
k +=y
print(k)

#Substruct AND opreator (-=) substructs the left Operand 'k' and right operand 'y' and assigns them to the left operand k
k = 20
y=10
k-=y
print(k)

# multiply AND opreator (*=) Multiplies  the left Operand 'k' and right operand 'y' and assigns them to the left operand k
k = 20
y=10
k*=y
print(k)

# division AND opreator (/=) Multiplies  the left Operand 'k' and right operand 'y' and assigns them to the left operand k
k = 20
y=10
k/=y
print(k)

#modulus AND operator (%=) divides and takes the reminder of the left operand and the right operand  and assigns them to the left operand
k = 20
y=10
k%=y
print(k)

# exponent AND powers  the left Operand 'k' and right operand 'y' and assigns them to the left operand k
k = 20
y=10
k**=y
print(k)

#floor division AND It performs floor division on operators and assign value to the left operand
k = 20
y=10
k//=y
print(k)

# bitwise Operators 
# AND "&" operator copies and displays if the bit is 1 in both operands 
x = 60
z = 13
g = 0
print(x & z)

# OR'|' operator dispalys if bit if it is 1 in either operands 
x = 60
z = 13
g = 0
print(x | z)

# XOR '^' operator displays the opposite of one operand 
x = 60
z = 13
g = 0
print(x ^ z)

# binary left shift '<<' adds specific number of bits on the right side of the left operand 
print(x << 2)

# binary right sift '>>' adds specific number of bits on the left side of the left operand 
print(x>>2)




















