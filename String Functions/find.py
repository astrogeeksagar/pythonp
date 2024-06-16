# Syntax
# str.find(sub, start, end)
# Start And End Is Optional

# Finding The Index Of A Character Or Word In A String Using find() :Yes Args...
string = "Astrogeek Sagar lives in kanpur and also work in kanpur"
finding = string.find("a")
print(finding) # O/P = 11

string = "Astrogeek Sagar lives in kanpur and also work in kanpur"
finding = string.find("Monkey")
print(finding) # O/P = -1

string = "Astrogeek Sagar lives in kanpur and also work in kanpur"
finding = string.find("a", 25, 36)
print(finding) # O/P = 26

string = 'Astro Geek Sagar'
substring = 'Dhruv Pedigree'

if string.find(substring) != -1 :
    print(f"String Contains The Word {substring}.")
else: 
    print(f"String Doesn't Contains The Word {substring}.")
