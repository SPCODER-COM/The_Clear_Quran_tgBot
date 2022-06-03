
def lang(msg):
    
    msg=" ".join(msg[1:])

    ar="ذدجحخهعغفقثصضطكمنتالبيسشظزوةىلارؤءئأآ"
    en="poiuytrezamlkjhgfdsqnbvcxw"
    for i in en.lower():
        if i in msg.lower() :
            x="en"
            return x
    
    for i in ar:
        if i in msg :
            x="ar"
            return x





def surahName(msg):
    
    
    
    if lang(msg)=="ar" :
        with open ("Data/ar_Snames.txt",mode="r",encoding="utf_8") as su:
            su=su.read().split("\n")
            su.insert(0,None)
            
            return su
    if lang(msg)=="en":
        with open ("Data/en_Snames.txt",mode="r",encoding="utf_8") as su:
            su=su.read().split("\n")
            su.insert(0,None)
            
            return su 


            



