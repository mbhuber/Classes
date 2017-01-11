# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def load_queries(slist):
    return [Query(s.split()) for s in slist]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

def process_queries2(queries):
    result = []
    phoneBook = ['']*10000000 # keep phone book
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            phoneBook[cur_query.number]=cur_query.name
        elif cur_query.type == 'del':
            phoneBook[cur_query.number]=''
        else:
            response = 'not found'
            if len(phoneBook[cur_query.number])>0:
                response = phoneBook[cur_query.number]
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries2(read_queries()))

##    slist=['add 911 police','add 76213 Mom','add 17239 Bob','find 76213','find 910','find 911','del 910','del 911','find 911','find 76213','add 76213 daddy','find 76213']
##    write_responses(process_queries(load_queries(slist)))
##    print()
##    write_responses(process_queries2(load_queries(slist)))