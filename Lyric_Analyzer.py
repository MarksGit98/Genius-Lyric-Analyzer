import lyricsgenius as genius
api=genius.Genius('M2NGssjEmf1sVQ9Wl9VrFccCnat6V8bFxgXw0cb22WO-9ByfIdmS3-feZgMmDvU4')
#artist= api.search_artist('XXXTentacion', max_songs=3)
song = api.search_song('GUMMO', '6IX9INE')
Soundcloud_Albums={'6ix9ine': {'DAY69':['BILLY','GUMMO','RONDO','KEKE','93','DOOWEE','KOODA','BUBA','MOOKY','GUMMO (Remix)','CHOCOLATÉ']},
                   'XXXTENTACION' : {'Ice Hotel':['Ice Hotel','Inuyasha','Ocean (Interlude)','Blood Stains','Very Rare Boyz','Sounds Of The Melting Pot','Fuck V2'],
                                     'The Fall':['Never','Ghost','The Fall','White Girl', 'FuckABitchFace'],
                                     #'Heartbreak Hotel': ['Skin','Teeth (Interlude)','Eyes','Lips','Glass House'],
                                     'ItWasntEnough':['Snow','Manikin','I LUv My CliQue LiKe KaNyE WeSt'],
                                     'WILLY WONKA WAS A CHILD MURDERER' : ['Valentine','King','Willy Wonka Was A Child Murderer','Never'],
                                     'Revenge':['Look at Me!',"I don't wanna do this anymore","Looking for a Star (Can't Get You Out My Head)",'Valentine','King','Slipknot','YuNg BrAtz'],
                                     '17': ['The Explanation','Jocelyn Flores','Depression & Obsession','Everybody Dies in Their Nightmares','Revenge','Save Me', 'Dead Inside (Interlude)','Fuck Love','Carry On','Orlando','Ayala (Outro)'],
                                     'A GHETTO CHRISTMAS CAROL!':['A GHETTO CHRISTMAS CAROL','hate will never win','UP LIKE AN INSOMNIAC (Freestyle)','Red Light!','Indecision'],
                                     'Ugly - EP':['UGLY*','Love Yourself*','Angel*'],
                                     '"?" (Question Mark)':['OMG!*','SMASH!*','Untitled*','SAD!','Before I close my eyes*','Poison*','Moonlight!*','changes','The interlude that never ends*','PAIN = BEST FRIEND*','Through The Night*'],
                                     }
                    }

#print (song.lyrics)
bad_words=[]
word_dict={}
word=''
total_words=0
for letter in song.lyrics:
    
    if letter == ' ' or letter == '\n' or letter == '(' or letter == ')' or letter == ','  or letter == '"':
        total_words+=1
        if word in word_dict:
            word_dict[word]+=1
            word=''
        else:
            word_dict[word]=1   
            word=''
    else:
        word+=(letter.lower())

new_word_dict={}
for word in word_dict:
    if word != '':
        new_word_dict[word]=word_dict[word]

word_dict=new_word_dict
        
word_list=[]
for word in word_dict:
    word_list.append(word)

def main():
    key_word = input("Enter a word from the song: ")
    search_word=key_word.upper()
    if search_word in word_dict:
        print("The word", '"'+key_word+'" appears', word_dict[search_word], "times in the song", song.title, "by", song.artist)
    else:
        print("The word",'"'+key_word+'" is not in the song',song.title, "by", song.artist)
        
    print("Total words in song:",total_words)
    
def album_analyzer(name):
    artists_songs = Soundcloud_Albums[name]
    word_dict={}
    for album in artists_songs:
        print ('ALBUM:',album)
        album_songs = artists_songs[album]
        for song in album_songs:
            print(song)
            track = api.search_song(song , name)
            word=''
            total_words=0
            for letter in track.lyrics:
                if letter == ' ' or letter == " " or letter == '\n' or letter == '(' or letter == ')' or letter == ','  or letter == '"':
                    total_words+=1
                    if word in word_dict:
                        word_dict[word]+=1
                        word=''
                    else:
                        word_dict[word]=1
                        word=''
                else:
                    word+=(letter.upper())
                    
    word_list=[]
    for word in word_dict:
        word_list.append(word)
    return exclude_articles(word_list, word_dict)
        
def sort(word_list, word_dict):
    less=[]
    equal=[]
    greater=[]
        
    if len(word_list) > 0:
        pivot=word_dict[word_list[0]]
            
        for word in word_list:
            if word_dict[word] < pivot:
                less.append(word)
        
            if word_dict[word] > pivot:
                greater.append(word)
                
            if word_dict[word] == pivot:
                equal.append(word)
                    
        return sort(less, word_dict)+equal+sort(greater, word_dict)
    
    else:
        return word_list

def get_sorted_list(word_list, word_dict):
    array=sort(word_list, word_dict)
    new_list=[]
    for word in array:
        if len(word)>0:
            new_list.append(word)
            print(word+":", word_dict[word])
        else:
            continue
    return new_list

def exclude_articles(word_list, word_dict):
    array=sort(word_list,word_dict)
    articles_list=["THE", "A"]
    new_list=[]
    for word in array:
        if len(word)>0 and word not in articles_list:
            new_list.append(word)
            print(word+":", word_dict[word])
        else:
            continue
    return new_list
            
#get_sorted_list(word_list)
album_analyzer('XXXTENTACION')
