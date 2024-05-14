class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        fast = head
        slow = head
        cycleFound = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycleFound = 1
                break


        if cycleFound:
            p = head
            while p != slow:
                p = p.next
                slow = slow.next
            return p
        else:
            return None



            

           
                

        


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head.next  # creating a cycle at node 3 pointing back to node 2
    obj = Solution()
    print(obj.detectCycle(head).val)
    
    


