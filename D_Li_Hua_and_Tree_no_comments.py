from __future__ import division, print_function
import os,sys
from io import BytesIO, IOBase
from random import randint, randrange
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip
from math import ceil, floor, factorial, log10
from bisect import bisect_left, bisect_right
from collections import deque, Counter, defaultdict
M=1000000007
INF = 9223372036854775807
PI = 3.141592653589793
R = randrange(2, 1 << 32)
import warnings
from enum import Enum
class Extra:
    __name__ = "extra.Extra()"
    def _validate_item(self, item):
        if item is None:
            raise ValueError(
                f"Can't use `None` as an element within `{self.__name__}`!!"
            )
        elif isinstance(item, Extra):
            raise TypeError(
                f"Can't use `{self.__name__}` with `{item.__name__}`!!"
            )
class TreeNode(Extra):
    __name__ = "extra.TreeNode()"
    def __init__(self, value):
        super()._validate_item(value)
        if type(value) == str:
            value = value.replace("\n", "\\n")
        self._data = value
        self._children = []
    def get_data(self):
        return self._data
    def get_children(self):
        return self._children
    def set_child(self, child):
        if not isinstance(child, TreeNode):
            raise TypeError(
                f"You can't set a child unless it's an `{self.__name__}` "
                + "object!!"
            )
        self._children.append(child)
    def set_children(self, lst):
        if not hasattr(lst, "__iter__"):
            raise TypeError("Given object isn't iterable!!")
        children = []
        for item in lst:
            if not isinstance(item, TreeNode):
                raise TypeError(
                    f"You can't set a child unless it's an `{self.__name__}` "
                    + "object!!"
                )
            children.append(item)
        self._children = children
    def is_leaf(self):
        return self.get_children() == []
    def __repr__(self):
        return f"TreeNode({self._data})"
    def _represent(self):
        return str(self._data)
    @staticmethod
    def swap(node1, node2):
        if not isinstance(node1, TreeNode) or not isinstance(node2, TreeNode):
            raise TypeError(
                "Incompitable objects' type preventing swapping!!"
            )
        node1._data, node2._data = node2._data, node1._data
class Tree(Extra):
    __name__ = "extra.Tree()"
    def __init__(self):
        self._root = None
    @staticmethod
    def __form_tree_from_path(parent_abs_path, curr_folder):
        assert type(parent_abs_path) == str
        assert type(curr_folder) == str
        node = TreeNode(curr_folder)
        abs_path = os.path.join(parent_abs_path, curr_folder)
        if os.path.isdir(abs_path):
            for child in sorted(os.listdir(abs_path)):
                node.set_child(Tree.__form_tree_from_path(abs_path, child))
        return node
    @staticmethod
    def from_path(path):
        if type(path) != str:
            raise TypeError("Invalid path was given!!")
        elif not os.path.exists(path):
            raise ValueError("Invalid path was given!!")
        t = Tree()
        abs_path = os.path.abspath(path)
        parent, folder = os.path.split(abs_path)
        t._root = Tree.__form_tree_from_path(parent, folder)
        return t
    def __count_nodes(self, start_node):
        assert isinstance(start_node, TreeNode)
        total_nodes = 1
        for child in start_node.get_children():
            total_nodes += self.__count_nodes(child)
        return total_nodes
    def __len__(self):
        if self.is_empty():
            return 0
        return self.__count_nodes(self._root)
    def is_empty(self):
        return self._root is None
    def __print_subtree(self, start_node, lines, is_last_child, seq=[]):
        assert isinstance(start_node, TreeNode)
        assert type(lines) == list
        assert type(is_last_child) == bool
        assert type(seq) == list
        line = []
        if seq:
            for is_parent_last_child in seq[1:]:
                (line.append("  ")
                    if is_parent_last_child
                    else line.append("│ "))
            line.append("└─") if is_last_child else line.append("├─")
            (line.append("┬ ")
                if start_node.get_children()
                else line.append("─ "))
        line.append(start_node._represent())
        lines.append("".join(line))
        my_seq = seq.copy()
        my_seq.append(is_last_child)
        children = start_node.get_children()
        num_children = len(children)
        for idx in range(num_children):
            child = children[idx]
            is_last_child = True if idx == num_children - 1 else False
            self.__print_subtree(child, lines, is_last_child, my_seq)
        return lines
    def _print_empty_tree(self):
        assert self.is_empty()
        return "--"
    def __repr__(self):
        if self.is_empty():
            return self._print_empty_tree()
        elif self._root.get_children():
            return "\n".join(self.__print_subtree(self._root, [], False))
        else:
            return str(self._root.get_data())
    def _get_height(self, start_node):
        assert isinstance(start_node, TreeNode)
        height = 0
        for child in start_node.get_children():
            height = max(height, 1 + self._get_height(child))
        return height
    def get_height(self):
        if self.is_empty():
            return 0
        return self._get_height(self._root)
    def _get_depth(self, start_node):
        assert isinstance(start_node, TreeNode)
        return self._get_height(self._root) - self._get_height(start_node)
    def get_depth(self):
        if self.is_empty():
            return 0
        return self._get_depth(self._root)
    def _count_leaf_nodes(self, start_node):
        assert isinstance(start_node, TreeNode)
        if start_node.is_leaf():
            return 1
        total_nodes = 0
        for child in start_node.get_children():
            total_nodes += self._count_leaf_nodes(child)
        return total_nodes
    def count_leaf_nodes(self):
        if self.is_empty():
            return 0
        return self._count_leaf_nodes(self._root)
    def __iter__(self):
        if not self.is_empty():
            current_nodes = [self._root]
            while len(current_nodes) > 0:
                next_nodes = []
                for node in current_nodes:
                    yield node.get_data()
                    next_nodes.extend(node.get_children())
                current_nodes = next_nodes
    def to_list(self):
        if self.is_empty():
            return []
        return [node for node in self]
    def _search(self, value):
        queue = [self._root]
        while queue:
            curr_node = queue.pop()
            if curr_node.get_data() == value:
                return curr_node
            queue.extend(curr_node.get_children())
        return None
    def __contains__(self, value):
        found_node = self._search(value)
        return True if found_node is not None else False
    def _get_nodes_per_level(self, start_node, level, nodes, save_data=True):
        assert isinstance(start_node, TreeNode)
        assert type(level) == int and level >= 0
        assert type(nodes) == list
        if start_node is not None:
            if level == len(nodes):
                nodes.append([])
            if save_data:
                nodes[level].append(start_node.get_data())
            else:
                nodes[level].append(start_node)
            for child in start_node.get_children():
                self._get_nodes_per_level(child,
                                          level + 1,
                                          nodes,
                                          save_data)
        return nodes
    def get_nodes_per_level(self):
        if self.is_empty():
            return []
        return self._get_nodes_per_level(self._root, 0, [], True)
    def clear(self):
        self.__init__()
class BinaryTreeNode(TreeNode):
    __name__ = "extra.BinaryTreeNode()"
    def __init__(self, value):
        super().__init__(value)
        self._left = self._right = None
        del self._children
    def get_data(self):
        return super().get_data()
    def get_left(self):
        return self._left
    def get_right(self):
        return self._right
    def get_children(self):
        children = []
        if self._left is not None:
            children.append(self._left)
        if self._right is not None:
            children.append(self._right)
        return children
    def set_children(self, lst):
        raise NotImplementedError(
            "You can use `set_left()` or `set_right()` methods instead!!"
        )
    def set_left(self, new_node):
        if not isinstance(new_node, BinaryTreeNode):
            raise TypeError(
                f"You can't set a child unless it's an `{self.__name__}` "
                + "object!!"
            )
        self._left = new_node
    def set_right(self, new_node):
        if not isinstance(new_node, BinaryTreeNode):
            raise TypeError(
                f"You can't set a child unless it's an `{self.__name__}` "
                + "object!!"
            )
        self._right = new_node
    def is_leaf(self):
        return self.get_children() == []
    def has_one_child(self):
        return (
            not super().is_leaf()
            and (self._left is None or self._right is None)
        )
    def __repr__(self):
        return f"BinaryTreeNode({self._data})"
class BinaryTree(Tree):
    _basic_node = BinaryTreeNode
    __name__ = "extra.BinaryTree()"
    def __init__(self):
        super().__init__()
    @staticmethod
    def __create_subtree(lst):
        if type(lst) not in {list, tuple}:
            lst = [lst]
        if len(lst) == 0 or len(lst) >= 4:
            raise ValueError(f"Given {type(lst)} can not be parsed!!")
        try:
            parent = BinaryTreeNode(lst[0])
            parent.set_left(BinaryTree.__create_subtree(lst[1]))
            parent.set_right(BinaryTree.__create_subtree(lst[2]))
        except IndexError:
            pass
        return parent
    @staticmethod
    def parse(lst):
        if type(lst) not in {list, tuple}:
            raise TypeError("Given object must be a `list` or `tuple`!!")
        bt = BinaryTree()
        bt._root = BinaryTree.__create_subtree(lst)
        return bt
    def __len__(self):
        return super().__len__()
    def is_empty(self):
        return super().is_empty()
    def _print_subtree(self, root, curr_index):
        if root is None:
            return [], 0, 0, 0
        else:
            line1 = []
            line2 = []
            node_repr = root._represent()
            new_root_width = gap_size = len(node_repr)
            l_box, l_box_width, l_root_start, l_root_end = self._print_subtree(
                root.get_left(), 2 * curr_index + 1
            )
            r_box, r_box_width, r_root_start, r_root_end = self._print_subtree(
                root.get_right(),
                2 * curr_index + 2,
            )
            if l_box_width > 0:
                l_root = (l_root_start + l_root_end) // 2 + 1
                line1.append(" " * (l_root + 1))
                line1.append("_" * (l_box_width - l_root))
                line2.append(" " * l_root + "/")
                line2.append(" " * (l_box_width - l_root))
                new_root_start = l_box_width + 1
                gap_size += 1
            else:
                new_root_start = 0
            line1.append(node_repr)
            line2.append(" " * new_root_width)
            if r_box_width > 0:
                r_root = (r_root_start + r_root_end) // 2
                line1.append("_" * r_root)
                line1.append(" " * (r_box_width - r_root + 1))
                line2.append(" " * r_root + "\\")
                line2.append(" " * (r_box_width - r_root))
                gap_size += 1
            new_root_end = new_root_start + new_root_width - 1
            gap = " " * gap_size
            new_box = ["".join(line1), "".join(line2)]
            for i in range(max(len(l_box), len(r_box))):
                l_line = l_box[i] if i < len(l_box) else " " * l_box_width
                r_line = r_box[i] if i < len(r_box) else " " * r_box_width
                new_box.append(l_line + gap + r_line)
            return new_box, len(new_box[0]), new_root_start, new_root_end
    def _print_empty_tree(self):
        return "/ \\"
    def __repr__(self):
        if self.is_empty():
            return self._print_empty_tree()
        lines, _, _, _ = self._print_subtree(self._root, 0)
        return "\n".join((line.rstrip() for line in lines[:-1]))
    def get_height(self):
        return super().get_height()
    def get_depth(self):
        return super().get_depth()
    def count_leaf_nodes(self):
        return super().count_leaf_nodes()
    def is_balanced(self):
        if self.is_empty():
            warnings.warn(
                f"You are checking the balance of an empty `{self.__name__}`",
                UserWarning,
            )
            return True
        left_depth = (
            0
            if self._root.get_left() is None
            else 1 + super()._get_depth(self._root.get_left())
        )
        right_depth = (
            0
            if self._root.get_right() is None
            else 1 + super()._get_depth(self._root.get_right())
        )
        return abs(left_depth - right_depth) <= 1
    def is_perfect(self):
        if self.is_empty():
            warnings.warn(
              f"You are checking the perfection of an empty `{self.__name__}`",
              UserWarning,
            )
            return True
        for level, nodes in enumerate(self.get_nodes_per_level()):
            if 2 ** level != len(nodes):
                return False
        return True
    def __is_subtree_strict(self, start_node):
        assert start_node is None or isinstance(start_node, self._basic_node)
        left_node = start_node.get_left()
        right_node = start_node.get_right()
        if left_node is None and right_node is None:
            return True
        elif left_node is not None and right_node is None:
            return False
        elif left_node is None and right_node is not None:
            return False
        else:
            return self.__is_subtree_strict(
                start_node.get_left()
            ) and self.__is_subtree_strict(start_node.get_right())
    def is_strict(self):
        if self.is_empty():
            warnings.warn(
              f"You are checking the strictness of an empty `{self.__name__}`",
              UserWarning,
            )
            return True
        return self.__is_subtree_strict(self._root)
    def __iter__(self):
        return super().__iter__()
    def to_list(self):
        return super().to_list()
    def get_nodes_per_level(self):
        return super().get_nodes_per_level()
    def __preorder_traverse(self, start_node):
        assert start_node is None or isinstance(start_node, self._basic_node)
        nodes = []
        if start_node is not None:
            nodes.append(start_node.get_data())
            if start_node.get_left():
                nodes.extend(self.__preorder_traverse(start_node.get_left()))
            if start_node.get_right():
                nodes.extend(self.__preorder_traverse(start_node.get_right()))
        return nodes
    def preorder_traverse(self):
        return self.__preorder_traverse(self._root)
    def depth_first_traverse(self):
        return self.__preorder_traverse(self._root)
    def __postorder_traverse(self, start_node):
        assert start_node is None or isinstance(start_node, self._basic_node)
        nodes = []
        if start_node is not None:
            if start_node.get_left():
                nodes.extend(self.__postorder_traverse(start_node.get_left()))
            if start_node.get_right():
                nodes.extend(self.__postorder_traverse(start_node.get_right()))
            nodes.append(start_node.get_data())
        return nodes
    def postorder_traverse(self):
        return self.__postorder_traverse(self._root)
    def __inorder_traverse(self, start_node):
        assert start_node is None or isinstance(start_node, self._basic_node)
        nodes = []
        if start_node is not None:
            if start_node.get_left():
                nodes.extend(self.__inorder_traverse(start_node.get_left()))
            nodes.append(start_node.get_data())
            if start_node.get_right():
                nodes.extend(self.__inorder_traverse(start_node.get_right()))
        return nodes
    def inorder_traverse(self):
        return self.__inorder_traverse(self._root)
    def breadth_first_traverse(self):
        return super().to_list()
    def traverse(self, method="inorder"):
        trav_methods = {
            "inorder",
            "postorder",
            "preorder",
            "depth-first",
            "breadth-first",
        }
        if type(method) != str:
            raise TypeError(
                "Given traverse method has to be one of these:\n"
                + str(trav_methods)
            )
        method = method.lower()
        if method == "inorder":
            return self.inorder_traverse()
        elif method == "postorder":
            return self.postorder_traverse()
        elif method in {"preorder", "depth-first"}:
            return self.preorder_traverse()
        elif method == "breadth-first":
            return self.breadth_first_traverse()
        else:
            raise ValueError(
                "Given traverse method has to be one of these:\n"
                + str(trav_methods)
            )
    def get_leftside_view(self):
        if self.is_empty(): return []
        levels = {0: self._root._data}
        stack = [(self._root, 0)] 
        while(stack):
            curr_node, depth = stack.pop()
            levels[depth] = curr_node._data
            if curr_node._left is not None:
                stack.append((curr_node._left, depth+1))
            if curr_node._right is not None:
                stack.append((curr_node._right, depth+1))
        return list(levels.values())
    def get_rightside_view(self):
        if self.is_empty(): return []
        levels = {0: self._root._data}
        stack = [(self._root, 0)] 
        while(stack):
            curr_node, depth = stack.pop()
            levels[depth] = curr_node._data
            if curr_node._right is not None:
                stack.append((curr_node._right, depth+1))
            if curr_node._left is not None:
                stack.append((curr_node._left, depth+1))
        return list(levels.values())
    def __contains__(self, value):
        return super().__contains__(value)
    def _invert_subtree(self, curr_node):
        if curr_node is not None:
            curr_node._left, curr_node._right = (
                self._invert_subtree(curr_node._right), 
                self._invert_subtree(curr_node._left)
            )
        return curr_node
    def invert(self):
        self._root = self._invert_subtree(self._root)
    def clear(self):
        super().clear()
class BSTNode(BinaryTreeNode):
    __name__ = "extra.BSTNode()"
    def __init__(self, value):
        if type(value) not in {int, float}:
            raise TypeError(f"`{self.__name__}` contains only numbers!!")
        super().__init__(value)
        self._parent = None
    def get_parent(self):
        return self._parent
    def get_grand_parent(self):
        return self._parent.get_parent() if self._parent is not None else None
    def get_uncle(self):
        parent = self._parent
        if parent is None:
            return None
        grand_parent = parent.get_parent()
        if grand_parent is None:
            return None
        return (
            grand_parent.get_right()
            if parent.is_left_child()
            else grand_parent.get_left()
        )
    def get_sibling(self):
        parent = self._parent
        if parent is None:
            return None
        return (
            parent.get_right()
            if self.is_left_child()
            else parent.get_left()
        )
    def set_left(self, new_node):
        if not (new_node is None or isinstance(new_node, BSTNode)):
            raise TypeError(f"Can't set {type(new_node)} as a left child!!")
        self._left = new_node
        if new_node is not None:
            self._left._parent = self
    def set_right(self, new_node):
        if not (new_node is None or isinstance(new_node, BSTNode)):
            raise TypeError(f"Can't set {type(new_node)} as a right child!!")
        self._right = new_node
        if new_node is not None:
            self._right._parent = self
    def set_parent(self, new_node):
        if not (new_node is None or isinstance(new_node, BSTNode)):
            raise TypeError(
                f"Can't set {type(new_node)} as a child's parent!!"
            )
        self._parent = new_node
    def is_left_child(self):
        return self._parent.get_data() > self.get_data()
    def __repr__(self):
        return f"BSTNode({self._data})"
class BST(BinaryTree):
    _basic_node = BSTNode
    __name__ = "extra.BST()"
    def __init__(self, iterable=None):
        super().__init__()
        self._length = 0
        if iterable is None:
            return
        elif not hasattr(iterable, "__iter__"):
            raise TypeError("The given object isn't iterable!!")
        else:
            for item in iterable:
                self.insert(item)
    def _validate_item(self, item):
        super()._validate_item(item)
        if type(item) not in {int, float}:
            raise TypeError(f"`{self.__name__}` accepts only numbers!!")
    def __len__(self):
        return self._length
    def is_empty(self):
        return super().is_empty()
    def _get_max_node(self, start_node):
        assert isinstance(start_node, self._basic_node)
        if start_node.get_right() is None:
            return start_node
        else:
            return self._get_max_node(start_node.get_right())
    def get_max(self):
        if self.is_empty():
            raise IndexError(
                f"Can't get the maximum value of an empty `{self.__name__}`"
            )
        max_node = self._get_max_node(self._root)
        return max_node.get_data()
    def _get_min_node(self, start_node):
        assert isinstance(start_node, self._basic_node)
        if start_node.get_left() is None:
            return start_node
        else:
            return self._get_min_node(start_node.get_left())
    def get_min(self):
        if self.is_empty():
            raise IndexError(
                f"Can't get the minimum value of an empty `{self.__name__}`"
            )
        min_node = self._get_min_node(self._root)
        return min_node.get_data()
    def _search(self, find_val, start_node):
        assert isinstance(start_node, self._basic_node)
        assert type(find_val) in {float, int}
        if find_val == start_node.get_data():
            return start_node
        elif find_val < start_node.get_data():
            if start_node.get_left():
                return self._search(find_val, start_node.get_left())
            else:
                return start_node
        else:
            if start_node.get_right():
                return self._search(find_val, start_node.get_right())
            else:
                return start_node
    def __contains__(self, find_val):
        if self.is_empty() or type(find_val) not in {int, float}:
            return False
        found_node = self._search(find_val, self._root)
        return found_node.get_data() == find_val
    def _insert_node(self, start_node, inserted_node):
        assert isinstance(start_node, self._basic_node)
        assert (
            inserted_node is None
            or isinstance(inserted_node, self._basic_node)
        )
        value = inserted_node.get_data()
        if value == start_node.get_data():
            warnings.warn(
                f"`{value}` already exists in `{self.__name__}`", UserWarning
            )
            return start_node
        elif value < start_node.get_data():
            if start_node.get_left():
                return self._insert_node(start_node.get_left(), inserted_node)
            else:
                start_node.set_left(inserted_node)
                self._length += 1
                return inserted_node
        else:
            if start_node.get_right():
                return self._insert_node(start_node.get_right(), inserted_node)
            else:
                start_node.set_right(inserted_node)
                self._length += 1
                return inserted_node
    def _insert_value(self, start_node, value):
        assert isinstance(start_node, self._basic_node)
        assert type(value) in {float, int}
        inserted_node = self._basic_node(value)
        return self._insert_node(start_node, inserted_node)
    def _insert(self, value):
        assert (
            type(value) in {int, float}
            or isinstance(value, self._basic_node)
        )
        if isinstance(value, self._basic_node):
            return self._insert_node(self._root, value)
        else:
            return self._insert_value(self._root, value)
    def insert(self, value):
        self._validate_item(value)
        if self.is_empty():
            self._root = self._basic_node(value)
            self._length += 1
        else:
            self._insert(value)
    def _find_replacement(self, node):
        assert isinstance(node, self._basic_node)
        if node.get_right():
            replacement_node = self._get_min_node(node.get_right())
        elif node.get_left():
            replacement_node = self._get_max_node(node.get_left())
        else:
            replacement_node = None
        return replacement_node
    def _transplant(self, node, replacement):
        assert isinstance(node, self._basic_node)
        assert replacement is None or isinstance(replacement, self._basic_node)
        if replacement is None:
            parent = node.get_parent()
            if parent.get_left() == node:
                parent.set_left(replacement)
            else:
                parent.set_right(replacement)
        else:
            if replacement.is_leaf():
                new_replacement = None
            elif replacement.get_left():
                new_replacement = replacement.get_left()
            else:
                new_replacement = replacement.get_right()
            self._basic_node.swap(node, replacement)
            self._transplant(replacement, new_replacement)
    def _remove(self, del_value, start_node):
        assert type(del_value) in {int, float}
        assert isinstance(start_node, self._basic_node)
        removed_node = self._search(del_value, self._root)
        if removed_node.get_data() != del_value:
            warnings.warn(
                f"Couldn't find `{del_value}` in `{self.__name__}`",
                UserWarning
            )
            last_accessed_node = removed_node
            return last_accessed_node
        replacement = self._find_replacement(removed_node)
        if replacement is None:
            parent = removed_node.get_parent()
        else:
            parent = replacement.get_parent()
        self._transplant(removed_node, replacement)
        self._length -= 1
        last_accessed_node = parent
        return last_accessed_node
    def remove(self, del_value):
        if self.is_empty():
            warnings.warn(f"`{self.__name__}` is empty!!", UserWarning)
            return
        elif type(del_value) not in {int, float}:
            warnings.warn(
                f"Couldn't find `{del_value}` in `{self.__name__}`!!",
                UserWarning
            )
            return
        elif self._root.is_leaf() and del_value == self._root.get_data():
            self._root = None
            self._length -= 1
        else:
            self._remove(del_value, self._root)
    def clear(self):
        super().clear()
    def _rotate_left(self, start_node):
        assert isinstance(start_node, self._basic_node)
        middle = start_node.get_right()
        middle.set_parent(start_node.get_parent())
        start_node.set_right(middle.get_left())
        middle.set_left(start_node)
        return middle
    def _rotate_right(self, start_node):
        assert isinstance(start_node, self._basic_node)
        middle = start_node.get_left()
        middle.set_parent(start_node.get_parent())
        start_node.set_left(middle.get_right())
        middle.set_right(start_node)
        return middle
    def _rotate_left_right(self, start_node):
        assert isinstance(start_node, self._basic_node)
        middle = start_node.get_left().get_right()
        middle.set_parent(start_node.get_parent())
        start_node.get_left().set_right(middle.get_left())
        middle.set_left(start_node.get_left())
        start_node.set_left(middle.get_right())
        middle.set_right(start_node)
        return middle
    def _rotate_right_left(self, start_node):
        assert isinstance(start_node, self._basic_node)
        middle = start_node.get_right().get_left()
        middle.set_parent(start_node.get_parent())
        start_node.get_right().set_left(middle.get_right())
        middle.set_right(start_node.get_right())
        start_node.set_right(middle.get_left())
        middle.set_left(start_node)
        return middle
    def _attach(self, parent, child):
        assert parent is None or isinstance(parent, self._basic_node)
        assert isinstance(child, self._basic_node)
        if parent is None:
            self._root = child
        else:
            if parent.get_data() > child.get_data():
                parent.set_left(child)
            else:
                parent.set_right(child)
    def get_height(self):
        return super().get_height()
    def get_depth(self):
        return super().get_depth()
    def count_leaf_nodes(self):
        return super().count_leaf_nodes()
    def is_balanced(self):
        return super().is_balanced()
    def is_perfect(self):
        return super().is_perfect()
    def is_strict(self):
        return super().is_strict()
    def __iter__(self):
        return super().__iter__()
    def to_list(self):
        return super().to_list()
    def get_nodes_per_level(self):
        return super().get_nodes_per_level()
    def preorder_traverse(self):
        return super().preorder_traverse()
    def depth_first_traverse(self):
        return super().depth_first_traverse()
    def postorder_traverse(self):
        return super().postorder_traverse()
    def inorder_traverse(self):
        return super().inorder_traverse()
    def breadth_first_traverse(self):
        return super().breadth_first_traverse()
    def traverse(self, method="inorder"):
        return super().traverse(method)
class Color(Enum):
    BLACK = 0
    RED = 1
class RedBlackNode(BSTNode):
    __name__ = "extra.RedBlackNode()"
    def __init__(self, value, color=Color.RED):
        if color not in {Color.RED, Color.BLACK}:
            raise ValueError(f"Invalid color for `{self.__name__}`!!")
        super().__init__(value)
        self._color = color
    def get_color(self):
        return self._color
    def set_color(self, new_color):
        if new_color not in {Color.RED, Color.BLACK}:
            raise ValueError(f"Invalid color for `{self.__name__}`!!")
        self._color = new_color
    def __repr__(self):
        if self._color == Color.RED:
            return f"RedNode({self._data})"
        elif self._color == Color.BLACK:
            return f"BlackNode({self._data})"
    def _represent(self):
        if self._color == Color.RED:
            return str(self._data) + "|R"
        elif self._color == Color.BLACK:
            return str(self._data) + "|B"
    @staticmethod
    def swap(node1, node2):
        super().swap(node1, node2)
        node1._color, node2._color = node2._color, node1._color
class RedBlackTree(BST):
    _basic_node = RedBlackNode
    __name__ = "extra.RedBlackTree()"
    def __init__(self, iterable=None):
        super().__init__(iterable)
    def __len__(self):
        return self._length
    def is_empty(self):
        return super().is_empty()
    def get_max(self):
        return super().get_max()
    def get_min(self):
        return super().get_min()
    def __contains__(self, find_val):
        return super().__contains__(find_val)
    def __recolor_case3(self, start_node):
        assert isinstance(start_node, self._basic_node)
        parent = start_node.get_parent()
        grandparent = parent.get_parent() if parent else None
        if parent.is_left_child() and start_node.is_left_child():
            grandparent.set_color(Color.RED)
            parent.set_color(Color.BLACK)
            grandparent = super()._rotate_right(grandparent)
        elif parent.is_left_child() and not start_node.is_left_child():
            parent = super()._rotate_left(parent)
            grandparent.set_left(parent)
            grandparent.set_color(Color.RED)
            grandparent = super()._rotate_right(grandparent)
            grandparent.set_color(Color.BLACK)
        elif not parent.is_left_child() and start_node.is_left_child():
            parent = super()._rotate_right(parent)
            grandparent.set_right(parent)
            grandparent.set_color(Color.RED)
            grandparent = super()._rotate_left(grandparent)
            grandparent.set_color(Color.BLACK)
        else:
            grandparent.set_color(Color.RED)
            parent.set_color(Color.BLACK)
            grandparent = super()._rotate_left(grandparent)
        return grandparent
    def __recolor(self, start_node):
        assert isinstance(start_node, self._basic_node)
        uncle = start_node.get_uncle()
        parent = start_node.get_parent()
        grandparent = parent.get_parent() if parent else None
        if parent is None or grandparent is None:
            return parent if parent else start_node
        if parent.get_color() == Color.BLACK:
            return self._root
        else:
            if uncle and uncle.get_color() == Color.RED:
                parent.set_color(Color.BLACK)
                uncle.set_color(Color.BLACK)
                grandparent.set_color(Color.RED)
            else:
                great_grandparent = grandparent.get_parent()
                grandparent = self.__recolor_case3(start_node)
                if great_grandparent:
                    if great_grandparent.get_data() > grandparent.get_data():
                        great_grandparent.set_left(grandparent)
                    else:
                        great_grandparent.set_right(grandparent)
            return self.__recolor(grandparent)
    def insert(self, value):
        super()._validate_item(value)
        if self.is_empty():
            self._root = self._basic_node(value)
            self._root.set_color(Color.BLACK)
            self._length += 1
        else:
            new_node = super()._insert(value)
            self._root = self.__recolor(new_node)
            self._root.set_color(Color.BLACK)
    def _find_replacement(self, node):
        assert isinstance(node, RedBlackNode)
        if node.is_leaf():
            replacement_node = None
        else:
            successor = (
                super()._get_min_node(node.get_right())
                if node.get_right()
                else None
            )
            predecessor = (
                super()._get_max_node(node.get_left())
                if node.get_left()
                else None
            )
            if successor and successor.get_color() == Color.RED:
                replacement_node = successor
            elif predecessor and predecessor.get_color() == Color.RED:
                replacement_node = predecessor
            else:
                replacement_node = successor if successor else predecessor
        return replacement_node
    def __handle_double_black(self, parent, double_black_node):
        assert isinstance(parent, RedBlackNode)
        assert (
            double_black_node is None
            or isinstance(double_black_node, RedBlackNode)
        )
        while double_black_node != self._root and (
            not double_black_node
            or double_black_node.get_color() == Color.BLACK
        ):
            if double_black_node == parent.get_left():
                sibling = parent.get_right()
                if sibling and sibling.get_color() == Color.RED:
                    sibling.set_color(Color.BLACK)
                    parent.set_color(Color.RED)
                    grandparent = parent.get_parent()
                    parent = super()._rotate_left(parent)
                    super()._attach(grandparent, parent)
                    parent = parent.get_left()
                    sibling = parent.get_right()
                s_left_child = sibling.get_left()
                s_right_child = sibling.get_right()
                s_left_color = (
                    s_left_child.get_color() if s_left_child else Color.BLACK
                )
                s_right_color = (
                    s_right_child.get_color() if s_right_child else Color.BLACK
                )
                if (s_left_color == Color.BLACK
                        and s_right_color == Color.BLACK):
                    sibling.set_color(Color.RED)
                    double_black_node = parent
                else:
                    if s_right_color == Color.BLACK:
                        s_left_child.set_color(Color.BLACK)
                        sibling.set_color(Color.RED)
                        sibling = super()._rotate_right(sibling)
                        super()._attach(parent, sibling)
                        sibling = parent.get_right()
                    sibling.set_color(parent.get_color())
                    parent.set_color(Color.BLACK)
                    s_right_child = sibling.get_right()
                    s_right_child.set_color(Color.BLACK)
                    grandparent = parent.get_parent()
                    parent = super()._rotate_left(parent)
                    super()._attach(grandparent, parent)
                    double_black_node = self._root
            else:
                sibling = parent.get_left()
                if sibling and sibling.get_color() == Color.RED:
                    sibling.set_color(Color.BLACK)
                    parent.set_color(Color.RED)
                    grandparent = parent.get_parent()
                    parent = super()._rotate_right(parent)
                    super()._attach(grandparent, parent)
                    parent = parent.get_right()
                    sibling = parent.get_left()
                s_left_child = sibling.get_left()
                s_right_child = sibling.get_right()
                s_left_color = (
                    s_left_child.get_color() if s_left_child else Color.BLACK
                )
                s_right_color = (
                    s_right_child.get_color() if s_right_child else Color.BLACK
                )
                if (s_right_color == Color.BLACK
                        and s_right_color == Color.BLACK):
                    sibling.set_color(Color.RED)
                    double_black_node = parent
                else:
                    if s_left_color == Color.BLACK:
                        s_right_child.set_color(Color.BLACK)
                        sibling.set_color(Color.RED)
                        sibling = super()._rotate_left(sibling)
                        super()._attach(parent, sibling)
                        sibling = parent.get_left()
                    sibling.set_color(parent.get_color())
                    parent.set_color(Color.BLACK)
                    s_left_child = sibling.get_left()
                    s_left_child.set_color(Color.BLACK)
                    grandparent = parent.get_parent()
                    parent = super()._rotate_right(parent)
                    super()._attach(grandparent, parent)
                    double_black_node = self._root
        self._root.set_color(Color.BLACK)
    def remove(self, del_value):
        if self.is_empty():
            warnings.warn(f"`{self.__name__}` is empty!!", UserWarning)
            return
        elif type(del_value) not in {int, float}:
            warnings.warn(
                f"Couldn't find `{del_value}` in `{self.__name__}`!!",
                UserWarning
            )
            return
        elif self._root.is_leaf() and del_value == self._root.get_data():
            self._root = None
            self._length -= 1
            return
        removed_node = super()._search(del_value, self._root)
        if removed_node.get_data() != del_value:
            warnings.warn(
                f"Couldn't find `{del_value}` in `{self.__name__}`!!",
                UserWarning
            )
            return
        replacement = self._find_replacement(removed_node)
        if removed_node.get_color() == Color.RED and (
            replacement is None or replacement.get_color() == Color.RED
        ):
            super()._transplant(removed_node, replacement)
        elif (
            removed_node.get_color() == Color.RED
            and replacement.get_color() == Color.BLACK
        ):
            raise ValueError("Debug this, this case shouldn't occur!!")
        elif removed_node.get_color() == Color.BLACK and (
            replacement is None or replacement.get_color() == Color.BLACK
        ):
            if replacement:
                parent = replacement.get_parent()
            else:
                parent = removed_node.get_parent()
            super()._transplant(removed_node, replacement)
            if replacement is None:
                if parent.get_left() is None:
                    double_black_node = parent.get_left()
                else:
                    double_black_node = parent.get_right()
            else:
                if replacement.get_data() < parent.get_data():
                    double_black_node = parent.get_left()
                else:
                    double_black_node = parent.get_right()
            self.__handle_double_black(parent, double_black_node)
        elif (
            removed_node.get_color() == Color.BLACK
            and replacement.get_color() == Color.RED
        ):
            replacement.set_color(Color.BLACK)
            super()._transplant(removed_node, replacement)
        self._length -= 1
    def clear(self):
        super().clear()
    def get_black_height(self):
        black_height = 0
        start_node = self._root.get_left()
        while start_node is not None:
            if start_node.get_color() == Color.BLACK:
                black_height += 1
            start_node = start_node.get_left()
        return black_height + 1
    def get_height(self):
        return super().get_height()
    def get_depth(self):
        return super().get_depth()
    def count_leaf_nodes(self):
        return super().count_leaf_nodes()
    def is_balanced(self):
        return super().is_balanced()
    def is_perfect(self):
        return super().is_perfect()
    def is_strict(self):
        return super().is_strict()
    def __iter__(self):
        return super().__iter__()
    def to_list(self):
        return super().to_list()
    def get_nodes_per_level(self):
        return super().get_nodes_per_level()
    def preorder_traverse(self):
        return super().preorder_traverse()
    def depth_first_traverse(self):
        return super().depth_first_traverse()
    def postorder_traverse(self):
        return super().postorder_traverse()
    def inorder_traverse(self):
        return super().inorder_traverse()
    def breadth_first_traverse(self):
        return super().breadth_first_traverse()
    def traverse(self, method="inorder"):
        return super().traverse(method)
def encode(sz, idx):
    return (sz << 20) | (idx ^ 0xfffff)
def decode(x):
    return (x >> 20, (x & 0xfffff) ^ 0xfffff)
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
@bootstrap
def dfs(u, p, g, importance, size, tree, parent, arr):
    parent[u] = p
    sz = imp = 0
    for v in g[u]:
        if v != p:
            yield dfs(v, u, g, importance, size, tree, parent, arr)
            sz += size[v]
            imp += importance[v]
            tree[u].insert(encode(size[v], v))
    size[u] = sz + 1
    importance[u] = imp + arr[u]
    yield
def main():
    TestCases = 1
    for _ in range(TestCases):
        n, qq = [int(i) for i in input().split()]
        arr = [int(i) for i in input().split()]
        g = [[] for i in range(n)]
        for _ in range(n - 1):
            u, v = [int(i) - 1 for i in input().split()]
            g[u].append(v)
            g[v].append(u)
        imp = [0] * n
        size = [0] * n
        parent = [-1] * n
        tree = [RedBlackTree() for i in range(n)]
        dfs(0, -1, g, imp, size, tree, parent, arr)
        for _ in range(qq):
            q, x = [int(i) - 1 for i in input().split()]
            if q == 0:
                print(imp[x])
                continue
            if tree[x].is_empty():
                continue
            par, node = parent[x], x
            val = tree[node].get_max()
            sz, ch = decode(val)
            tree[node].remove(val)
            tree[par].remove(encode(size[node], node))
            imp[node], imp[ch] = imp[node] - imp[ch], imp[node]
            size[node], size[ch] = size[node] - size[ch], size[node]
            tree[par].insert(encode(size[ch], ch))
            tree[ch].insert(encode(size[node], node))
            parent[node], parent[ch] = ch, par
abc='abcdefghijklmnopqrstuvwxyz'
abd={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
def copy2d(lst): return [x[:] for x in lst]   
def no_of_digits(num): return 0 if num <= 0 else int(log10(num)) + 1
def powm(num, power, mod=M): return pow(num, power, mod)
def isPowerOfTwo(x): return (x and (not(x & (x - 1))))
def LSB(num):
    return num & -num
def MSB(num):
    if num <= 0: return 0
    ans = 1; num >>= 1
    while num:
        num >>= 1; ans <<= 1
    return ans
LB = bisect_left   
UB = bisect_right  
def BS(a, x):      
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
def lcm(x, y):
    return (x*y)//gcd(x,y)
class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ R
Int = lambda x:Wrapper(int(x))        
class myDict():
    def __init__(self,func=int):
        self.RANDOM = R
        self.default=func
        self.dict={}
    def __getitem__(self,key):
        myKey=self.RANDOM^key
        if myKey not in self.dict:
            self.dict[myKey]=self.default()
        return self.dict[myKey]
    def __setitem__(self,key,item):
        myKey=self.RANDOM^key
        self.dict[myKey]=item
    def __contains__(self,key):
        myKey=self.RANDOM^key
        return myKey in self.dict
    def __delitem__(self,key):
        myKey=self.RANDOM^key
        del self.dict[myKey]
    def keys(self):
        return [self.RANDOM^i for i in self.dict]
if not os.path.isdir('C:/users/acer'):
    BUFSIZE = 8192
    class FastIO(IOBase):
        newlines = 0
        def __init__(self, file):
            self._fd = file.fileno()
            self.buffer = BytesIO()
            self.writable = "x" in file.mode or "r" not in file.mode
            self.write = self.buffer.write if self.writable else None
        def read(self):
            while True:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                if not b:
                    break
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines = 0
            return self.buffer.read()
        def readline(self):
            while self.newlines == 0:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                self.newlines = b.count(b"\n") + (not b)
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines -= 1
            return self.buffer.readline()
        def flush(self):
            if self.writable:
                os.write(self._fd, self.buffer.getvalue())
                self.buffer.truncate(0), self.buffer.seek(0)
    class IOWrapper(IOBase):
        def __init__(self, file):
            self.buffer = FastIO(file)
            self.flush = self.buffer.flush
            self.writable = self.buffer.writable
            self.write = lambda s: self.buffer.write(s.encode("ascii"))
            self.read = lambda: self.buffer.read().decode("ascii")
            self.readline = lambda: self.buffer.readline().decode("ascii")
    def print(*args, **kwargs):
        sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
        at_start = True
        for x in args:
            if not at_start:
                file.write(sep)
            file.write(str(x))
            at_start = False
        file.write(kwargs.pop("end", "\n"))
        if kwargs.pop("flush", False):
            file.flush()
    if sys.version_info[0] < 3:
        sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
    else:
        sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    input = lambda: sys.stdin.readline().rstrip("\r\n")
if __name__ == "__main__":
    main()
