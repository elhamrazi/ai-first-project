import copy
import random


class Node:

    def __init__(self, deck_no, parent):
        self.slots = []
        self.no = deck_no
        self.parent = parent

    def add_slots(self, slots):
        for i in range(self.no):
            temp = slots[i]
            self.slots.append(temp)

    def print_state(self):
        for i in self.slots:
            if len(i) > 0:
                print(*i)
            else: print('#')

    def goal_state(self):
        for i in self.slots:
            if check_s(i):
                pass
            else:
                return False
        return True


def check_s(lst):
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
    if initial_state.goal_state():
        print("goal")
        initial_state.print_state()
        return
    frontier = []
    explored = []
    parents = []
    parents.append(initial_state)
    frontier.append(initial_state.slots)
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
                    child_node = Node(k, pstate)
                    child_node.add_slots(child)
                    if child_node.goal_state():
                        done = True
                        print("the goal state is: ")
                        for q in child:
                            if len(q) > 0:
                                print(*q)
                            else: print('#')
                        return child_node, explored
                    else:
                        frontier.append(child)
                        parents.append(child_node)
                        for q in child:
                            if len(q) > 0:
                                print(*q)
                            else: print('#')
                        print("---------")
    return "failure", explored


if __name__ == '__main__':
    k, m, n = input().split()
    slots = []
    for i in range(int(k)):
        slot = []
        x = input().split()
        if x[0] != '#':
            for j in x:
                slot.append(j)
        slots.append(slot)

    action_arr = []
    for i in range(int(k)):
        for j in range(int(k)):
            tmp = ()
            if i != j:
                tmp = (i, j)
                action_arr.append(tmp)
    # random.shuffle(action_arr)
    node = Node(int(k), None)
    node.add_slots(slots)
    node.print_state()
    goal, ex = bfs(node, int(k), action_arr)
    depth = 0
    if goal != "failure":
        print("********************")
        print("number of explored nodes: {}".format(len(ex)))
        s = goal
        print("the path is:")
        while s.parent is not None:
            s = s.parent
            depth += 1

            for q in s.slots:
                if len(q) > 0:
                    print(*q)
                else: print('#')
            print("\n↑")
            print()
        print("********************")
        print("depth of the path is: ", depth)
        print("you can see the path above")
        print("the goal state is:")
        goal.print_state()

    else: print("********could not find a solution*********")




















