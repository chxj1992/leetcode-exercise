import unittest


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        if root is None:
            return []
        stack = [root]
        data = []
        while stack:
            row = []
            while stack:
                node = stack.pop()
                if node is None:
                    data.append(None)
                    continue
                data.append(node.val)
                row += [node.right, node.left]
            stack += row
        return data

    def deserialize(self, data):
        if len(data) == 0:
            return None
        root = TreeNode(data.pop(0))
        stack = [root]
        while stack and data:
            row = []
            while stack:
                node = stack.pop()
                if node is None:
                    continue
                left_val = data.pop(0)
                if left_val is not None:
                    node.left = TreeNode(left_val)
                right_val = data.pop(0)
                if right_val is not None:
                    node.right = TreeNode(right_val)
                row += [node.left, node.right]
            stack = row
        return root


class Test(unittest.TestCase):

    def assertTreeEqual(self, expected: TreeNode, actual: TreeNode):
        if expected is None and actual is None:
            return True
        if expected is None:
            assert False, 'actual should be None'
        if actual is None:
            assert False, 'expected should not be None'
        if expected.val != actual.val:
            assert False, 'expected : %s , actual: %s' % (expected.val, actual.val)
        return self.assertTreeEqual(expected.left, actual.left) and self.assertTreeEqual(expected.right, actual.right)

    def test1(self):
        tree = TreeNode(2)
        tree.left = TreeNode(1)
        tree.right = TreeNode(3)
        codec = Codec()
        deserialized = codec.deserialize(codec.serialize(tree))
        self.assertTreeEqual(tree, deserialized)

    def test2(self):
        tree = TreeNode(5)
        tree.left = TreeNode(1)
        tree.right = TreeNode(4)
        tree.right.left = TreeNode(3)
        tree.right.right = TreeNode(6)
        codec = Codec()
        deserialized = codec.deserialize(codec.serialize(tree))
        self.assertTreeEqual(tree, deserialized)

    def test3(self):
        tree = TreeNode(1)
        tree.left = TreeNode(2)
        codec = Codec()
        deserialized = codec.deserialize(codec.serialize(tree))
        self.assertTreeEqual(tree, deserialized)


if __name__ == '__main__':
    unittest.main()
