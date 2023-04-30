def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    b=0
    while b<len(list1):
        if list1[b]==0:
            list1[b]="False"
        b=b+1
    return list1
print(main([9,0,0,9,0]))