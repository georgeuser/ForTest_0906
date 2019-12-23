#这是官方的队列的实现,队列的tail就是len
#用list可以很好的实现栈，list.append,list.pop即可
#栈的纸针直接len（list）-1即可
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
queue[queue.__len__()-1]       #d队列尾部
queue                           # Remaining queue in order of arrival

