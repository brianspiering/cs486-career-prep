#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""A demonstration implementation of a Binary Search Tree (BST)
"""

class Node:
    """Base Binary Tree Data Structure"""
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    """https://en.wikipedia.org/wiki/Binary_search_tree"""
    def __init__(self, root=None):
        self.root = root

    def insert(self, item):
        """Insert an element into the bst."""
        if self.root is None:
            self.root = Node(item)
        else:
            new_node = self.root
            while new_node is not None:
                if item < new_node.data:
                    if new_node.left is None:
                        new_node.left = Node(item)
                        return
                    else:
                        new_node = nd.left
                else: # Assume greater than or equal
                    if new_node.right is None:
                        new_node.right = Node(item)
                        return
                    else:
                        new_node = nd.right

    def search_iterative(self, needle):
        """Iteratively search an element."""
        if self.root is None:
            return False
        else:
            current_node = self.root
            while current_node is not None:
                if current_node.data == needle:
                    return True
                elif current_node.data < needle:
                    current_node = current_node.right
                else:
                    current_node = current_node.left
            return False

    def search_recursive(self, node, needle):
        """Recursively search an element."""
        if node is None:
            return False
        else:
            if node.data == needle:
                return True
            elif node.data < needle:
                return self.search_recursive(node.right, needle)
            else:
                return self.search_recursive(node.left, needle)

    @property
    def size(self, node):
        """Fetch the number of items in the bst."""
        if node is None:
            return 0
        else:
            return 1 + self.size(node.left) + self.size(node.right)

    @property        
    def max_depth(self, node):
        """Find the maximum depth."""
        if node is None:
            return 0
        else:
            return 1 + max(self.max_depth(node.left), self.max_depth(node.right))

    def inorder(self, node):
        """Inorder traversal; Data should be sorted from low to high"""
        return (self.inorder(node.left)    # If possible, always traverse left
                + [node.data]              # If data, put it in list
                + self.inorder(node.right) # Otherwise traverse right
                ) if node else []

    def preorder(self, node):
        """Pre-order Traversal."""
        if node:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        """Post-order Traversal."""
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

    @property        
    def min(self, node):
        """Get the minimum value."""
        if node.left is None:
            return node.data
        else:
            return self.get_min(node.left)

    @property
    def max(self, node):
        """Get the maximum value."""
        if self.root is None:
            return "Tree is empty."
        else:
            if node.right is None:
                return node.data
            else:
                return self.get_max(node.right)

    def level_width(self, node, k):
        """Return the number of nodes in level k."""
        if node is None:
            return 0
        elif k == 1:
            return 1
        elif k > 1:
            return self.level_width(node.left, k-1) + self.level_width(node.right, k-1)

    @property
    def max_width(self):
        """Return the maximum width of the tree."""
        if self.root is None:
            return 0
        else:
            nd = self.root
            width = 0
            height = self.max_depth(self.root)
            for x in range(1, height+11): # TODO: Why is that 11?
                lwidth = self.level_width(self.root, height-x)
                if lwidth > width:
                    width = lwidth

            return lwidth

    def nodes_at_distance(self, node, k):
        """Print all nodes at distance k from the root."""
        if node is None:
            return
        elif k == 0:
            print(f"{node.data} ")
        else:
            self.nodes_at_distance(node.left, k-1)
            self.nodes_at_distance(node.right, k-1)


    def kth_smallest(self, node, k):
        """Kth smallest element of the bst."""
        if k == 0:
            print(node.data)
            return
        else:
            kth_smallest(node.left)
            kth_smallest(node.right)

    @property        
    def n_leafs(self, node):
        """Count the number of leaf nodes."""
        if node is None:
            return 0
        elif (node.left is None) and (node.right is None):
            return 1
        else:
            return self.count_leafs(node.left) + self.count_leafs(node.right)

    def remove(self, node, item):
        """Remove an element from bst."""
        if node is None:
            return
        if item < node.data:
            self.remove(node.left, item)
        elif item > node.data:
            self.remove(node.right, item)
        else:
            if node.left is None:
                tmp = node.right
                node = None
            elif node.right is None:
                tmp = node.left
                node = None
            else:
                tmp = self.get_min(node.right)
                node.data = tmp
                node.right = self.remove(node.right, tmp)

def test_bst():
    # Setup
    tree = BinarySearchTree()
    for n in [8, 3, 10, 14, 6, 13, 7, 4, 1]:
        tree.insert(n)

    # Test inserts    
    assert tree.root.data == 8
    assert tree.root.left.data == 3
    assert tree.root.right.data == 10
    assert tree.root.left.left.data == 1

    # Test search
    assert tree.search_iterative(1)
    assert tree.search_recursive(tree.root, 1)
    assert not tree.search_iterative(-1)
    assert not tree.search_recursive(tree.root, -1) 
    assert not tree.search_iterative(2)
    assert not tree.search_recursive(tree.root, 2)

    # Test inorder traversal
    assert inorder_results == sorted(inorder_results)

def main():
    test_bst()

if __name__ == '__main__': main()