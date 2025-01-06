impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let word1_length = word1.len();
        let word2_length = word2.len();

        let mut result = String::with_capacity(word1_length + word2_length);

        for (c1, c2) in word1.chars().zip(word2.chars()) {
            result.push(c1);
            result.push(c2);
        }

        if word1_length > word2_length {
            result.push_str(&word1[word2_length..]);
        } else if word2_length > word1_length {
            result.push_str(&word2[word1_length..]);
        }
        result
    }
}
