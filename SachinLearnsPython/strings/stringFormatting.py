name = "Sachin"
score = 95.678
rank = 3

# f-string with format specifiers
print(f"Name: {name}")
print(f"Score: {score:.2f}")        # 2 decimal places
print(f"Score: {score:.0f}")        # no decimal
print(f"Rank: {rank:03d}")          # zero-padded to width 3

# alignment inside f-strings
print(f"{'Left':<10}|")             # left align in 10 chars
print(f"{'Right':>10}|")            # right align in 10 chars
print(f"{'Center':^10}|")           # center align in 10 chars

# .format() method
print("Hello, {}!".format(name))
print("Name: {0}, Score: {1:.2f}".format(name, score))
print("Name: {n}, Score: {s}".format(n=name, s=score))

# zfill - pad with zeros on the left
student_id = "42"
print(student_id.zfill(6))          # 000042

# ljust, rjust, center with fill character
print("Python".ljust(15, "-"))      # Python---------
print("Python".rjust(15, "-"))      # ---------Python
print("Python".center(15, "*"))     # ****Python*****

# % formatting (old style)
print("Name: %s, Score: %.2f" % (name, score))
