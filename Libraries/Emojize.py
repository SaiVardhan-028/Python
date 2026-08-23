import emoji

text = input("Input: ")

print(emoji.__version__); 
result = emoji.emojize(text, language="alias")
print("Output:", result)

#Colon's should add before and after input
