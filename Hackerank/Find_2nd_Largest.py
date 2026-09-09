def swap(x,y):
    return y, x
    
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    
    runner_up = -1
    numOfSwaps = 0
    isSwapped = False
    lastUpdateSwap = 0
    
    for i in range(len(arr)):
        isSwapped = False
        
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                (arr[j], arr[j+1]) = swap(arr[j], arr[j+1])
                numOfSwaps += 1
                isSwapped = True
                lastUpdateSwap = j
                
        if not isSwapped:
            runner_up = arr[lastUpdateSwap]
            break

    if numOfSwaps == 0:
        runner_up = arr[len(arr) - 2]



    print(arr)
    print(lastUpdateSwap)
    print(runner_up)