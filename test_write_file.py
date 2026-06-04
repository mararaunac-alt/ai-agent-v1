from functions.write_file import write_file

print(f"Result for writing to 'lorem.txt':")
result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(result)

print(f"Result for writing to 'pkg/morelorem.txt':")
result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(result)

print(f"Result for writing to '/tmp/temp.txt':")
result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(result)
