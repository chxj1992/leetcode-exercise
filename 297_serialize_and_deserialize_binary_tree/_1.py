import unittest


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        if root is None:
            return [None]
        return [root.val] + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data):
        if data[0] is None:
            data.pop(0)
            return None
        root = TreeNode(data.pop(0))
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
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
