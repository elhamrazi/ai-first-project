import copy


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

    def prints(self):
        for i in self.slots:
            if len(i) > 0:
                print(*i)
            else: print('#')


def check_s(lst, n):
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
path = []

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

                return False,temp
        else:
            temp[act[1]].append(a)
            # print(temp)

            return True, temp

    return False, temp


def dls(initial_state, actions, limit, k, n):
    global path
    if initial_state.goal_state(n):
        print("goal")
        initial_state.prints()
        return initial_state

    else:
        if limit <= 0:
            return False
        path = []
        for a in actions:
            flag, child = action(initial_state.slots, a)
            child_state = State(k, initial_state)
            child_state.add_slots(child)
            if flag:
                if len(path) == limit:
                    path.clear()
                path.append(child_state)
                child_state.prints()
                if dls(child_state, actions, limit-1, k, n):
                    return True


def ids(initial_state, actions, depth, k, n):
    done = False
    for limit in range(0, depth):
        if dls(initial_state, actions, limit, k, n):
            e = dls(initial_state, actions, limit, k, n)
            print("there is a solution")
            done = True
            return e

        else:
            pass
    return done


if __name__ == '__main__':
    k, m, n = input().split()
    depth = int(input("enter depth "))
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
    state = State(int(k), None)
    state.add_slots(slots)
    state.print_state()
    y = ids(state, action_arr, depth, int(k), int(n))
    if len(path) > 0:
        s = path.pop()
        s.prints()

        print(y)
        print("the path is:")
        while s.parent is not None:
            s = s.parent
            for q in s.slots:
                if len(q) > 0:
                    print(*q)
                else:
                    print('#')
            print()
        print("********************")





