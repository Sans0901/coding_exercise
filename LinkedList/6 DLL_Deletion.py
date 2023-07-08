https://www.youtube.com/watch?v=50vOpFLB428&list=PLzgPDYo_3xukPJdH6hVQ6Iic7KiJuoA-l&index=26

1.  DELETION AT THE BEGINNING:

    def del_begin(self):
        if self.head is None:
            print("Linkedlist is empty")
            return
        if self.head.nref is None:
            self.head = None
            print("Doubly linkedlist is empty after deleting node x")
        else:
            self.head = self.head.nref
            self.head.pref = None
            
2.  DELETION AT THE END:

    def del_end(self,data):
        if self.head is None:
            print("Doubly linkedlist is empty we can't delete it")
            return
        if self.head.nref is None:
            print("Doubly linkedlist is empty after deleting the node x")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None
            
3.  DELETION BY VALUE:

    def del_value(self,data,x):
        if self.head is None:
            print("Doubly linkedlist is empty")                     # If list is empty
            return
        if self.head.nref is None:                                  # If only one node is present
            if x == self.head.data:
                self.head = None
            else:
                print("X is not present in doubly linked list")
            return
        if self.head.data == x:                                     # If X is present as first node
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:                                      # If X is present in between
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:                                         # If x is last node
                n.pref.nref = None
            else:
                print("X is not present in doubly linked list)