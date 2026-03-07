class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next


class MyLinkedList:

    def __init__(self):
        self.head=None

    def get(self, index: int) -> int:
        curr=self.head
        i=0

        while curr:
            if i==index:
                return curr.val
            curr=curr.next
            i+=1

        return -1


    def addAtHead(self, val: int) -> None:
        self.head=Node(val,self.head)


    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head=Node(val)
            return

        curr=self.head
        while curr.next:
            curr=curr.next

        curr.next=Node(val)


    def addAtIndex(self, index: int, val: int) -> None:

        if index==0:
            self.addAtHead(val)
            return

        curr=self.head
        i=0

        while curr and i<index-1:
            curr=curr.next
            i+=1

        if not curr:
            return

        new_node=Node(val)
        new_node.next=curr.next
        curr.next=new_node


    def deleteAtIndex(self, index: int) -> None:

        if not self.head:
            return

        if index==0:
            self.head=self.head.next
            return

        curr=self.head
        i=0

        while curr.next and i<index-1:
            curr=curr.next
            i+=1

        if curr.next:
            curr.next=curr.next.next
