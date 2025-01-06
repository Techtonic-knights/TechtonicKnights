impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let mut result = String::with_capacity(word1.len() + word2.len());
        let max_length = word1.len().max(word2.len());
        
        let mut word1_iter = word1.chars();
        let mut word2_iter = word2.chars();

        for _ in 0..max_length {
            if let Some(c) = word1_iter.next() {
                result.push(c);
            }
            if let Some(c) = word2_iter.next() {
                result.push(c);
            }
        }
        result
    }
}
