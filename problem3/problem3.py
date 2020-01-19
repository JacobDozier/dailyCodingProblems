class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkForNone(obj):
    if obj == None: return ''
    else: return ',' + obj.val

def serialize(root):
    # TODO Find a more elegant way of checking the nodes.
    serializedNode = root.val
    serializedNode += checkForNone(root.left) + checkForNone(root.left.left) + checkForNone(root.left.right)
    serializedNode += checkForNone(root.right) + checkForNone(root.right.left) + checkForNone(root.right.right)
    return serializedNode

def deserialize(s):
    deserializedNode = Node(None)
    # TODO Find a more elegant way of checking which branch of the node it is on.
    nodeVal = ''
    commaCounter = 0
    for char in s:
        nodeVal += char
        if char == ',' and commaCounter == 0: 
            deserializedNode.val = nodeVal
            nodeVal = ''
            commaCounter += 1
            continue
        elif char == ',' and commaCounter > 0: 
            nodeVal = ''
            commaCounter += 1
            continue
        elif nodeVal == 'left' or nodeVal == 'left.left': 
            if nodeVal == 'left.left':
                deserializedNode.left.left = Node(nodeVal)
            else: 
                deserializedNode.left = Node(nodeVal)
        elif nodeVal == 'right' or nodeVal == 'right.right': 
            if nodeVal == 'right.right':
                deserializedNode.right.right = Node(nodeVal)
            else: 
                deserializedNode.right = Node(nodeVal)
    return deserializedNode

if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
