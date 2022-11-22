import re
from sys import argv
import os
from pprint import pprint

green = "\033[32m"
red = "\033[31m"
yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
endc = "\033[0m"


def get_words1():
    pwd1 = os.getcwd()
    pstring1 = f"python3 {pwd1}/get_words.py {comp1}"
    os.system(pstring1)


def get_words2():
    pwd2 = os.getcwd()
    pstring2 = f"python3 {pwd2}/get_words.py {comp2}"
    os.system(pstring2)
    
def get_files1():
    pwd3 = os.getcwd()
    pstring3 = f"{pwd3}/{comp1}"
    pstring4 = f"{pwd3}/{comp2}"
    with open(pstring3, 'r') as first_topic:
        first = [str(x).strip("\n") for x in first_topic.readlines()]
    return first
    
def get_files2():
    pwd4 = os.getcwd()
    pstring4 = f"{pwd4}/{comp2}"
    with open(pstring4, 'r') as second_topic:
        second = [str(x).strip("\n") for x in second_topic.readlines()]
    return second
        
def compare(list1, list2):
    
    words = []
    words2 = []
    notwords = []
    notwords2 = []

    for word1 in list1:
        if word1 in list2:
            if word1 in words:continue
            else:words.append(word1)
        else:
            if word1 in notwords:continue
            else:notwords.append(word1)

    for word2 in list2:
        if word2 in list1:
            if word2 in words2:continue
            else:words.append(word2)
        else:
            if word2 in notwords:continue
            else:notwords.append(word2)

    total_first = len(list1)
    total_in_first = len(words)
    total_out_in_first = len(notwords)

    words_in_first_not_in_second = total_out_in_first

    first_inwords = total_in_first/total_first
    first_outwords = total_out_in_first/total_first

    total_second = len(list2)
    total_in_second = len(words2)
    total_out_in_second = len(notwords2)

    second_inwords = total_in_second/total_second
    second_outwords = total_out_in_second/len(list2)


    print(f"total words in first topic not in second:\t {words_in_first_not_in_second} words\n")
    print(f"total words in first topic in second:\t\t {total_in_first} words\n")
    print(f"total words in first topic:\t\t\t {total_first}\n")
    print(f"total words in second topic in first:\t\t {total_second}\n")


    first_inward_percent = first_inwords*100
    first_outword_percent = 100-first_inward_percent

    print(f"Words in First that are in second: {first_inward_percent}%\n")
    print(f"Words in First not in second: {first_outword_percent}%\n")
    
    argv1 = re.compile(argv[1])

    
    if argv[1] in list2 or argv[2] in list1:
        print(f"{green} {argv[1]}{endc} {cyan}is mentioned in {endc} {argv[2]} ")
    elif first_inward_percent > 100:
        print(f"{red}{argv[1]}{endc} {green}is{endc} {red}{argv[2]}{endc}")
    elif first_inward_percent > 70:
        print(f"{red}{argv[1]}{endc} {green}is directly related to{endc} {red}{argv[2]}{endc}")
    elif first_inward_percent > 60:
        print(f"{red}{argv[1]}{endc} {green}is strongly related to{endc} {red}{argv[2]}{endc}")
    elif first_inward_percent > 35:
        print(f"{red}{argv[1]}{endc} {green}is kinda related to{endc} {red}{argv[2]}{endc}")
    elif first_inward_percent > 23:
        print(f"{red}{argv[1]}{endc} {green}is weakly related to{endc} {red}{argv[2]}{endc}")
    elif first_inward_percent > 15:
        print(f"{red}{argv[1]}{endc} {green}is not really related to {endc} {red}{argv[2]}{endc}")
    else:
        print(f"{red}{argv[1]}{endc} {green} has little relation to {endc} {red}{argv[2]}{endc}")

    check1 = argv[1].split(" ")
    xc=False
    for x in check1:
        if x in list2:
            if len(x)>1:
                if xc is False:
                    print(f"{argv[1]} contains words from topic {argv[2]}")
                    xc = True
    xc = False
    check2 = argv[2].split(" ")
    for x in check2:
        if len(x)>1:
            if xc is False:
                print(f"{argv[2]} contains words from topic {argv[1]}")
                xc = True
    g2 = False
    similiar = []
    for x in check1:
        if x in check2:
            g2 = True
            similiar.append(x)

    if g2:
        print(f"They share {[x for x in similiar]} in their names")
    else:
        print('The dont share any similiar words in their names')
    

def compare_names(name1, name2):
    name_words1 = name1.split(" ")
    name_words2 = name2.split(' ')
    total_words1 = len(name_words1)-1
    total_words2 = len(name_words2)-1
    word_density1 = total_words1/total_words2
    word_density2 = total_words2/total_words1
    word_density = word_density2/2 - word_density1/2
    print(f"word Density: {word_density+100}%")

def check_that_have(topic):
    files = os.listdir()
    if topic in files:
        return True
    return False

def filecheck():
    if check_that_have(comp1):pass
    else:get_words1()
    if check_that_have(comp2):pass
    else:get_words2()
    

if __name__ == '__main__':
    comp1 = argv[1]
    comp2 = argv[2]
    filecheck()
    first = get_files1()
    second = get_files2()
    first_count = compare(first, second)
