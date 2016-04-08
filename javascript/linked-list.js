class Node {
  constructor (value) {
    this.value = value;
    this.next_node = null;
  }
}

class LinkedList {
  constructor () {
    this.head = null;
    this.tail = null;

    this.size = 0;
  }

  add (node) {

    const current = this.tail;

    // if it's empty, set node to head
    if (this.head === null) {
      this.head = node;
      this.tail = node;
      this.size ++;
      return
    }

    // point current node to new node
    current.next_node = node;

    // set new node to tail & increment size
    this.tail = node;
    this.size ++;

  }

  print () {
    let current = this.head;

    while (current !== null) {
      console.log(current);
      console.log("--------------------------------------")
      current = current.next_node;
    }
  }

  addAtIndex (node, idx) {
    let current = this.head,
        counter = 0;

    while (counter !== idx - 1) {
      current = current.next_node;
      counter ++;
    }

    const old_nodes_next_node = current.next_node;
    current.next_node = node;
    node.next_node = old_nodes_next_node

  }

}

const reverseList = function(linked_list) {
  let current = linked_list.head,
      counter = 0,
      counter2 = 0,
      last_item_index = null;


  while (current !== null) {
    current = current.next_node;
    counter ++;
  }

  last_item_index = counter;
  console.log("???")
  current = linked_list.head;

  while (counter !== 0) {
    while (counter - last_item_index) {
      console.log("1")
      counter2 ++;
    }
    console.log(counter)
    // while ( === last_item_index) {
    //   console.log(last_item_index - counter)
    // }

    counter --;
  }




}

const linked_list = new LinkedList;
console.log(linked_list.constructor === LinkedList); //true

linked_list.add(new Node("ceviche"));
linked_list.add(new Node("tortilla"));
linked_list.add(new Node("avocado"));
// linked_list.add(new Node("banana"));
// linked_list.add(new Node("chocolate"));
// linked_list.add(new Node("candy"));
linked_list.print();

console.log("#######################################")

linked_list.addAtIndex(new Node("bob"), 2);

linked_list.print();

console.log("#######################################")

reverseList(linked_list);

// An individual node is by default ignorant of who it should point to until
// it is added to a linked list.
// In a singly linked list, once a node is added to a linked list,
// it should still point to nothing because it's the last item.
// But it's also the add function within the linked list who should
// overwrite the previous node's null pointer reference to point to
// the new node.

// Do you have any ideas how to do this?
// It seems like add should iterate through the linked list
// until it finds the last item.
// once it finds it, it should reference the new item.

// Before writing our find function we need something else though.
// Take a moment to think what the find function should be doing.
// It needs to transverse through the linked list.
// That means finding head (first item), then asking who is next, until current.next_node === null.
// So loop until current.next_node === null.
// Now inside the loop is pretty trivial.
// All we need to do it keep asking for current.next_node.


// transverse () {
//   var current = this.head;
//   console.log(`head is: ${current}`);
//
//   while (current === null) {
//     console.log(`current: ${current.value}`);
//     current = current.next_node;
//   }
// }
