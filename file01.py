def main(data:str):
    l=open(data).read().split(',')
    array=[]
    for i in l:
        array.append(int(i))
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    return array

print (main('data01.txt'))
# Read data from file