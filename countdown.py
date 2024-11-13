# create a c countdown clock for 2hrs to 0
import time
stime = int(input(" enter the time : "))
for x in range( stime,0,-1):

    second= x % 60
    minute= int(x /60)%60
    hour = int (x /3600)

    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)
print(" times over")



# import time
# time.sleep(2)
# print(" time")

# based on user input it should count backwards

# my_time = int(input( "  enter the number "))
# for x in range(0 ,my_time):
#     time.sleep(1)
#     print(f"hello {x}")

# my_time = int(input( "  enter the number "))
# for x in reversed(range(0 ,10)):
#     time.sleep(1)
#     print(f" {x}")

# or


# for x in range(10 ,0,-1):
#     time.sleep(1)
#     print(f" {x}")
# print(" times up")

# print 0 - 10 in reverse order 3 times

