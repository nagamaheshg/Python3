# regular expression is used for search patterns
import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.com
'''



emails = '''nagamaheshgatta@gmail.com
g.nagamahesh62@gmail.com
mahesh.gatta@gmail.com
'''

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

Meta Characters (Need to be escaped)
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234


Mr. Sacafer
Mr Smith
Ms. Davis
Mrs. Robinson
Mr. T 

cat
mat
rat
bat

.       - Any character except new line
\d      - Digit (0-9)
\D      - Not a Digit(0-9)
\w      - Word character (a-z, A-Z, 0-9, _)
\W      _ Not a word Character 
\s      _ White Space (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

# these are not matched any characters 

\b      - Word Boundary            - re.compile(r'\bHa')
\B      - Not a Word Boundary      - re.compile(r'\BHa')
^       - Beginning of a starting  - re.compile(r'^Start')
$       - End of a String          - re.compile(r'end$')

# 
[]      - Match characters in brackets
[^]     - Match characters Not in
|       - Either or
()      = Group

Quantifiers:
*       - 0 or more
+       - 1 or more
?       - 0 or more
{3}     - Exact Number
{3,4}   - Range of Numbers(Minimum, Maximum)

'''
# Raw string in python a string prefix. python can n't handle backslash 
# for that purpose we are using re.compile() method to handle or separate backslash things
# re separate methods patterns into variable 

sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'abc') # search through out text 
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match) #<re.Match object; span=(1, 4), match='abc'> span contain matched beginning and ending index
    
print(text_to_search[1:4])

#pattern = re.compile(r'.') # only searching for a period. it matches all most everything. (.) dot is special character in regular expression to excape that dot we use backslash(\.).

# pattern = re.compile(r'\.')


pattern = re.compile(r'coreyms\.com')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# match phone number
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')  # or
# pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')  # [.-] square brackets match either one present inside pattern. no need to escape dot. square bracket contain multiple character set it still only matching one character in text. either . or -




# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# with open('data.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
    
#     for match in matches:
#         print(match)
    
    
# # match 800 or 900 number
# pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d') #it find out phone number start with 800 or 900

# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# with open('data.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
    
#     for match in matches:
#         print(match)
    
# between range[-]
# pattern = re.compile(r'[1-5]00[.-]\d\d\d[.-]\d\d\d\d')
# with open('data.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
    
#     for match in matches:
#         print(match)

# ^if you mention carriot sign outside of character set the carrot match beginning of the string but with in a character set it's negate the set and it matches everything not matched character set 

# get not matched items
pattern = re.compile(r'[^b]at')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

# To match multiple characters at a time.

pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
with open('data.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    
    for match in matches:
        print(match)

pattern = re.compile(r'Mr\.?\s[A-Z]\w*') #question mark match zero or one character # s for space
# \w for any character # * zero or more character
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
    
#pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') # here we are using group character() and or character |
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

#pattern = re.compile(r'[a-zA-Z]\w*\.?\w*@\w*\.[a-zA-Z]\w*')
pattern = re.compile(r'[a-zA-Z.0-9-]+@[a-zA-Z-]+\.(com|edu|net)')
matches = pattern.finditer(emails)

for match in matches:
    print(match)
    
### Sample Regex ###

#[a-zA-Z0-9_.+-]+[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

# pattern = re.compile(r'[a-zA-Z]+[:](//)[a-zA-Z]*\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)

for match in matches:
    print(match.group(2))

# sub tution urls
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)

# ignore case flag.
sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'start', re.IGNORECASE)
matches = pattern.search(sentence)
print(matches)