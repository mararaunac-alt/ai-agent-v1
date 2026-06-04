from functions.get_file_content import get_file_content

print(f"Result for 'lorem.txt':")
result =get_file_content("calculator", "lorem.txt")
print(f"lorem.txt truncated: {'truncated' in result}")

print(f"Result for 'main.py':")
result = get_file_content("calculator", "main.py")
print(result)

print(f"Result for 'pkg/calculator.py':")
result = get_file_content("calculator", "pkg/calculator.py")
print(result)

print(f"Result for '/bin/cat':")
result = get_file_content("calculator", "/bin/cat")
print(result)

print(f"Result for 'pkg/does_not_exist.py':")
result = get_file_content("calculator", "pkg/does_not_exist.py")
print(result)

