def oxford_comma(elements):
    if len(elements) == 0:
        return ""
    elif len(elements) == 1:
        return elements[0]
    elif len(elements) == 2:
        return f"{elements[0]} and {elements[1]}"
    else:
        comma_separated = ", ".join(elements[:-1])
        return f"{comma_separated}, and {elements[-1]}"

# Test the function
elements = ["fiddleheads", "okra", "kohlrabi"]
result = oxford_comma(elements)
print(result)  # Output: "fiddleheads, okra, and kohlrabi"
