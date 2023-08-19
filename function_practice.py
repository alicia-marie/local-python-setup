def hello():
    print("Greetings, python user!")

def pack(param1, param2, param3):
    print([param1, param2, param3])
    return [param1, param2, param3]

def eat_lunch(list_input):
    if len(list_input) == 0:
        print("My lunchbox is empty")
    elif len(list_input) ==1:
        print("First I eat", list_input[0])
    else:
        print("First I eat", list_input[0])
        for item in list_input[1:]:
            print("Next I eat", item)


hello()
pack("sandwiches","hot dogs","pretzels")
eat_lunch([])
eat_lunch(["sandwiches"])
eat_lunch(["sandwiches","hot dogs","pretzels"])