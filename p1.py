import copy
import random
created = 0
# 4 3 3
# 1a 2a 3b
# 3a
# 1c 1b 3c
# 2b 2c


class Node:

    def __init__(self, deck_no, parent):
        self.decks = []
        self.no = deck_no
        self.parent = parent

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
        # count = n
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


def bfs(initial_state, k, actions):
    global created
    if initial_state.goal_state():
        print("goal")
        initial_state.print_state()
        return
    frontier = []
    explored = []
    parents = [initial_state]
    frontier.append(initial_state.decks)
    done = False
    while len(frontier) > 0 and not done and len(parents) > 0:
        print("number of nodes in frontier: ", len(frontier))
        state = frontier.pop(0)
        pstate = parents.pop(0)
        explored.append(state)

        for a in actions:
            flag, child = action(state, a)
            if flag:
                if child not in explored and child not in frontier:
                    created += 1
                    child_node = Node(k, pstate)
                    child_node.add_decks(child)
                    if child_node.goal_state():
                        done = True
                        print("the goal state is: ")
                        child_node.print_state()
                        return child_node, explored
                    else:
                        frontier.append(child)
                        parents.append(child_node)
                        child_node.print_state()
                        print("---------")
    return "failure", explored


def main():
    k, m, n = input().split()
    decks = []
    for i in range(int(k)):
        slot = []
        x = input().split()
        if x[0] != '#':
            for j in x:
                slot.append(j)
        decks.append(slot)

    action_arr = []
    for i in range(int(k)):
        for j in range(int(k)):
            tmp = ()
            if i != j:
                tmp = (i, j)
                action_arr.append(tmp)
    # random.shuffle(action_arr)
    node = Node(int(k), None)
    node.add_decks(decks)
    node.print_state()
    goal, ex = bfs(node, int(k), action_arr)
    depth = 0
    if goal != "failure":
        print("********************")
        s = goal
        print("the path is:")
        goal.print_state()
        print("\n↑")
        print()
        while s.parent is not None:
            s = s.parent
            depth += 1
            s.print_state()
            print("\n↑")
            print()
        print("********************")
        print("depth of the path is: ", depth)
        print("number of explored nodes: {}".format(len(ex)))
        print("number of created nodes: ", created)
        print("you can see the path above")
        print("the goal state is:")
        goal.print_state()

    else:
        print("********could not find a solution*********")


if __name__ == '__main__':
    main()

