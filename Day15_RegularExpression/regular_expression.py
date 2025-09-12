#Regular Expressions
#A regular expression or RegEx is a special text string that helps to find patterns in data.
# To use RegEx in python first we should import the RegEx module which is called re.

'''
The re Module: After importing the module we can use it to detect or find patterns.
import re
Methods in re Module:
To find a pattern we use different set of re character sets that allows to search for a match in a string.

re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string
'''

#Match

import re

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)  #re.I (or re.IGNORE CASE)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>

#no match

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None

#Search

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>

#findall()

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']

#re.sub
#Replacing a Substring

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

#re.split

txt = '''I am teacher and  I love teaching. There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs. Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # splitting using \n - end of line symbol

#Writing RegEx Patterns

import re

regex_pattern = r'apple'  #The r before the string tells Python not to treat backslashes \ as escape characters.
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple'] #case-sensitive by default that's why print only apple

# To make case-insensitive adding flag
matches = re.findall(regex_pattern, txt, re.I) ##re.I (or re.IGNORE CASE)
print(matches)  # ['Apple', 'apple']

#Excercise:
# Clean the following text. After cleaning, count three most frequent words in the string.

import re
from collections import Counter

def clean_text(text):
    # Remove all non-alphabetic characters (keep letters and spaces)
    cleaned = re.sub(r'[^A-Za-z\s]', '', text)
    # Convert to lowercase for uniformity
    cleaned = cleaned.lower()
    return cleaned

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# Clean the text
cleaned_sentence = clean_text(sentence)

# Split into words
words = cleaned_sentence.split()

# Count word frequencies
word_counts = Counter(words)

# Get top 3 most common words
top_three = word_counts.most_common(3)

print("Cleaned text:\n", cleaned_sentence)
print("\nTop 3 most frequent words:", top_three)

