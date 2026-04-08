# 🐍 Python Basics 

## 1. Variables
Variables store data values dynamically.

```
user_name = "Nabeel"
login_attempts = 3
is_logged_in = False

print(f"User: {user_name}")
print(f"Attempts: {login_attempts}")
print(f"Logged In: {is_logged_in}")
```

```
Output:
User: Nabeel
Attempts: 3
Logged In: False
```

---

## 2. type()
Used to check the data type of a variable.

```
data = {"user": "admin", "active": True}

print(type(data))
print(type(data["user"]))
print(type(data["active"]))
```

```
Output:
<class 'dict'>
<class 'str'>
<class 'bool'>
```

---

## 3. Data Types
Common types include int, float, str, list, tuple, dict, bool.

```
response = {
    "status": 200,
    "message": "Success",
    "data": ["item1", "item2"],
    "is_valid": True
}

print(response)
```

```
Output:
{'status': 200, 'message': 'Success', 'data': ['item1', 'item2'], 'is_valid': True}
```

---

## 4. Numbers
Used for calculations.

```
price = 499.99
quantity = 2

total = price * quantity
print(f"Total Bill: {total}")
```

```
Output:
Total Bill: 999.98
```

---

## 5. Operators
Includes arithmetic, comparison, logical, assignment, identity, membership.

```
age = 25
has_id = True

if age >= 18 and has_id:
    print("Access Granted")
else:
    print("Access Denied")
```

```
Output:
Access Granted
```

---

## 6. if-else
Executes code based on condition.

```
balance = 1000
withdraw = 1200

if withdraw <= balance:
    print("Transaction Successful")
else:
    print("Insufficient Balance")
```

```
Output:
Insufficient Balance
```

---

## 7. Multiple if-elif-else
Handles multiple conditions.

```
marks = 85

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print(f"Grade: {grade}")
```

```
Output:
Grade: B
```

---

## 8. For Loop with range()
Used to iterate fixed number of times.

```
for i in range(1, 6):
    print(f"Processing record {i}")
```

```
Output:
Processing record 1
Processing record 2
Processing record 3
Processing record 4
Processing record 5
```

---

## 9. For Loop in String

```
username = "admin"

for char in username:
    print(f"Character: {char}")
```

```
Output:
Character: a
Character: d
Character: m
Character: i
Character: n
```

---

## 10. While Loop

```
count = 1

while count <= 3:
    print(f"Retry attempt {count}")
    count += 1
```

```
Output:
Retry attempt 1
Retry attempt 2
Retry attempt 3
```

---

## 11. Nested Loops

```
for i in range(1, 3):
    for j in range(1, 3):
        print(f"i={i}, j={j}")
```

```
Output:
i=1, j=1
i=1, j=2
i=2, j=1
i=2, j=2
```

---

## 12. User Input

```
name = input("Enter your name: ")
print(f"Welcome {name}")
```

```
Output:
Enter your name: Nabeel
Welcome Nabeel
```

---

## 13. Converters

```
age = input("Enter age: ")
age = int(age)

print(f"Next year age: {age + 1}")
```

```
Output:
Enter age: 25
Next year age: 26
```

---

## 14. Functions Concept

```
def greet():
    print("Welcome to the system")

greet()
```

```
Output:
Welcome to the system
```

---

## 15. Functions with Parameters

```
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(100, 5)
print(f"Total: {total}")
```

```
Output:
Total: 500
```

---

## 16. Functions with User Input

```
def greet_user():
    name = input("Enter name: ")
    print(f"Hello {name}")

greet_user()
```

```
Output:
Enter name: Nabeel
Hello Nabeel
```

---

## 17. Converter using Function

```
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

result = celsius_to_fahrenheit(30)
print(result)
```

```
Output:
86.0
```

---

## 18. Modifying Function

```
def update_balance(balance, deposit):
    balance += deposit
    return balance

new_balance = update_balance(1000, 500)
print(new_balance)
```

```
Output:
1500
```

---

## 19. Methods

```
email = "USER@GMAIL.COM"

formatted_email = email.lower()
print(formatted_email)
```

```
Output:
user@gmail.com
```

---
