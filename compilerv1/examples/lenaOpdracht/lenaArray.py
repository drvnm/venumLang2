chars = " .:-=+*#%@"
# open a file and write the following for loop in it
with open("char_array.vlang", "w") as f:
    f.write(f"var characters char[{len(chars)}]]\n")
    for i in range(len(chars)):
        f.write(f"{ord(chars[i])} characters {i} writearr\n")