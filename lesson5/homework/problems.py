import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
operating_systems = ["windows", "mac", "linux"]
print(operating_systems[len(operating_systems)-1])
operating_systems.reverse()
print(operating_systems)

# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
school = ["Math", "E.L.A.", "World History", "Science"]
print(school[1])
school.sort()
print(school)


# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.
errors = ["403","404","405","446","458"]
print(len(errors))
yes = errors.index("403") 
print(yes)


# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
programming_languages = ["C#", "Python"]
print(random.choice(programming_languages))
programming_languages.append("scratch")
print(programming_languages)


# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwords = ["password", "12345", "pass1", "11111", "junk", "pass_of_words"]
index = len(passwords) // 2
print(passwords[index])
passwords.pop(0)
print(passwords)