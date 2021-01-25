#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so

items = [1, 5, 11, 24, 32, 55]
#Given list
print (" : ", items)

items_copy = items[:]
#Apply sort to copy
items_copy.sort()

if (items == items_copy):
    print("Yes, items are sorted.")
else:
    print("No, items are not sorted.")


print(is_sorted(items))

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    list = len(items)
    #Traverse throug all array elemts 
    for a in range(len(items)-1, 0, -1):
    #Last I elements are a lreay in correct position 
        for  i in range(a):
            #Swap if the element found is greater than the next element 
            if items[i] > items[i + 1] :
                swap = items[i]
                items[i] = items[i + 1]
                items[i+1] = swap


items = ['a', 'f', 'g', 'z', 'b', 'i', 'k', 'c']
bubble_sort(items)
print ("Your sorted array is:", items)



def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    index_length = range(0, len(items)-1)

    for i in index_length:
        min_value = i

        for j in range(i+1, len(items)):
            if items[j] < items[min_value]:
                min_value = j

        if min_value != i:
            items[min_value], items[i] = items[i], items[min_value]

    return items

print(selection_sort([1, 8, 22, 45, 9, 47, 80])) 

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items






# print(bubble_sorted(items))