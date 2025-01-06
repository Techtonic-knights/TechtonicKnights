// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;
impl Solution {
    pub fn is_unival_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
      
        // Initialize a queue to perform a breadth-first traversal
        let mut queue = VecDeque::new();
        let mut univalue = 0;
        if let Some(node) = root {
            univalue = node.borrow().val;
            queue.push_back(node);
        } else {
            return false;
        }

        while !queue.is_empty() {
            let node = queue.pop_front().unwrap();
            let node_val = node.borrow().val;

            if univalue != node_val {
                return false;
            };

            if let Some(left) = node.borrow().left.clone() {
            queue.push_back(left);
        };

        if let Some(right) = node.borrow().right.clone() {
            queue.push_back(right);
        };
        }

        return true
    }
}
