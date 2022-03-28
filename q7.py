import humps

myString="PythonProgram"
print("my string is", myString)

print("UPPERCASE is ",myString.upper())

print("lowercase is ",myString.lower())

print("PascalCase is ",humps.pascalize(myString))

print("camelCase is ",humps.camelize(myString))

print("SnakeCase is ",humps.decamelize(myString))


