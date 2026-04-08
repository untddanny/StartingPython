# 🧠 Python Practice Problems – Skill Test

## 1. Sum of All Digits
Get sum of digits from a number (common in data validation & parsing).

```
number = 12345

total = 0

for digit in str(number):
    total += int(digit)

print(total)
```

```
Output:
15
```

---

## 2. Reverse an Array
Used in data processing and transformations.

```
arr = [1, 2, 3, 4, 5]

reversed_arr = []

for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])

print(reversed_arr)
```

```
Output:
[5, 4, 3, 2, 1]
```

---

## 3. Highest Number from List
Used in analytics and reporting.

```
numbers = [10, 45, 67, 23, 89, 12]

max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print(max_num)
```

```
Output:
89
```

---

## 4. Highest Number from String
Used when parsing numeric data from APIs/logs.

```
data = "10,45,67,23,89,12"

numbers = data.split(",")

max_num = int(numbers[0])

for num in numbers:
    if int(num) > max_num:
        max_num = int(num)

print(max_num)
```

```
Output:
89
```

---

## 5. Count Vowels in String
Used in text processing.

```
text = "devops engineer"

vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(count)
```

```
Output:
7
```

---

## 6. Check Palindrome
Used in validation and pattern matching.

```
text = "madam"

is_palindrome = True

for i in range(len(text) // 2):
    if text[i] != text[-i - 1]:
        is_palindrome = False
        break

print(is_palindrome)
```

```
Output:
True
```

---

## 7. Find Duplicate Elements
Used in data cleaning.

```
data = [1, 2, 3, 2, 4, 1, 5]

duplicates = []

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] == data[j] and data[i] not in duplicates:
            duplicates.append(data[i])

print(duplicates)
```

```
Output:
[2, 1]
```

---

## 8. Count Words in Sentence
Used in NLP and logging systems.

```
sentence = "python is easy to learn"

words = sentence.split(" ")

count = 0

for word in words:
    count += 1

print(count)
```

```
Output:
5
```

---

## 9. Find Second Largest Number
Common interview question.

```
numbers = [10, 45, 67, 23, 89, 12]

largest = second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print(second)
```

```
Output:
67
```

---

## 10. Remove Duplicates from List
Used in data preprocessing.

```
data = [1, 2, 2, 3, 4, 4, 5]

unique = []

for item in data:
    if item not in unique:
        unique.append(item)

print(unique)
```

```
Output:
[1, 2, 3, 4, 5]
```

---

## 11. Frequency Count of Elements
Used in analytics/log processing.

```
data = ["a", "b", "a", "c", "b", "a"]

freq = {}

for item in data:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print(freq)
```

```
Output:
{'a': 3, 'b': 2, 'c': 1}
```

---

## 12. Check Prime Number
Used in algorithmic problems.

```
num = 29

is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

print(is_prime)
```

```
Output:
True
```

---

## 13. Factorial of Number
Used in math computations.

```
num = 5

fact = 1

for i in range(1, num + 1):
    fact *= i

print(fact)
```

```
Output:
120
```

---

## 14. Fibonacci Series
Used in recursion & sequence problems.

```
n = 5

a, b = 0, 1

for i in range(n):
    print(a)
    a, b = b, a + b
```

```
Output:
0
1
1
2
3
```

---

## 15. Find Common Elements Between Two Lists
Used in data comparison.

```
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = []

for item in list1:
    if item in list2:
        common.append(item)

print(common)
```

```
Output:
[3, 4]
```

---
