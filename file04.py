def main(data:str):
    array=[]
    for i in data:
        if not i.isdigit():
            array.append(i)

    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    return array

print(main("""python2022
coder01
"""))
# Read data from file