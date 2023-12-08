import random

end = False
word_list=["samruddhi","siddhi","ncc","gun","india","chimni","sangola","home","dog","cat","dinner","biscuit","food","table","medal","gold"]
word=random.choice(word_list)
#print("\n     ",word,"\n")
count=0
ans=[]
lives=0
for _i in range(len(word)) : 
  ans+="-"
man= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
while not end:
       print("-----------------------------------------------")
       guess=input("\n Guess the Letter:  ").lower()
       print("\n")
       count=0
       for i in range(len(word)) : 
           if guess==word[i]:
            ans[i]=guess
            print(ans)
           else:  
            count+=1
       if count==len(word):
          print(" Wrong\n")
          print(ans)
          lives+=1
          print(man[lives-1])
       if "-" not in ans:
           end = True
           print("\n----------- you Win!*> Add more words -------------")
       if lives==7:
           print("----------------You lose!! Try again -------------------")
           print(" \n    Correct word is ", word)
           end=True
      
