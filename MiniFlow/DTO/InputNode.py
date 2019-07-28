import Node


class Input(Node):
    def __init__(self):
        # 输入节点没有 inbound nodes
        Node.__init__(self)

        #

    def forward(self, value = None):
        # 重写值
        if value is not None:
            self.value = value
