import collections


def deque_last(deq):
    last = deq.pop()
    deq.append(last)
    return last


def deque_first(deq):
    first = deq.popleft()
    deq.appendleft(first)
    return first


class ListDeque(list):
    def __init__(self, seq=()):
        super(ListDeque, self).__init__(seq)

    def search(self, condition, *args, **kwargs):
        if hasattr(condition, '__call__'):
            result = []
            for item in self:
                cond_result = condition(item, *args, **kwargs)
                if cond_result is not None:
                    result.append(cond_result)
            return result
        if isinstance(condition, object):
            if len(self)>0:
                return self[self.index(condition)]


# ob1 = {1:11,2:12,3:14}
# de = ListDeque()
# de.append(ob1)
# print(de.search(ob1))
# def testFunc(dict1, arg1):
#     return dict1[arg1]
# print(de.search(testFunc, 1))
# print(de.search(lambda dict1, key1: dict1[key1], 1))

# de = ListDeque()
# de1 = collections.deque()
# de1.append({1: 11, 2: 12, 3: 14})
# de1.append({1: 14, 22: 12, 3: 14})
# de2 = collections.deque()
# de2.append({1: 14, 22: 12, 32: 14})
# de2.append({1: 11, 2: 12, 3: 14})
# de.append(de1)
# de.append(de2)
# print(de)
# print(deque_first(de))
# print(de)
# print(deque_first(deque_first(de)))
# print(de)
# print(deque_last(deque_last(de))[1])
# function1 = lambda ldq, key: deque_last(deque_last(ldq))[key]
# print(function1(de, 1))
# print(de.search(lambda ldq_item, key: deque_last(ldq_item)[key], 1))
# function2 = lambda ldq, key: [item for item in ldq if key in deque_last(item)]
# print(function2(de, 1))
# print(de.search(lambda ldq_item, key: ldq_item if key in deque_last(ldq_item) else None, 2))
# print(de.search(lambda ldq_item, value: ldq_item if value in deque_last(ldq_item).values() else None, 14))
# print(de.search(lambda ldq_item, key, value: ldq_item if deque_last(ldq_item)[key]==value else None, 1,14))
# print(de.search(lambda ldq_item, key, value: ldq_item if deque_last(ldq_item)[key]==value else None, 3,14))
# print(de.search(lambda ldq_item, key, value: ldq_item if deque_last(ldq_item)[key]==value else None, 3,1445))

data = {1: {'itemID': 1, 'parentID': '2', 'key2': 'value2'}, 2: {'itemID': 2, 'parentID': '11', 'key2': 'value2'},
        11: {'itemID': 11, 'parentID': '0', 'key2': 'value2'}, 22: {'itemID': 22, 'parentID': '1', 'key2': 'value22'},
        23: {'itemID': 23, 'parentID': '222', 'key2': 'value22'}}
results = ListDeque()
datakeys = list(data.keys())
while len(datakeys) > 0:
    for itemID in datakeys:
        item_data = data[itemID]
        parentItemID = int(item_data['parentID'])
        parentIn = results.search(
            lambda ldq_item, key, value: ldq_item if deque_last(ldq_item)[key] == value else None,
            'itemID',
            parentItemID)
        if parentItemID not in data.keys():
            new_dq = collections.deque()
            new_dq.append(item_data)
            results.append(new_dq)
            del (datakeys[datakeys.index(itemID)])
        if len(parentIn) > 0:
            for dq in parentIn:
                dq.append(item_data)
                del (datakeys[datakeys.index(itemID)])
for item in results:
    print(item)
# f1 = lambda ldq_item, key: ldq_item if key in deque_last(ldq_item).keys() else None
# f2 = lambda ldq_item, key, value: ldq_item if deque_last(ldq_item)[key] == value else None
# results2 = ListDeque()
# for item in data.values():
#     new_dq = collections.deque()
#     new_dq.append(item)
#     results2.append(new_dq)
# print(results2.search(f2, 'key2', 'value2'))
# print(results2)
# r2 = ListDeque()
# d1 = {1: {'itemID': 1, 'parentID': '2', 'key2': 'value2'}, 2: {'itemID': 2, 'parentID': '11', 'key2': 'value2'}}
# d2 = {11: {'itemID': 11, 'parentID': '2', 'key2': 'value2'}, 2: {'itemID': 2, 'parentID': '11', 'key2': 'value2'}}
# new_dq1 = collections.deque()
# new_dq1.append(d1)
# r2.append(new_dq1)
# new_dq2 = collections.deque()
# new_dq2.append(d2)
# r2.append(new_dq2)
# print(r2)
# print(r2.search(f1, 1))
