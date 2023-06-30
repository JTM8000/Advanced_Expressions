# #advanced expressions:
# #for inline
# #for any
# #for sum
# #zip function = group dif list into only 1 list

# class Pizza:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
        
# pizzas = [
#     Pizza("Margaritta", 9.99),
#     Pizza("Hawaiian", 6.99),
#     Pizza("Pepperonii", 12.99),
#     Pizza("Meat", 9.99),
# ]

# #print names
# # pizzas_names = []

# # for pizza in pizzas:
# #     pizzas_names.append(pizza.name)
    
# # print(pizzas_names)

# #or

# pizzas_names = [i.name for i in pizzas
#                 #conditions
#                 #if len(i.name) < 5
#                 if i.price >= 10
#                 ]


# #print(pizzas_names)

    
# #any : return True if one item is True
# #any takes a collection and returns boolean
# # print(any([False,False,False]))

# # #if any in list is True, displays True
# # print(any([True, False, False]))

# #if expensive exist, display true

# expensive_pizza_exist = any([i.price > 10 for i in pizzas])
# #print(expensive_pizza_exist)

# #sum
# #print(sum[10, 5, 2])
# #take list of numbers and print sum

# #count how many expensive pizzas

# # expensive_pizza_count = sum([i.price > 10 for i in pizzas])
# #or
# expensive_pizza_count = sum([1 for i in pizzas if i.price > 10])

# print(expensive_pizza_count)

#-----zip function-------

pizza_names = ("cheese", "cal", "meat")
pizza_price = (10.5, 11, 9)

#group the lists

# (("cheese", 10.5), ("cal", 11),("meat", 9))

# =

# names_prices = zip(pizza_names, pizza_price)

#to numerate zip transform to list

names_prices = list(zip(pizza_names, pizza_price))

for (name, price) in names_prices:
    print(f"{name} : ${price}")


#to reverse process (shown in debugger)
#star splits name and prices into dif functions

unzipped = list(zip(*names_prices))

