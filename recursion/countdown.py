# Use Recursion to implement a countdown counter

def countdown(num: int) -> int:
    if num == 0:
        print("Done!")
        return
    else:
        print(num ,"...")
        countdown(num - 1)
    

countdown(2)