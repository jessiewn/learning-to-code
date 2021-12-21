from pathlib import Path

file_path = Path(__file__).resolve()
file_parent = file_path.parent
my_file = file_parent / "my_file.txt"
print("File path: ", file_path)
print("File parent: ", file_parent)
print("My file: ", my_file)

with my_file.open(mode="a") as file:
    file.write("shayan\n")

with open("../../../../Desktop/new_file.txt",mode="r") as file:
    contents=file.read()
    print(contents)
