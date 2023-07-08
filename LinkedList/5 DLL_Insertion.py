https://www.youtube.com/watch?v=jDCEOqY_Uuw&list=PLzgPDYo_3xukPJdH6hVQ6Iic7KiJuoA-l&index=22

1.  TRANSVERSAL OF DOUBLY LINKED LIST:

class Node:
    def _init_(self,data):
        self.data = data
        self.nref = None
        self.pref = None
                
class doublyLL:
    def _init_(self):
        self.head = None
        
    def Print_LL(self):
        if self.head is None:
            print("Linklist is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.nref
                
2.  REVERSAL OF DOUBLY LINKED LIST:
                
    def Print_LL_reverse(self):
        if self.head is None:
            print("Linklist is empty")
        else:
            n = self.head
            while n.ref is not None:
                n = n.nref
            while n is not None:
                print(n.data)
                n = n.pref
                
3.  INSERTION IN DOUBLY LINKED LIST WHEN EMPTY:

    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linklist is empty")
            
4.  INSERTION AT THE BEGINNING:

    def insert_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
            
5.  INSERTION AT THE END:

    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.ref
            n.nref = new_node
            new_node.pref = n
            
6.  INSERTION AFTER X IN THE LIST:

    def add_after(self,data,x):
        if self.head is None:
            print("Linklist is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given node is not present in doubly link list")
            elif n.nref is None:
                new_node = Node(data)
                n.nref = new_node
                new_node.pref = n
            else:
                new_node = Node(data)
                n.nref.pref = new_node
                new_node.nref = n.nref
                n.nref = new_node
                new_node.pref = n
                
7.  INSERTION BEFORE X IN THE LIST:

    def add_before(self,data,x):
        if self.head is None:
            print("Linklist is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            self.head.pref = new_node
            new_node.nref = self.head
            self.head = new_node
            return
        n = self.head
        while n.nref is not None:
            if x == n.nref.data:
                break
            n = n.nref
        if n.nref is None:
            print("Given node x is not present in linkedlist")
        else:
            new_node = Node(data)
            new_node.pref = n
            new_node.nref = n.nref
            n.nref.pref = new_node
            n.nref = new_node



            