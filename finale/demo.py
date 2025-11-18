from collections import deque

# Thuật toán BFS cơ bản
def bfs_traversal(graph, start):
    visited = set()               # Lưu node đã duyệt
    queue = deque([start])        # Hàng đợi, bắt đầu từ start
    visited.add(start)

    order = []                    # Lưu thứ tự duyệt

    while queue:
        node = queue.popleft()    # Lấy node ra khỏi hàng đợi
        order.append(node)        # Lưu vào kết quả

        # Duyệt tất cả hàng xóm của node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


# BFS tìm đường đi ngắn nhất trong đồ thị không trọng số
def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])      # Hàng đợi chứa cả đường đi

    while queue:
        path = queue.popleft()    # Lấy một đường đi ra
        node = path[-1]           # Lấy node cuối của đường đi

        if node == goal:
            return path            # Tìm thấy đường đi

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)    # Sao chép đường đi hiện tại
                new_path.append(neighbor)
                queue.append(new_path)

    return None   # Không tìm thấy đường đi


# ======================
# Chạy thử
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    # Duyệt BFS
    print("BFS Traversal từ A:")
    print(bfs_traversal(graph, 'A'))

    # Tìm đường đi ngắn nhất
    print("\nĐường đi ngắn nhất từ A đến F:")
    print(bfs_shortest_path(graph, 'A', 'F'))
