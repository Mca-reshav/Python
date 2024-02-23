#python have in built module called re
import re

str = " hello world is the first message"
match = re.search(r'world', str)
print(match)

#meta characters
'''
[]: class
^: matches the beginning
$: matches the ending
.: matches any character except newline
|: or
?: matches zero or one occurrence
*: any number of occurrence

'''

#special character
'''
\A: matches if string begins with given character
\b: matches if word begin or end with given character
\B: opposite of \b, string not start with
\s: matches any whitespace
\S: opposite of \s
\w: alphanumeric character


'''