def div_by(x,y):
# figure out how to check for a valid integer input first and error out otherwise...
#    if:      
#        x 
#    else:
        if x % y == 0:
            print x, "is divisble by", y
            print x, " / ", y, " = ", x / y
        else:
            print x, "is not divisible by", y
            print "The remainder of ", x, " / ", y, " = ", x % y

# def compute_div(x,y):
#    print x, " / ",  y, " = ", x / y

x_value = float(raw_input("Enter a number: "))

y_value = float(raw_input("Enter another number: "))

div_by(x_value,y_value)

# compute_div(x_value,y_value)
