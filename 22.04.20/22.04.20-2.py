a = int(input())
a = list(str(a))
a = sorted(a, reverse=True)
# a = reversed(sorted(a))
# a = a[::-1]
a = "".join(a)
print(a)