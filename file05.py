def main(data:str):
    d=0
    s=0
    array=[]
    for i in data:
        if i.isdigit():
            d+=1
        else:
            s+=1
    array.append(d)  
    array.append(s)  
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    return array
print(main('fsadfas 342 '))
# Read data from file