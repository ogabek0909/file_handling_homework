def main(data:str):
    array=[]
    counter=0
    l=0
    for i in data:
        # if i!='\n':

        counter+=1

        if i=='\n':
            l+=counter
            array.append(counter-1)
            counter=0
            continue

    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    array.append(len(data)-l)
    return array

print(main("""dsfaf
dfsafd"""))
# Read data from file