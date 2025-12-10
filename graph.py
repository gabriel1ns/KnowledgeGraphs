class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.nodes_data = {}
        
    def add_node(self, node, **attributes):
        """Adiciona um nó ao grafo"""
        if node not in self.adjacency_list:
            self.adjacency_list[node] = {}
            self.nodes_data[node] = attributes
            
    def add_edge(self, node1, node2, label=None):
        """Adiciona uma aresta entre dois nós (grafo não direcionado)"""
        if node1 not in self.adjacency_list:
            self.add_node(node1)
        if node2 not in self.adjacency_list:
            self.add_node(node2)
        
        self.adjacency_list[node1][node2] = label
        self.adjacency_list[node2][node1] = label
        
    def remove_node(self, node):
        """Remove um nó e todas as suas arestas"""
        if node in self.adjacency_list:
            for neighbor in list(self.adjacency_list[node].keys()):
                del self.adjacency_list[neighbor][node]
            
            del self.adjacency_list[node]
            if node in self.nodes_data:
                del self.nodes_data[node]
                
    def remove_edge(self, node1, node2):
        """Remove uma aresta entre dois nós"""
        if node1 in self.adjacency_list and node2 in self.adjacency_list[node1]:
            del self.adjacency_list[node1][node2]
            del self.adjacency_list[node2][node1]
            
    def get_neighbors(self, node):
        """Retorna os vizinhos de um nó"""
        return list(self.adjacency_list.get(node, {}).keys())
    
    def get_edge_label(self, node1, node2):
        """Retorna o label da aresta entre dois nós"""
        if node1 in self.adjacency_list and node2 in self.adjacency_list[node1]:
            return self.adjacency_list[node1][node2]
        return None
    
    def get_degree(self, node):
        """Retorna o grau (número de conexões) de um nó"""
        return len(self.adjacency_list.get(node, {}))
    
    def get_all_nodes(self):
        """Retorna lista de todos os nós"""
        return list(self.adjacency_list.keys())
    
    def get_all_edges(self):
        """Retorna lista de todas as arestas"""
        edges = []
        visited = set()
        for node1 in self.adjacency_list:
            for node2 in self.adjacency_list[node1]:
                edge = tuple(sorted([node1, node2]))
                if edge not in visited:
                    visited.add(edge)
                    edges.append((node1, node2, self.adjacency_list[node1][node2]))
        return edges
    
    def number_of_nodes(self):
        """Retorna o número total de nós"""
        return len(self.adjacency_list)
    
    def number_of_edges(self):
        """Retorna o número total de arestas"""
        return len(self.get_all_edges())
    
    def has_edge(self, node1, node2):
        """Verifica se existe aresta entre dois nós"""
        return node1 in self.adjacency_list and node2 in self.adjacency_list[node1]
