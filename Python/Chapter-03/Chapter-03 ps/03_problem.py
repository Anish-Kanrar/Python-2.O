#write a program to detect double space in a string.
name = "Anish is good boy and"
name1 = "Anish is good  boy and"

print(name.find("  "))  #-1,here there are no double space
print(name1.find("  "))  #13,here there have double space
print(name.find("is")) #2