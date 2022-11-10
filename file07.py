def main(data:str):
    s=0
    for i in data:
        if i.isdigit():
            s+=int(i)

    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    return s
# Read data from file
print(main("""0707codeschooluz
python2022"""))