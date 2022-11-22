import os
import wikipediaapi
import sys

ALPHAX = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHA = [x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
alpha = [x.lower() for x in ALPHA]
ok_fine = "-_'`&@"
punctuationx = '!?.,:;"[]}{()*&^%$#~\n\t'
punctuation = [x for x in punctuationx]
match sys.platform:
    case 'linux':SLASH = "/"
    case 'windows':SLASH = '\\'
words = {
    'a': ['a', 'ability', 'able', 'about', 'above', 'accept', 'according', 'account', 'across', 'act', 'action', 'activity', 'actually', 'add', 'address', 'administration', 'admit', 'adult', 'affect', 'after', 'again', 'against', 'age', 'agency', 'agent', 'ago', 'agree', 'agreement', 'ahead', 'air', 'all', 'allow', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'among', 'amount', 'analysis', 'and', 'another', 'answer', 'any', 'anyone', 'anything', 'appear', 'apply', 'approach', 'area', 'argue', 'arm', 'around', 'arrive', 'art', 'article', 'artist', 'as', 'ask', 'assume', 'at', 'attack', 'attention', 'audience', 'author', 'authority', 'available', 'avoid', 'away'],  
    'b': ['american','baby', 'back', 'bad', 'bag', 'ball', 'bank', 'bar', 'base', 'be', 'beat', 'beautiful', 'because', 'become', 'bed', 'before', 'begin', 'behavior', 'behind', 'believe', 'benefit', 'best', 'better', 'between', 'beyond', 'big', 'bill', 'billion', 'bit', 'black', 'blood', 'blue', 'board', 'body', 'book', 'born', 'both', 'box', 'boy', 'break', 'bring', 'brother', 'budget', 'build', 'building', 'business', 'but', 'buy', 'by'], 
    'c': ['congress','call', 'camera', 'campaign', 'can', 'cancer', 'candidate', 'capital', 'car', 'card', 'care', 'career', 'carry', 'case', 'catch', 'cause', 'cell', 'center', 'central', 'century', 'certain', 'certainly', 'chair', 'challenge', 'chance', 'change', 'character', 'charge', 'check', 'child', 'choice', 'choose', 'church', 'citizen', 'city', 'civil', 'claim', 'class', 'clear', 'clearly', 'close', 'coach', 'cold', 'collection', 'college', 'color', 'come', 'commercial', 'common', 'community', 'company', 'compare', 'computer', 'concern', 'condition', 'conference', 'consider', 'consumer', 'contain', 'continue', 'control', 'cost', 'could', 'country', 'couple', 'course', 'court', 'cover', 'create', 'crime', 'cultural', 'culture', 'cup', 'current', 'customer', 'cut'], 
    'd': ['dark', 'data', 'daughter', 'day', 'dead', 'deal', 'death', 'debate', 'decade', 'decide', 'decision', 'deep', 'defense', 'degree', 'democratic', 'describe', 'design', 'despite', 'detail', 'determine', 'develop', 'development', 'die', 'difference', 'different', 'difficult', 'dinner', 'direction', 'director', 'discover', 'discuss', 'discussion', 'disease', 'do', 'doctor', 'dog', 'door', 'down', 'draw', 'dream', 'drive', 'drop', 'drug', 'during'], 
    'e': ['each', 'early', 'east', 'easy', 'eat', 'economic', 'economy', 'edge', 'education', 'effect', 'effort', 'eight', 'either', 'election', 'else', 'employee', 'end', 'energy', 'enjoy', 'enough', 'enter', 'entire', 'environment', 'environmental', 'especially', 'establish', 'even', 'evening', 'event', 'ever', 'every', 'everybody', 'everyone', 'everything', 'evidence', 'exactly', 'example', 'executive', 'exist', 'expect', 'experience', 'expert', 'explain', 'eye'], 
    'f': ['face', 'fact', 'factor', 'fail', 'fall', 'family', 'far', 'fast', 'father', 'fear', 'federal', 'feel', 'feeling', 'few', 'field', 'fight', 'figure', 'fill', 'film', 'final', 'finally', 'financial', 'find', 'fine', 'finger', 'finish', 'fire', 'firm', 'first', 'fish', 'five', 'floor', 'fly', 'focus', 'follow', 'food', 'foot', 'for', 'force', 'foreign', 'forget', 'form', 'former', 'forward', 'four', 'free', 'friend', 'from', 'front', 'full', 'fund', 'future'], 
    'g': [ 'garden', 'gas', 'general', 'generation', 'get', 'give', 'glass', 'go', 'goal', 'good', 'government', 'great', 'green', 'ground', 'group', 'grow', 'growth', 'guess', 'gun', 'guy'], 
    'h': ['hair', 'half', 'hand', 'hang', 'happen', 'happy', 'hard', 'have', 'he', 'head', 'health', 'hear', 'heart', 'heat', 'heavy', 'help', 'her', 'here', 'herself', 'high', 'him', 'himself', 'his', 'history', 'hit', 'hold', 'home', 'hope', 'hospital', 'hot', 'hotel', 'hour', 'house', 'how', 'however', 'huge', 'human', 'hundred', 'husband'], 
    'i': ['idea', 'identify', 'if', 'image', 'imagine', 'impact', 'important', 'improve', 'in', 'include', 'including', 'increase', 'indeed', 'indicate', 'individual', 'industry', 'information', 'inside', 'instead', 'institution', 'interest', 'interesting', 'international', 'interview', 'into', 'investment', 'involve', 'issue', 'it', 'item', 'its', 'itself'], 
    'j': ['job', 'join', 'just'], 
    'k': ['keep', 'key', 'kid', 'kill', 'kind', 'know', 'knowledge'], 
    'l': ['land', 'language', 'large', 'last', 'late', 'later', 'laugh', 'law', 'lawyer', 'lay', 'lead', 'leader', 'learn', 'least', 'leave', 'left', 'leg', 'legal', 'less', 'let', 'letter', 'level', 'lie', 'life', 'light', 'like', 'likely', 'line', 'list', 'listen', 'little', 'live', 'local', 'long', 'look', 'lose', 'loss', 'lot', 'love', 'low'], 
    'm': ['machine', 'magazine', 'main', 'maintain', 'major', 'majority', 'make', 'man', 'manage', 'management','many', 'market', 'marriage', 'material', 'matter', 'may', 'maybe', 'me', 'mean', 'measure', 'media', 'medical', 'meet', 'meeting', 'member', 'memory', 'mention', 'message', 'method', 'middle', 'might', 'military', 'million', 'mind', 'minute', 'miss', 'mission', 'model', 'modern', 'moment', 'money', 'month', 'more', 'morning', 'most', 'mother', 'mouth', 'move', 'movement', 'movie', 'much', 'music', 'must', 'my', 'myself'],
    'n': ['name', 'nation', 'national', 'natural', 'nature', 'near', 'nearly', 'necessary', 'need', 'network', 'never', 'new', 'news', 'newspaper', 'next', 'nice', 'night', 'no', 'none', 'nor', 'north', 'not', 'note', 'nothing', 'notice', 'now', 'not', 'number'], 
    'o': ['occur', 'of', 'off', 'offer', 'office', 'officer', 'official', 'often', 'oh', 'ok', 'old', 'on', 'once', 'one', 'only', 'onto', 'open', 'operation', 'opportunity', 'option', 'or', 'order', 'organization', 'other', 'others', 'our', 'out', 'outside', 'over', 'own', 'owner'], 
    'p': ['page', 'pain', 'paper', 'parent', 'part', 'participant', 'particular', 'particularly', 'partner', 'party', 'pass', 'past', 'patient', 'pattern', 'pay', 'peace', 'people', 'per', 'perform', 'performance', 'perhaps', 'period', 'person', 'personal', 'phone', 'physical', 'pick', 'picture', 'piece', 'place', 'plan', 'plant', 'play', 'player', 'point', 'police', 'policy', 'political', 'politics', 'poor', 'popular', 'population', 'position', 'positive', 'possible', 'power', 'practice', 'prepare', 'present', 'president', 'pressure', 'pretty', 'prevent', 'price', 'private', 'probably', 'problem', 'process', 'produce', 'product', 'production', 'professional', 'professor', 'program', 'project', 'property', 'protect', 'prove', 'provide', 'public', 'pull', 'purpose', 'push', 'put'],
    'q': ['quality', 'question', 'quickly', 'quite'], 
    'r': ['race', 'raise', 'range', 'rate', 'rather', 'reach', 'read', 'ready', 'real', 'reality', 'realize', 'really', 'reason', 'receive', 'recent', 'recently', 'recognize', 'record', 'red', 'reduce', 'reflect', 'region', 'relate', 'relationship', 'religious', 'remain', 'remember', 'remove', 'report', 'represent', 'require', 'research', 'resource', 'respond', 'response', 'responsibility', 'rest', 'result', 'return', 'reveal', 'rich', 'right', 'rise', 'risk', 'road', 'rock', 'role', 'room', 'rule', 'run', 'republican'], 
    's': ['safe', 'same', 'save', 'say', 'scene', 'school', 'science', 'score', 'sea', 'season', 'seat', 'second', 'section', 'security', 'see', 'seek', 'seem', 'sell', 'send', 'senior', 'sense', 'series', 'serious', 'serve', 'service', 'set', 'seven', 'several', 'sex', 'sexual', 'shake', 'share', 'she', 'shoot', 'short', 'shot', 'should', 'shoulder', 'show', 'side', 'sign', 'significant', 'similar', 'simple', 'simply', 'since', 'sing', 'single', 'sister', 'sit', 'site', 'situation', 'six', 'size', 'skill', 'skin', 'small', 'smile', 'so', 'social', 'society', 'soldier', 'some', 'somebody', 'someone', 'something', 'sometimes', 'son', 'song', 'soon', 'sort', 'sound', 'source', 'south', 'space', 'speak', 'special', 'specific', 'speech', 'spend', 'sport', 'spring', 'staff', 'stage', 'stand', 'standard', 'star', 'start', 'state', 'statement', 'station', 'stay', 'step', 'still', 'stock', 'stop', 'store', 'story', 'strategy', 'street', 'strong', 'structure', 'student', 'study', 'stuff', 'style', 'subject', 'success', 'successful', 'such', 'suddenly', 'suffer', 'suggest', 'summer', 'support', 'sure', 'surface', 'system'], 
    't': ['table', 'take', 'talk', 'task', 'tax', 'teach', 'team', 'television', 'tell', 'ten', 'tend', 'term', 'test', 'than', 'thank', 'that', 'the', 'their', 'them', 'themselves', 'then', 'theory', 'there', 'these', 'they', 'thing', 'think', 'third', 'this', 'those', 'though', 'thought', 'thousand', 'threat', 'three', 'through', 'throughout', 'throw', 'thus', 'time', 'to', 'today', 'together', 'tonight', 'too', 'top', 'total', 'tough', 'toward', 'town', 'trade', 'training', 'travel', 'treat', 'treatment', 'tree', 'trial', 'trip', 'trouble', 'true', 'truth', 'try', 'turn', 'two', 'type'], 
    'u': ['under', 'understand', 'unit', 'until', 'up', 'upon', 'us', 'use', 'usually'], 
    'v': ['value', 'various', 'very', 'victim', 'view', 'violence', 'visit', 'voice', 'vote'], 
    'w': ['wait', 'walk', 'wall', 'want', 'war', 'watch','way', 'we', 'weapon', 'wear', 'week', 'weight', 'well', 'west','what', 'whatever', 'when', 'where', 'whether', 'which', 'while', 'white', 'who', 'whole', 'whom', 'whose', 'why', 'wide', 'wife', 'will', 'win', 'wind', 'window', 'wish', 'with', 'within', 'without', 'woman', 'wonder', 'word', 'work', 'worker', 'world', 'worry', 'would', 'write', 'writer', 'wrong'], 
    'y': ['yard', 'yeah', 'year', 'yes', 'yet', 'you', 'young', 'your', 'yourself'],
    'x': ['x',],
    'z': ['z',]
}


COMMON=[
    'the','at','there','some','my','of','be','use',
    'her','than','and','this','an','would','first','a','have',
    'each','make','water''to','from','which','like','been','in',
    'or','she','him','call','is','one','do','into','who','you','had',
    'how','time','oil','that','by','their','has','its','it','word','if',
    'look','now','he','but','will','two','find''was','not','up','more',
    'long','for','what','other','write','down''on','all','about','go','day',
    'are','were','out','see','did','as','we','many','number','get','with',
    'when','then','no','come','his','your','them','way','made','they',
    'can','these','could','may','I','said','so','people','part'
]


def check_if_in_word_map(word):
    tag = word[0]
    if word in words[tag]:
        return None
    else:
        return word


def get_page_about(topic):
    wikipedia_helper = wikipediaapi.Wikipedia(language='en',extract_format=wikipediaapi.ExtractFormat.WIKI)
    try:
        wikipedia_page = wikipedia_helper.page(topic)
    except:
        raise Exception("TopicError","Can not find the topic ask for")
    return wikipedia_page.text

def wikipedia_page_to_word_list(page):
    mypage = str(page)
    current_word = []
    words = []
    for character in mypage:
        current_char = character
        if current_char in ALPHA:
            current_word.append(current_char)
            continue
        if current_char in alpha:
            current_word.append(current_char)
            continue   
        if current_char == " ":
            if current_word != "":
                words.append("".join(current_word).strip())
                current_word = []
                continue
            else:
                continue
        if current_char in punctuation:
            if current_word != []:
                words.append("".join(current_word).strip())
                current_word = []
                continue  
            else:
                continue
    non_repeating_words = set(words)
    plist = list(non_repeating_words)
    mywords2have = []
    for word in plist:
        length = len(word)
        if length < 2:
            continue
        else:
            xword = str(word).lower()
            mywords2have.append(xword)
    return mywords2have


def get_words_about_nofile(this_topic):
    mytopic = get_page_about(this_topic)
    words_on_topic = wikipedia_page_to_word_list(mytopic)
    return words_on_topic

def remove_common_words(wordss):
    return [word for word in wordss if word not in words[str(word[0])]]



def main():
    from sys import argv

    topic = " ".join(argv[1:]).strip()
    page = get_page_about(topic)
    words = wikipedia_page_to_word_list(page)
    nc_words = remove_common_words(words)
    with open(topic, 'w') as wfile:
        for word in nc_words:
            wfile.write(f"{word}\n")


if __name__ == '__main__':
    main()
    