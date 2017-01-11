# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []
        self.hashTable = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def load_query(self,query):
        return Query(query.split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_query2(self, query):
        if query.type == "find":
            L = self.hashTable[self._hash_func(query.s)]
            isEle = False
            for ele in L:
                if ele == query.s:
                    isEle = True
            self.write_search_result(isEle)

        if query.type == "add":
            idx = self._hash_func(query.s)
            for ele in self.hashTable[idx]:
                if ele == query.s:
                    return
            self.hashTable[idx].append(query.s)

        if query.type == "check":
            self.write_chain(reversed(self.hashTable[query.ind]))

        if query.type == "del":
            idx = self._hash_func(query.s)
            for k in range(len(self.hashTable[idx])):
                if self.hashTable[idx][k] == query.s:
                    self.hashTable[idx].pop(k)
                    return

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query2(self.read_query())

    def test_queries(self,qlist):
        for q in qlist:
            self.process_query(self.load_query(q))

    def test_queries2(self,qlist):
        for q in qlist:
            self.process_query2(self.load_query(q))

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

##    bucket_count = 5
##    q = ['add world','add HellO','check 4','check 0','find World','find world','del world','check 4','del HellO','add luck','add GooD','check 2','del good']
##    proc = QueryProcessor(bucket_count)
##    proc.test_queries(q)
##    print()
##    proc.test_queries2(q)