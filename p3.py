import copy

def get_colors(lst):
    temp = lst
    count = 0
    if len(temp) > 0:
        c = temp[0]
        lc = len(c)
        colorc = c[lc - 1:lc]
        for i in temp:
            l = len(i)
            color = i[l - 1:l]
            if color != colorc:
                count += 1
    return count


def heuristic_func(lst, k):
    total = 0
    for i in range(k):
        total += get_colors(lst[i])
    return total


def get_inv(arr):
    inv_count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                inv_count += 1

    return inv_count


def count_inversions(lst, k):
    total = 0
    for i in range(k):
        # print("inv shit: ", lst[i])
        total += get_inv(lst[i])
    return total


class State:
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

    def goal_state(self, n):
        # if self.heuristic == 0:
        #     return True
        for i in self.decks:
            if check(i, n):
                pass
            else:
                return False
        return True


def check(lst, n):
    temp = lst
    if len(temp) > 0:
        c = temp[0]
        lc = len(c)
        colorc = c[lc - 1:lc]
        # print("kir: ", c[0:lc - 1])
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
    if initial_state.goal_state(n):
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
        # print("temp and node")
        # print("************")
        # print(temp)
        # print("-------------")
        # print(node.decks)
        explored.append(temp)

        for a in actions:
            flag, child = action(temp, a)
            # print("child", child)
            if flag:
                # print(child in explored)
                if child not in explored:
                    h = heuristic_func(child, k)
                    x = copy.deepcopy(node.path)
                    child_state = State(k, node, h, x+1)
                    child_state.add_decks(child)
                    if child_state.goal_state(n):
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
    # random.shuffle(action_arr)
    h = heuristic_func(decks, int(k))
    state = State(int(k), None, h, 0)
    state.add_decks(decks)
    # state.print_state()
    goal, ex = a_star(state, action_arr, int(n), int(k))
    depth = 0
    if goal != "failure":
        print("********************")
        print("number of explored nodes: {}".format(len(ex)))
        s = goal
        print("the path is:")
        while s.parent is not None:
            s = s.parent
            depth += 1
            for q in s.decks:
                if len(q) > 0:
                    print(*q)
                else: print('#')
            print()
        print("********************")
        print("depth of the path is: ", depth)

    else: print("********could not find a solution*********")

