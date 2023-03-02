N = input()
length = len(N)
a = 0
b = 0 

for i in range(length//2):
    a += int(N[i])
for j in range(length//2, length):
    b += int(N[j])
    
if a == b :
    print("LUCKY")
else:
    print("READY")