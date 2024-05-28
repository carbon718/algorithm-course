import random
import time

def insertion_sort(A):
    for i in range(1, len(A)):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = x

def merge(Array, leftArray, rightArray):
    i = 0
    j = 0
    k = 0
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] < rightArray[j]:
            Array[k] = leftArray[i]
            i += 1
        else:
            Array[k] = rightArray[j]
            j += 1
        k += 1

    while i < len(leftArray):
        Array[k] = leftArray[i]
        i += 1
        k += 1

    while j < len(rightArray):
        Array[k] = rightArray[j]
        j += 1
        k += 1


def merge_sort(Array):
    if len(Array) > 1:
        leftArray = Array[:(len(Array) // 2)]
        rightArray = Array[(len(Array) // 2):]
        merge_sort(leftArray)
        merge_sort(rightArray)
        merge(Array, leftArray, rightArray)


def main():
    dane = []
    arrayLength = 2000
    iterations = 100
    randA = 0
    randB = 10000

    insertionTimes = []
    start_All = time.time()
    for i in range(iterations):
        A = [random.randint(randA, randB) for _ in range(arrayLength)]
        start = time.time()
        insertion_sort(A)
        end = time.time()
        insertionTimes.append(end - start)
    end_All = time.time()
    print("Insertion sort all iterations: ", end_All - start_All)


    mergeTimes = []
    start_All = time.time()
    for i in range(iterations):
        A = [random.randint(randA, randB) for _ in range(arrayLength)]
        start = time.time()
        merge_sort(A)
        end = time.time()
        mergeTimes.append(end - start)
    end_All = time.time()
    print("Merge sort all iterations: ", end_All - start_All)


    print("Insertion sort average time: ", sum(insertionTimes) / len(insertionTimes))
    print("Insertion sort max time: ", max(insertionTimes))
    print("Insertion sort min time: ", min(insertionTimes))

    print("Merge sort average time: ", sum(mergeTimes) / len(mergeTimes))
    print("Merge sort max time: ", max(mergeTimes))
    print("Merge sort min time: ", min(mergeTimes))


if __name__ == "__main__":
    main()