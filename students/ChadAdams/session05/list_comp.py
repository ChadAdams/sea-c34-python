def count_evens(nums):
    """
    Returns the number of even ints in a given array
    """
    count = [num for num in nums if num % 2 == 0]
    return len(count)

if __name__ == "__main__":
    print count_evens([2,4,6])
    print count_evens([0,1,7])
    print count_evens([1,4,4,9])
    print count_evens([3,5,11,19])
    print count_evens([6,4,2])

