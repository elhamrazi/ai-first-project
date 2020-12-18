import copy
import random


class State:

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

    def goal_state(self, n):
        for i in self.slots:
            if check_s(i, n):
                pass
            else:
                return False
        return True


def check_s(lst, n):
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


def bfs(initial_state, n, k, actions):
    if initial_state.goal_state(n):
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
        node = frontier.pop(0)
        pnode = parents.pop(0)
        explored.append(node)

        for a in actions:

            flag, child = action(node, a)
            if flag:

                if child not in explored and child not in frontier:
                    child_state = State(k, pnode)
                    child_state.add_slots(child)
                    if child_state.goal_state(n):
                        done = True
                        print("the goal state is: ")
                        for q in child:
                            if len(q) > 0:
                                print(*q)
                            else: print('#')
                        return child_state, explored
                    else:
                        frontier.append(child)
                        parents.append(child_state)
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
    state = State(int(k), None)
    state.add_slots(slots)
    state.print_state()
    goal, ex = bfs(state, int(n), int(k), action_arr)
    if goal != "failure":
        print("********************")
        print("number of explored nodes: {}".format(len(ex)))
        s = goal
        print("the path is:")
        while s.parent is not None:
            s = s.parent
            for q in s.slots:
                if len(q) > 0:
                    print(*q)
                else: print('#')
            print()
        print("********************")

    else: print("********could not find a solution*********")




















