def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    n=0
    while n<len(list1):
        if list1[0]==list1[n]:
            s="true"
        else :
            s="false"
        n=n+1
    return s
print(main([0,0,0,0,0]))