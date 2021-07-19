from tkinter import *
from PIL import ImageTk, Image
import os
import webbrowser
from tkinter import ttk

master=Tk()
master.title("coach.com")

def open():
    print("Nothing")

def format():
    for widget in handbags_win.winfo_children():
        widget.destroy()
    for widget in giftservice_win.winfo_children():
        widget.destroy()
    handbags_win.pack_forget()
    giftservice_win.pack_forget()


def handbags():
    format()

    handbags_win.pack(fill="both", expand=1)
    handcanvas=Canvas(handbags_win)
    handcanvas.pack(side=LEFT,fill="both",expand=1)
    handscrollbar=Scrollbar(handcanvas,command=handcanvas.yview)
    handscrollbar.pack(side=RIGHT,fill=Y)
    handcanvas.config(yscrollcommand=handscrollbar.set)
    handcanvas.bind("<Configure>",lambda e:handcanvas.config(scrollregion=handcanvas.bbox("all")))
    hand_frame=Frame(handcanvas)
    handcanvas.create_window((0,0),window=hand_frame,anchor="nw")
    myscrollbar.pack_forget()

    hand_frame1 = Frame(hand_frame)
    hand_frame1.pack()
    toplabel=Label(hand_frame1,text="\n\nExplore All Bags\n", font="Calibri 22")
    toplabel.grid(row=0,columnspan=7)

    # professor's path:
    '''
    b1="C:/SDTPGMS/FL2020/button1.png"
    b2="C:/SDTPGMS/FL2020/button2.png"
    b3="C:/SDTPGMS/FL2020/button3.png"
    b4="C:/SDTPGMS/FL2020/button4.png"
    b5="C:/SDTPGMS/FL2020/button5.png"
    b6="C:/SDTPGMS/FL2020/button6.png"
    b7="C:/SDTPGMS/FL2020/button7.png"
    himg1="C:/SDTPGMS/FL2020/h_image1.png"
    himg2="C:/SDTPGMS/FL2020/h_image2.png"
    himg3="C:/SDTPGMS/FL2020/h_image3.png"
    himg4="C:/SDTPGMS/FL2020/h_image4.png"
    himg5="C:/SDTPGMS/FL2020/h_image5.png"
    himg6="C:/SDTPGMS/FL2020/h_image6.png"
    himg7="C:/SDTPGMS/FL2020/h_image7.png"
    himg8="C:/SDTPGMS/FL2020/h_image8.png"
    himg9="C:/SDTPGMS/FL2020/h_image9.png"
    himg10="C:/SDTPGMS/FL2020/h_image10.png"
    himg11="C:/SDTPGMS/FL2020/h_image11.png"
    himg12="C:/SDTPGMS/FL2020/h_image12.png"
    himg13="C:/SDTPGMS/FL2020/h_image13.png"
    himg14="C:/SDTPGMS/FL2020/h_image14.png"
    himg15="C:/SDTPGMS/FL2020/h_image15.png"
    himg16="C:/SDTPGMS/FL2020/h_image16.png"
    himg17="C:/SDTPGMS/FL2020/h_image17.png"
    himg18="C:/SDTPGMS/FL2020/h_image18.png"
    '''

    # my path:
    b1="coach/button1.png"
    b2="coach/button2.png"
    b3="coach/button3.png"
    b4="coach/button4.png"
    b5="coach/button5.png"
    b6="coach/button6.png"
    b7="coach/button7.png"
    himg1="coach/h_image1.png"
    himg2="coach/h_image2.png"
    himg3="coach/h_image3.png"
    himg4="coach/h_image4.png"
    himg5="coach/h_image5.png"
    himg6="coach/h_image6.png"
    himg7="coach/h_image7.png"
    himg8="coach/h_image8.png"
    himg9="coach/h_image9.png"
    himg10="coach/h_image10.png"
    himg11="coach/h_image11.png"
    himg12="coach/h_image12.png"
    himg13="coach/h_image13.png"
    himg14="coach/h_image14.png"
    himg15="coach/h_image15.png"
    himg16="coach/h_image16.png"
    himg17="coach/h_image17.png"
    himg18="coach/h_image18.png"


    def bag1():
        webbrowser.open("https://www.coach.com/shop/women-handbags-shoulder-bags")
    def bag2():
        webbrowser.open("https://www.coach.com/shop/women-handbags-totes")
    def bag3():
        webbrowser.open("https://www.coach.com/shop/women-handbags-satchels")
    def bag4():
        webbrowser.open("https://www.coach.com/shop/women-handbags-crossbody-bags")
    def bag5():
        webbrowser.open("https://www.coach.com/shop/women-handbags-belt-bags")
    def bag6():
        webbrowser.open("https://www.coach.com/shop/women-handbags-clutches")
    def bag7():
        webbrowser.open("https://www.coach.com/shop/women-handbags-backpacks")

    global bn1, bn2,bn3,bn4,bn5,bn6,bn7
    bn1 = ImageTk.PhotoImage(Image.open(b1).resize((180,210),Image.ANTIALIAS))
    button1=Button(hand_frame1, image=bn1,bd=0,command=bag1)
    button1.grid(row=1,column=0)
    bn2= ImageTk.PhotoImage(Image.open(b2).resize(((180,210)),Image.ANTIALIAS))
    button2= Button(hand_frame1, image=bn2,bd=0,command=bag2)
    button2.grid(row=1, column=1)
    bn3 = ImageTk.PhotoImage(Image.open(b3).resize((((180,210))),Image.ANTIALIAS))
    button3 = Button(hand_frame1, image=bn3,bd=0,command=bag3)
    button3.grid(row=1, column=2)
    bn4 = ImageTk.PhotoImage(Image.open(b4).resize((((180,210))),Image.ANTIALIAS))
    button4= Button(hand_frame1, image=bn4, bd=0,command=bag4)
    button4.grid(row=1, column=3)
    bn5 = ImageTk.PhotoImage(Image.open(b5).resize((((180,210))),Image.ANTIALIAS))
    button5 = Button(hand_frame1, image=bn5, bd=0,command=bag5)
    button5.grid(row=1, column=4)
    bn6 = ImageTk.PhotoImage(Image.open(b6).resize((((180,210))),Image.ANTIALIAS))
    button6 = Button(hand_frame1, image=bn6, bd=0, command=bag6)
    button6.grid(row=1, column=5)
    bn7 = ImageTk.PhotoImage(Image.open(b7).resize((((180,210))),Image.ANTIALIAS))
    button7 = Button(hand_frame1, image=bn7, bd=0, command=bag7)
    button7.grid(row=1, column=6)

    hand_frame2=Frame(hand_frame,bg="white",padx=10)
    hand_frame2.pack(side=LEFT,anchor=NW)
    labelx=Label(hand_frame2,text="FILTERS",font="Calibri 13",bg="white")
    labelx.grid(row=0,sticky=W,pady=(20,30))
    labely = Label(hand_frame2, text="CLEAR", font="Calibri 13", bg="white",state="disabled")
    labely.grid(row=0, sticky=N,pady=(20,30))

    combobox1=ttk.Combobox(hand_frame2,width=20,height=70,font="Calibri 13")
    combobox1['value']=("Color","Black","Brown","White","Beige","Blue","Red","Burgundy")
    combobox1.current(0)
    combobox1.grid(row=1,pady=5,sticky=W)
    combobox2 = ttk.Combobox(hand_frame2, width=20,height=70,font="Calibri 13")
    combobox2['value'] = ("price", "$0-$100","$100-$200","$200-$300","$300-$400","$400-$500")
    combobox2.current(0)
    combobox2.grid(row=2, pady=5)
    combobox3 = ttk.Combobox(hand_frame2,width=20,height=70,font="Calibri 13")
    combobox3['value'] = ("Categories", "Backpacks", "Belt Bags", "Business Bags", "Crossbodies", "Diaper Bags","Duffles","Pouches","Satchels")
    combobox3.current(0)
    combobox3.grid(row=3, pady=5)
    combobox4 = ttk.Combobox(hand_frame2,width=20,height=70,font="Calibri 13")
    combobox4['value'] = ("Hndbag Size","Mini","Small","Medium","Large")
    combobox4.current(0)
    combobox4.grid(row=4, pady=5)
    combobox5 = ttk.Combobox(hand_frame2,width=20,height=60,font="Calibri 13")
    combobox5['value'] = ("Hardware Color","Brass","Pewter","Black","Gold","Nickel","Silver","Gunmetal")
    combobox5.current(0)
    combobox5.grid(row=5, pady=5)
    combobox6= ttk.Combobox(hand_frame2, width=20,height=70,font="Calibri 13")
    combobox6['value'] = ("Collection","Alie","Beat","Cargo","Carrie","Cassie","Charlie","Dinky","Duffle","Field Tote","Hadley","Hutton","Kira","Kitt","Madison")
    combobox6.current(0)
    combobox6.grid(row=6, pady=5)


    hand_frame3=Frame(hand_frame,bg="white")
    hand_frame3.pack(side=RIGHT,anchor=NW)
    hlabel1=Label(hand_frame3,text="\n\n195 Products",font="Calibri 13 italic",bg="white")
    hlabel1.grid(row=0,column=0,padx=(30,3),sticky=W)
    hlabel2 = Label(hand_frame3, text="\nWomen's Bags",font="Calibri 20",bg="white")
    hlabel2.grid(row=0, column=1,sticky=E)
    hlabel3=Label(hand_frame3,text="\nSORT BY:          Best Matches",font="Calibri 14",bg="white")
    hlabel3.grid(row=0,column=3,sticky=SE,padx=(3,30))

    global himage1,himage2,himage3,himage4,himage5,himage6,himage7,himage8,himage9,himage10,himage11,himage12,himage13,himage14,himage15,himage16,himage17,himage18
    himage1=ImageTk.PhotoImage(Image.open(himg1).resize((290,350),Image.ANTIALIAS))
    himage2=ImageTk.PhotoImage(Image.open(himg2).resize((290,350),Image.ANTIALIAS))
    himage3=ImageTk.PhotoImage(Image.open(himg3).resize((290,350),Image.ANTIALIAS))
    himage4=ImageTk.PhotoImage(Image.open(himg4).resize((290,350),Image.ANTIALIAS))
    himage5=ImageTk.PhotoImage(Image.open(himg5).resize((290,350),Image.ANTIALIAS))
    himage6=ImageTk.PhotoImage(Image.open(himg6).resize((290,350),Image.ANTIALIAS))
    himage7=ImageTk.PhotoImage(Image.open(himg7).resize((580,350),Image.ANTIALIAS))
    himage8=ImageTk.PhotoImage(Image.open(himg8).resize((290,350),Image.ANTIALIAS))
    himage9=ImageTk.PhotoImage(Image.open(himg9).resize((290,350),Image.ANTIALIAS))
    himage10=ImageTk.PhotoImage(Image.open(himg10).resize((290,350),Image.ANTIALIAS))
    himage11=ImageTk.PhotoImage(Image.open(himg11).resize((290,350),Image.ANTIALIAS))
    himage12=ImageTk.PhotoImage(Image.open(himg12).resize((290,350),Image.ANTIALIAS))
    himage13=ImageTk.PhotoImage(Image.open(himg13).resize((290,350),Image.ANTIALIAS))
    himage14=ImageTk.PhotoImage(Image.open(himg14).resize((290,350),Image.ANTIALIAS))
    himage15=ImageTk.PhotoImage(Image.open(himg15).resize((290,350),Image.ANTIALIAS))
    himage16=ImageTk.PhotoImage(Image.open(himg16).resize((580,350),Image.ANTIALIAS))
    himage17=ImageTk.PhotoImage(Image.open(himg17).resize((290,350),Image.ANTIALIAS))
    himage18=ImageTk.PhotoImage(Image.open(himg18).resize((290,350),Image.ANTIALIAS))

    h_imglabel1=Label(hand_frame3,image=himage1)
    h_imglabel1.grid(row=1,column=0,padx=(30,3),pady=(50,1),sticky=W)
    h_imglabel2 = Label(hand_frame3, image=himage2)
    h_imglabel2.grid(row=1, column=1,padx=(3,3),pady=(50,1),sticky=W)
    h_imglabel3 = Label(hand_frame3, image=himage3)
    h_imglabel3.grid(row=1, column=2,padx=(3,3),pady=(50,1),sticky=W)
    h_imglabel4 = Label(hand_frame3, image=himage4)
    h_imglabel4.grid(row=1, column=3,padx=(3,30),pady=(50,1),sticky=W)
    h_label1=Label(hand_frame3,text="Alie Shoulder Bag In\nSignature Jacquard\nWith...\n\n$695",font="Calibri 12",justify=LEFT,bg="white")
    h_label1.grid(row=2,column=0)
    h_label2 = Label(hand_frame3, text="Alie Shoulder Bag\n\n$595", font="Calibri 12",justify=LEFT,bg="white")
    h_label2.grid(row=2, column=1,sticky=N)
    h_label3 = Label(hand_frame3, text="Alie Shoulder Bag In\nColorblock\n\n$595", font="Calibri 12",justify=LEFT,bg="white")
    h_label3.grid(row=2, column=2,sticky=N)
    h_label4 = Label(hand_frame3, text="Alie Shoulder Bag 18 In\nSignature Jacquard\nWith...\n\n$495", font="Calibri 12",justify=LEFT,bg="white")
    h_label4.grid(row=2, column=3)

    h_imglabel5 = Label(hand_frame3, image=himage5)
    h_imglabel5.grid(row=3, column=0,padx=(30,3),pady=(50,1),sticky=W)
    h_imglabel6 = Label(hand_frame3, image=himage6)
    h_imglabel6.grid(row=3, column=1,padx=(3,3),pady=(50,1),sticky=W)
    h_imglabel7 = Label(hand_frame3, image=himage7)
    h_imglabel7.grid(row=3, column=2,columnspan=2,padx=(3,30),pady=(50,1),sticky=W)
    h_label4=Label(hand_frame3,text="Alie Shoulder Bag 18\n\n$495",font="Calibri 12",justify=LEFT,bg="white")
    h_label4.grid(row=4,column=0)
    h_label5 = Label(hand_frame3, text="Alie Shoulder Bag 18 In\nColorblock\n\n$495", font="Calibri 12", justify=LEFT, bg="white")
    h_label5.grid(row=4, column=1)

    h_imglabel8 = Label(hand_frame3, image=himage8)
    h_imglabel8.grid(row=5, column=0, padx=(30, 3), pady=(50, 1), sticky=W)
    h_imglabel9 = Label(hand_frame3, image=himage9)
    h_imglabel9.grid(row=5, column=1, padx=(3, 3), pady=(50, 1), sticky=W)
    h_imglabel10 = Label(hand_frame3, image=himage10)
    h_imglabel10.grid(row=5, column=2, padx=(3, 3), pady=(50, 1), sticky=W)
    h_imglabel11 = Label(hand_frame3, image=himage11)
    h_imglabel11.grid(row=5, column=3, padx=(3, 30), pady=(50, 1), sticky=W)
    h_label6 = Label(hand_frame3, text="Madison Shoulder Bag In\nSignature Canvas With...\n\n$495", font="Calibri 12",justify=LEFT, bg="white")
    h_label6.grid(row=6, column=0)
    h_label7= Label(hand_frame3, text="Madison Shoulder Bag In\nSignature Canvas\n\n$395", font="Calibri 12", justify=LEFT, bg="white")
    h_label7.grid(row=6, column=1)
    h_label8 = Label(hand_frame3, text="Madison Shoulder Bag\n\n$395", font="Calibri 12", justify=LEFT, bg="white")
    h_label8.grid(row=6, column=2)
    h_label9 = Label(hand_frame3, text="Madison Shoulder Bag\nWith Quilting\n\n$495", font="Calibri 12", justify=LEFT, bg="white")
    h_label9.grid(row=6, column=3)

    h_imglabel12 = Label(hand_frame3, image=himage12)
    h_imglabel12.grid(row=7, column=0, padx=(30, 3), pady=(50, 1), sticky=W)
    h_imglabel13 = Label(hand_frame3, image=himage13)
    h_imglabel13.grid(row=7, column=1, padx=(3, 3), pady=(50, 1), sticky=W)
    h_imglabel14 = Label(hand_frame3, image=himage14)
    h_imglabel14.grid(row=7, column=2, padx=(3, 3), pady=(50, 1), sticky=W)
    h_imglabel15 = Label(hand_frame3, image=himage15)
    h_imglabel15.grid(row=7, column=3, padx=(3, 30), pady=(50, 1), sticky=W)
    h_label10 = Label(hand_frame3, text="Madison Shoulder Bag\n16 InSignature Canvas...\n\n$295", font="Calibri 12",justify=LEFT, bg="white")
    h_label10.grid(row=8, column=0)
    h_label11 = Label(hand_frame3, text="Madison Shoulder Bag \n16\n\n$250", font="Calibri 12",justify=LEFT, bg="white")
    h_label11.grid(row=8, column=1)
    h_label12 = Label(hand_frame3, text="Madison Shoulder Bag\n16 With Quilting\n\n$350", font="Calibri 12", justify=LEFT,bg="white")
    h_label12.grid(row=8, column=2)
    h_label13 = Label(hand_frame3, text="Tabby Shoulder Bag 26\nWith Signature Canvas\n\n$237-$395", font="Calibri 12",justify=LEFT, bg="white")
    h_label13.grid(row=8, column=3)

    h_imglabel16 = Label(hand_frame3, image=himage16)
    h_imglabel16.grid(row=9, column=0, columnspan=2,padx=(30, 3), pady=(50, 1), sticky=W)
    h_imglabel17 = Label(hand_frame3, image=himage17)
    h_imglabel17.grid(row=9, column=2, padx=(3, 3), pady=(50, 1), sticky=W)
    h_imglabel18 = Label(hand_frame3, image=himage18)
    h_imglabel18.grid(row=9, column=3, padx=(3, 3), pady=(50, 1), sticky=W)
    h_label14 = Label(hand_frame3, text="Tabby Shoulder Bag 26\nIn Signature Canvas\nWith...\n$395", font="Calibri 12", justify=LEFT, bg="white")
    h_label14.grid(row=10, column=2)
    h_label15 = Label(hand_frame3, text="Tabby Shoulder Bag 26\nWith Beadchain\n$395", font="Calibri 12", justify=LEFT,bg="white")
    h_label15.grid(row=10, column=3,sticky=N)

    feet_text=Text(hand_frame3,bd=0)
    feet_text.grid(row=11,columnspan=4,pady=(200,100),sticky=EW)
    feet_text.insert(END,"Designer handbags, purses, crossbody bags, tote bags, backpacks, shoulder bags, satchels, clutches and belt\nbags. In leather, suede, Signature, patchwork and prints. (Decisions, decisions.) Whether you’re making a\npersonal style statement, toting a laptop or just keeping your wallet, and essentials close, Coach bags bring\ntogether utility, good looks and quality craftsmanship. (We’ve been perfecting all that since 1941.)")
    feet_text.tag_add("first",'1.0','end')
    feet_text.tag_config('first',justify=CENTER,font="Centaur 16")
    feet_text.tag_add("second", '1.27', '1.41')
    feet_text.tag_config('second', font="Centaur 16 underline")
    feet_text.tag_add("third", '1.80', '1.88')
    feet_text.tag_config('third', font="Centaur 16 underline")
    feet_text.tag_add("fourth", '3.63', '3.69')
    feet_text.tag_config('fourth', font="Centaur 16 underline")


def giftservice():
    format()

    giftservice_win.pack(fill=BOTH, expand=1)
    giftcanvas=Canvas(giftservice_win,bg="white")
    giftcanvas.pack(side=LEFT, fill=BOTH,expand=1)
    giftsrollbar=Scrollbar(giftservice_win,command=giftcanvas.yview)
    giftsrollbar.pack(fill=Y,side=RIGHT)
    giftcanvas.config(yscrollcommand=giftsrollbar.set)
    giftcanvas.bind("<Configure>",lambda e:giftcanvas.configure(scrollregion=giftcanvas.bbox("all")))
    gift_frame=Frame(giftcanvas,bg="white")
    giftcanvas.create_window((0,0),window=gift_frame,anchor="nw")
    myscrollbar.pack_forget()

    global icon1, icon2, icon3, icon4, icon5, icon6
    g_label1=Label(gift_frame,text="Gift Coach",font="SimSun 26 bold",bg="white")
    g_label1.grid(row=0,columnspan=3,pady=20)

    # professor's path:
    '''
    ic1 = "C:/SDTPGMS/FL2020/icon1.png"
    ic2 = "C:/SDTPGMS/FL2020/icon2.png"
    ic3 = "C:/SDTPGMS/FL2020/icon3.png"
    ic4 = "C:/SDTPGMS/FL2020/icon4.png"
    ic5 = "C:/SDTPGMS/FL2020/icon5.png"
    ic6 = "C:/SDTPGMS/FL2020/icon6.png"
    '''

    # my path:
    ic1 = "coach/icon1.png"
    ic2 = "coach/icon2.png"
    ic3 = "coach/icon3.png"
    ic4 = "coach/icon4.png"
    ic5 = "coach/icon5.png"
    ic6 = "coach/icon6.png"

    g_text1=Text(gift_frame, relief="solid",bd=0.5,width=50,height=30)
    icon1=ImageTk.PhotoImage(Image.open(ic1))
    g_text1.insert(END,"\n\n\n")
    g_text1.image_create(END,image=icon1)
    g_text1.insert(END,"\n\nGift & E-Gift\nCards\n","t1")
    g_text1.insert(END,"\nThe gift of Coach + the gift of choice.\n","c1")
    g_text1.insert(END,"\nSHOP GIFT CARDS\nSHOP E-GIFT CARDS\nCHECK YOUR BALANCE\n","f1")
    g_text1.grid(row=1,column=0,padx=(140,0),pady=(20,0))

    g_text1.tag_config("t1",font="Calibri 22",justify=CENTER)
    g_text1.tag_config("c1",font="Calibri 14",justify=CENTER)
    g_text1.tag_config("f1",font="Calibri 11 underline",justify=CENTER)
    g_text1.tag_add("1",1.0,END)
    g_text1.tag_config("1",justify=CENTER)

    g_text2 = Text(gift_frame, relief="solid",bd=0.5,width=50,height=30)
    icon2 = ImageTk.PhotoImage(Image.open(ic2))
    g_text2.insert(END, "\n\n\n")
    g_text2.image_create(END, image=icon2)
    g_text2.insert(END, "\n\nGiftNow\nAvailable\n","t2")
    g_text2.insert(END, "\nWe’re all for flexibility. Surprise them\nwith an email that contains a gift they\n“open” online. Then let them choose a\ndifferent color or size, or exchange it\nbefore it ships.\n","c2")
    g_text2.insert(END, "\nLEARN MORE\n","f2")
    g_text2.grid(row=1, column=1,padx=(0,0),pady=(20,0))
    g_text2.tag_config("t2", font="Calibri 22", justify=CENTER)
    g_text2.tag_config("c2", font="Calibri 14", justify=CENTER)
    g_text2.tag_config("f2", font="Calibri 11 underline", justify=CENTER)
    g_text2.tag_add("1", 1.0, END)
    g_text2.tag_config("1", justify=CENTER)

    g_text3 = Text(gift_frame, relief="solid",bd=0.5,width=50,height=30)
    icon3= ImageTk.PhotoImage(Image.open(ic3))
    g_text3.insert(END, "\n\n\n")
    g_text3.image_create(END, image=icon3)
    g_text3.insert(END, "\n\nGift Boxes\n& Messaging\n","t3")
    g_text3.insert(END,"\nOur complimentary gift boxes include a\nbow and card—all wrapped up and ready\nto give. Request yours at checkout with\nany purchase.\n","c3")
    g_text3.insert(END, "\nSHOP GIFTS\n","f3")
    g_text3.grid(row=1, column=2,padx=(0,70),pady=(20,0))
    g_text3.tag_config("t3", font="Calibri 22", justify=CENTER)
    g_text3.tag_config("c3", font="Calibri 14", justify=CENTER)
    g_text3.tag_config("f3", font="Calibri 11 underline", justify=CENTER)
    g_text3.tag_add("1", 1.0, END)
    g_text3.tag_config("1", justify=CENTER)

    g_text4 = Text(gift_frame, relief="solid",bd=0.5,width=50,height=30)
    icon4= ImageTk.PhotoImage(Image.open(ic4))
    g_text4.insert(END, "\n\n\n")
    g_text4.image_create(END, image=icon4)
    g_text4.insert(END,"\n\nComplimentary\nMonogramming\n","t4")
    g_text4.insert(END,"\nChoose from over 100 motifs, letters and\nnumbers. It’s the perfect way to make\nyour gift extra-special—and it’s free.\n","c4")
    g_text4.insert(END, "\nSHOP NOW\n","f4")
    g_text4.grid(row=2, column=0,padx=(140,0),pady=(0,20))
    g_text4.tag_config("t4", font="Calibri 22", justify=CENTER)
    g_text4.tag_config("c4", font="Calibri 14", justify=CENTER)
    g_text4.tag_config("f4", font="Calibri 11 underline", justify=CENTER)
    g_text4.tag_add("1", 1.0, END)
    g_text4.tag_config("1", justify=CENTER)

    g_text5 = Text(gift_frame, relief="solid",bd=0.5,width=50,height=30)
    icon5= ImageTk.PhotoImage(Image.open(ic5))
    g_text5.insert(END, "\n\n\n")
    g_text5.image_create(END, image=icon5)
    g_text5.insert(END, "\n\nIn-Store\nPickup\n","t5")
    g_text5.insert(END,"\nFree and fast. Buy online, and three\nhours later, pick up your items at the\nstore of your choice (and don’t forget to\nadd a monogram and gift wrap—they’re\non us).\n","c5")
    g_text5.insert(END, "\nSHOP GIFTS","f5")
    g_text5.grid(row=2, column=1,padx=(0,0),pady=(0,20))
    g_text5.tag_config("t5", font="Calibri 22", justify=CENTER)
    g_text5.tag_config("c5", font="Calibri 14", justify=CENTER)
    g_text5.tag_config("f5", font="Calibri 11 underline", justify=CENTER)
    g_text5.tag_add("1", 1.0, END)
    g_text5.tag_config("1", justify=CENTER)

    g_text6 = Text(gift_frame, relief="solid",bd=0.5,width=50,height=30)
    icon6= ImageTk.PhotoImage(Image.open(ic6))
    g_text6.insert(END, "\n\n\n")
    g_text6.image_create(END, image=icon6)
    g_text6.insert(END, "\n\nWish List\n","t6")
    g_text6.insert(END,"\nHint hint. Start a wish list—\nor find someone else’s.\n","c6")
    g_text6.insert(END, "\nSTART A WISH LIST\n","f6")
    g_text6.grid(row=2, column=2,padx=(0,70),pady=(0,20))
    g_text6.tag_config("t6", font="Calibri 22", justify=CENTER)
    g_text6.tag_config("c6", font="Calibri 14", justify=CENTER)
    g_text6.tag_config("f6", font="Calibri 11 underline", justify=CENTER)
    g_text6.tag_add("1", 1.0, END)
    g_text6.tag_config("1", justify=CENTER)

    g_label2=Label(gift_frame,text="\n\nHave Any Questions?", font="Calibri 22",justify=CENTER,bg="white")
    g_label2.grid(row=3,columnspan=3)
    g_label3=Text(gift_frame,bd=0,height=10)
    g_label3.grid(row=4,columnspan=3)
    g_label3.insert(END,"Contact or call us at 888-262-6224 anytime.\nFor answers to product-related questions, chat us online.\n\n")
    g_label3.tag_add('1','1.0','end')
    g_label3.tag_config('1',justify=CENTER,font="Calibri 14")
    g_label3.tag_add('2','1.0','1.7')
    g_label3.tag_config('2',font="Calibri 14 underline")
    g_label3.tag_add('3','1.22','1.34')
    g_label3.tag_config('3',font="Calibri 14 underline")
    g_label3.tag_add('4', '2.42', '2.49')
    g_label3.tag_config('4', font="Calibri 14 underline")

    bottom_frame=Frame(gift_frame,bg="#f8f8f8")
    bottom_frame.grid(row=5,columnspan=4,sticky=EW)

    b_text1=Text(bottom_frame,width=45,bd=0,bg="#f8f8f8")
    b_text1.grid(row=0,column=0,sticky=E)
    b_text1.insert(END,"\nCOACH\n\n","1")
    b_text1.insert(END,"COACH RULE #2020:\n\n","2")
    b_text1.insert(END,"Holiday is where you find it.","3")
    b_text1.tag_config('1',font="Calibri 25 bold")
    b_text1.tag_config('2',font="Calibri 13 ")
    b_text1.tag_config('3',font="Calibri 16 ")
    b_text1.tag_add('4','1.0','end')
    b_text1.tag_config('4',justify=CENTER)

    b_text2 = Text(bottom_frame,width=38,bd=0,bg="#f8f8f8")
    b_text2.grid(row=0, column=1,sticky=W)
    b_text2.insert(END,"\n\nCUSTOMER CARE\n\n",'5')
    b_text2.insert(END,"Contact US\nFAQ\nOrder Status\nReturns & Exchanges\nShipping Information\nProduct Care & Reparis\nGift Cards\nGift Services\nStore Locator\nFeedback",'6')
    b_text2.tag_config('5', font="Calibri 14")
    b_text2.tag_config('6', font="Calibri 12 ")

    b_text3 = Text(bottom_frame,width=28,bd=0,bg="#f8f8f8")
    b_text3.grid(row=0, column=2,sticky=W)
    b_text3.insert(END,"\n\nABOUT US\n\n",'7')
    b_text3.insert(END,"Coach Story\nResponsibility\nCoach Foundation\nCareers\nTapstry\ninvestor Relations",'8')
    b_text3.tag_config('7', font="Calibri 14")
    b_text3.tag_config('8', font="Calibri 12 ")

    b_text4 = Text(bottom_frame,width=64,bd=0,bg="#f8f8f8")
    b_text4.grid(row=0, column=3,sticky=W)
    b_text4.insert(END,"\n\nEmail Address                                                         SIGN UP\n\n",'9')
    b_text4.insert(END,"Sign up to receive Coach emails and be first to hear about new\narrivals, events and more. You can withdraw your consent at any\ntime. Read our privacy policy or contact us for more details.",'10')
    b_text4.tag_config('9', font="Calibri 14")
    b_text4.tag_config('10', font="Calibri 12 ")

# add menu
menubar=Menu(master)
# menubar.entryconfig("NEW",state="diabled")
newmenu=Menu(menubar,tearoff=0)
newmenu.add_command(label="Women's New Arrivals",font="Calibri 12",command=open)
newmenu.add_command(label="Men's New Arrivals",font="Calibri 12",command=open)
newmenu.add_command(label="Featured",font="Calibri 12",command=open)
menubar.add_cascade(label="NEW",menu=newmenu)

womenmenu = Menu(menubar, tearoff=0)
womenmenu.add_command(label="Handbags", font="Calibri 12",command=handbags)
womenmenu.add_command(label="Wallets & Wristlets",font="Calibri 12", command=open)
womenmenu.add_command(label="Ready-to-Wear",font="Calibri 12", command=open)
womenmenu.add_command(label="Shoes", font="Calibri 12",command=open)
womenmenu.add_command(label="Accessories", font="Calibri 12",command=open)
womenmenu.add_command(label="Edits",font="Calibri 12",command=open)
menubar.add_cascade(label="WOMEN", menu=womenmenu)

menmenu = Menu(menubar, tearoff=0)
menmenu.add_command(label="Bags",font="Calibri 12", command=open)
menmenu.add_command(label="Wallets",font="Calibri 12", command=open)
menmenu.add_command(label="Ready-to-Wear",font="Calibri 12", command=open)
menmenu.add_command(label="Shoes",font="Calibri 12", command=open)
menmenu.add_command(label="Accessories", font="Calibri 12",command=open)
menmenu.add_command(label="Edits", font="Calibri 12",command=open)
menubar.add_cascade(label="MEN", menu=menmenu)

giftsmenu = Menu(menubar, tearoff=0)
giftsmenu.add_command(label="For Her", font="Calibri 12",command=open)
giftsmenu.add_command(label="For Him", font="Calibri 12",command=open)
giftsmenu.add_command(label="Customization", font="Calibri 12",command=open)
giftsmenu.add_command(label="Gift Services", font="Calibri 12",command=giftservice)
menubar.add_cascade(label="GIFTS", menu=giftsmenu)

salemenu = Menu(menubar, tearoff=0)
salemenu.add_command(label="Women's Sale",font="Calibri 12", command=open)
salemenu.add_command(label="Men's Sale", font="Calibri 12",command=open)
salemenu.add_command(label="TGIBF Treats", font="Calibri 12",command=open)
salemenu.add_command(label="Event Picks",font="Calibri 12", command=open)
menubar.add_cascade(label="SALE", menu=salemenu)
master.config(menu=menubar)

# add scrollbar for the full screen
myframe=Frame(master)
myframe.pack(fill=BOTH, expand=1)
mycanvas=Canvas(myframe)
mycanvas.pack(side=LEFT,fill=BOTH, expand=1)
myscrollbar=Scrollbar(myframe,command=mycanvas.yview)
myscrollbar.pack(side=RIGHT,fill=Y)
mycanvas.config(yscrollcommand=myscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox("all")))
anoframe=Frame(mycanvas,bg="#fbf6ed")
mycanvas.create_window((0,0),window=anoframe, anchor="nw")

# professor's path:
'''
img1="C:/SDTPGMS/FL2020/image1.jpg"
img2="C:/SDTPGMS/FL2020/image2.png"
img3="C:/SDTPGMS/FL2020/image3.png"
img4="C:/SDTPGMS/FL2020/image4.png"
img5="C:/SDTPGMS/FL2020/image5.png"
img6="C:/SDTPGMS/FL2020/image6.png"
img7="C:/SDTPGMS/FL2020/image7.png"
img9="C:/SDTPGMS/FL2020/image9.png"
img10="C:/SDTPGMS/FL2020/image10.png"
img11="C:/SDTPGMS/FL2020/image11.png"
img12="C:/SDTPGMS/FL2020/image12.png"
img13="C:/SDTPGMS/FL2020/image13.png"
img14="C:/SDTPGMS/FL2020/image14.png"
img15="C:/SDTPGMS/FL2020/image15.png"
img16="C:/SDTPGMS/FL2020/image16.png"
img17="C:/SDTPGMS/FL2020/image17.png"
img18="C:/SDTPGMS/FL2020/image18.png"
img19="C:/SDTPGMS/FL2020/image19.png"
img20="C:/SDTPGMS/FL2020/image20.png"
img21="C:/SDTPGMS/FL2020/image21.png"
img22="C:/SDTPGMS/FL2020/image22.png"
img23="C:/SDTPGMS/FL2020/image23.png"
img24="C:/SDTPGMS/FL2020/image24.png"
img25="C:/SDTPGMS/FL2020/image25.png"
img26="C:/SDTPGMS/FL2020/image26.png"
img27="C:/SDTPGMS/FL2020/image27.png"
'''

# my path:
img1="coach/image1.jpg"
img2="coach/image2.png"
img3="coach/image3.png"
img4="coach/image4.png"
img5="coach/image5.png"
img6="coach/image6.png"
img7="coach/image7.png"
img9="coach/image9.png"
img10="coach/image10.png"
img11="coach/image11.png"
img12="coach/image12.png"
img13="coach/image13.png"
img14="coach/image14.png"
img15="coach/image15.png"
img16="coach/image16.png"
img17="coach/image17.png"
img18="coach/image18.png"
img19="coach/image19.png"
img20="coach/image20.png"
img21="coach/image21.png"
img22="coach/image22.png"
img23="coach/image23.png"
img24="coach/image24.png"
img25="coach/image25.png"
img26="coach/image26.png"
img27="coach/image27.png"

image1=ImageTk.PhotoImage(Image.open(img1).resize((anoframe.winfo_screenwidth(),150),Image.ANTIALIAS))
imagelabel1=Label(anoframe, image=image1,bg="#fbf6ed")
imagelabel1.grid(row=0,sticky="ew")
label2=Label(anoframe, text="\n\nAll-in on Alie", font="Arial 22 bold",bg="#fbf6ed")
label2.grid(row=1)
label3=Label(anoframe, text="A practical bag that brings all the cheer", font="Arial 16",bg="#fbf6ed")
label3.grid(row=2)
label4=Label(anoframe, text="SHOP WOMEN’S NEW ARRIVALS\n\n", font="Calibri 11 underline",bg="#fbf6ed")
label4.grid(row=3)
label4.bind("<Button-1>",lambda e: webbrowser.open("https://www.coach.com/shop/women-new-arrivals-new-arrivals?hp=text_m1_shop_new_arrivals_women"))

image2=ImageTk.PhotoImage(Image.open(img2))
imagelabel2=Label(anoframe,image=image2,bg="#fbf6ed")
imagelabel2.grid(row=4, sticky="w",padx=(70,10))
image3=ImageTk.PhotoImage(Image.open(img3))
imagelabel3=Label(anoframe,image=image3,bg="#fbf6ed")
imagelabel3.grid(row=4,sticky="e",padx=(10,70))
piclabel1=Label(anoframe,text="Yang Zi", font="Calibri 15",bg="#fbf6ed")
piclabel1.grid(row=5,sticky="w",padx=(70,10))
piclabel2=Label(anoframe,text="Jennifer Lopez", font="Calibri 15",bg="#fbf6ed")
piclabel2.grid(row=5,padx=(170,50))

label5=Label(anoframe,text="\n\nThree sizes. So many colors. Find an Alie that’s just right.\n", font="Calibri 22 bold",bg="#fbf6ed")
label5.grid(row=6)
newframe=Frame(anoframe,bg="#fbf6ed")
newframe.grid(row=7)
image4=ImageTk.PhotoImage(Image.open(img4))
imagelabel4=Label(newframe,image=image4,height=300,width=300,bg="#fbf6ed")
imagelabel4.grid(row=0,column=0,padx=(20,5))
image5=ImageTk.PhotoImage(Image.open(img5))
imagelabel5=Label(newframe,image=image5,height=300,width=300,bg="#fbf6ed")
imagelabel5.grid(row=0,column=1,padx=(5,2))
image6=ImageTk.PhotoImage(Image.open(img6))
imagelabel6=Label(newframe,image=image6,height=300,width=300,bg="#fbf6ed")
imagelabel6.grid(row=0,column=2,padx=(5,2))
image7=ImageTk.PhotoImage(Image.open(img7))
imagelabel7=Label(newframe,image=image7,height=300,width=300,bg="#fbf6ed")
imagelabel7.grid(row=0,column=3,padx=(5,50))

label6=Label(newframe,text="SHOP THE SHOULDER BAG 18\n\n\n", font="Calibri 14 underline",bg="#fbf6ed")
label6.grid(row=1,column=0)
label6.bind("<Button-1>", lambda e:webbrowser.open("https://www.coach.com/coach-alie-shoulder-bag-18-in-signature-jacquard-with-snakeskin-detail/4616.html?dwvar_color=B4RH3&hp=img_m2_product_4616"))
label7=Label(newframe,text="SHOP THE CAMERA BAG\n\n\n", font="Calibri 14 underline",bg="#fbf6ed")
label7.grid(row=1,column=1)
label7.bind("<Button-1>", lambda e:webbrowser.open("https://www.coach.com/coach-alie-camera-bag-with-quilting/4875.html?dwvar_color=B4%2FHA&hp=img_m2_product_4875"))
label8=Label(newframe,text="SHOP THE SHOULDER BAG\n\n\n", font="Calibri 14 underline",bg="#fbf6ed")
label8.grid(row=1,column=2)
label8.bind("<Button-1>", lambda e:webbrowser.open("https://www.coach.com/coach-alie-shoulder-bag/3928.html?dwvar_color=B4%2FBK&hp=img_m2_product_3928"))
label9=Label(newframe,text="SHOP THE SHOULDER BAG\n\n\n", font="Calibri 14 underline",bg="#fbf6ed")
label9.grid(row=1,column=3)
label9.bind("<Button-1>", lambda e:webbrowser.open("https://www.coach.com/coach-alie-shoulder-bag-18/4617.html?dwvar_color=V5RYG&hp=img_m2_product_4617"))

text1=Text(anoframe,bd=0, height=30, width=110,bg="#fbf6ed")
text1.grid(row=8,sticky="w")
text1.insert(END, '''
\n\n\nAdd some pins, add a
monogram—so there’s no
mistaking it’s yours (or theirs).''',"bold")
text1.tag_config("bold",font="Calibri 20", justify=CENTER)
text1.tag_config("underline1",font="Calibri 13 underline", justify=CENTER)
text1.tag_config("underline2",font="Calibri 13 underline", justify=CENTER)
text1.insert(END,"\n\nCUSTOMIZE IT","underline1")
text1.insert(END, "\n\nSHOP WOMEN'S BAGS","underline2")

image9=ImageTk.PhotoImage(Image.open(img9))
imagelabel8=Label(anoframe,image=image9,bg="#fbf6ed")
imagelabel8.grid(row=8,sticky="e",padx=(3,130))
label10=Label(anoframe,text="\n\nLittle ways to make their holiday.\n\n", font="Arial 20 bold",bg="#fbf6ed")
label10.grid(row=9)
label11=Label(anoframe,text="\nSHOP GIFTS FOR HER\tSHOP GIFTS FOR HIM\n\n", font="Calibri 12 underline",bg="#fbf6ed")
label11.grid(row=10)
image10=ImageTk.PhotoImage(Image.open(img10))
imagelabel10=Label(anoframe,image=image10,bg="#fbf6ed")
imagelabel10.grid(row=11,sticky="w",padx=(70,2))
image11=ImageTk.PhotoImage(Image.open(img11))
imagelabel11=Label(anoframe,image=image11,bg="#fbf6ed")
imagelabel11.grid(row=11,sticky="e",padx=(2,70))
image12=ImageTk.PhotoImage(Image.open(img12).resize((260,300),Image.ANTIALIAS))
imagelabel12=Label(anoframe,image=image12,bd=0)
imagelabel12.grid(row=11,sticky="sw")

lowframe=Frame(anoframe,bg="white")
lowframe.grid(row=12,sticky="ew")

label12=Label(lowframe,text="More Coach Stories",font="Arial 30 bold",bg="white")
label12.grid(row=0,pady=70,columnspan=2)
image13=ImageTk.PhotoImage(Image.open(img13).resize((700,450),Image.ANTIALIAS))
imagelabel13=Label(lowframe,image=image13)
imagelabel13.grid(row=1,column=0,padx=(50,3))
text2=Text(lowframe,bd=0)
text2.insert(END,"\n\nCustomize their gifts (on us).\n","title1")
text2.insert(END,"\nUse code PRINTME to digital-print\nselect styles for free through December 11.","content1")
text2.insert(END,"\n\nSTART CUSTOMIZING\n","feet1")
text2.grid(row=1,column=1,padx=(3,50))
text2.tag_config("title1",font="Arial 24", justify=CENTER)
text2.tag_config("content1",font="Calibri 17", justify=CENTER)
text2.tag_config("feet1",font="Calibri 14 underline", justify=CENTER)

text3=Text(lowframe,bd=0)
text3.insert(END,"\n\nPresenting the totally new\nMadison—so you can gift that\nlittle thrill of discovery.\n","title2")
text3.insert(END,"\n\nSHOP THE MADISON\n","feet2")
text3.grid(row=2,column=0,pady=40)
text3.tag_config("title2",font="Calibri 24", justify=CENTER)
text3.tag_config("feet2",font="Calibri 14 underline", justify=CENTER)
image14=ImageTk.PhotoImage(Image.open(img14).resize((700,450),Image.ANTIALIAS))
imagelabel14=Label(lowframe,image=image14)
imagelabel14.grid(row=2,column=1,pady=40)

b_frame=Frame(anoframe,bg="white")
b_frame.grid(row=13,sticky="ew")
label13=Label(b_frame,text="Still need a little gifting inspiration?", font="Arial 35",justify=CENTER,bg="white")
label13.grid(row=0,columnspan=4,pady=(80,6))
label14=Label(b_frame,text="See what the Coach Family is giving (and getting) this holiday.", font="Calibri 15",justify=CENTER,bg="white")
label14.grid(row=1,columnspan=4,pady=(6,6))
label15=Label(b_frame,text="SHOP THEIR PICKS", font="Calibri 12 underline",justify=CENTER,bg="white")
label15.grid(row=2,columnspan=4,pady=(6,50))
image15=ImageTk.PhotoImage(Image.open(img15).resize((300,300),Image.ANTIALIAS))
imagelabel15=Label(b_frame,image=image15)
imagelabel15.grid(row=3,column=0,padx=(100,3))
image16=ImageTk.PhotoImage(Image.open(img16).resize((300,300),Image.ANTIALIAS))
imagelabel16=Label(b_frame,image=image16)
imagelabel16.grid(row=3,column=1,padx=(3,3))
image17=ImageTk.PhotoImage(Image.open(img17).resize((300,300),Image.ANTIALIAS))
imagelabel17=Label(b_frame,image=image17)
imagelabel17.grid(row=3,column=2,padx=(3,3))
image18=ImageTk.PhotoImage(Image.open(img18).resize((300,300),Image.ANTIALIAS))
imagelabel18=Label(b_frame,image=image18)
imagelabel18.grid(row=3,column=3,padx=(3,100))
label16=Label(b_frame,text="RIVINGTON BACKPACK",bg="white",font='Calibri 12')
label16.grid(row=4,column=0,padx=(100,3))
label16=Label(b_frame,text="ACADEMY CROSSBODY",bg="white",font='Calibri 12')
label16.grid(row=4,column=1,padx=(3,3))
label16=Label(b_frame,text="TABBY SHOULDER BAG 26",bg="white",font='Calibri 12')
label16.grid(row=4,column=2,padx=(3,3))
label16=Label(b_frame,text="HITCH BACKPACK",bg="white",font='Calibri 12')
label16.grid(row=4,column=3,padx=(3,100))
image19=ImageTk.PhotoImage(Image.open(img19).resize((b_frame.winfo_screenwidth(),350),Image.ANTIALIAS))
imagelabel19=Label(b_frame,image=image19)
imagelabel19.grid(row=5,columnspan=4,pady=100)

last_frame=Frame(anoframe,bg="#f4ede7")
last_frame.grid(row=14,sticky="ew")
label17=Label(last_frame,text="Coach at Your Service",font="Arial 30 bold",justify=CENTER,bg="#f4ede7")
label17.grid(row=0,columnspan=4,pady=40)

image20=ImageTk.PhotoImage(Image.open(img20))
last_text1=Text(last_frame,bd=0,bg="#f4ede7",width=43)
last_text1.image_create(END,image=image20)
last_text1.insert(END,"\n\nBUY NOW,\nPAY LATER\n\n")
last_text1.insert(END,"Split your total into four easy,\ninterest-free payments with Klarna.\n\n")
last_text1.insert(END,"LEARN MORE")
last_text1.tag_add("1",1.0,END)
last_text1.tag_config("1",justify=CENTER)
last_text1.tag_add("2",3.0,'4.end')
last_text1.tag_config("2",font="Calibri 16")
last_text1.tag_add("3",6.0,'7.end')
last_text1.tag_config("3",font="Calibri 12")
last_text1.tag_add("4",9.0,'9.end')
last_text1.tag_config("4",font="Calibri 13 underline")
last_text1.grid(row=1,column=0)

image21=ImageTk.PhotoImage(Image.open(img21))
last_text2=Text(last_frame,bd=0,bg="#f4ede7",width=43)
last_text2.image_create(END,image=image21)
last_text2.insert(END,"\n\nBCOACH\nTO GOR\n\n")
last_text2.insert(END,"Select stores now offer pickup\nand virtual shopping appointments.\n\n")
last_text2.insert(END,"LEARN MORE\nFIND A STORE")
last_text2.tag_add("1",1.0,END)
last_text2.tag_config("1",justify=CENTER)
last_text2.tag_add("2",3.0,'4.end')
last_text2.tag_config("2",font="Calibri 16")
last_text2.tag_add("3",6.0,'7.end')
last_text2.tag_config("3",font="Calibri 12")
last_text2.tag_add("4",9.0,'10.end')
last_text2.tag_config("4",font="Calibri 13 underline")
last_text2.grid(row=1,column=1)

image22=ImageTk.PhotoImage(Image.open(img22))
last_text3=Text(last_frame,bd=0,bg="#f4ede7",width=43)
last_text3.image_create(END,image=image22)
last_text3.insert(END,"\n\nFREE SHIPPING & \nEXTENDED RETURNS\n\n")
last_text3.insert(END,"On all orders\n\n")
last_text3.insert(END,"ABOUT SHIPPING\nABOUT RETURNS")
last_text3.tag_add("1",1.0,END)
last_text3.tag_config("1",justify=CENTER)
last_text3.tag_add("2",3.0,'4.end')
last_text3.tag_config("2",font="Calibri 16")
last_text3.tag_add("3",6.0,'6.end')
last_text3.tag_config("3",font="Calibri 12")
last_text3.tag_add("4",8.0,'9.end')
last_text3.tag_config("4",font="Calibri 13 underline")
last_text3.grid(row=1,column=2)

image23=ImageTk.PhotoImage(Image.open(img23))
last_text3=Text(last_frame,bd=0,bg="#f4ede7",width=43)
last_text3.image_create(END,image=image23)
last_text3.insert(END,"\n\nCOMPLIMENTARY\nMONOGRAMMING\n\n")
last_text3.insert(END,"Choose frome over 100 motifs, letters\nand numbers. Why not? It's free.\n\n")
last_text3.insert(END,"SHOP NOW")
last_text3.tag_add("1",1.0,END)
last_text3.tag_config("1",justify=CENTER)
last_text3.tag_add("2",3.0,'4.end')
last_text3.tag_config("2",font="Calibri 16")
last_text3.tag_add("3",6.0,'7.end')
last_text3.tag_config("3",font="Calibri 12")
last_text3.tag_add("4",9.0,'9.end')
last_text3.tag_config("4",font="Calibri 13 underline")
last_text3.grid(row=1,column=3)

image24=ImageTk.PhotoImage(Image.open(img24))
last_text4=Text(last_frame,bd=0,bg="#f4ede7",width=43)
last_text4.image_create(END,image=image24)
last_text4.insert(END,"\n\nCOACH CREATE\nCUSTOMIZATION\n\n")
last_text4.insert(END,"Our craftsmen can embellish, rivet,\nor digitally print your design.\n\n")
last_text4.insert(END,"EXPLORE")
last_text4.tag_add("1",1.0,END)
last_text4.tag_config("1",justify=CENTER)
last_text4.tag_add("2",3.0,'4.end')
last_text4.tag_config("2",font="Calibri 16")
last_text4.tag_add("3",6.0,'7.end')
last_text4.tag_config("3",font="Calibri 12")
last_text4.tag_add("4",9.0,'9.end')
last_text4.tag_config("4",font="Calibri 13 underline")
last_text4.grid(row=2,column=0)

image25=ImageTk.PhotoImage(Image.open(img25))
last_text5=Text(last_frame,bd=0,bg="#f4ede7",width=43)
last_text5.image_create(END,image=image25)
last_text5.insert(END,"\n\nONE-YEAR WARRANTY\nAND REPAIRS\n\n")
last_text5.insert(END,"All repairs are handled with care\nby our Coach Repair Workshop.\n\n")
last_text5.insert(END,"REPAIR SERVICES")
last_text5.tag_add("1",1.0,END)
last_text5.tag_config("1",justify=CENTER)
last_text5.tag_add("2",3.0,'4.end')
last_text5.tag_config("2",font="Calibri 16")
last_text5.tag_add("3",6.0,'7.end')
last_text5.tag_config("3",font="Calibri 12")
last_text5.tag_add("4",9.0,'9.end')
last_text5.tag_config("4",font="Calibri 13 underline")
last_text5.grid(row=2,column=1)

image26=ImageTk.PhotoImage(Image.open(img26))
last_text6=Text(last_frame,bd=0,bg="#f4ede7",width=43)
last_text6.image_create(END,image=image26)
last_text6.insert(END,"\n\nGIFT SERVICES\n\n")
last_text6.insert(END,"Complimentary gift wrap,\nmonogramming, GiftNow and more.\n\n")
last_text6.insert(END,"SEE ALL")
last_text6.tag_add("1",1.0,END)
last_text6.tag_config("1",justify=CENTER)
last_text6.tag_add("2",3.0,'3.end')
last_text6.tag_config("2",font="Calibri 16")
last_text6.tag_add("3",5.0,'6.end')
last_text6.tag_config("3",font="Calibri 12")
last_text6.tag_add("4",8.0,'8.end')
last_text6.tag_config("4",font="Calibri 13 underline")
last_text6.grid(row=2,column=2)

image27=ImageTk.PhotoImage(Image.open(img27))
last_text7=Text(last_frame,bd=0,bg="#f4ede7",width=43)
last_text7.image_create(END,image=image27)
last_text7.insert(END,"\n\n24/7 EXPERT\nADVICE\n\n")
last_text7.insert(END,"Questions? Ask away.\nWe love hearing from you.\n\n")
last_text7.insert(END,"CONTACT US")
last_text7.tag_add("1",1.0,END)
last_text7.tag_config("1",justify=CENTER)
last_text7.tag_add("2",3.0,'4.end')
last_text7.tag_config("2",font="Calibri 16")
last_text7.tag_add("3",6.0,'7.end')
last_text7.tag_config("3",font="Calibri 12")
last_text7.tag_add("4",9.0,'9.end')
last_text7.tag_config("4",font="Calibri 13 underline")
last_text7.grid(row=2,column=3)


handbags_win=Frame(mycanvas)
giftservice_win=Frame(mycanvas,bg="white")


master.mainloop()

