import datetime

def time_based_greeting(func):
    hour = datetime.datetime.now().hour
    if 12 <= hour < 22:
        func("Hello","all..!","Whats","Up")
        print("\nHope You are doing Good")

# Message() Is Passed as a Function to timed_greeting() automatically or internally
# time_based_greeting is a decorator for greeting()
@time_based_greeting
def Message(*args):
    for arg in args:
        print(f"{arg}", end=" ")

print(datetime.datetime.now().hour)