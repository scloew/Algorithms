from random import randint
import operator

def _merge(lst_one, lst_two, compare = operator.lt):
    """
    helper function for merge sort
    :param lst_one:
    :param lst_two:
    :param compare:
    :return:
    """
    ret, i, j = [], 0, 0
    while i<len(lst_one) and j<len(lst_two):
        if compare(lst_one[i],lst_two[j]):
            ret.append(lst_one[i])
            i+=1
        else:
            ret.append(lst_two[j])
            j+=1
    return ret+lst_one[i:]+lst_two[j:]

def merge_sort(to_sort, reverse=False, compare = operator.lt):
    """
    merge_Sort(to_sort, reverse=False, compare = operator.lt)
    return new, sorted list containing elements of to_sort
    """
    sub_lists = [[i] for i in to_sort]
    while len(sub_lists)!=1:
        sub_lists = [_merge(sub_lists[i], sub_lists[i+1], compare) for i in range(0, len(sub_lists)-1, 2)] \
                    + ([sub_lists[-1]] if len(sub_lists)%2==1 else [])
    return sub_lists[0] if not reverse else sub_lists[0][::-1]


if __name__ == "__main__":

    print('hello sortss')
    lst = [randint(-500,500) for _ in range(14)]
    sorted = merge_sort(lst, reverse=True)
    print('original list:= ', lst)
    print('merge sort:=    ', sorted)
    lst.sort(reverse=True)
    print('truth value:=   ', lst)
    print('algorithm correct:=', lst==sorted)

    ##test custome compare function
    lst_two = [{i:randint(-25,25) for i in range(randint(2,5))} for _ in range(10)]
    my_compare = lambda dict_one, dict_two: True if len(dict_one)<len(dict_two) else False
    print('original list:= ', lst_two)
    print('sorted list:=   ', merge_sort(lst_two, compare=my_compare))

