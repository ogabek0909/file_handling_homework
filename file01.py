def main(data:str):
    
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    return open(data).read().split()
# Read data from file