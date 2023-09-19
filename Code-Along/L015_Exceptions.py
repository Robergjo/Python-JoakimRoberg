def input_int(prompt):
    while True: 
        try: 
            my_int = int(input(prompt))
        except ValueError: 
            print("my_int is not an integer.")
        else:
            return my_int

age = input_int("input age: ")
length = input_int("input length: ")
weight = input_int("input weight: ")
print(f"age = {age}, lenght = {length}, weight = {weight}")