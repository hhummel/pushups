def print_name(prefix):
    print(f"Prefix is set to {prefix}")
    while True:
        name = (yield)
        if prefix in name:
            print(name)

def polynomial(a: int, b: int, c: int) -> int:
    print(f"Evaluate {a}x**2 + {b}x + {c}")
    while True:
        x = (yield)
        print(a * x**2 + b * x + c)

if __name__ == "__main__":
    coroutine = print_name("Dear")
    next(coroutine)
    #coroutine.__next__()
    coroutine.send("Harry")
    coroutine.send("Dear Harry")
    coroutine.close()
