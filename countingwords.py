cw = input ("enter your introduction")
wordcount = 1
character = 0
for Z in cw:
    character=character+1
    if(Z==' '):
        wordcount=wordcount+1

print("No Of Words In A Sting")
print(wordcount)
print("No Of Characters")
print(character)