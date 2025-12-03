# ================================================================
# Alignment & Formatting Methods
# ================================================================
print("Alignment & Formatting Methods")

s = "python"

print(s.center(12, "*"))          # Output: ***python***
print(s.ljust(12, "-"))           # Output: python------
print(s.rjust(12, "+"))           # Output: ++++++python
print("543".zfill(8))             # Output: 00000543

print()


# ================================================================
# Search & Find Methods
# ================================================================
print("Search & Find Methods")

s = "hello python programming"

print(s.find("python"))           # Output: 6
print(s.rfind("o"))               # Output: 22
print(s.index("programming"))     # Output: 13
print(s.count("o"))               # Output: 3

print()


# ================================================================
# Replace & Modify Methods
# ================================================================
print("Replace & Modify Methods")

s = "apple apple mango apple"

print(s.replace("apple", "banana"))
# Output: banana banana mango banana

# translate() + maketrans()
table = str.maketrans("aeiou", "12345")
print("hello world".translate(table))
# Output: h2ll4 w4rld

print()


# ================================================================
# Splitting & Joining Methods
# ================================================================
print("Splitting & Joining Methods")

s = 'python programming lang'
print(s.split())  
# Output: ['python', 'programming', 'lang']

s = 'python,java,sql,flask,html,css'
print(s.split(','))  
# Output: ['python', 'java', 'sql', 'flask', 'html', 'css']

print(s.rsplit(','))  
# Output: ['python', 'java', 'sql', 'flask', 'html', 'css']

print(s.rsplit(',', 3))  
# Output: ['python,java,sql', 'flask', 'html', 'css']

s2 = """python
java
sql
flask
html
css"""

print(s2.splitlines())  
# Output: ['python', 'java', 'sql', 'flask', 'html', 'css']

# join() examples
s3 = "pythonjavasqlflaskhtmlcss"
print(",".join(s3))  
# Output: p,y,t,h,o,n,j,a,v,a,s,q,l,f,l,a,s,k,h,t,m,l,c,s,s

print("".join(s3))  
# Output: pythonjavasqlflaskhtmlcss

# partition
s = 'python,java,sql,flask,html,css'
print(s.partition(','))  
# Output: ('python', ',', 'java,sql,flask,html,css')

print(s.rpartition(','))  
# Output: ('python,java,sql,flask,html', ',', 'css')

print()


# ================================================================
# Whitespace & Trimming Methods
# ================================================================
print("Whitespace & trimming Methods")

s = '     python'

print(s.strip())                 # Output: python
print(s.lstrip())                # Output: python
print(s.rstrip())                # Output: '     python'

print()


# ================================================================
# Encode & Decode Methods
# ================================================================
print("Encode & Decode Methods")

s = 'hello'
print(s.encode())                # Output: b'hello'

print()


# ================================================================
# String Testing Methods
# ================================================================
print("String Testing Methods")

s = 'python.py'
print(s.startswith('pyt'))       # Output: True
print(s.endswith('.py'))         # Output: True

s = 'PYTHON'
print(s.isalpha())               # Output: True

s = 'python123'
print(s.isalnum())               # Output: True

s = 'python'
print(s.islower())               # Output: True

s = 'PYTHON'
print(s.isupper())               # Output: True

s = 'Python language'
print(s.isspace())               # Output: False
print(s.istitle())               # Output: False
print(s.isidentifier())          # Output: False

print(len(s))                    # Output: 9
print(max(s))                    # Output: 'y'
print(min(s))                    # Output: ' '

print(sorted(s))                 
#[' ', 'a', 'a', 'e', 'j', 't', 'u', 'v', 'y']

print(ord(s[0]))                 # Output: 121
print(chr(121))                  # Output: y

print()


# ================================================================
# Operations on Strings
# ================================================================
print("Concatenation")

a = "Python"
b = "Program"
print(a + b)                     # Output: PythonProgram

d = a + b
print()

print("Repetition")
print(a * 5)                     # Output:PythonPythonPythonPythonPython
print()

print("Indexing")
print(d[0])                      # Output: P
print(d[-1])                     # Output: m
print()

print("Slicing")
print(d[0:13])                    # Output: PythonProgram
print(d[0:])                     # Output: PythonProgram
print(d[6:])                     # Output: Program
print(d[::2])                    # Output: PtoPorm
print()

print(d[::-1])                   # Output: margorPnohtyP
print(d[12:7:-1])                 # Output: margorP
print(d[5::-1])                  # Output: nohtyP
print()


# ================================================================
# Membership
# ================================================================
print("Membership")

print("Python in a:", "Python" in a)            # Output: True
print("Program not in b:", "Program" not in b)    # Output: False

print()


# ================================================================
# Case Conversion Methods
# ================================================================
print("Case Conversion Methods")

print("upper()", d.upper())               # Output: PYTHONPROGRAM
print("lower()", d.lower())               # Output: pythonprogram
print("capitalize()", d.capitalize())     # Output: Pythonprogram
print("title()", d.title())               # Output: Pythonprogram
print("swapcase()", d.swapcase())         # Output: pYTHONPROGRAM
print("casefold()", d.casefold())         # Output: pythonprogram
print()