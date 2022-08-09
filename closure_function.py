# def outer_function():
#     test = 10
#
#     def inner_function(test=test):
#         test += 10
#         print(test)
#
#     return inner_function
#
# ifn = outer_function()
# ifn()

# Python program to illustrate
# nested functions
def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()