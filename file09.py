def main(data:str):
    array=[]
    for i in data:
        if i.isdigit():
            array.append(i)
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    return min(array)
# Read data from file
print(main("""Django 4.0
NumPy 1.22.0
TensorFlow 2
python 3.10.0
Windows 7"""))