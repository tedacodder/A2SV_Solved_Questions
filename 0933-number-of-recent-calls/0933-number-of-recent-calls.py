class RecentCounter:

    def __init__(self):
        self.request=deque()



    def ping(self, t: int) -> int:
        mini=t-3000
        while self.request and self.request[0]<mini:
            self.request.popleft()
        self.request.append(t)
        
        return len(self.request)
        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)