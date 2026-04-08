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

# 🔍 Python Membership Operators

## 1. Membership Operators (in, not in)
Used to check whether a value exists in a sequence (list, string, tuple, set, dict).

- in → Returns True if value exists  
- not in → Returns True if value does NOT exist  

WHY: Widely used in validation, access control, filtering, and searching data.

---

## 2. Membership in List
WHY: Used in applications like role validation, allowed users, feature flags.

```
allowed_roles = ["admin", "devops", "user"]

current_role = "devops"

if current_role in allowed_roles:
    print("Access Granted")
else:
    print("Access Denied")
```

```
Output:
Access Granted
```

---

## 3. Membership in String
WHY: Used in search, log parsing, and keyword detection.

```
log_message = "ERROR: Database connection failed"

if "ERROR" in log_message:
    print("Trigger Alert")
```

```
Output:
Trigger Alert
```

---

## 4. Membership in Dictionary (Keys)
WHY: Used to check if a key exists before accessing it (prevents errors).

```
user = {
    "name": "Nabeel",
    "role": "admin"
}

if "role" in user:
    print(f"Role: {user['role']}")
```

```
Output:
Role: admin
```

---

## 5. Membership in Dictionary Values
WHY: Used when validating values in config/data.

```
status_codes = {
    200: "OK",
    404: "Not Found"
}

if "OK" in status_codes.values():
    print("Valid Status Present")
```

```
Output:
Valid Status Present
```

---

## 6. Using not in
WHY: Used for blocking invalid inputs or enforcing restrictions.

```
blocked_users = ["spam_user", "bot123"]

username = "guest_user"

if username not in blocked_users:
    print("User Allowed")
else:
    print("User Blocked")
```

```
Output:
User Allowed
```

---

## 7. Membership with Loop (Filtering Data)
WHY: Used in real-world apps for filtering datasets.

```
users = ["admin", "test_user", "guest"]
blocked = ["test_user"]

for user in users:
    if user not in blocked:
        print(f"Processing {user}")
```

```
Output:
Processing admin
Processing guest
```

---

## 8. Membership in Set (Fast Lookup)
WHY: Sets provide faster lookup (used in high-performance systems).

```
allowed_ips = {"192.168.1.1", "10.0.0.1"}

ip = "10.0.0.1"

if ip in allowed_ips:
    print("IP Allowed")
```

```
Output:
IP Allowed
```

---
