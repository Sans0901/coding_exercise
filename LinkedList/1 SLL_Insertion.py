https://www.youtube.com/watch?v=AFKtwTqEwTk&list=PLzgPDYo_3xukPJdH6hVQ6Iic7KiJuoA-l&index=12

Data structure is a way of storing and organising the data so that it can be accessed effectively.
Linked List is a linear data structure made up of chain of nodes in which each node contains a data field and link or reference.


1.  TRANSVERSAL OF LINKED LIST:

class Node:
    def _init_(self,data):
        self.data = data
        self.head = None
        
class LinkedList:
    def _init_(self):
        self.head = None
        
    def Print_LL(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
                
                
2.  INSERTION AT THE BEGINNING:

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
3.  INSERTION AT THE END:

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
                n.ref = new_node
           
     
4.  INSERTION BETWEEN THE LIST:

    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
            if n is None:
                print("To add after x is not present in list")
            else:
                new_node = n.ref
                n.ref = new_node
                
    def add_before(self,data,x):
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            
        if self.head is None:
            print("LinkedList is empty")
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
            
        if n.ref is None:
            print("To before x that node is not present in list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
            
5   INSERTING INTO EMPTY LINKEDLIST:

    def insert_empty(self.data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linkedlist is not empty")
 
        
        
        