class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"
    


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(6)

temp = l1
temp.next =  ListNode(4)
l1.next = temp
l1 =  temp

l1 = [2,4,6]

for i in range(len(l1)):
    
    if i ==0:
        x = ListNode(l1[i])
        temp = x
    else:

        temp.next = ListNode(l1[i])
        temp = temp.next

        print(x)


list1 = [4,5,1,2,0,4]
head = ListNode(list1[0])
tail = head
e = 0
while e < len(list1):
      
      tail.next = ListNode(list1[e])
      tail = tail.next
      e+=1
print(head)


for i in range(3):
    if i==0:
        temp =  ListNode(l1[i])
    else:
        temp.next = ListNode(l1[i])
        temp.val = temp
        temp.next = None



# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #print(l1, l2)
        #print(l1.val, l1.next.val, l1.next.next.val)
        list_l1, list_l2 = [], []
        while l1.next is not None:
            list_l1.append(l1.val)
            l1 = l1.next
        else:
            list_l1.append(l1.val)
        while l2.next is not None:
            list_l2.append(l2.val)
            l2 = l2.next
        else:
            list_l2.append(l2.val)   
        
        #print(list_l1, list_l2)
        if l1.val == 0 and l2.val==0:
            return ListNode(0)
        else:
            sum_ = 0
            for i in range(len(list_l1)):
                sum_ += (list_l1[i])*(10**i)
            for i in range(len(list_l2)):
                sum_ += (list_l2[i])*(10**i)
            str_num = str(sum_)
            #print(str_num)
            len_digit = len(str_num)
            #digit = []
            #digit = ListNode()
            for i in range(len_digit):
                p_ = -(i+1)#len_digit-1 - i
                #digit.append(int(str_num[p_]))
                if i ==0:
                    digit = ListNode(int(str_num[p_]))
                    temp = digit
                else:
                    temp.next = ListNode(int(str_num[p_]))
                    temp = temp.next
            return digit
