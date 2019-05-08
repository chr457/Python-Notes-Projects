#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
#but returns the greater if one or both numbers are odd
# def lesserof(a,b):
#     if (a % 2 == 0 and b% 2 == 0):
#         return min((a,b))
#     else:
#         return max((a,b))
  
#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# def animalcrackers(text):
#     word = text.split()
#     return word[0][0] == word[1][0]

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# def MakesTwenty(a,b):
#     if ((a + b == 20) or a == 20 or b == 20):
#         return True
#     else:
#         return False

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# def capit(name):
#     if len(name) < 3:
#         return "Name is too short"
#     else:
#         return name[:3].capitalize() + name[3:].capitalize()
        
#MASTER YODA: Given a sentence, return a sentence with the words reversed        
# def yoda(text):
#     return ' '.join(text.split()[::-1])
# print(yoda("how are you today"))

#Part 2
# def volSphere(rad):
#     return (4.0/3)*(3.14)*(rad**3)
# print(volSphere(3))

# def printLetter(letter):
#     #only checks A-E
#     patterns = {1: '  *   ', 2: ' * * ', 3: '*   *', 4: '*****', 5: '**** ', 6: '   * ', 7: ' *    ', 8: '*   * ',
#     9: '*    '}
#     alphabet = {'A': [1,2,4,3,3], 'B': [5,3,5,3,5], 'C': [4,9,9,9,4], 'D': [5,3,3,3,5], 'E': [4,9,4,9,4]}
#     for pattern in alphabet[letter.upper()]:
#         print(patterns[pattern])
        
        
# printLetter('b')
















