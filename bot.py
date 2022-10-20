

from pyarabic.araby import  strip_diacritics 
import os,os.path
import telebot 
from get_surahslist import send_list
from detLang import lang , surahName






bot = telebot.TeleBot("bot token")



#_______________________________________________________    



#______________ ver ______________________________
q="/q" # to get surah os verses from surah
Q="/Q" # to get surah os verses from surah too
l="/l" # to get list of surah(s) wheth nem of it
ar="ar"
en="en"





#_________________________________________________


#_____________ start end help _______________________________________________________________________
@bot.message_handler(commands=['start'])
def start_replay(message):
    bot.reply_to(message, "Hello USER with this bot \nyou can have surah as text or\nverse from it or collection\n of verses use /help to see how it works\n\n.")

@bot.message_handler(commands=['v'])
def v_replay(message):
    with open ("v.txt",mode="r",encoding="utf_8") as versions:
        versions=versions.read()
        bot.reply_to(message,f"*{versions}*",parse_mode="Markdown")
    

@bot.message_handler(commands=['help'])
def help_replay(message):
    with open ("doc.txt",mode="r",encoding="utf_8") as he:
        he=he.read()
        bot.reply_to(message,he,parse_mode="Markdown")
#____________________________________________________________________________________________________



#__________mes handler ____________________________
@bot.message_handler(func=lambda message: True)
def get_msg(message):
    s="/s" # ver to search in Quran
    msg=message.text.split(" ") 
    
    
    if msg[0]==l:
        bot.reply_to(message, f"List of the names of the Holy Quran\n\n{send_list()}")
        
    if msg[0] == s :
        def w(msg):
            msg=" ".join(msg[1:])
            w=msg
            return w
        w=w(msg)
        
        if lang(msg)== ar:
            arFilles="Data/ar"
            files=os.listdir(arFilles)
            d=arFilles
            

        if lang(msg)== en:
            enFilles="Data/en"
            files=os.listdir(enFilles)
            d=enFilles   


        if len(msg)<= 3 :
            
            bot.reply_to(message, f"*Sorry!.\n You must enter a sentence of at least three words*",parse_mode="Markdown")
        else:
            a=0
            
                 
            

            
    
            fileList=[]
            tempfile=message.message_id
            #___________________ creat new txt file as temp to past 
            #___________________ search rus in it 
            with open (f"{tempfile}.txt",mode="w",encoding="utf_8") as m:
                m.close()
        #_________________________________________________________________
            
            
        #______ search for w =" user search words" on all verses of quran
            for i in range(0,len(files)):
                
                with open(f"{d}/{files[a]}",mode="r",encoding="utf_8") as file: 
                    for line in file.read().split("\n"):
                        
                        
                        if lang(msg)==ar :
                            
                            word=strip_diacritics(line)
            
                            w=strip_diacritics(w)
                            word=word.replace('إ','ا')
                            word=word.replace('أ','ا')

                            w=w.replace('إ','ا')
                            w=w.replace('أ','ا')

                            
                        else: 
                        
                            word=line.lower()
                                
                            w=w.lower()
                            w.replace(", .","")
                        if w in word:
                            
                            
                        #___ cheng num of surah whith name of it
                            su=surahName(msg)
                            surah=str(files[a])
                            surah=surah[:-4]
                        #___if w whas find , printit to file 
                            if lang(msg)==en:
                                ref=  f"#*Surah* :*{su[int(surah)]}*\n\n"
                            if lang(msg)==ar:
                                ref=f"#*سورة*:*{su[int(surah)]}*\n\n"
                            bold=line.replace(w,f"*{w}*")
                            x=f"{bold}\n{ref}" 
                            
                            
                            fileList.append(x)

                            with open (f"{tempfile}.txt",mode="a",encoding="utf_8") as wr:
                                wr.write(x)
                            #____________________________________________________________________
                a=a+1
            #___ check if res exist 
            if  os.stat(f'{tempfile}.txt').st_size != 0 :
                
         
        
            #____  send res to user
                with open (f'{tempfile}.txt',mode="r",encoding="utf_8") as r:
                    se_res=r.read()
                    #___ split res msg 
                    if len(se_res) > 4090:
                        for n in range(0, len(se_res), 4090):
                            bot.reply_to(message, f"{se_res[n:n+4090]}",parse_mode="Markdown")
                    
                    else:
                        bot.reply_to(message, f"{se_res}",parse_mode="Markdown")

            else: # send error msg if ther is no res in temp file"
                bot.reply_to(message, "**Sorry!.\n It seems that there is no result for your search. Try other words**")
            #--- CLEAR temp folder 
            os.remove(f"{tempfile}.txt")
        
    #______ get surah or vers _ verses 
    if msg[0]==q or msg[0]==Q :

        if msg[1] != ar and msg[1] != en:
            bot.reply_to(message, "*Please chois lang \n /help to see how it's work*",parse_mode="Markdown")
        else:
            if msg[1] == ar:

                s=f"ar/{int(msg[2])}"
            if msg[1] == en :
                s=f"en/{int(msg[2])}"
        

            if not os.path.exists(f"Data/{s}.txt") :
                bot.reply_to(message, f"*Error !\nThere is no surah with this number ({s[3:]})*",parse_mode="Markdown")
            
            else:
                if len(msg) ==4:
            
                    add=msg[3]
                    msg.append(add)
            
    
                with open (str(f"Data/{s}.txt"),mode='r',encoding="utf_8")as f:

                    search=f.read().split("\n")
        
                if len(msg) == 3:
                    v=search
                    verse=""
            
                    for i in v:
                        verse=verse+i+"\n"
            
                    if len(verse) > 4090:
                        for n in range(0, len(verse), 4090):
                            bot.reply_to(message, f"\n{verse[n:n+4090]}\n\n.")
                    
                    else:
                        bot.reply_to(message, f"\n{verse}\n\n.")
                    
                else:
                    fro=int(msg[3])
                    t=int(msg[4])
                    f=fro-1
                    r=len(search)
                    if fro > r or t > r:
                        
                        bot.reply_to(message, "*Error ! \nThe number you entered is greater than the number of verses in the surah*",parse_mode="Markdown")
                    else:
            
                        v=search[f:t]
            
                        verse=""
            
                        for i in v:
                            verse=verse+i+"\n"
            
                        if len(verse) > 4090:
                            for n in range(0, len(verse), 4090):
                                bot.reply_to(message, f"\n{verse[n:n+4090]}\n\n")
                    
                        else:
                            bot.reply_to(message, f"\n{verse}\n\n")
                



            
                
                
               
            
                

        
        
    else:
        pass


bot.infinity_polling()
