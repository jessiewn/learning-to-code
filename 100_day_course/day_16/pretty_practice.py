from prettytable import PrettyTable
table = PrettyTable()
print(table)
table.add_column("Pokemon Name",["Pikachu","Squiretle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

print(table.align)
table.align="l"
print(table)