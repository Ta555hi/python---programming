my_city = "New York"
print(type(my_city))
#single quotes have exactly the same use as double quote

my_city = 'New York'
print(type(my_city))

#setting the variable type explicitly
my_city = str('New York')
print(type(my_city))

word1 = 'New '
word2 = 'York'
print(word1 + word2)

#how to select character 
word = "Rio de Janeiro"
char = word[4] #selects the value in the particular index, even space has index
print(char)

#how to replace part of string
word = word.replace('Rio', 'Mar')
print(word)

#how to count 
word = "Rio de Janeiro" 
print(word.count(" ")) #counts the numbers of occurance (cahracter)

#how to repeat a string
print(word * 3)

# how to split the string
word = "Rio de janerio"
split_word = word.split(' ') #to split string whenever there is white space
print(split_word)



