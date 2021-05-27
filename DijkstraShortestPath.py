"""
ds: 1 hash[hash] to hold the graph [node + cost]
    1 hash to node + cost
    1 hash to node and parent
    1 list to hold processed nodes

algo: find lowest cost node
     while node-
      get cost
      get neighbors
      for each neighbor-
        update cost
        update parent
      add node to processed
      get next lowest cost node

      to get lowest cost node:
        for each node in costs-
            update lowest cost
            update lowest cost node
        :return lowest cost node
"""
