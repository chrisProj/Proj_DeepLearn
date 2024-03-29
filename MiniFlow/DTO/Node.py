class Node(object):

    def __init__(self, inbound_nodes=[]):
        # Nodes from which this Node receives values
        self.inbound_nodes = inbound_nodes

        # Nodes to which this Node passes values
        self.outbound_nodes = []

        # For each inbound Node here, add this Node as an outbound Node to _that_ Node
        for n in self.inbound_nodes:
            n.outbound_nodes.append(self)

        # A calculated value
        self.value = None

    def forward(self):
        """"
        Forward propagation.

        Compute the output value based on 'inbound_nodes' and store the
        result in self.value
        """

        raise NotImplemented



