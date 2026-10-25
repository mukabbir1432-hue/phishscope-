import re

# Read the current file
with open(r'c:\Users\admin\.cline\phishscope\phishscope\cli\main.py', 'r') as f:
    content = f.read()

# Fix the rsplit syntax error
content = content.replace(
    "rsplit('.\", 1)[0]",
    "rsplit('.', 1)[0]"
)

# Write the fixed file
with open(r'c:\Users\admin\.cline\phishscope\phishscope\cli\main.py', 'w') as f:
    f.write(content)

print("CLI file fixed")