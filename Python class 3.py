# 1. Print numbers from 1 to 50
for i in range(1, 51):
    print(i)

 # 2. Print even numbers from 1 to 100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# 3. Print odd numbers from 1 to 100
for i in range(1, 101):
    if i % 2 != 0:
        print(i)

# 5. Find sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i
print("Sum:", total)

# 6. Print numbers in reverse from 50 to 1
for i in range(50, 0, -1):
    print(i)

# 7. Count how many numbers are divisible by 3 (1–100)
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print("Count:", count)

# 8. Print squares of numbers from 1 to 10
for i in range(1, 11):
    print(i * i)

# 9. Print cube of first 10 numbers
for i in range(1, 11):
    print(i ** 3)

# 10. Take input n, print numbers from 1 to n
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(i)

# Section 2: While Loop (11–15)

# 11. Print numbers from 1 to 20 using while
i = 1
while i <= 20:
    print(i)
    i += 1

# 12. Find factorial of a number using while
num = int(input("Enter number: "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print("Factorial:", fact)

# 13. Reverse a number using while
num = int(input("Enter number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed:", rev)

# 14. Count digits in a number
num = int(input("Enter number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("Digits:", count)

# 15. Input until 'stop'
while True:
    val = input("Enter value (stop to end): ")
    if val == "stop":
        break

# Section 3: Nested Loop (16–20)
# =============================

# 16. Pattern *
for i in range(1, 5):
    print("*" * i)

# 17. Pattern numbers
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 18. Table 1 to 5
for i in range(1, 6):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

# 19. A B C pattern
for i in range(3):
    print("A B C")

# 20. 1 to 9 grid
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()

# =============================
# Section 4: String Basics (21–25)
# =============================

# 21. Count characters
s = input("Enter string: ")
print(len(s))

# 22. Count vowels
count = 0
for ch in s:
    if ch.lower() in 'aeiou':
        count += 1
print("Vowels:", count)

# 23. Count consonants
count = 0
for ch in s:
    if ch.isalpha() and ch.lower() not in 'aeiou':
        count += 1
print("Consonants:", count)

# 24. Reverse string
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

# 25. Palindrome
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# =============================
# Section 5: String Slicing (26–30)
# =============================

# 26. First 5 chars
print(s[:5])

# 27. Last 3 chars
print(s[-3:])

# 28. Reverse using slicing
print(s[::-1])

# 29. Every 2nd char
print(s[::2])

# 30. Remove first & last
print(s[1:-1])

# Section 6: List Basics (31–35)
# =============================

# 31. Sum of list
lst = [1, 2, 3, 4, 5]
print(sum(lst))

# 32. Max value
print(max(lst))

# 33. Min value
print(min(lst))

# 34. Count elements
print(len(lst))

# 35. Check element
x = int(input("Enter element: "))
if x in lst:
    print("Exists")
else:
    print("Not Exists")

# =============================
# Section 7: List Operations (36–40)
# =============================

# 36. Append elements
lst = []
lst.append(1)
lst.append(2)
lst.append(3)
print(lst)

# 37. Insert element
lst.insert(1, 99)
print(lst)

# 38. Remove element
lst.remove(2)
print(lst)

# 39. Reverse without reverse()
rev_lst = []
for i in lst:
    rev_lst = [i] + rev_lst
print(rev_lst)

# 40. Sort without sort()
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)