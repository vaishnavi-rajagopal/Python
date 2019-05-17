import random
import game_class.explain as explain

f = open("/Users/vaishnavi/Documents/MIDS/Python/Assignments/assignments_upstream_spring19/SUBMISSIONS/project_1/pokemon.txt",'r')
data = f.readlines()
    
class Player():
    '''
    This is the class created for the Players in the Game. 
    The class contains details of the players like card, active pokemon, name and count of cards.
    '''

    plyr_actpk = ''
    plyr_crd = []
    plyr_nm = ''
    pk_count = 3
    
    def __init__(self,name):
        self.plyr_nm = name
        
    def __str__(self):
        return (','.join(self.plyr_nm))
    
    def __repr__(self):
        return (self.plyr_nm)

    def set_actpk(self,attr):
        self.plyr_actpk = attr
    
    def status(self):
        '''This method displays the status of the player in terms of the pokemons left and the active pokemon details.
           This does not return any value.'''
        print ("Status of Player {0}:" .format(self.plyr_nm))
        print ("Total Pokemons left {0} and the active Pokemon is {1} with balance HP = {2}" .format(self.pk_count, self.plyr_actpk.crd_nm,self.plyr_actpk.pk_hp))
        
    def rem_actpk(self,attr):
        '''This method is used to remove the active pokemon from the players total pokemons. This method does not return any value'''
        for i in range(len(self.plyr_crd)):
            if (self.plyr_crd[i].crd_nm == attr):
                self.plyr_crd.pop(i)
                break

    def choose_pokemon(self):
        '''This method is used to choose an active pokemon from the players list of pokemon.'''
        
        if (len(self.plyr_crd) > 1 ):
            print("")
            print("Player {0} - Your Pokemon's are - {1}" .format(self.plyr_nm,self.plyr_crd))
            print("")
            for i in range(len(self.plyr_crd)):
                explain.poke_expl(self.plyr_crd[i])
            check = False
            while(check == False):
                ap = input("Please choose your active pokemon - ")
                check = explain.validate(ap,'pk_name',self)
            self.set_actpk(Card('P',ap))
            self.rem_actpk(ap)
        else :
            ap = str(self.plyr_crd[0].crd_nm)
            self.set_actpk(Card('P',ap))
            print("Player {0} - Your active Pokemon is {1}" .format(self.plyr_nm,self.plyr_actpk.crd_nm))
            self.rem_actpk(ap)
    
class Card():
    '''Class for the pokemon cards in the game and lists all the attributes specific to the pokemon'''
    
    crd_type = ''
    crd_nm = ''
    pk_type = ''
    pk_mov1 = ''
    pk_mov2 = ''
    pk_hp = 0
    apk_hp = 0
    pk_weakness = ''
    enrgy_type = ''
    sup_msg = ''
    item_msg = ''
    global data
    
    def __init__(self,card_type,card_name):
        list_data2 = []
        if (card_type == 'P' or card_type == 'I' or card_type == 'S' or card_type =='E'):
            self.crd_type = card_type
            self.crd_nm = card_name
        for i in range(len(data)):
            list_data2.append(data[i].split(',')) 
            if (self.crd_nm == list_data2[i][1]):
                self.pk_type = list_data2[i][2]
                self.pk_mov1 = list_data2[i][3]
                self.pk_hp = list_data2[i][4]
                self.pk_weakness = list_data2[i][5]
                self.pk_mov2 = list_data2[i][6]
                break

    def __str__(self):
        return (str(self.crd_nm))
    
    def __repr__(self):
        return (str(self.crd_nm))

    def get_char(self,char = None):
        x = 0
        mv1 = str(self.pk_mov1).split('-')
        if ('-' in self.pk_mov2):
            mv2 = str(self.pk_mov2).split('-')
            x = 1
        if (char == 'move1'):
            return str(mv1[0])
        elif (char == 'move1_hp'):
            return str(mv1[1])
        elif (char == 'hp'):
            return str(self.pk_hp)
        elif (char == 'type'):
            return str(self.pk_type)
        elif (char == 'move2' and x == 1):
            return str(mv2[0])
        elif (char == 'move2_hp' and x == 1):
            return str(mv2[1])
        elif (char == 'weak'):
            return str(self.pk_weakness)
        elif (char == None):
            return (str(self.crd_type)+'|'+str(self.crd_nm)+'|'+str(self.pk_type)+'|'+str(mv1[0])
                +'|'+str(self.pk_hp)+'|'+str(mv2[0])+'|'+str(self.pk_weakness))
    
class Deck():
    '''Class for the card Deck and contains all the pokemon cards loaded using the pokemon.txt file.'''
    
    crd_deck = []
    global data

    def __init__(self):
        self.crd_deck = []
        for i in range(len(data)):
            list_data = data[i].split(',')
            self.crd_deck.append(Card(card_type = 'P',card_name = list_data[1]))
            
    def shuffle(self):
        random.shuffle(self.crd_deck)
        
    def __str__(self):
        cards = []
        for i in range(len(self.crd_deck)):
            cards.append(self.crd_deck[i].crd_nm)
        return (' '.join(cards))
    
    def __repr__(self):
        return (str(self.crd_deck.crd_nm))
    
    def deal_cards(self,cnt):
        self.cards_final = []
        if (len(self.crd_deck)<cnt):
            raise Exception ("Cannot deal {0} cards. The deck only has {1} cards left!".format(cnt,len(self.crd_deck)))
        for i in range(cnt):
            self.cards_final.append(self.crd_deck.pop(0))
        return (self.cards_final)
