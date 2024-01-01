class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        a_nodes = list()
        b_nodes = list()
        for path in paths:
            a_nodes.append(path[0])
            b_nodes.append(path[1])
        current_node = b_nodes[0]
        while True:
            if current_node not in a_nodes:
                break
            current_node = b_nodes[a_nodes.index(current_node)]
        
        return current_node