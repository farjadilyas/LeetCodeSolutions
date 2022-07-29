"""
  138. Copy List with Random Pointer
  [ Medium ] | [ 49.3% ] -- Solved 29/07/2022 -- [ Linked List, Hash Table ]
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN: 90.22%
  MEMORY USAGE: 82.55%

  Problem Statement:
  - A normal singly linked list with the addition of random pointers on every node that may link to any other Node or
    none at all is given
  - Write a program that creates a deep copy of the given linked list, such that no node involved in the output linked
    list involves a node that was present in the input linked list

  APPROACH: RESPECT THE DEPENDENCY
  - IDEA: There is a dependency between the nodes that are pointing to and the one that is pointed by the random pointer
    - In addition, there is the next pointer dependency as well
    - In short, if we are at a Node, we don't know if the next Node or the random Node have been copied
    - When combined with the fact that the random node is part of the next chain..
    - The order in which new Nodes should be created isn't clear

  - So... there are two clear options:
    - Respect the dependencies one by one and copy all nodes using the next chain
        - Since random nodes can point only to a node that is part of the next chain or is None
        - We can now look up the copied Nodes in the next chain and use them to inform the random pointer
    - Traverse the dependency in the order in which they are encountered
      - Explicitly keep track of the mapping from original node to potentially copied node
      - Do a graph-style traversal, if any node encountered in the traversal has not been copied, copy it, continue to
        traverse

  - SELECT APPROACH
    - Both options have the same O(N) Time Complexity
    - Both have the same space complexity (O(N) if answer is counted)
    - Can go with either, I went with the first one

  - IMPORTANT: Line used to point random pointer of copied list to correct random pointer:
    - node.copied_node.random = node.random.copied_node
    - Intuition: First loop ensures random.copied_node has been set

  - OPTIMIZATION: Remove need for a HashMap (a bit of a hack)
    - The need for a hashmap in both options can be removed by introducing a pointer in the original node to reference
      a potentially copied node
    - Hence, having the original - copy mapping no longer requires a hashmap

  Time Complexity: O(N)
  Space Complexity: O(N) - for deep copied linked list
"""


def copyRandomList(self, head):
    cur = head
    ans = cur_ans = Node(-1)

    # Copy next chain and simultaneously build output linked list
    # Place each copied node as a reference inside the corresponding original node
    while cur:
        cur_ans.next = cur.cp = Node(cur.val, None, None)
        cur_ans = cur_ans.next
        cur = cur.next

    # Point random pointers to the copied nodes that are available with each original node
    cur = head
    while cur:
        if cur.random:
            cur.cp.random = cur.random.cp
        cur = cur.next

    return ans.next
