import copy
created = 0
# 4 3 3
# 1a 2a 3b
# 3a
# 1c 1b 3c
# 2b 2c


def get_colors(lst):
    temp = lst
    count = 0
    if len(temp) > 0:
        c = temp[0]
        lc = len(c)
        colorc = c[lc - 1:lc]
        for i in range(len(temp)):
            l = len(temp[i])
            color = temp[i][l - 1:l]
            if color != colorc or get_inv(temp, i) > 0 or not check(lst):
                count += len(temp) - i + 1
    return count


def get_heuristic(lst, k):
    total = 0
    for i in range(k):
        total += get_colors(lst[i])
    return total


def get_inv(arr, index):
    inv_count = 0
    n = len(arr)
    for j in range(index + 1, n):
        if arr[index] < arr[j]:
            inv_count += 1

    return inv_count


def count_inversions(lst, k):
    total = 0
    for i in range(k):
        total += get_inv(lst[i], i)
    return total


class Node:
    def __init__(self, deck_no, parent, heuristic, path):
        self.decks = []
        self.no = deck_no
        self.parent = parent
        self.heuristic = heuristic
        self.path = path

    def add_decks(self, decks):
        for i in range(self.no):
            temp = decks[i]
            self.decks.append(temp)

    def print_state(self):
        for i in self.decks:
            if len(i) > 0:
                print(*i)
            else: print('#')

    def goal_state(self):
        if self.heuristic == 0:
            return True
        for i in self.decks:
            if check(i):
                pass
            else:
                return False
        return True


def check(lst):
    temp = lst
    if len(temp) > 0:
        c = temp[0]
        lc = len(c)
        colorc = c[lc - 1:lc]
        count = int(c[0:lc - 1])
        flag = True
        for i in temp:
            l = len(i)
            color = i[l - 1:l]
            number = int(i[0:l - 1])
            if color == colorc and number == count:
                pass
            else:
                flag = False
                break
            count -= 1
        return flag
    return True


def action(s, act):
        t = copy.deepcopy(s)
        temp = t
        if len(temp[act[0]]) > 0:
            a = temp[act[0]].pop()
            if len(temp[act[1]]) > 0:
                b = temp[act[1]].pop()
                la = len(a)
                numbera = int(a[0:la - 1])
                lb = len(b)
                numberb = int(b[0:lb - 1])
                if numbera < numberb:
                    temp[act[1]].append(b)
                    temp[act[1]].append(a)
                    return True, temp
                else:
                    temp[act[1]].append(b)
                    temp[act[0]].append(a)

                    return False, temp
            else:
                temp[act[1]].append(a)
                # print(temp)

                return True, temp

        return False, temp


def a_star(initial_state, actions, n, k):
    global created
    if initial_state.goal_state():
        print("goal state")
        initial_state.print_state()
        print()
        return initial_state, '1'

    frontier = {0+initial_state.heuristic: initial_state}
    dic = {0+initial_state.heuristic: initial_state.decks}
    explored = []
    while len(frontier) > 0:
        node_key = min(frontier)
        # print(node_key)
        node = frontier.pop(node_key)
        print("the h for expanded node: ", node.heuristic)
        print("the g for expanded node: ", node.path)
        node.print_state()
        print()
        temp = dic.pop(node_key)
        explored.append(temp)

        for a in actions:
            flag, child = action(temp, a)
            # print("child", child)
            if flag:
                # print(child in explored)
                if child not in explored:
                    h = get_heuristic(child, k)
                    x = copy.deepcopy(node.path)
                    created += 1
                    child_state = Node(k, node, h, x + 1)
                    child_state.add_decks(child)
                    if child_state.goal_state():
                        print("the goal state is:")
                        child_state.print_state()
                        return child_state, explored
                    frontier[h+x+1] = child_state
                    dic[h+x+1] = child

    return "failure", explored


if __name__ == '__main__':
    k, m, n = input().split()
    decks = []
    for i in range(int(k)):
        deck = []
        x = input().split()
        if x[0] != '#':
            for j in x:
                deck.append(j)
        decks.append(deck)

    action_arr = []
    for i in range(int(k)):
        for j in range(int(k)):
            tmp = ()
            if i != j:
                tmp = (i, j)
                action_arr.append(tmp)

    h = get_heuristic(decks, int(k))
    state = Node(int(k), None, h, 0)
    state.add_decks(decks)

    goal, ex = a_star(state, action_arr, int(n), int(k))
    depth = 0
    if goal != "failure":
        print("********************")

        s = goal
        print("the path is:")
        while s.parent is not None:
            s = s.parent
            depth += 1
            print("↑\n")
            for q in s.decks:
                if len(q) > 0:
                    print(*q)
                else: print('#')
            print()
        print("********************")
        print("depth of the path is: ", depth)
        print("number of explored nodes: {}".format(len(ex)))
        print("number of created nodes: ", created)
        print("you can see the path above")
        print("the goal state is:")
        goal.print_state()

    else: print("********could not find a solution*********")

