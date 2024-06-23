# # 1. Printing The Length Of The String Using Len String Function
# string = "Astrogeek Sagar"
# stringlength = len(string)
# print(stringlength)  # O/P = 15

# # 2. Printing Individual Character From The String Using Square Brackets By Index Number(Index Starts From 0)
# string = "Astrogeek Sagar"
# charat = string[10]
# print(charat)  # O/P = S

# # 3. Printing A Range Characters From The String Using Square Brackets With Colon(:) By Index Number(Index Starts From 0)
# string = "AstroGeek Sagar"
# # We Can Also Escape 1 Side Part By Writing string[:10] It Prints First 10 Character From Start And Skipping
# charrange = string[10:15]
# # Rest O/P = Astrogeek, Writing string[10:] It Prints Chracter Starts After The Index 10 O/P = Sagar
# print(charrange)  # O/P = "Sagar"

# # 4. Changing String All Character To Uppercase using upper() :No Args...
# string = "Astrogeek Sagar"
# uppercase = string.upper()
# print(uppercase)  # O/P = ASTROGEEK SAGAR

# # 5. Changing String All Character To Lowercase using lower() :No Args...
# string = "Astrogeek Sagar"
# uppercase = string.lower()
# print(uppercase)  # O/P = astrogeeksagar

# # 6. Counting A Character Or Word In A String Using count() :Yes Args...
# string = "Astrogeek Sagar lives in kanpur and also work in kanpur"
# counting = string.count('s')
# print(counting)  # O/P = 3

# # 7. Finding The Index Of A Character Or Word In A String Using find() :Yes Args...
# string = "Astrogeek Sagar lives in kanpur and also work in kanpur"
# finding = string.find("a")
# # If The Character Is Not In The String It Will return -1
# print(finding)  # O/P = 11

# # 8. Replacing A Character Or Word In A String With Another Character Or Word Using replace() :Yes Args...
# string = "Astrogeek Sagar"
# replace = string.replace('a', 'b')
# print(replace)  # O/P = Astrogeek sbgbr

# # 9.1. Concataning 2 Or More String Using + sign
# string1 = "Astrogeek"
# string2 = "Sagar"
# concat = string1 + ' ' + string2 + ' Python Developer'
# print(concat)  # O/P = Astrogeek Sagar Python Developer

# # 9.2. Concataning 2 Or More String Using format() :Yes Args...
# string1 = "Astrogeek"
# string2 = "Sagar"
# concat = '{} {} Python Developer'.format(string1, string2)
# print(concat)  # O/P = Astrogeek Sagar Python Developer

# # 9.3. Concataning 2 Or More String Using f :Yes Args...
# string1 = "Astrogeek"
# string2 = "sagar"
# concat = f'{string1} {string2.upper()} Python Developer'
# print(concat)  # O/P = Astrogeek SAGAR Python Developer

# # 10. Getting Avaiable Executable Function On A String Using dir() :Yes Args...
# string = "Astrogeek Sagar"
# dir = dir(string)
# print(dir)  # O/P = List Of Avaibale Executable Function

# # 10.1. Getting Avaiable Executable Function On A String Using help() :Yes Args...
# #help = help(str.upper)
# #print(help)  # O/P = Tells About The Usages Of Function .upper

# # 11. Converting The First Character Of A String To Upper Case Using capitalize() :No Args...
# string = 'astrogeek sagar'
# capitalize = string.capitalize()
# print(capitalize) # O/P Astrogeek sagar

# # 12. Converting The String Into Title Case Using title() :No Args...
# string = 'astrogeek sagar'
# title = string.title()
# print(title) # O/P Astrogeek Sagar

# # 13. Converting The String Into Swap Case Using swapcase() :No Args...
# string = 'AstroGeek sagaR'
# swapcase = string.swapcase()
# print(swapcase) # O/P astTROgEEK SAGAr

# # 14. String Center Method Padding using center() :Yes Args...
# string = 'Astrogeek Sagar'
# center = string.center(len(string) + 5, '#') # You Can Remove The Fill Char # And If Passed Number Is Equal To String Length No Padding Will Be Added
# print(center) # O/P ##Astrogeek Sagar###

# # 15. Checking The End Of A String Is True Or False Using endswith() :Yes Args...
# string = 'Astrogeek Sagar.'
# endswith = string.endswith('Sagar.') # Remove The Dot(.) It Will Return False
# print(endswith) # O/P True

# # 16. Checking The Start Of A String Is True Or False Using startswith() :Yes Args...
# string = 'Astrogeek Sagar Loves Astronomy'
# startswith = string.startswith('Loves', 16, 21) # It's Checking Start With A Provided Index Starts And End Works Same With endswith
# print(startswith) # O/P True

# # 17. Checking The Start Of A String Is True Or False Using startswith() :Yes Args...
# string = 'Astrogeek Sagar Loves Astronomy'
# startswith = string.startswith('Loves', 16, 21) # It's Checking Start With A Provided Index Starts And End Works Same With endswith
# print(startswith) # O/P True

# # 18. Specifying The Amount Of Space To Be Substituted with the "\t" Symbol In The String Using expandtabs :Yes/No Args...
# string = "\t\tAstro\tGeekSagar"
# expandtabs = string.expandtabs() # You Can Modify The Spacing By Passing Custom Numbers As args...
# print(expandtabs) # O/P Print Centered String

# # 19. Getting The Unicode Of A Character Using ord() :Yes/No Args...
# string = "S"
# ord = ord(string)
# print(ord) # O/P 83

# 20. Finding A Character In A String Using in Return Boolean
string = "Astrogeek Sagar"
finding = "ro" in string
print(finding) # O/P = true