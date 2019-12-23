# aab  aba  abba df
test = "abdasfdafeac"

a = list(test)

la = list(range(26))

for i in range(26):
    la[i] = 0
for i in range(0, len(a)):
    la[ord(a[i]) - 97] = la[ord(a[i]) - 97] + 1

Re = max(la)
print(2)
