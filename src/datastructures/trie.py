class __Node__ :
    __slots__=['char','children','is_word']
   
    def __init__(self, char):
        self.char = char
        self.children =  [None] * 26
        self.is_word = False

class Trie:
    __slots__=['root']

    def __init__(self):
        self.root = __Node__("\0")
         
    def __get_last_node (self, pristine_word):
        word = pristine_word.lower()
        current = self.root;
        
        for i, char in enumerate(word, start=0):
            letter_position = ord(char) - ord('a')
            node = current.children[letter_position]
            if node is None:
                return None
            current = node
        return current
         
    def insert_word(self, pristine_word):
        word = pristine_word.lower()
        current = self.root
        for i, char in enumerate(word, start=0):
            # gets an absolut index
            letter_position = ord(char) - ord('a')
            node = current.children[letter_position]
            if node is None:
                node = __Node__(char)
            current.children[letter_position] = node
            current = node
        current.is_word = True

    def has_word (self, pristine_word):
        word = pristine_word.lower()
        last_node = self.__get_last_node(word)        
        return (last_node is not None) and (last_node.is_word == True)

    def has_prefix (self, pristine_word):
        word = pristine_word.lower()
        last_node = self.__get_last_node(word)        
        return last_node is not None
   