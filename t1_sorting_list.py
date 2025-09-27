class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    def print_list_inline(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    # Інверсія зв'язного списку
    def inverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування зв'язного списку за допомогою алгоритму "Злиття"
    def merge_sort_list(self):
        if self.head is None or self.head.next is None:
            return self.head

        def split(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            # коли fast досягає кінця, slow буде в середині
            middle = slow.next
            slow.next = None
            return head, middle

        def merge(left, right):
            if not left:
                return right
            if not right:
                return left
            if left.data < right.data:
                left.next = merge(left.next, right)
                return left
            else:
                right.next = merge(left, right.next)
                return right

        left, right = split(self.head)
        left_list = LinkedList()
        left_list.head = left
        right_list = LinkedList()
        right_list.head = right

        left_sorted = left_list.merge_sort_list()
        right_sorted = right_list.merge_sort_list()

        merged_head = merge(left_sorted, right_sorted)
        self.head = merged_head
        return self.head

# Злиття двох відсортованих зв'язних списків в один відсортований список
def join_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    merged_list = LinkedList()
    dummy = Node()
    tail = dummy

    cur1 = list1.head
    cur2 = list2.head

    while cur1 and cur2:
        if cur1.data < cur2.data:
            tail.next = cur1
            cur1 = cur1.next
        else:
            tail.next = cur2
            cur2 = cur2.next
        tail = tail.next

    if cur1:
        tail.next = cur1
    elif cur2:
        tail.next = cur2

    merged_list.head = dummy.next
    return merged_list

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_beginning(3)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)
llist.insert_at_end(26)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list_inline()

# Інверсія зв'язного списку
llist.inverse_list()
print("\nЗв'язний список після інверсії:")
llist.print_list_inline()

# Сортування зв'язного списку
llist.merge_sort_list()
print("\nЗв'язний список після сортування:")
llist.print_list_inline()

llist1 = LinkedList()
a = [1, 3, 5, 7, 19, 8, 27, 39, 4]
for i in a:
    llist1.insert_at_end(i)
llist1.merge_sort_list()
print("\nДругий відсортований зв'язний список:")
llist1.print_list_inline()

final_sorted_list = LinkedList()
final_sorted_list = join_sorted_lists(llist, llist1)
print("\nОб'єднаний відсортований зв'язний список:")
final_sorted_list.print_list_inline()
