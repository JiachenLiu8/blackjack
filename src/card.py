class Card:
    _VALID_FACE_VALUES = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
    _VALID_SUITS = {'spade', 'club', 'diamond', 'heart'}
    
    def __init__(self, face_value: str, suit: str):
        if face_value not in Card._VALID_FACE_VALUES:
            raise ValueError(f'Invalid face_value input. Valid face_values are {Card._VALID_FACE_VALUES}.')
        if suit not in Card._VALID_SUITS:
            raise ValueError(f'Invalid suit input. Valid suits are {self._VALID_SUITS}.')
        self._face_value = face_value
        self._suit = suit
        
    def __eq__(self, other): # __eq__ (i.e. A == B ) is always reserved for comparing all fields of two objects A and B
        return (self._face_value == other._face_value and 
                self._suit == other._suit)

    def __gt__(self, other):
        '''
            Check if A > B by comparing their face_value.
        '''
        face_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        face_value_str_to_int = {}
        for i in range(len(face_values)):
            face_value_str_to_int[face_values[i]] = i + 1
        return face_value_str_to_int[self._face_value] > face_value_str_to_int[other._face_value] 

    def has_same_face_value(self, other):
        '''
            Check if two cards have same face_value.
        '''
        return self._face_value == other._face_value
    
    def __ge__(self, other):
        '''
           Check if A >= B by comparing their face_value.
        '''
        return self > other or self.has_same_face_value(other)
    
    def __lt__(self, other):
        '''
            Check if A < B by comparing their face_value.
        '''
        return not self >= other
    
    def __le__(self, other):
        return self < other or self.has_same_face_value(other)
    
    def __str__(self):
        return f"Card object with face_value={self._face_value}, suit={self._suit}"
        
    def set_face_value(self, face_value: str) -> bool:
        if face_value not in Card._VALID_FACE_VALUES:
            raise ValueError(f'Invalid face_value input. Valid face_values are {Card._VALID_FACE_VALUES}.')
        self._face_value = face_value
        return True
        
    def set_suit(self, suit: str) -> bool:
        if suit not in Card._VALID_SUITS:
            raise ValueError(f'Invalid suit input. Valid suits are {Card._VALID_SUITS}.')
        self._suit = suit   
        return True
        
    def get_face_value(self) -> str:
        return self._face_value
    
    def get_suit(self) -> str:
        return self._suit
    
    def is_face(self) -> bool:
        '''
            Check if the face_value is 'J','K','Q'. 
            Return True if so, False otherwise.
        '''
        return self._face_value.isalpha() and self._face_value != 'A'
    
    def is_ace(self) -> bool:
        return self._face_value == 'A'
    
    def score(self) -> int:
        '''
            Return the numeric value of the card.
            1-10: 1-10.
            J,K,Q: 10.
            A: -1.
        '''
        if self._face_value.isnumeric():
            return int(self._face_value)
        elif self.is_face():
            return 10
        else:
            return -1

    
    
    
    