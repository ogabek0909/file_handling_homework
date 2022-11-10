def main(data:str):
    
    s=0
    for i in data:
        if i.isdigit():
            if int(i)>int(s):
                s=i
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    return int(s)
print(main("""Django 4.0
NumPy 1.22.0
TensorFlow 2
python 3.10.0
Windows 7"""))
# Read data from file