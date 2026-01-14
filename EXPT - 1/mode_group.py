class_lower = []
class_higher = []
freq = []
n = int(input("Enter the number of classes: "))
for i in range(n):
    a = int(input(f"Enter Lower limit of class {i+1}: "))
    b = int(input(f"Enter higher limit of class {i+1}: "))
    c = int(input(f"Enter the freq of class {i+1}: "))
    class_lower.append(a)
    class_higher.append(b)
    freq.append(c)
modal_class_index = freq.index(max(freq))
L = class_lower[modal_class_index]
f1 = freq[modal_class_index]
f0 = 0
if modal_class_index > 0:
    f0 = freq[modal_class_index - 1]
f2 = 0
if modal_class_index < n - 1:
    f2 = freq[modal_class_index + 1]
h = class_higher[modal_class_index] - class_lower[modal_class_index]
mode = L + (f1 - f0) / (2 * f1 - f0 - f2) * h
print("Mode of the given data is: ", mode)