#Handling multiple exception types
def safeAccess(lst, index):
    try:
        value = lst[index]
        result = 100 / value
        print(f"Result: {result}")
    except IndexError:
        print(f"Index {index} is out of range!")
    except ZeroDivisionError:
        print("List has 0 at that index - can't divide!")
    except TypeError:
        print("List item is not a number!")
    except Exception as e:
        print(f"Unexpected error: {e}")

data = [10, 0, "hello", 5]

safeAccess(data, 0)    #works
safeAccess(data, 1)    #ZeroDivisionError
safeAccess(data, 2)    #TypeError
safeAccess(data, 10)   #IndexError
