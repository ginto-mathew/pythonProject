#List Manipulation exercise 2

# using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list

# 2. Remove "Blueberries" from the list.

# 3. Put "Kiwi" at the end of the list.

# 4. Add "Apples" at the beginning of the list

# 5. Count how many apples in the basket

# 6. empty the basket

#Answers
# #1
# basket.remove("Banana")
# basket.pop(0)
# #2
# basket.pop()
# #3
# basket.append("Kiwi")
# #4
basket.insert(0, "Apples")
# #5
print(basket.count("Apples"))
# #6
basket.clear()
print(basket)
