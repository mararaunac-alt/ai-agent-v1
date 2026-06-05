from functions.run_python_file import run_python_file

print(f"Result of running main.py:")
result = run_python_file("calculator", "main.py")
print(result)

print(f"Result of running main.py, with arguments:")
result = run_python_file("calculator", "main.py", ["3 + 5"])
print(result)

print(f"Result of running tests.py:")
result = run_python_file("calculator", "tests.py")
print(result)

print(f"Result of running ../main.py:")
result = run_python_file("calculator", "../main.py")
print(result)

print(f"Result of running nonexistent.py:")
result = run_python_file("calculator", "nonexistent.py")
print(result)

print(f"Result of running lorem.txt:")
result = run_python_file("calculator", "lorem.txt")
print(result)