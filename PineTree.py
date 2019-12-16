n = input("How tall the tree has to be ? ")
n = int(n)
i = 1
h = 1
s = n-i
stump_space = s

while n != 0 :
    for i in range(s):
        print(" ", end="");
    for i in range(h):
        print("#", end="");
    print()
    s -= 1
    h += 2
    n -= 1

for i in range(stump_space):
     print(" ", end="")

print("#");