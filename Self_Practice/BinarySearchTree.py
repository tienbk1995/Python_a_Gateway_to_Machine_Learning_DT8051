class _Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class order_dict:
    def __init__(self):
        self._root = None

    def _set(self, x, key, val):
        # No any node available -> Insert new node
        if x is None:
            return _Node(key, val)
        
        # Traverse to the left of the tree for the element[key] less than that of the parent node
        if x.key > key:
            x.left = self._set(x.left, key, val)

        # Traverse to the right of the tree for the element[key] greater than that of the parent node
        elif x.key < key:
            x.right = self._set(x.right, key, val)

        # if parent node key is equal to key
        else:
            x.val = val

        return x

    # Special method built in python: eg: new_object[key] = val to create a new node
    def __setitem__(self, key, val):
        self._root = self._set(self._root, key, val)

    def _get(self, x, key):
        if x is None:
            raise KeyError(key)
        
        # Traverse to the left of the tree for the element[key] less than that of the parent node
        if x.key > key:
            return self._get(x.left, key)

        # Traverse to the right of the tree for the element[key] greater than that of the parent node
        elif x.key < key:
            return self._get(x.right, key)

        else:
            return x.val

    # Special method built in python: eg: new_object[key] to retrieve a new node value
    def __getitem__(self, key):
        return self._get(self._root, key)
    
    # Traverse in order of the tree, starting from the leftest
    def _inorder(self, x, a):
        if x is None:
            return
        self._inorder(x.left, a)
        a += [x.key]
        self._inorder(x.right, a)

    # Special method built in python, return an iterator for ordered_dict object self.
    def __iter__(self):
        a = []
        self._inorder(self._root, a)
        return iter(a)
    
if __name__ == "__main__":
    new_order_list = order_dict();
    new_order_list['m'] = 1
    new_order_list['d'] = 2
    new_order_list['c'] = 4
    for key in new_order_list:
        print(key)
