# class State:
#     def __init__(self):
#         self.slots = []
# class Slot:
#
#     def __init__(self, num):
#         self.num = num
#         self.cards = []
#
#     def add_card(self, card):
#         self.cards.append(card)
#
#     def last_elem(self, card):
#         a = self.cards.pop(card)
#         self.cards.append(card)
#         return a.number
#
#     def is_empty(self):
#         if len(self.cards) == 0:
#             return True
#         return False
#
#     def pop(self):
#         q = self.cards.pop()
#         return q
#
#     def equal_slot(self, other):
#         return self.__dict__ == other.__dict__
#
#     def check(self):
#         if len(self.cards) > 0:
#             c = self.cards[0]
#             lc = len(c)
#             colorc = c[lc - 1:lc]
#             flag = True
#             count = 1
#             for i in self.cards:
#                 l = len(i)
#                 color = i[l - 1:l]
#                 number = int(i[0:l - 1])
#                 if color == colorc and number == count:
#                     pass
#                 else:
#                     flag = False
#                     break
#                 count += 1
#             return flag
#         return True
#
#     def print_slot(self):
#         if len(self.cards) > 0:
#             for i in self.cards:
#                 print(i, end=' ')
#             print()
#         else: print('#')
#
#
# class Card:
#     def __init__(self, id):
#         l = len(id)
#         color = id[l-1:l]
#         number = int(id[0:l-1])
#         self.id = id
#         self.color = color
#         self.number = number
#
#

    # def action(self, action):
    #     tmp = self.slots
    #     temp = self.slots
    #     if not temp[action[0]].is_empty():
    #         a = temp[action[0]].pop()
    #         if not temp[action[1]].is_empty():
    #             b = temp[action[1]].pop()
    #             # print(a.id, b.id)
    #             if a.number > b.number:
    #                 temp[action[1]].add_card(b)
    #                 temp[action[1]].add_card(a)
    #                 # for x in temp:
    #                 #     x.print_slot()
    #                 self.slots = tmp
    #                 return True, temp
    #             else:
    #                 temp[action[1]].add_card(b)
    #                 temp[action[0]].add_card(a)
    #                 self.slots = tmp
    #                 return False, temp
    #         else:
    #             temp[action[1]].add_card(a)
    #             # print(temp)
    #             self.slots = tmp
    #             return True, temp
    #     self.slots = tmp
    #     return False, temp
