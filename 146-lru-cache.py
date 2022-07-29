"""
  146. LRU Cache
  [ Medium ] | [ 40.3% ] -- Solved 30/07/2022 -- [ Doubly Linked List, Hash Table, Design ]
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN: 90.20%
  MEMORY USAGE: 82.24%

  Problem Statement:
  - Design a data structure that implements an LRU Cache
  - get() and put() operations must be O(1), both affect the LRU order
  - Size specified, Least Recently Used is the cache eviction policy
  - put() operation on existing key updates its value

  APPROACH: Linked List for order, Hash Table for get()
  - DOUBLY LINKED LIST: One end is for the Least Recently Used KV pair, the other is for the Most Recently Used, this
    allows us to keep track of the order that needs to be maintained for the cache eviction policy
  - get() - Hash Table for O(1) lookup. KV pair = (key, Node())
  - put() - Insert to LRU end of Doubly Linked List and Hash Table

  - Doubly Linked List required since rearranging nodes requires access to the previous Node
    - One alternative that seems feasible is storing the Node that precedes the target node in the HashMap, but this is
      problematic since that requires the reference to be updated when the preceding node's order changes. It is
      possible, but it means that this approach is on par, or slightly worse, and is more complex to implement.
  - Hence, using a Doubly Linked List is a suitable way to remember the LRU order

  SIMPLIFICATION (IMPLEMENTATION SPECIFIC)
  - In the doubly linked list, use two dummy nodes for either end of the Linked List, this makes it easy to reference
    either end of the linked list. In the implementation below, only one dummy node is used to mark the LRU end, so the
    MRU end has to be managed with more work and conditions

  Time Complexity: O(1) for get() & put() operations
"""


class Node:
    def __init__(self, key, value, prev):
        self.key = key
        self.value = value
        self.next = None
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.head = self.tail = Node(-1, -1, None)
        self.size = 0
        self.capacity = capacity
        self.hm = {}

    def get(self, key: int) -> int:
        if key in self.hm:
            target = self.hm[key]
            if target == self.tail:
                return target.value

            pre_target = target.prev
            pre_target.next = pre_target.next.next
            if pre_target.next:
                pre_target.next.prev = pre_target

            self.tail.next = target
            target.prev = self.tail

            self.tail = self.tail.next
            self.tail.next = None
            return target.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            target = self.hm[key]
            target.value = value
            if target == self.tail:
                return

            pre_target = target.prev
            pre_target.next = target.next
            pre_target.next.prev = pre_target

            self.tail.next = target
            target.prev = self.tail

            self.tail = self.tail.next
            self.tail.next = None
        else:
            if self.size == self.capacity:
                del self.hm[self.head.next.key]
                if self.head.next == self.tail:
                    self.tail = self.head
                self.head.next = self.head.next.next
                if self.head.next:
                    self.head.next.prev = self.head
            else:
                self.size += 1
            self.hm[key] = self.tail.next = Node(key, value, prev=self.tail)
            self.tail = self.tail.next
