x = 5  # Global variable


def local_scope():
    x = 10  # Local variable with the same name
    print(x)  # Output: 10 (Local variable is used)


local_scope()
print(x)  # Output: 5 (Global variable remains unchanged)
