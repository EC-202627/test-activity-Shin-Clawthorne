# X ml of water today. Determine if the client followed the doctor's advice or not.
# Input Format

# The first line contains a single integer 
# T — the number of test cases. Then the test cases follow.
# The first and only line of each test case contains one integer 
# X — the amount of water client drank today.##
 
t = int(input())
for i in range(t):
    x = int(input())
    if x >= 2000 and x < 10000:
        print(f"Yes")
    elif x >= 10000:
        print(f"It's too much")
    else:
        print(f"No")
