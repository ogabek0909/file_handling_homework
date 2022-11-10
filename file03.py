def main(data:str):
    array=[]
    for i in data:
        if i.isdigit():
            array.append(i)
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    return array
# Read data from file