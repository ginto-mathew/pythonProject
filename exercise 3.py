# use different methods to print "Hello Ginto, your balance is 50" from Name and balance variables.

# 1
print("Hello {}, your balance is {}.".format("Ginto", 50))

# 2
print("Hello {0}, your balance is {1}.".format("Ginto", 50))

# 3
print('Hello {name}, your balance is {amount}.'.format(name="Ginto", amount=50))

# 4
print("Hello {}, your balance is {amount}.".format("Ginto", amount=50))

# 5 using f string
name5="Ginto"
amount5=50
print(f'Hello {name5}, your balance is {amount5}.')
