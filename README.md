Introduction:

You are given an array of strings products and a string searchWord.Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.Return a list of lists of the suggested products after each character of searchWord is typed.

Implementation:

To implement This, Here We Used Trie Data Structure.

STEPS:

1)we want To Create a Trie Class
2)we need to insert words present in products array one by one into Trie,for this we define insert method in trie class.
3)we need to take words from trie,whose's Prefix match with entered searchwordWord.if we have more words then we want to take three lexicographically minimums products.
4)for performing '3' step we use DFS(depth first Search) on Trie.

RESULT/USES:

search suggestions system is widely used in real life for enhancing user experience, speeding up
searches, and improving accuracy.EXAMPLES:1)E-commerce sites (Amazon, eBay)– Suggest products based on user
input.2)Google, Bing, and Yahoo– Auto-complete queries based on popular searches.3)Messaging Apps (WhatsApp,
Telegram)– Predict words for faster typing.

