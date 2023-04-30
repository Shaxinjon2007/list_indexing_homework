def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    x=0
    while x<len(list1):
        if list1[x]==1:
            list1[x]="true"
        x=x+1
    return list1
print(main([1,6,7,1,8])) 