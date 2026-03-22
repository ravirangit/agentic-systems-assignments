items = ['Hello','','World','!']
    
print(items[-3:-1])
print(items[-3:])
print(items[-4:-1])

for item in items:
    if 'hello' in item.lower():
        print(item)
    else:
        print("Not found")

print(10 % 3)

#  % => it will give you the remainder of the division operation. For example, 10 % 3 will give you 1, because when you divide 10 by 3, the quotient is 3 with a remainder of 1.
# // => it will give you the quotient of the division operation, discarding any remainder. For example, 10 // 3 will give you 3, because when you divide 10 by 3, the quotient is 3 and the remainder is discarded.
# ** => it is the exponentiation operator, which raises the left operand to the power of the right operand. For example, 2 ** 3 will give you 8, because 2 raised to the power of 3 is 8.

print(2 ** 3)
print(3 ** 2)
print('Hello' * 3)