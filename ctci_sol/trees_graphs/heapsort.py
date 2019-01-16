
from min_heap import * 

# build heap using given input_list
def build_heap(input_list):
    heap = min_heap()
    for val in input_list:
        heap.insert(val)
    return heap

# sort list in ascedning or descedning order by deleting min value from heap 
def sort_list(heap, ascending=1):
    sorted_list = []
    tmp = heap.min_value()
    while tmp[0]:
        if ascending == 1:
           sorted_list.append(tmp[1])
        else:
           sorted_list.insert(0,tmp[1])
        heap.delete_min()
        tmp = heap.min_value()
    return sorted_list

# main sorting func
def sort(input_list, ascending=1):
    heap = build_heap(input_list) 
    sorted_list = sort_list(heap, ascending)
    return sorted_list


if __name__ == "__main__":
    l1 = [10,5,21,2,-1,20]
    print ("input list : ", l1)
    print ("ascending sorted list : ",sort(l1, 1))
    print ("descedning sorted list : ",sort(l1, 0))


