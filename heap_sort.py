from typing import List

def heapify(arr: List[int], N: int, i: int) -> None:
    """
    Heapify the given list to maintain the max heap property.

    Args:
        arr (List[int]): The list of integers to be heapified.
        N (int): The size of the heap.
        i (int): The index to start heapifying from.

    Returns:
        None
    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and arr[largest] < arr[l]:
        largest = l

    if r < N and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, N, largest)

def heapSort(arr: List[int]) -> None:
    """
    Sort the given list in ascending order using the heap sort algorithm.

    Args:
        arr (List[int]): The list of integers to be sorted.

    Returns:
        None
    """
    N = len(arr

    # Build a max heap.
    for i in range(N // 2 - 1, -1, -
