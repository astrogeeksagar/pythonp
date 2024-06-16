from encodings.aliases import aliases

print("Available Encodings Are: ")
print(aliases.keys())

# Encoding A String Using encode() :No Args...
string = 'Astrogeek Sagar'
encode = string.encode('greek')
print(encode) # O/P = b'Astrogeek Sagar'