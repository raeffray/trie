from datastructures.trie import Trie

trie = Trie()

trie.insert_word('leira') 

trie.insert_word('renato') 

trie.insert_word('lena') 

trie.insert_word('hana') 

trie.insert_word('zahav') 

has = trie.has_word('renato') 

hasPrefix = trie.has_prefix('le') 

print(has)
print(hasPrefix)