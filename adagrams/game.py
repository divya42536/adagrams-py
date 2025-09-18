from random import randint
LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

SCORE_CHART = {
1 : ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T' ],
2 : ['D', 'G'],
3 : ['B', 'C', 'M', 'P'],
4 : ['F', 'H', 'V', 'W', 'Y'],
5 : ['K'],	
8 : ['J', 'X'],
10 : ['Q', 'Z']
}

def draw_letters():
    # letters = (LETTER_POOL.keys())
    # freq_of_letters = (LETTER_POOL.values())
    pool = []
    for letter , freq in LETTER_POOL.items():
        for freq_count in range(freq):
            pool.append(letter)
    hand = []
    for draw_count in range(10):
        index_val = randint(0,len(pool)-1)
        hand.append(pool[index_val])
        pool.pop(index_val)
    return hand

def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_bank_copy = letter_bank.copy()
    for char in word:
        if char in letter_bank_copy:
            letter_bank_copy.remove(char)
        else:
            return False
    return True

def score_word(word):
    word = word.upper()
    sum_of_points = 0
    for letter in word:
        for points,list_of_letters in SCORE_CHART.items():
            if letter in list_of_letters:
                sum_of_points += points

    if len(word) >= 7:
        sum_of_points += 8

    return sum_of_points

def get_highest_word_score(word_list):
    total_score_chart = {} #In dictionary we storing both word and word_score
    for word in word_list:
        word_score = score_word(word)
        total_score_chart[word] = word_score
    high_score = 0
    best_word = ""
    for word,score in total_score_chart.items():
        if high_score < score  :
            high_score = score
            best_word = word
        elif len(best_word) == 10  :
            return best_word,high_score
        elif len(word) == 10  and len(best_word) != 10:
            best_word = word
            high_score = score
        elif high_score == score and len(best_word)> len(word):
            high_score = score
            best_word = word

    return best_word,high_score
    
    