import copy

path = []
created = 0
explored = 0


class Node:

    def __init__(self, deck_no, parent):
        self.slots = []
        self.no = deck_no
        self.parent = parent

    def add_slots(self, slots):
        for i in range(self.no):
            temp = slots[i]
            self.slots.append(temp)

    def goal_state(self):
        for i in self.slots:
            if check(i):
                pass
            else:
                return False
        return True

    def prints(self):
        for i in self.slots:
            if len(i) > 0:
                print(*i)
            else: print('#')
        print()


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


def dls(state, actions, limit, k, n):
    global path, explored, created
    if state.goal_state():
        print("goal state is: ")
        state.prints()
        return state

    else:

        if limit <= 0:
            return False
        explored += 1
        for a in actions:
            flag, child = action(state.slots, a)
            child_node = Node(k, state)
            child_node.add_slots(child)
            created += 1
            if flag:
                if len(path) == limit:
                    path.clear()
                path.append(child_node)
                child_node.prints()
                if dls(child_node, actions, limit-1, k, n):
                    return True


def ids(initial_state, actions, depth, k, n):
    done = False
    for limit in range(0, depth):
        if dls(initial_state, actions, limit, k, n):
            e = dls(initial_state, actions, limit, k, n)
            print("a solution exists")
            print()
            done = True
            return e

        else:
            pass
    return done


def main():
    global path, explored, created
    depth = int(input("enter depth "))
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
            if i != j:
                tmp = (i, j)
                action_arr.append(tmp)
    node = Node(int(k), None)
    node.add_slots(slots)
    node.prints()
    y = ids(node, action_arr, depth, int(k), int(n))
    if not y:
        print("***********no solution found************")
    else:
        d = 0
        if len(path) > 0:
            s = path.pop()
            print("the path is:")
            s.prints()
            print("↑\n")
            while s.parent is not None:
                s = s.parent
                for q in s.slots:
                    if len(q) > 0:
                        print(*q)
                    else:
                        print('#')
                d += 1
                print("\n↑")
                print()
            print("********************")
            print("the depth is: ", d)
            print("number of explored nodes: ", explored)
            print("number of created nodes: ", created)
            print("you can see the path above")


if __name__ == '__main__':
    main()

