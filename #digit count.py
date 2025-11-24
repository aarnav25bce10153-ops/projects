n = int(input("Enter the number you want to be printed: "))
l = []
og = []
for i in range(1, n + 1):
    digits = [int(d) for d in str(i)]
    l.extend(digits)
    og.extend([i] * len(digits))
if l and og:
    l.pop()
    og.pop()
print("Digit list:", l)
i = int(input("Enter index for whose original number you want to be printed : "))
i -= 1
if 0 <= i < len(og):
    print("Number:", og[i])
else:
    print("Invalid")
