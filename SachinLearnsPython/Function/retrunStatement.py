#Retrun a singe value
def square(n):
    return n**2

#Return a single value
def min_max(nums):
    return min (nums), max(nums)

#Return ends the function immediately
def check_age(age):
    if age<0:
        return "Invalid"
    if age <18:
        return "Minor"
    return "Adult"

#Using the retrun
print(square(7))
lo, hi = min_max([4,1,9,2,7])
print(f"Min = {lo}, max={hi}")
print(check_age(25))