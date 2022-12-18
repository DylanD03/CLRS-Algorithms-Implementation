# Mergesort, O(nlogn) Complexity
# Written by Dylan Du

from math import floor
DEBUG = True

def merge_sort(array, lo, hi):
    if lo < hi:
        mid = floor((lo + hi)/2)
        lhs = merge_sort(array, lo, mid)
        rhs = merge_sort(array, mid+1, hi)
        merged_array = merge(lhs, rhs)
        return merged_array
    else:
        return [array[hi]] # lo = hi 

def merge(lhs, rhs):
    lhs_ptr = 0
    rhs_ptr = 0
    merged_array = []
    while (lhs_ptr < len(lhs)) and (rhs_ptr < len(rhs)):
        if lhs[lhs_ptr] < rhs[rhs_ptr]:
            merged_array.append(lhs[lhs_ptr])
            lhs_ptr += 1
        else:
            merged_array.append(rhs[rhs_ptr])
            rhs_ptr += 1
    # One of lhs or rhs is empty. Can concatonate the rest.
    if lhs_ptr < len(lhs):
        # lhs is non-empty
        merged_array.extend(lhs[lhs_ptr:])
    else:
        # rhs is non-empty
        merged_array.extend(rhs[rhs_ptr:])
    return merged_array


def main():
    tests = []
    tests.append([1,5,7,3,2,4,6,8])
    tests.append([1,3,5,7,9,11,13,15])
    tests.append([9,5,3,21,2,53,5,21,59,3,5,7])
    tests.append([-1,-2,-1,3,5,6,7,5])

    if DEBUG:
        # Testing edge cases
        print("Edge cases\n\n")
        tests.append([1,1,1,1,1,1])
        tests.append([0,0,0,0,0,0,0,0])
        tests.append([0])

    print("Sorting . . .\n")
    for test in tests:
        print("\nBefore:")
        print('\t',test)
        print("After:")
        print('\t',merge_sort(test, 0, len(test)-1))


if __name__ == '__main__':
    main()
