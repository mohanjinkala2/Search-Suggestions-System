# **INTRODUTION**:

You are given an array of strings products and a string searchWord.Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.Return a list of lists of the suggested products after each character of searchWord is typed.

# **IMPLEMENTATION**:

  To implement This, Here We Used Trie Data Structure.

  # **STEPS**:

     1)we want To Create a Trie Class which contain's:
         i)hash map # which store word alphabets
         ii)boolean value(True/false) # which indicate end of word
         iii)insert method
         iv)prefix method
     2)we need to insert words present in products array one by one into Trie,for this we define insert method in trie class.
     3)we need to take words from trie,whose's Prefix match with entered searchwordWord.if we have more words then we want to take three lexicographically minimums 
     products.
     4)for performing '3'rd step we apply DFS(depth first Search) on Trie.

# **RESULT/USES**:

search suggestions system is widely used in real life for enhancing user experience, speeding up
searches, and improving accuracy.EXAMPLES:1)E-commerce sites (Amazon, eBay)– Suggest products based on user
input.2)Google, Bing, and Yahoo– Auto-complete queries based on popular searches.3)Messaging Apps (WhatsApp,
Telegram)– Predict words for faster typing.
# **EXAMPLE**:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
# **Explanation**: 
products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
