file = open("C:/Users/user/Music/new.txt", "r")
count = 0
for line in file:
	words = line.split(" ")
	count += len(words)
file = open("C:/Users/user/Music/new.txt","r")
content=file.read()
print("PRINTING LINE WORDS : ")
print(content)
print("=========================")

print("Number of words in a Text File", count)
print("=========================")

str1 = input("Enter your own String : ")
total = 1
for i in range(len(str1)):
    if(str1[i] == ' ' or str1 == '\n' or str1 =='\t'):
        total = total + 1
print("Total Number of words in this string = ", total)
file.close()
