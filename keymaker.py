import string

def shift_characters(word, shift, cara):
    caracters = cara
    abc = list(string.ascii_lowercase)
    #print(abc.index("a"))
    new_word = ""
    index = shift%26

    for i in word.lower():
        if i in caracters:
            pass
        elif abc.index(i)+index <= len(abc)-1:
            new_word +=  abc[abc.index(i)+index]
        else:
            new_word += abc[abc.index(i)+index-len(abc)]
    return new_word


#print(shift_characters("abby",3))



def pad_up_to(word, shift, n, cara):
    caracters = cara
    shifted_word = word
    for i in range(n-len(word)):
        new_word =  shift_characters(shifted_word[i],shift, cara)
        shifted_word += new_word
    return shifted_word

#print(pad_up_to('morpheus',15,19))


def abc_mirror(word, cara):
    caracters = cara
    abc = list(string.ascii_lowercase)
    new_word = ""
    for i in word.lower():
        if i in caracters:
            pass
        else:
            new_word += abc[25-abc.index(i)]
    return new_word

#print(abc_mirror("morpheus"))


def create_matrix(word1, word2, cara):
    abc = list(string.ascii_lowercase)
    matrix = []
    for i in range(len(word2)):
        if i in cara:
            pass
        else:
            new_word = shift_characters(word1,abc.index(word2[i]),cara)
            matrix.append(new_word)
    return matrix

#print(create_matrix('mama',"papa"))


def zig_zag_concatenate(matrix, cara):
    conc_word = ""
    count = 0
    for index in range(len(matrix[0])):
        for index in range(len(matrix)):
            temp = ""
            for i in range(len(matrix[index])):
                temp += matrix[index][count]
                break
            conc_word += temp
        count += 1
    return conc_word

#print(zig_zag_concatenate(['xyzabcdef', 'xyzabcdef', 'xyzabcdef', 'xyzabcdef']))


def rotate_right(word, n, cara):
    *letters, = word
    shift_num = len(letters)-(n%len(word))
    #print(letters, shift_num)
    new_word = ""
    for i in range(len(letters)):
        if i in cara:
            pass
        else:
            new_word+= letters[i+shift_num-len(letters)]
    return new_word

#print(rotate_right('morpheus', 3))


def get_square_index_chars(word, cara):
    squere_index = ""
    try:
        for i in range(len(word)):
            if i in cara:
                pass
            else:
                squere_index += word[i**2]
        return squere_index
    except:
        return squere_index

#print(get_square_index_chars('abcdefghijklm'))


def remove_odd_blocks(word, block_length, cara):
    sliced_word_parts = []
    for i in range(len(word)//block_length+1):
        sliced_word_parts.append(word[block_length*i:block_length*(i+1)])
    new_word=""
    for i in range(len(sliced_word_parts)):
        if i%2==0:
            new_word+= sliced_word_parts[i]
    return new_word

#print(remove_odd_blocks('abcdefghijklm',3))


def reduce_to_fixed(word, n, cara):
    cut_word = word[:n]
    new_word = rotate_right(cut_word[::-1],n//3,cara)
    return new_word

#print(reduce_to_fixed('abcdefghijklm',6))


def hash_it(word):
    caracters = [".",",","?","!","/","<","1",'2',"3","4","5","6","7","8","9","0","'",'"']
   
    padded = pad_up_to(word, 15, 19, caracters) #oké
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded,caracters),caracters),caracters) #ooké
    rotated = rotate_right(elongated, 3000003,caracters) #okkkkk
    cherry_picked = get_square_index_chars(rotated,caracters) #donee
    halved = remove_odd_blocks(cherry_picked, 3,caracters)
    key = reduce_to_fixed(halved, 6, caracters)
    return key


# if __name__ == '__main__':
#     name = input("Enter your name! ").lower()
#     print(f'Your key: {hash_it(name)}')

def write_to_txt(text, text2):
    cara = [".",",","?","!","/","<","1",'2',"3","4","5","6","7","8","9","0","'",'"']
    with open(text,'r',encoding = 'utf-8') as f, open(text2, "w") as f2:
        old = f.readlines()
        print(old)
        for line in old:
            new = line.split()
            for word in range(len(new)):
                for letter in new[word]:
                    if letter in cara:
                        new[word].replace(letter,"")
                        new[word] = hash_it(new[word])+letter
                    else:
                        new[word] = hash_it(new[word])
            print(new)
            f2.write(" ".join(new)+"\n")

  
      

path = "/home/andrograf/github_rep/Projects/test_projects/keymaker-python-andrograf/titkos.txt"
path2 = "/home/andrograf/github_rep/Projects/test_projects/keymaker-python-andrograf/test.txt"
   
write_to_txt(path, path2)

   
