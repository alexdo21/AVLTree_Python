from src.Exceptions import IllegalNoneKeyException, DuplicateKeyException, KeyNotFoundException
from collections import deque

class AVLTree:
    """
    Class defining a BST that automatically
    maintains its balance using AVL rotations.

    Author: AlexDo

    """
    class AVLNode:
        """
        Inner class defining a node in an AVL tree. Contains a key value pair,
        references to its children, balanceFactor and height of the node.

        Author: Alex Do

        """
        def __init__(self, key, value, left = None, right = None):
            """
            Constructor of an AVL node. Initializes params of node.

            :param key: the key of this node
            :param value: value of this node
            :param left: the reference to the left child
            :param right: the reference to the right child
            """
            self._key = key
            self._value = value
            self._height = 0 # the height rooted at this node
            self._balanceFactor = 0 # the balance factor of this node

    def __init__(self):
        """
        Constructor of an AVL tree. Initializes params of AVL tree.

        """
        self._root = None # the root of this AVL tree
        self._num_keys = 0 # the number of keys in this tree

    def num_keys(self):
        """
        :return: the number of keys
        """
        return self._num_keys

    def update(self, node):
        """
        Updates the height and balance factor of each node as it is inserted/removed from a BST.
        Especially used to rebalance the node in an AVL tree.

        :param node: the node to update
        :return: void
        """

        # updates the height of each child subtree
        leftHeight = -1 if node.left is None else node.left.height
        rightHeight = -1 if node.right is None else node.right.height

        # height is the greatest between left height and right height
        node.height = 1 + leftHeight if leftHeight > rightHeight else 1 + rightHeight

        # updates balance factor given new heights of each child subtree
        node.balanceFactor = leftHeight - rightHeight

    def contains(self, key):
        """
        Returns true if the key is in the data structure If key is None, raise IllegalNoneKeyException
        Returns false if key is not None and is not present.

        :param key: key to check in AVL tree
        :return: true if key is found in the AVL tree
        """
        if self.contains_helper(self._root, key) is not None: return True
        else: return False

    def contains_helper(self, node, key):
        """
        Recursive contains helper

        :param node: node currently checking
        :param key: the key to check against
        :return: true if key is found in the AVL tree
        """
        if node is None: return None
        if key is None: return IllegalNoneKeyException()
        if node.key is key: return node

        # if key is greater than current node's key, traverse right else traverse left
        if key > node.key: return self.contains_helper(node.right, key)
        else: return self.contains_helper(node.left, key)

    def get_height(self):
        """
        Returns the height of this BST. H is defined as the number of levels in the tree.

        If root is None, return 0 If root is a leaf, return 1 Else return 1 + max( height(root.left),
        height(root.right) )

        Examples: A BST with no keys, has a height of zero (0). A BST with one key, has a height of one
        (1). A BST with two keys, has a height of two (2). A BST with three keys, can be balanced with
        a height of two(2) or it may be linear with a height of three (3) ... and so on for tree with
        other heights.

        :return: the number of levels that contain keys in this AVL tree
        """
        return self.height_helper(self._root)

    def height_helper(self, node):
        """
        Recursive height helper method
        :param node: node currently checking
        :return: the height of this AVL tree
        """
        if node is None: return 0

        # get heights of respective subtrees
        leftHeight = self.height_helper(node.left)
        rightHeight = self.height_helper(node.right)

        # height of tree is the max height between two subtrees
        return leftHeight + 1 if leftHeight > rightHeight else rightHeight + 1

    def get(self, key):
        """
        Returns the value associated with the specified key Does not remove key or decrease number of
        keys If key is None, raise IllegalNoneKeyException If key is not found, raise
        KeyNotFoundException().

        :param key: the key to get from AVL tree
        :return: the value of the key found
        """
        return self.get_helper(self._root, key).value

    def get_helper(self, node, key):
        """
        Recursive get helper method to find and return the specified node in the AVL tree.

        :param node: node currently checking
        :param key: key to check against
        :return: the node to get
        """
        if key is None: raise IllegalNoneKeyException()
        elif node.left is None and node.right is None and node.key is not key:
            raise KeyNotFoundException

        # if node is found
        if node.key is key: return node
        elif key > node.key: # if key is greater than current node, traverse right
            node = self.get_helper(node.right, key)
        else: # if key is less than current node, traverse left
            node = self.get_helper(node.left, key)

        return node

    def get_in_order_traversal(self):
        """
        Returns the keys of the data structure in sorted order. In the case of binary search trees, the
        visit order is: L V R

        If the SearchTree is empty, an empty list is returned.

        :return: list of keys in-order
        """
        list = []
        self.x_order_helper(list, self._root, 2)
        return list

    def get_pre_order_traversal(self):
        """
        Returns the keys of the data structure in sorted order. In the case of binary search trees, the
        visit order is: V L R

        If the SearchTree is empty, an empty list is returned.

        :return: list of keys pre-order
        """
        list = []
        self.x_order_helper(list, self._root, 1)
        return list

    def get_post_order_traversal(self):
        """
        Returns the keys of the data structure in sorted order. In the case of binary search trees, the
        visit order is: L R V

        If the SearchTree is empty, an empty list is returned.

        :return: list of keys post-order
        """
        list = []
        self.x_order_helper(list, self._root, 3)
        return list

    def get_level_order_traversal(self):
        """
        Returns the keys of the data structure in level-order traversal order.

        The root is first in the list, then the keys found in the next level down, and so on.

        If the SearchTree is empty, an empty list is returned.

        :return: list of keys in level-order
        """
        list = [] # list to return level order traversal
        if self._root is None: return list

        # queue implemented level order traversal
        queue = deque()
        queue.append(self._root) # add the root to start

        while True:
            keyCount = len(queue) # initial size of the level to add
            if keyCount == 0: break

            while keyCount > 0:
                current = queue.popleft() # add level nodes into queue
                list.append(current.key) # add nodes into list

                # add other level nodes into queue while children aren't None
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)

                keyCount -= 1

        # list contains all nodes of AVL tree
        return list


    def x_order_helper(self, list, node, x):
        """
        Recursive traversal order helper depending on traversal type.
        1 - preorder,
        2 - inorder,
        3 - postorder.

        :param list: updates reference to list object called form respective traversal method
        :param node: the current node being traversed
        :param x: the number referring to the type of traversal
        :return: void
        """
        if node is None: return

        # do traversal depending on x
        if x == 1:
            list.append(node.key)
            self.x_order_helper(list, node.left, 1)
            self.x_order_helper(list, node.right, 1)
        elif x == 2:
            self.x_order_helper(list, node.left, 2)
            list.append(node.key)
            self.x_order_helper(list, node.right, 2)
        elif x == 3:
            self.x_order_helper(list, node.left, 3)
            self.x_order_helper(list, node.right, 3)
            list.append(node.key)


    def insert(self, key, value):
        """
        Add the key,value pair to the data structure and increase the number of keys. If key is None,
        raise IllegalNoneKeyException; If key is already in data structure, raise
        DuplicateKeyException().

        :param key: the key to be inserted
        :param value: the value of key to be inserted
        :return: void
        """
        self._root = self.insert_avl(self._root, key, value)
        self._num_keys += 1

    def insert_avl(self, node, key, value):
        """
        Recursive insert helper method for an AVL tree, updates height, balance factor and rebalances
        the node inserted.

        :param node: the node currently being checked
        :param key: the key to check against being inserted
        :param value: the value of the key to be inserted
        :return: the node inserted after rebalancing and updating
        """
        if key is None: raise IllegalNoneKeyException()
        if node is None:
            return self.AVLNode(key, value, None, None)

        # traverse left if key is less than node
        if key < node.key:
            node.left = self.insert_avl(node.left, key, value)
        elif key > node.key: # traverse right
            node.right = self.insert_avl(node.right, key, value)
        else: raise DuplicateKeyException() # key already exists

        self.update(node)
        return self.rebalance(node)

    def left_rotation(self, node):
        """
        Left rotates the rooted node with its right child.

        :param node: the node being rotated on
        :return: the new rooted node
        """
        newParent = node.right # new parent node to swap
        node.right = newParent.left # should be None
        newParent.left = node # swaps new parent and node to left child of new parent
        self.update(node) # update the changed node's height
        self.update(newParent) # update the new parent's height

        return newParent

    def right_rotation(self, node):
        """
        Right rotates the rooted node with its left child.

        :param node: the node being rotated on
        :return: the new rooted node
        """
        newParent = node.left # new parent node to swap
        node.left = newParent.right # should be None
        newParent.right = node # swaps new parent and node to right child of new parent
        self.update(node) # update the changed node's height
        self.update(newParent) # update the new parent's height

        return newParent

    def rebalance(self, node):
        """
        Rebalance helper method for insert and remove in the AVL tree. 4 possible cases: 1. if
        node is right heavy, left rotation 2. if node is right heavy and is slightly left heavy,
        right-left rotation 3. if node is left heavy, right rotation 4. if node is left heavy and is
        slightly right heavy, left-right rotation.

        :param node: the node being checked
        :return: the rebalanced node
        """
        # left subtree heavy
        if node.balanceFactor == 2:
            # left node right heavy
            if node.left.balanceFactor <= 0:
                node.left = self.left_rotation(node.left)
                return self.right_rotation(node)
            else: return self.right_rotation(node) # left left heavy
        # right subtree heavy
        elif node.balanceFactor == -2:
            # right node left heavy
            if node.right.balanceFactor >= 0:
                node.right = self.right_rotation(node.right)
                return self.left_rotation(node)
            else: return self.left_rotation(node) # right right heavy

        return node

    def remove(self, key):
        """
        Overrides remove method of AVL tree to account for auto rebalancing of AVL tree.

        :param key: key to be removed
        :return: true if key has been properly removed from tree
        """
        self.remove_avl(self._root, key) # remove the node of specified key

        # if tree no longer contians key, then it has been removed properly
        if self.contains(key) is False:
            self._num_keys -= 1 # decrement keys in tree
            return True
        else:
            return False


    def remove_avl(self, node, key):
        """
        Recursive remove helper method for an AVL tree, updates height, balance factor and
        rebalances the position of the node removed.

        :param node: the node currently being checked
        :param key: the key being checked against
        :return: the node removed after updating and rebalancing node
        """
        if key is None: raise IllegalNoneKeyException()
        elif self.contains(key) is False: raise KeyNotFoundException() # key isn't in tree

        # if key is less than node, traverse left
        if key < node.key:
            node.left = self.remove_avl(node.left, key)
        # if key is greater than node, traverse right
        elif key > node.key:
            node.right = self.remove_avl(node.right, key)
        else:
            # if deleting root with one child, non-None root child becomes the new root
            if node is self._root:
                if node.left is None:
                    self._root = node.right
                    return node
                elif node.right is None:
                    self._root = node.left
                    return node

            # node has one child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else: # node has two children
                # swap key and value of node to be deleted and the inorder predecessor
                temp = self.greatest_left(node.left)
                node.value = self.get(temp)
                node.key = temp
                # remove swapped node
                node.left = self.remove_avl(node.left, node.key)

        self.update(node)
        return self.rebalance(node)

    def greatest_left(self, node):
        """
        Protected accessible recursive helper method to find the inorder predecessor of the current
        node for AVL tree.

        :param node: node currently being checked
        :return: the key of the inorder predecessor
        """
        if node.right is None: return node.key # key is found
        else: return self.greatest_left(node.right) # traverse down left subtree moving right

    def get_key_at_root(self):
        """
        :return: key found at root node, or None
        """
        return self._root.key

    def get_key_of_left_child_of(self, key):
        """
        Tries to find a node with a key that matches the specified key. If a matching node is found, it
        returns the returns the key that is in the left child. If the left child of the found node is
        None, returns None.

        :param key: a key to search for
        :return: the key that is in the left child of the found key
        """
        if key is None: raise IllegalNoneKeyException()
        elif self.contains(key) is False: raise KeyNotFoundException() # key doesn't exist
        else: # retrieve node
            node = self.get_helper(self._root, key)
            # left child of node found is None
            if node.left is None:
                return None
            else:
                return node.left.key

    def get_key_of_right_child_of(self, key):
        """
        Tries to find a node with a key that matches the specified key. If a matching node is found, it
        returns the returns the key that is in the right child. If the right child of the found node is
        None, returns None.

        :param key:
        :return:
        """
        if key is None: raise IllegalNoneKeyException()
        elif self.contains(key) is False: raise KeyNotFoundException() # key doesn't exist
        else: # retrieve node
            node = self.get_helper(self._root, key)
            # right child of node found is None
            if node.right is None:
                return None
            else:
                return node.right.key






