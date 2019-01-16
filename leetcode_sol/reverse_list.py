

# start, end indexes 
def reverse(l1, start, end):
    while start < end:
        temp = l1[start]
        l1[start] = l1[end]
        l1[end] = temp
        start += 1
        end -= 1
    return l1


if __name__ == "__main__":
   l1 = [1,2,3,4,5,6]
   l2 = [1,2,3,4,5,6]
   n = len(l1)
   res = reverse(l1, 0, n-1)
   print(res)
   res = reverse(l2, 0, 3)
   print(res)
