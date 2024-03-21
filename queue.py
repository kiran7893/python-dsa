stock_queue=[]
stock_queue.insert(0,123)
stock_queue.insert(0,121)
stock_queue.insert(0,122)
print(stock_queue)

q=deque()

q.appendleft(5)
q.appendleft(8)
q.appendleft(27)
print(q)
q.pop()
print(q)
q.pop()
print(q)