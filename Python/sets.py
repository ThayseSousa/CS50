s = set()

# numbers in the set are always particulars, so they don't repeat
# so, if I add to the set a number one time and other time, python will show you just one time
s.add(1)
s.add(2)
s.add(5)
s.add(2)
print(s)