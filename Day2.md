# 📂 Python File Handling & String Methods 

## 1. Opening a File
Used to open a file for reading or writing in applications like logging, configs, or data processing.

```
file = open("app.log", "r")
content = file.read()
file.close()

print(content)
```

```
Output:
[INFO] Application started
[INFO] User logged in
```

---

## 2. File Modes (With WHY)

- r → Read only (used when you only need to fetch data, safe from accidental overwrite)  
- w → Write (used when resetting logs/configs; deletes old content)  
- a → Append (used in logging systems to preserve history)  
- r+ → Read + Write (used when you want to modify existing file without deleting content)  
- w+ → Write + Read (used when recreating file and then reading it immediately)  
- a+ → Append + Read (used in monitoring/logging systems where you both log and read)  
- x → Create new file (used when file must not already exist, like secure file creation)

---

## 3. Writing to a File (w)
WHY: Used when you want a fresh file (e.g., regenerate reports/logs).

```
with open("app.log", "w") as file:
    file.write("Application Initialized\n")
    file.write("Server Started\n")

print("Write Successful")
```

```
Output:
Write Successful
```

---

## 4. Appending to a File (a)
WHY: Used in real systems to keep adding logs without losing history.

```
with open("app.log", "a") as file:
    file.write("New User Registered\n")

print("Append Successful")
```

```
Output:
Append Successful
```

---

## 5. Read + Write Mode (r+)
WHY: Used when you need to read existing data and update it (e.g., audit logs).

```
with open("app.log", "r+") as file:
    content = file.read()
    file.write("Audit Log Added\n")

print(content)
```

```
Output:
Application Initialized
Server Started
New User Registered
```

---

## 6. Write + Read Mode (w+)
WHY: Used when you want to recreate file and then verify/read content immediately.

```
with open("temp.log", "w+") as file:
    file.write("Temporary Log\n")
    file.seek(0)
    print(file.read())
```

```
Output:
Temporary Log
```

---

## 7. Append + Read Mode (a+)
WHY: Used in monitoring systems where logs are written and analyzed in real-time.

```
with open("app.log", "a+") as file:
    file.write("System Health OK\n")
    file.seek(0)
    print(file.read())
```

```
Output:
Application Initialized
Server Started
New User Registered
System Health OK
```

---

## 8. Exclusive Creation Mode (x)
WHY: Used when file must be created only once (e.g., unique report or secure file).

```
try:
    with open("new_file.txt", "x") as file:
        file.write("File created successfully")
    print("File Created")
except FileExistsError:
    print("File already exists")
```

```
Output:
File Created
```

---

## 9. Operations on Files
WHY: Used to control how much data is read (important in large files).

```
with open("app.log", "r") as file:
    print(file.read(20))
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
```

```
Output:
Application Initiali
Application Initialized

['Application Initialized\n', 'Server Started\n', ...]
```

---

# 🔤 String Methods (When & WHY Used)

## 10. .upper() and .lower()
WHY: Used for normalization (e.g., emails, usernames).

```
email = "User@Company.com"

print(email.upper())
print(email.lower())
```

```
Output:
USER@COMPANY.COM
user@company.com
```

---

## 11. .find() and .index()
WHY: Used to locate substrings (e.g., parsing logs, validation).

```
text = "error: invalid request"

print(text.find("invalid"))
print(text.index("error"))
```

```
Output:
7
0
```

---

## 12. .count()
WHY: Used in analytics/log monitoring (count occurrences).

```
logs = "error error warning info error"

print(logs.count("error"))
```

```
Output:
3
```

---

## 13. .replace()
WHY: Used for data cleaning and transformation.

```
message = "Server is down"

updated = message.replace("down", "running")
print(updated)
```

```
Output:
Server is running
```

---

## 14. .split()
WHY: Used to parse CSV/API/string data into lists.

```
data = "user1,user2,user3"

users = data.split(",")
print(users)
```

```
Output:
['user1', 'user2', 'user3']
```

---

## 15. .strip(), .lstrip(), .rstrip()
WHY: Used to clean unwanted spaces from user input or files.

```
raw = "   admin   "

print(raw.strip())
print(raw.lstrip())
print(raw.rstrip())
```

```
Output:
admin
admin   
   admin
```

---

## 16. .startswith() and .endswith()
WHY: Used in validations (file types, prefixes, URLs).

```
filename = "report.pdf"

print(filename.startswith("report"))
print(filename.endswith(".pdf"))
```

```
Output:
True
True
```

---

## 17. .join()
WHY: Used to combine list into string (e.g., logs, messages).

```
words = ["DevOps", "is", "awesome"]

sentence = " ".join(words)
print(sentence)
```

```
Output:
DevOps is awesome
```

---

## 18. .isdigit() and .isalpha()
WHY: Used for input validation.

```
value = "12345"
name = "Nabeel"

print(value.isdigit())
print(name.isalpha())
```

```
Output:
True
True
```

---

## 19. .capitalize() and .title()
WHY: Used for formatting display text.

```
text = "hello world"

print(text.capitalize())
print(text.title())
```

```
Output:
Hello world
Hello World
```

---
