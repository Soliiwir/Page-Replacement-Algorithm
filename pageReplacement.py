from queue import Queue

def FIFO(refString, strLength, frame):
    currentSet = set()
    queue = Queue()
    pageFault =0
    
    for i in range(strLength):
        if(len(currentSet) < frame):
            if (refString[i] not in currentSet):
                currentSet.add(refString[i])
                queue.put(refString[i])
                pageFault +=1
                
        else:

            if (refString[i] not in currentSet):
              oldest = queue.queue[0]
              queue.get()
              currentSet.remove(oldest)
              currentSet.add(refString[i])
              queue.put(refString[i])
              pageFault +=1
    return pageFault

def Optimal(refString, strLength, frame):
    currentSet = set()
    pageFault = 0

    for i in range(strLength):
        page = refString[i]
        if page not in currentSet:
            if len(currentSet) < frame:
                currentSet.add(page)
            else:
                farthest = -1
                replacePage = None
                for p in currentSet:
                    try:
                        nextUse = refString[i+1:].index(p)
                    except ValueError:
                        nextUse = float('inf') 

                    if nextUse > farthest:
                        farthest = nextUse
                        replacePage = p

                currentSet.remove(replacePage)
                currentSet.add(page)
            pageFault += 1

    return pageFault

def LRU(refString, strLength, frame):
    currentSet = set()
    stack = []
    pageFault = 0

    for i in range(strLength):
        page = refString[i]
        if page not in currentSet:
            if len(currentSet) < frame:
                currentSet.add(page)
            else:
                lru = stack.pop(0)
                currentSet.remove(lru)
                currentSet.add(page)
            pageFault += 1
        else:
            stack.remove(page)

        stack.append(page)  

    return pageFault



if __name__ == "__main__":
    refString = [1, 2, 3, 4, 2, 1, 5, 6, 2, 1, 2, 3, 7, 6, 3, 2, 1, 2, 3, 6]
    strLength = len(refString)
    frames = list(range(1, 6))

    for frame in frames:
        fifoFault = FIFO(refString, strLength, frame)
        lruFault = LRU(refString, strLength, frame)
        optimalFault = Optimal(refString, strLength, frame)  
        print(f"FIFO    Frames: {frame} --> Page Faults: {fifoFault}")
        print(f"LRU     Frames: {frame} --> Page Faults: {lruFault}")
        print(f"Optimal Frames: {frame} --> Page Faults: {optimalFault}")
        print("----")


