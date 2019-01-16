


def longest_substring_atmost_k_distinct_char(s1):
    n = len(s1)
    hash_map = {}
    max_substr_len = 0 
    i = 0 
    j = 0
    distinct_count = 0  
    while i < n and j < n:
        key = s1[j]
        if not key in hash_map:
            hash_map[s1[j]] = 1
            distinct_count += 1 
            j += 1
            max_substr_len = max(max_substr_len, j-i)
            max_substr = [i,j]
        else:
            if hash_map[key]
            hash_map.pop(s1[i])
            i += 1
    return max_substr, max_substr_len

if __name__ == "__main__":
    print ("enter a string :")
    str_input = str(input())
    #substr, substr_len = lengthOfLongestSubstring_without_repeition(str_input)
    substr, substr_len = lengthOfLongestSubstring_without_repeition_optimized(str_input)
    i = substr[0]
    j = substr[1]+ 1
    print ("the longest string is : ", str_input[i:j])
    print ("the length of longest string is : ", substr_len)

