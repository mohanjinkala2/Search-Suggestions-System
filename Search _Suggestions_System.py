class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        def dfs(temp,q,r,v):
            if len(r)==3:
                return
            if temp.full==True and temp.child=={}:
                z=''.join(q)
                r.append(v+z)
                return
            if temp.full==True and temp.child!={}:
                z=''.join(q)
                r.append(v+z)
            for i in temp.child:
                q.append(i)
                dfs(temp.child[i],q,r,v)
                q.pop()
        class node:
           def __init__(self):
             self.child={}
             self.full=False
        class Trie:
            def __init__(self):
               self.root=node()
            def insert(self, word):
                node1=self.root
                for i in word:
                    if i not in node1.child:
                        node1.child[i]=node()
                    node1=node1.child[i]
                node1.full=True
            def prefix(self,word,r):
                node1=self.root
                for i in word:
                    if i not in node1.child:
                        return
                    node1=node1.child[i]
                dfs(node1,[],r,word)
                return False
        trie1=Trie()
        t,r,y=[],[],''
        for i in products:
            trie1.insert(i)
        for i in searchWord:
            r,y=[],y+i
            trie1.prefix(y,r)
            t.append(r+[])
        return t
products=input().split(',')
searchword=input()
print(suggestedProducts(products, searchword))
