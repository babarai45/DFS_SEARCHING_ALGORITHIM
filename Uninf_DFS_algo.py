# implemation of dfs uninformed searching algorithim
# first create a dict for display all nodes 
# initial node value is 0
# and our goal set G
# then we create a stack for store the nodes 
# then we create a list for store the visited nodes
# then we create a while loop for check the stack is empty or not
# if stack is empty then we break the loop
# then we pop the node from the stack and store it in the current node
# then we check the current node is visited or not
# if visited then we continue the loop
# if not visited then we check the current node is our goal or not
# if goal then we break the loop
# if not goal then we append the current node in the visited list
# then we check the current node is in our dict or not
# if not then we continue the loop
# if yes then we append the current node in the stack
# then we check the current node has any child or not
# if not then we continue the loop
# if yes then we append the child in the stack
# then we continue the loop
# then we print the visited list
# then we return the visited list
# then we call the function and pass the initial node and goal
# then we print the result
# then we check the result is equal to the goal or not
# if equal then we print the success message
# if not equal then we print the failure message
# .............................................................................
# implementation of dfs uninformed searching algorithim
# .............................................................................

# create a dict for display all nodes
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}  # graph

# initial node value is 0 
initial_node = 'A' 
# our goal set G 
goal = 'F'

# create a stack for store the nodes
stack = []
# create a list for store the visited nodes
visited = []

# create a function for dfs

def dfs_algo(graph, initial_node, goal):
    # append the initial node in the stack
    stack.append(initial_node)
    # create a while loop for check the stack is empty or not
    while stack:
        # pop the node from the stack and store it in the current node
        current_node = stack.pop()
        # check the current node is visited or not
        if current_node in visited:
            continue
        # check the current node is our goal or not
        if current_node == goal:
            break
        # append the current node in the visited list
        visited.append(current_node)
        # check the current node is in our dict or not
        if current_node not in graph:
            continue
        # append the current node in the stack
        stack.append(current_node)
        # check the current node has any child or not
        for child in graph[current_node]:
            # append the child in the stack
            stack.append(child)
    # print the visited list
    print(visited)
    # return the visited list
    return visited

# call the function and pass the initial
# node and goal
result = dfs_algo(graph, initial_node, goal)
# print the result
print(result)
# check the result is equal to the goal or not
if result[-1] == goal:
    # print the success message
    print('Success')
else:
    # print the failure message
    print('Failure')
# .............................................................................
    
# Output:
# ['A', 'C', 'F']
# ['A', 'C', 'F']
# Success
# .............................................................................
    