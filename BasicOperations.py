# Testing simple Hello world
print("Hello World")

# Arithmatic operators

# 01.the addition, subtraction, multiplication, and division operators can be used with numbers.
print("\nthe addition, subtraction, multiplication, and division operators can be used with numbers.")
number = 1+2*3/4
print("number = 1+2*3/4 == ",      number)

# 02. the modulo (%) operator,
# which returns the integer remainder of the division. dividend % divisor = remainder.
print("\nthe modulo (%) operator returns the integer remainder of the division")
remainder = 11 % 3
print("remainder = 11%3 == ", remainder)

# 03. two multiplication symbols makes a power relationship
print("\ntwo multiplication symbols makes a power relationship")
squared = 7**2
cubed = 2**3
print(squared, cubed)


# using operators with strings
print("\n*****Using operators with strings*****")

# 01. concatenating strings using the addition operator:
print("01.concatenating strings using the addition operator:")
helloworld = "hello"+" "+"World"
print(helloworld)

# 02. multiplying strings to form a string with a repeating sequence::
print("\n02.multiplying strings to form a string with a repeating sequence:")
lotsofhi = "hi"*10
print(lotsofhi)


# using operators with list
print("\n*****Using operators with list*****")

# 01. Lists can be joined with the addition operators::
print("01.Lists can be joined with the addition operators:")
evennum = [2, 4, 6, 8]
oddnum=[1, 3, 5, 7]
allnum=oddnum + evennum
print(allnum)

# 02. forming new lists with a repeating sequence using the multiplication operator:
print("\n02.forming new lists with a repeating sequence using the multiplication operator:")
print([1, 2, 3]*3)
