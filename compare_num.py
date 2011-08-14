# define the function
def num_test(x,y):
    if x < y:
        print x, "is less than", y
    elif x > y:
        print x, "is greater than", y
    else:
        print x, "and", y, "are equal"

# get input from user
boo = int(raw_input("Enter a number :"))

bee = int(raw_input("Enter another number: "))

# run function
num_test(boo,bee)
