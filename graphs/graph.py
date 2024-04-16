class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dict:", self.graph_dict)

    def get_path(self,start,end,path=[]):
        path=path+[start]

        if start==end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths=self.get_path(node,end,path)
                for p in new_paths:
                    paths.append(p)
        return paths
    
    def get_shortestpath(self,start,end,path=[]):
        path =path+[start]
        if start not in self.graph_dict:
            return 
        if start==end:
            return path
        shortest_path=None
        for node in self.graph_dict[start]:
            if node not in path:
                sp =self.get_shortestpath(node,end,path)
                if sp:
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path=sp
        return shortest_path
        
            



if __name__ == '__main__':

    routes1 = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)
    start="Toronto"
    start1="Mumbai"
    end="Mumbai"
    end1="New York"
    print("****************")
    print(route_graph.get_path(start,end))
    print("****************")
    print(route_graph.get_path(start1,end))
    print("****************")
    print(route_graph.get_path(start1,end1))
    print("****************")
    print(route_graph.get_shortestpath(start1,end1))