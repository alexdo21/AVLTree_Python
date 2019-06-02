from src.AVLTree import AVLTree

a = AVLTree()

a.insert(25, None);
a.insert(76, None);
a.insert(17, None);
a.insert(63, None);
a.insert(91, None);
a.insert(46, None);
a.insert(45, None);
a.insert(93, None);
a.insert(31, None);
a.insert(77, None);

print(a.get_pre_order_traversal())
print(a.get_post_order_traversal())
print(a.get_level_order_traversal())

a.remove(63)
print(a.get_level_order_traversal())
print(a.get_post_order_traversal())





