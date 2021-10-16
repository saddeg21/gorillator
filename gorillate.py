from tkinter import *
from requests import *
import requests
root = Tk()
root.geometry("800x600")
root.configure(background="#ffeead")

canvas = Canvas(root,height=100,width=250,bg= "#ffcc5c",highlightbackground= "#ffaf00",highlightthickness=5)
canvas.place(x=500 ,y=165)

class Buttoner(object):
    def __init__(self,master,bg,text,fg,font,funca):
        self.master=master
        self.bg = bg
        self.text = text
        self.fg = fg
        self.font = font
        self.funca = funca
    def bu(self):
        return Button(self.master,bg = self.bg, text = self.text,fg = self.fg,font=self.font,command = self.funca)
font_title =('Segoe Script', 45, 'bold')
label_title = Label(root,text = "Translator",font = font_title, bg = "#ffeead",fg = "#ffffff")
label_title.pack(padx=30,pady=40)

class Entryer(object):
    def __init__(self,master,bg,font,varname):
        self.master=master
        self.bg=bg
        self.font=font
        self.varname = varname
    
    
    def en(self):
        return Entry(self.master,bg = self.bg,font=self.font,textvariable=self.varname)


    
    
    
font_label= ("Calibri",16)
entry1 = Entryer(root,"#88d8b0",font_label,StringVar())
entry1c = entry1.en()
entry1c.place(x=50,y=190)



lang_choi = ["en","nl","fr","de","it","tr"]
languages = ["English","Dutch","French","German","Italian","Turkish"]
    
var_lang = StringVar()
var_lang.set("English")

lang_sel = OptionMenu(root,var_lang,*languages,)
lang_sel.place( x=355, y =250)




def inputer():
    global translate_it
    translate_it = entry1.varname.get()
    



buton = Buttoner(root,"#ffcc5c","Select Language","#ffffff",font_label,inputer)
butonc = buton.bu()
butonc.place(x=320,y=360)




def target_lang_choicer():
    for n in range(0,6):
        if var_lang.get() == languages[n]:
            global target_lang
            target_lang = lang_choi[n] 
            
            

label2 = Label(canvas,bg="#ffeead",font=font_label,fg="#000000", borderwidth=5, relief="groove",width=5)
label2.place(x=75,y=30)

def gorillate():
    api_url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    payload = "q="+(translate_it)+"&"+"target="+(target_lang)+"&"
    headers = {'content-type': "application/x-www-form-urlencoded",
        'accept-encoding': "application/gzip",
        'x-rapidapi-host': "google-translate1.p.rapidapi.com",
        'x-rapidapi-key': "5b34cf11e9msh9db378adc917d23p15dd92jsnf35313199647"}
    response = requests.post(api_url,data=payload,headers=headers)
    translate = response.json()["data"]["translations"][0]["translatedText"]
    global label2
    label2.destroy()
    label2 = Label(canvas,bg="#ffeead",font=font_label,fg="#000000",text = translate, borderwidth=5, relief="groove")
    label2.place(x=75,y=30)

    
buton22 = Button(root,bg ="#ff6f69", font= font_label, command = lambda:[inputer(),target_lang_choicer(),gorillate()],text = "Translate",fg="#ffffff")

buton22.place(x=350,y=180)

root.mainloop()

    