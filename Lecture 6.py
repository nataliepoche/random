# Temperature Converter
def converter(celcius):
    result = celcius * (9/5) + 32
    return result # Not able to access result of computations without this

result = converter(25) # using the arguement

print(result)

# Distance Converter
def distance(kilometers):
    result = (5/8) * kilometers
    print(f'This is {result}') # Allows it to print even if not done outside def
    return result

result = distance(25)
print(result)

# Letter Counter
def counter(sentence):
    answer = 0
    for c in sentence: # Goes to every single character in the string, and store the character inside c
        if c == "!" or c == " " or c == "_" or c == ",":
            continue # If any of those characters, nothing happens and goes to the next character
        answer += 1 # If not equal to any one of the four characters, they will be counted
    return answer

answer = counter(input()) # if input Hello_world,!
print(answer) # Answer should be 10

# Reverse a word
def reverse(word):
    answer = ""
    for i in range(len(word)-1, 0-1, -1): # Len(word) - 1 allows for access of last character, needs 0-1 to access the first variable
        answer += word[i] # stores all of the characters, makes them print backwards in one string instead of a row
    return answer

answer = reverse("hello")
print(answer)

# Launch applications
import os # For windows
import subprocess # For Mac
def launcher(name, operatingsystem):
    if operatingsystem == "windows":
        if name == "minecraft":
            os.startfile("/Applications/Minecraft.app") # launches applications, have to specify which applications to have open.
        if name == "spotify":
            pass
    if operatingsystem == "macos":
        subprocess.run(["open", "/Applications/Minecraft.app"])

launcher("minecraft", "macos")

# Wallpaper Change
import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, "absolute path", 0)

from appscript import app, mactypes # for mac
def wallpaper_change(path_image):
    app("Finder").desktop_picture.set(mactypes.File(f"{path_image}"))