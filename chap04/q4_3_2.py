numbers = [1, 2, 3, 4]
def func_hint(*args):
    print("args:",args)
    print("len(args):",len(args))

func_hint(*numbers)

many_numbers = list(range(100))
print(many_numbers)
