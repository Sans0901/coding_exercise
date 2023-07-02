https://www.youtube.com/watch?v=wjW6Zhf-bqw&list=PLzgPDYo_3xukPJdH6hVQ6Iic7KiJuoA-l&index=21


1.  DELETION AT THE BEGINNING:

    def delete_begin(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            self.head = self.head.ref
            
2.  DELETION AT THE END:
  
    del delete_end(self):
        if self.head is None:
            print("Linkedlist is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
        n.ref = None
            
3.  DELETION BY GIVEN VALUE:
            
    def delete_ByValue(self,x):
        if self.head is None:
            print("Linkedlist is empty")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is Not None:
            if x == x.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node not present")
        else:
            n.ref = n.ref.ref