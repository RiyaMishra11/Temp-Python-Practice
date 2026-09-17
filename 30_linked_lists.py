# Day 8 - 30: Linked Lists
class Node:
    def __init__(self, data):  # 1
        self.data, self.next = data, None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):  # 2
        node = Node(data); node.next = self.head; self.head = node

    def insert_end(self, data):  # 3
        node = Node(data)
        if not self.head:
            self.head = node; return
        cur = self.head
        while cur.next: cur = cur.next
        cur.next = node

    def display(self):  # 4
        result=[]; cur=self.head
        while cur:
            result.append(cur.data); cur=cur.next
        return result

    def search(self, target):  # 5
        cur=self.head
        while cur:
            if cur.data == target: return True
            cur=cur.next
        return False

    def delete(self, target):  # 6
        cur=self.head; prev=None
        while cur:
            if cur.data == target:
                if prev: prev.next=cur.next
                else: self.head=cur.next
                return True
            prev,cur=cur,cur.next
        return False

    def length(self):  # 7
        count=0; cur=self.head
        while cur: count+=1; cur=cur.next
        return count

    def reverse(self):  # 8
        prev=None; cur=self.head
        while cur:
            nxt=cur.next; cur.next=prev; prev,cur=cur,nxt
        self.head=prev

    def middle(self):  # 9
        slow=fast=self.head
        while fast and fast.next:
            slow=slow.next; fast=fast.next.next
        return slow.data if slow else None

    def to_list(self):  # 10
        return self.display()

if __name__ == "__main__":
    ll=LinkedList()
    for n in (10,20,30): ll.insert_end(n)
    ll.insert_beginning(5)
    print(ll.display(), ll.search(20), ll.length(), ll.middle())
    ll.delete(20); print(ll.display())
    ll.reverse(); print(ll.display())
