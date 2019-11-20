import collections

from listUtils import remove_duplicates

# https://stackabuse.com/python-linked-lists/
# https://www.geeksforgeeks.org/deque-in-python/
# https://docs.python.org/2/library/collections.html

print(remove_duplicates([1, 1, 3, 2, 2, 4, 11, 1]))


def deque_last(deq):
    last = deq.pop()
    deq.append(last)
    return last


def deque_first(deq):
    first = deq.popleft()
    deq.appendleft(first)
    return first


# de = collections.deque()
# dict1 = {"key1": "value1"}
# de.append(dict1)
# # print(de.pop()["key1"])
# print(de)
# print(deque_last(de)["key1"])
# print(de)
# print(deque_first(de)["key1"])
# print(de)

# de = collections.deque()
# de1 = collections.deque()
# de1.append({"de1.key1": "de1.value1", "de1.key2": "de1.value2"})
# de2 = collections.deque()
# de2.append({"de2.key1": "de2.value1", "de2.key2": "de2.value2"})
# de.append(de1)
# de.append(de2)
# print(de)
