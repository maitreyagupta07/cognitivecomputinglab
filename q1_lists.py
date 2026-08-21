roll_no = "1024170404"
digits = [int(d) for d in roll_no]
L = [d * 10 for d in digits]

print("i. L =", L)

L.append(99)
print("ii. After append(99):", L)

L.insert(3, 55)
print("ii. After insert(55) at index 3:", L)

L.remove(40)
print("iii. After remove(40):", L)

popped = L.pop()
print(f"iii. After pop() removed {popped}:", L)

L.sort()
print("iv. Ascending sort:", L)

L.sort(reverse=True)
print("iv. Descending sort:", L)

print("v. First three:", L[:3])
print("v. Last three:", L[-3:])

avg = sum(L) / len(L)
above_avg = [x for x in L if x > avg]
print("vi. Average =", avg)
print("vi. Elements greater than average:", above_avg)
