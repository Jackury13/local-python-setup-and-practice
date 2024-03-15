print("Hello from inside the file!")

def hello():
    print("Hello from inside the function!")

def pack(arg_1, arg_2, arg_3 ):
    return[arg_1, arg_2, arg_3]


def eat_lunch(my_lunch):
    if len(my_lunch) == 0:
        print("My Lunch Box is Empty")
    for food_index in range(len(my_lunch)):
        if food_index == 0:
            print(f"First I eat {my_lunch[food_index]}")
        elif food_index < len(my_lunch) - 1:
            print(f"Then I eat {my_lunch[food_index]}")
        else:
            print("My lunch box is empty")

hello()

print (pack(1, 5, 10))
print (pack("a", "b", "c"))
            
eat_lunch([])
eat_lunch(["apple"])
eat_lunch(["apple", "banana", "hotdog", "cranberry sauce"])