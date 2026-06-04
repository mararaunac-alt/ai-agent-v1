from functions.get_files_info import get_files_info

print(f"Result for current directory:")
result = get_files_info("calculator", ".")
for line in result.splitlines():
    print(f"  {line}")

print(f"Result for 'pkg' directory:")
result = get_files_info("calculator", "pkg")
for line in result.splitlines():
    print(f"  {line}")

print(f"Result for '/bin' directory:")
result = get_files_info("calculator", "/bin")
for line in result.splitlines():
    print(f"  {line}")

print(f"Result for '../' directory:")
result = get_files_info("calculator", "../")
for line in result.splitlines():
    print(f"  {line}")
