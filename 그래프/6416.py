from collections import deque, defaultdict
import sys

input = sys.stdin.readline

caseCount = 0
Lines = defaultdict(list)


class Node:
    def __init__(self, item: int):
        self.item = item
        self.canGoTo = []
        self.canComeFrom = []
        self.canFromRoot = False


class Tree:
    def __init__(self, root: Node):
        self.root = root

    def levelorder(self, n: Node):
        if n != None:
            queue = deque()
            queue.append(n)
            while queue:
                tmp = queue.popleft()
                if tmp.canFromRoot == False:
                    tmp.canFromRoot = True
                    for item in tmp.canGoTo:
                        global nodes
                        queue.append(nodes[item])


while True:
    num = input().rstrip()
    # -1 -1이 입력된 경우 입력종료
    if num == "-1 -1":
        break
    # 빈 줄이 입력된 경우 무시
    elif num == "":
        continue
    caseEnd = 0
    inputLine = list(map(int, num.split()))

    # 입력으로 0 0이 들어올 때까지 간선 내용 저장
    for i in range(0, len(inputLine), 2):
        if inputLine[i] == 0 and inputLine[i + 1] == 0:
            caseEnd = 1
            break
        Lines[inputLine[i]].append(inputLine[i + 1])

    # 입력으로 0 0이 들어온 경우 case 결과 출력 후 입력 초기화
    if caseEnd == 1:
        caseCount += 1
        # key값이 node의 item인 node dict 생성
        nodes = dict()
        for key in Lines.keys():
            # 입력 내에서 간선의 출발점이 되는 정점을 노드로 추가
            if not key in nodes.keys():
                nodes[key] = Node(key)

            for value in Lines[key]:
                # 입력 내에서 간선의 도착점이 되는 정점을 노드로 추가
                if not value in nodes.keys():
                    nodes[value] = Node(value)

                # 정점으로 들어노는 간선 정보를 도착 정점 노드에 추가
                nodes[value].canComeFrom.append(key)
                # 정점에서 나가는 간선 정보를 출발정점 노드에 추가
                nodes[key].canGoTo.append(value)

        root = None
        isTree = True

        for nodeItem in nodes.keys():
            # 1. 들어오는 간선이 하나도 없는 단 하나의 노드가 존재, 이 노드가 root node
            if len(nodes[nodeItem].canComeFrom) == 0:
                if root == None:
                    root = nodeItem
                # 만약 들어오는 간선이 하나도 없는 노드를 찾았는데 root 노드가 이미 있는 경우
                else:
                    isTree = False
                    break

        # 만약 들어오는 간선이 하나도 없는 노드가 없다면 종료
        if root == None:
            isTree = False

        if isTree:
            for nodeItem in nodes.keys():
                # 2. 루트 노드를 제외한 모든 노드는 반드시 단 하나의 들어오는 간선이 존재
                if len(nodes[nodeItem].canComeFrom) != 1 and nodeItem != root:
                    isTree = False
                    break

            # 루트 노드로 들어오는 간선이 존재하면 종료
            if len(nodes[root].canComeFrom) > 0:
                isTree = False

        # 3. 루트에서 다른 노드로 가는 경로는 반드시 가능하며, 유일
        # 이는 루트를 제외한 모든 노드에 성립
        # 1, 2번을 만족하면 트리 형태를 만들 수 있으며 3번 형태가 만족되지 않는 경우
        # 트리에서 연결되지 않은 노드가 존재하는 다는 뜻, 트리를 순회하여
        # Node를 방문하게 되면 canFromRoot를 True 값으로 변경하고
        # 순회가 종료된 뒤에 canFromRoot가 False인 Node가 존재하면 트리가 아니라고 출력

        if not any(Lines):
            isTree = True
        if isTree and any(Lines):
            tree = Tree(nodes[root])
            tree.levelorder(nodes[root])
            for nodeItem in nodes.keys():
                if nodes[nodeItem].canFromRoot == False:
                    isTree = False
                    break

        if isTree:
            print("Case", caseCount, "is a tree.")
        else:
            print("Case", caseCount, "is not a tree.")

        Lines = defaultdict(list)


# import sys
# from collections import defaultdict

# input = sys.stdin.readline


# while True:
#     # -1 -1이 나올때까지 입력받도록
#     tree = defaultdict(list)
#     count = 1
#     while True:
#         # 0 0 이 나올때까지 입력받도록
#         a = list(map(int, input().split()))
#         test = False
#         for i in range(len(a)):
#             if i % 2 == 1:
#                 if a[i] == 0 and a[i - 1] == 0:
#                     test = True
#                     break
#                 tree[a[i]].append(a[i - 1])
#                 if len(tree[a[i]]) > 1:
#                     print("Case", count, "is not a tree")
#                     test = True
#                     break

#         if test:
#             count += 1
#             break

#         print("Case", count, "is a tree")
