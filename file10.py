def main(data:str):
    array =[]
    counter=0
    l=0
    for i in data:
        counter +=1
        if i=='\n':
            l+=counter
            array.append(counter-1)
            counter=0
    array.append(len(data)-l)
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    return max(array)
print(main("""Computer Vision
CODESCHOOLUZ
ML
CV
OpenCV
Numpy
PYTHON"""))
# Read data from file