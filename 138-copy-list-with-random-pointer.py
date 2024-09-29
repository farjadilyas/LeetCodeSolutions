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


class RecursiveSolution:
    """
    Treats input linked list like a graph, conducts DFS on it while keeping track of visited nodes to correctly
    resolve cyclic-dependencies
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {None: None}

        def recurse(current):
            if current in hm:
                return hm[current]
            copy_of_current = Node(x=current.val)
            hm[current] = copy_of_current
            copy_of_current.next = recurse(current.next)
            copy_of_current.random = recurse(current.random)
            return copy_of_current
        return recurse(head)


class IterativeSolution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {None: None}
        # Create copies for each node and store old -> new mapping
        current = head
        while current:
            hm[current] = Node(current.val, current.next, current.random)
            current = current.next
        # Now that all new copies are created, add the links
        # This way you don't have to bother with resolving depdendencies in the right order
        current = head
        while current:
            hm[current].next = hm[current.next]
            hm[current].random = hm[current.random]
            current = current.next
        return hm.get(head)


class OptimalInterweavingSolution:
    """
    Modify the input list, place copies of each original node next to the original node in the original list so that
    the list is interweaved with new-old-new-... nodes

    Update the copies' random pointers first
    Then update their next pointers as needed

    This solution basically sets up the linked list so that you can get the copy of any original node by going to the
    next node. So this avoids the need for a hashmap and achieves constant space complexity
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Insert copy of each original node after it in the original list
        current = head
        while current:
            current.next = Node(x=current.val, next=current.next)
            current = current.next.next

        def get_copy(node):
            return node.next

        # Set the random pointers for the copied nodes
        current = head
        while current:
            get_copy(current).random = get_copy(current.random)
            current = current.next.next

        # Create a list out of the copied pointers by changing their next ptr
        current = head
        while current:
            next_original_node = current.next.next
            get_copy(current).next = get_copy(next_original_node)
            current = next_original_node
        return get_copy(head)
