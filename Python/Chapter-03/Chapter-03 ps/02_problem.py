letter = '''Dear <|Name|>,
You are selected! 
<|Date|>'''

print(letter.replace("<|Name|>","Harray").replace("<Date>","24 September 2050"))
#here we do chaining