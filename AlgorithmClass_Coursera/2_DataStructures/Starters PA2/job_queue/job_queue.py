# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]

    def sol(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)

        self.nextFree = [[0,w] for w in range(self.num_workers)]

        for i in range(len(self.jobs)):
          self.assigned_workers[i] = self.nextFree[0][1]
          self.start_times[i] = self.nextFree[0][0]
          self.ChangePriority(0,self.nextFree[0][0]+self.jobs[i])

    def SiftDown(self,i):
      minIndex = i
      left = 2*i+1 # left child
      if left < self.num_workers and (self.nextFree[left][0]<self.nextFree[minIndex][0] or \
         (self.nextFree[left][0]==self.nextFree[minIndex][0] and self.nextFree[left][1]<self.nextFree[minIndex][1])):
        minIndex=left
      right = 2*i+2 # right child
      if right < self.num_workers and (self.nextFree[right][0]<self.nextFree[minIndex][0] or \
         (self.nextFree[right][0]==self.nextFree[minIndex][0] and self.nextFree[right][1]<self.nextFree[minIndex][1])):
        minIndex=right
      if i != minIndex:
        self.nextFree[i],self.nextFree[minIndex] = self.nextFree[minIndex],self.nextFree[i]
        self.SiftDown(minIndex)

    def SiftUp(self,i): # maybe not necessary
      parent = lambda x: int((x-1)/2)
      while i>0 and (self.nextFree[parent(i)][0]>self.nextFree[i][0] or \
        (self.nextFree[parent(i)][0]==self.nextFree[i][0] and self.nextFree[parent(i)][1]>self.nextFree[i][1])) :
        self.nextFree[i],self.nextFree[parent(i)] = self.nextFree[parent(i)],self.nextFree[i]
        i = parent(i)

    def ChangePriority(self,i,p):
      oldp = self.nextFree[i][0]
      self.nextFree[i][0]=p
      if p<oldp:
        self.SiftUp(i)
      else:
        self.SiftDown(i)

    def solve(self):
        self.read_data()
        #self.assign_jobs()
        self.sol()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

