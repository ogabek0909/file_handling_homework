def main(data:str):
    
    l=data.split(',')
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

print(main('1,2,3,4,5,6,7'))
# Read data from file