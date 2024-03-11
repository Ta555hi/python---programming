queue = [] #it will look same as stack but the performance is diff

queue.append('a')
queue.append('b')
queue.append('c')

print('Initial queue')
print(queue)

print("/nElement dequeued from queue")
print(queue.pop(1)) # 0 is the index, alys pop the first element,first in first out
print(queue.pop(0))