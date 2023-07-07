https://www.youtube.com/watch?v=jDCEOqY_Uuw&list=PLzgPDYo_3xukPJdH6hVQ6Iic7KiJuoA-l&index=22

1.  TRANSVERSAL OF DOUBLY LINKED LIST:

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


            