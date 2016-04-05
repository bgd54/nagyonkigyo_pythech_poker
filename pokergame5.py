import pokergui5
import tkMessageBox


path = "\\poker\\"
# projectdir/src mappa:
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# path = os.path.join(BASE_DIR, "src")+os.path.sep

def savegame():
    
    file_save=open(path+"pokersave.txt","w")
    file_save.write("My_first_card: "+pokergui5.mycards[0]+"\n")
    file_save.write("My_second_card: "+pokergui5.mycards[1]+"\n")

    file_save.write("Others_first_card: "+pokergui5.othercards[0]+"\n")
    file_save.write("Others_second_card: "+pokergui5.othercards[1]+"\n")
    
    file_save.write("Main1: " + pokergui5.maincards[0]+"\n")
    file_save.write("Main1_state "+pokergui5.card1.cget("text")+"\n")
   
    file_save.write("Main2: " + pokergui5.maincards[1]+"\n")
    file_save.write("Main2_state "+pokergui5.card2.cget("text")+"\n")
   
    file_save.write("Main3: " + pokergui5.maincards[2]+"\n")
    file_save.write("Main3_state "+pokergui5.card3.cget("text")+"\n")
   
    file_save.write("Main4: " + pokergui5.maincards[3]+"\n")
    file_save.write("Main4_state "+pokergui5.card4.cget("text")+"\n")
   
    file_save.write("Main5: " + pokergui5.maincards[4]+"\n")
    file_save.write("Main5_state "+pokergui5.card5.cget("text")+"\n")
   

def opengame():

    pokergui5.showbutton1.config(state="normal")
    del pokergui5.maincards[:]
    del pokergui5.othercards[:]
    del pokergui5.mycards[:]

    states = []
    
    try:
    
        file_open = open(path+"pokersave.txt","r")
        for line in file_open.readlines():
            
            if "My" in line:
                line = line.rstrip("\n")
                card = line.split(" ")[1]
                pokergui5.mycards.append(card)

            elif "Others" in line:
                line = line.rstrip("\n")
                card = line.split(" ")[1]
                pokergui5.othercards.append(card)

            elif "Main" in line and "state" not in line:
                line = line.rstrip("\n")
                card = line.split(" ")[1]
                pokergui5.maincards.append(card)

            elif "state" in line:

                line = line.rstrip("\n")
                state = line.split(" ")[1]
                states.append(state)
                

        pokergui5.gameopen1(pokergui5.maincards,pokergui5.mycards,pokergui5.othercards,states)
                        
    except IOError:
        tkMessageBox.showerror ("No file", "No saved game found")
        
    

def newgame():
    answer = tkMessageBox.askquestion("New Game", "Are You Sure?", icon="warning")
    if answer == "yes":

        answer2 = tkMessageBox.askquestion("Save", "Save game first?", icon="warning")

        if answer2 == "yes":
            savegame()
            pokergui5.game1()
        else:
            
            pokergui5.game1()
            

def showmaincards():

    if pokergui5.card1.cget("text") == "back":

        pokergui5.card1.config(image=pokergui5.cardpictures2[0],text="face")
        pokergui5.playsound(type1="3")

    elif pokergui5.card2.cget("text") == "back":
        
        pokergui5.card2.config(image=pokergui5.cardpictures2[1],text="face")
        pokergui5.playsound(type1="3")

    elif pokergui5.card3.cget("text") == "back":
        pokergui5.card3.config(image=pokergui5.cardpictures2[2],text="face")
        pokergui5.playsound(type1="3")
         

    elif pokergui5.card4.cget("text") == "back":
        pokergui5.card4.config(image=pokergui5.cardpictures2[3],text="face")
        pokergui5.playsound(type1="3")

    elif pokergui5.card5.cget("text") == "back":
        pokergui5.card5.config(image=pokergui5.cardpictures2[4],text="face")
        pokergui5.playsound(type1="3")

        pokergui5.showbutton1.config(state="disabled")
        
        pokergui5.card_others1.config(image=pokergui5.cardpictures3[0])
        pokergui5.card_others2.config(image=pokergui5.cardpictures3[1])
        allcards1 = pokergui5.mycards + pokergui5.maincards
        allcards2 = pokergui5.othercards + pokergui5.maincards
        



def showmycards():

    pokergui5.card_mine1.config(image=pokergui5.cardpictures[0])
    pokergui5.card_mine2.config(image=pokergui5.cardpictures[1])
    pokergui5.playsound(type1="3")

def putmaincards():

    pokergui5.cards1.lift()
    pokergui5.cards2.lift()
    pokergui5.cards3.lift()
    pokergui5.cards4.lift()
    pokergui5.cards5.lift()
    pokergui5.cards_mine.lift()
    pokergui5.cards_others.lift()
    pokergui5.mycardsbutton.config(state="normal")
    pokergui5.showbutton1.config(state="normal")
    pokergui5.showbutton2.config(state="disabled")


 

    
pokergui5.mycardsbutton.config(command=showmycards)
pokergui5.showbutton1.config(command=showmaincards)
pokergui5.showbutton2.config(command=putmaincards)
pokergui5.filemenu.add_command(label="New",command=newgame)
pokergui5.filemenu.add_command(label="Open",command=opengame)
pokergui5.filemenu.add_command(label="Save",command=savegame)


pokergui5.main()