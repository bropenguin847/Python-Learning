# def avgWeight(getUser):
#     avg = getUser.sum() / len(getUser)
#     return avg

# myWeight = np.array([0,0,0,0,0,0])
# for i in range(0,5):
#     myWeight[i] = input(f"Insert {i+1} weight here: ")
# # avg = myWeight.sum() / len(myWeight)
# avg = avgWeight(myWeight)
# print(f"The average weight of the class is {avg:.2f} kg")

# #######################
# drink = input("what coffee you want?:")
# sugar = input("Do you want sugar with that?:")
# cups = int(input("how many cups you want?:"))

# for i in cups:
#     print(f"Pouring {drink} into a cup")
#     if drink == "coffee":
#         print("Pouring milk into cup")

# def main():
#     while True:
#         coffee = ask_coffee_type()
#         add_sugar = ask_sugar()
#         n = ask_cups_num()

#         for step in range(n):
#             print(f"\n{coffee.capitalize()} is poured in a cup.")

#             if need_milk(coffee):
#                 print(f"Milk is added to {coffee}.")

#             if add_sugar:
#                 print(f"Sugar is added to {coffee}.")

#             print("Output coffee to user.\n")

#         print("All coffee cups are outputted.\n")

#         if ask_order():
#             continue
#         else:
#             print("Stop making coffee.")
#             break


# def ask_coffee_type():
#     while True:
#         coffee_available = ["latte", "cappuccino", "black coffee"]
#         coffee_type = input("\nThe coffee available are latte, cappuccino and black coffee."
#                             "\nEnter a coffee: ").lower().strip()
#         if coffee_type in coffee_available:
#             return coffee_type
#         else:
#             print("This coffee is not available.\n")


# def ask_sugar():
#     while True:
#         sugar_or_not = input("Add sugar? (Yes/No) : ").lower().strip()
#         if sugar_or_not == "yes":
#             return True
#         elif sugar_or_not == "no":
#             return False
#         else:
#             print("Invalid input. Please enter yes or no.\n")


# def ask_cups_num():
#     while True:
#         try:
#             cups_num = int(input("Number of cups: "))
#             return cups_num
#         except ValueError:
#             print("Invalid input. Please enter a number.\n")


# def need_milk(coffee_type):
#     if coffee_type in ["cappuccino", "latte"]:
#         return True
#     else:
#         return False


# def ask_order():
#     while True:
#         ans = input("Order again? (Yes/No) : ").lower().strip()
#         if ans == "yes":
#             return True
#         elif ans == "no":
#             return False
#         else:
#             print("Invalid input. Please enter yes or no.")


# if _name_ == "_main_":
#     main()