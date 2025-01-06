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
    pub fn average_of_levels(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<f64> {
        let mut res: Vec<f64> = Vec::new();
        let mut queue = VecDeque::new(); 

        if let Some(node) = root {
            queue.push_back(node);
        }
        while !queue.is_empty(){
            let level_size = queue.len();
            let mut level_sum: f64 = 0.0;

            for _ in 0..level_size{
                let curr = queue.pop_front().unwrap();        
                level_sum += curr.borrow().val as f64;

                if let Some(left) = &curr.borrow().left{
                    queue.push_back(left.clone());
                };

                if let Some(right) = &curr.borrow().right{
                    queue.push_back(right.clone());
                };
            }

            let level_avg = level_sum / level_size as f64;
            res.push(level_avg);
        }
        return res;
    }
}
