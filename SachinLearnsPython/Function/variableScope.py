x=100
def show_scope():
    y=200
    print(f"Inside: {y} Outside: {x}")

def modify_global():
    global x
    x= 999
    print(f"Changed : {x}")

show_scope()
modify_global()
print(f"Outside: {x}")
