from tkinter import *
import sqlite3
import time
import webbrowser
import datetime
import pyperclip
from tkinter import font
from automation import clickme
root=Tk()
root.title("Schedule")
root.geometry("412x470")
root.configure(background='#212121')

all=time.localtime()
day_now=str(time.strftime("%A"))
#print(day_now)

#datetimeinfo=datetime.datetime.now()
#nowhour=datetimeinfo.hour
#nowminute=datetimeinfo.minute
#nowtime=nowhour+(nowminute/60)
#print(nowtime)
global selected
selected=False




def create_a_tt_m():
    monday=Toplevel()
    monday.title("Monday")
    monday.configure(background='#212121')
    number_of_classes_label=Label(monday,text="Number of Classes :",background='#212121',foreground='white')
    number_of_classes_label.grid(row=0,column=0)
    number_of_classes_entry=Entry(monday)
    number_of_classes_entry.grid(row=0,column=1)

    m_frame=Frame(monday)
    m_frame.grid(row=1,columnspan=5,pady=(6,0))
    m_frame.configure(background='#333333')

    m_menu=Menu(monday,tearoff=0)
    monday.config(menu=m_menu)

    def input_classes():
        for widget in m_frame.winfo_children():
            widget.destroy()
        
        number_of_classes_monday=int(number_of_classes_entry.get())
        a=range(1,number_of_classes_monday+1)
        class_name_list=[]
        class_link_list=[]
        timei=[]
        timef=[]
        sno=Label(m_frame,text="S.NO",fg="white",background="#333333")
        sno.grid(row=0,column=0)
        name=Label(m_frame,text="Class Name",fg="white",background="#333333")
        name.grid(row=0,column=1)
        linkpaste=Label(m_frame,text="Class Link",fg="white",background="#333333")
        linkpaste.grid(row=0,column=2)
        start_time=Label(m_frame,text="Starting Time",fg="white",background="#333333")
        start_time.grid(row=0,column=3)
        end_time=Label(m_frame,text="Ending Time",fg="white",background="#333333")
        end_time.grid(row=0,column=4)
        for i in a:
            classlabels=Label(m_frame,text="class"+str(i),background='#333333',foreground='white')
            classlabels.grid(row=i,column=0)
            class_name=Entry(m_frame)
            class_name.grid(row=i,column=1)
            class_name_list.append(class_name)
            paste_link=Entry(m_frame)
            paste_link.grid(row=i,column=2)
            class_link_list.append(paste_link)

            clickedi=IntVar()
            droptimei=OptionMenu(m_frame,clickedi,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimei.configure(background='#191919',foreground='white')
            droptimei["menu"].config(bg="#191919",fg="white")
            droptimei.grid(row=i,column=3)
            timei.append(clickedi)

            clickedf=IntVar()
            droptimef=OptionMenu(m_frame,clickedf,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimef.configure(background='#191919',foreground='white')
            droptimef["menu"].config(bg="#191919",fg="white")
            droptimef.grid(row=i,column=4)
            timef.append(clickedf)

        def apply():
            ### CREATING/CONNECTING DATABASE TABLE ###
            myt1=sqlite3.connect("schedule.db")

            ### CREATE CURSOR ###
            myc1=myt1.cursor()

            ### CREATE TABLE ###
            myc1.execute("""CREATE TABLE IF NOT EXISTS mytt(day TEXT,class_name TEXT,class_link TEXT,time_start INTEGER,time_final INTEGER)""")

            for i in range(0,number_of_classes_monday):
                ### CREATING/CONNECTING DATABASE TABLE ###
                myt1=sqlite3.connect("schedule.db")

                ### CREATE CURSOR ###
                myc1=myt1.cursor()
                ### INSERTING ENETERED DATA INTO TABLE ###
                myc1.execute("INSERT INTO mytt VALUES (:d,:cn,:cl,:ts,:tf)",
                            {
                                'd':"Monday",
                                'cn':class_name_list[i].get(),
                                'cl':class_link_list[i].get(),
                                'ts':timei[i].get(),
                                'tf':timef[i].get()
                            })

                ### COMMIT CHANGES ###
                myt1.commit()

                ### CLOSE CONNECTIONS ###
                myt1.close()

                donelabel=Label(m_frame,text="DONE",background="#333333",foreground="white")
                donelabel.grid(row=number_of_classes_monday+2,column=2,padx=(0,70))


        apply=Button(m_frame,text="Apply",command=apply,background='#BB86FC')
        apply.grid(row=number_of_classes_monday+1,column=2,padx=(0,70))


        #def show():
            #entry=""
            #for entries in class_name_list:
                #entry = entry + str(entries.get()) + '\n'
                #mylabel=Label(monday,text=entry)
                #mylabel.grid(row=1,column=1)

        #prin=Button(monday,text="click",command=show)
        #prin.grid(row=1,column=0)


    number_of_classes_ok=Button(monday,text="OK",command=input_classes,background='#BB86FC')
    number_of_classes_ok.grid(row=0,column=2,padx=15)

    def showdata():
        ### CREATING/CONNECTING DATABASE TABLE ###
        myt1=sqlite3.connect("schedule.db")

        ### CREATE CURSOR ###
        myc1=myt1.cursor()
        
        ### fetching and printing ###
        myc1.execute("SELECT *,oid FROM mytt WHERE day = 'Monday'")
        records=myc1.fetchall()

        topm=Toplevel()
        topm.title("Data")
        topm.configure(bg="#191919")

        day=Label(topm,text="Day",fg="white",bg="#191919")
        day.grid(row=0,column=0)
        name=Label(topm,text="Class Name",fg="white",bg="#191919")
        name.grid(row=0,column=1)
        linkpaste=Label(topm,text="Class Link",fg="white",bg="#191919")
        linkpaste.grid(row=0,column=2)
        start_time=Label(topm,text="Starting Time",fg="white",bg="#191919")
        start_time.grid(row=0,column=3)
        end_time=Label(topm,text="Ending Time",fg="white",bg="#191919")
        end_time.grid(row=0,column=4)
        dataid=Label(topm,text="ID",fg="white",bg="#191919")
        dataid.grid(row=0,column=5)


        j=1
        for i in records:
            lab1=Label(topm,text=i[0],fg="white",bg="#191919")
            lab1.grid(row=j,column=0)
            lab2=Label(topm,text=i[1],fg="white",bg="#191919")
            lab2.grid(row=j,column=1)
            lab3=Label(topm,text=i[2],fg="white",bg="#191919")
            lab3.grid(row=j,column=2)
            lab4=Label(topm,text=str(i[3]),fg="white",bg="#191919")
            lab4.grid(row=j,column=3)
            lab5=Label(topm,text=str(i[4]),fg="white",bg="#191919")
            lab5.grid(row=j,column=4)
            lab6=Label(topm,text=str(i[5]),fg="white",bg="#191919")
            lab6.grid(row=j,column=5)
            j=j+1

        ### COMMIT CHANGES ###
        myt1.commit()

        ### CLOSE CONNECTIONS ###
        myt1.close()

    file_menu=Menu(m_menu,tearoff=0)
    m_menu.add_cascade(label="File",menu=file_menu)
    file_menu.add_command(label="Show Data",command=showdata)
    #showdatabutton=Button(monday,text="Show Data",command=showdata)
    #showdatabutton.grid(row=0,column=3)


    def delete():
        #topm2=Toplevel()
        #topm2.title("Delete entry")
        for widget in m_frame.winfo_children():
            widget.destroy()

        typeidlabel=Label(m_frame,text="Type id",fg="white",bg="#333333")
        typeidlabel.grid(row=0,column=0)
        typeid=Entry(m_frame,width=30)
        typeid.grid(row=0,column=1)
        def lastdelete():
            ### CREATING/CONNECTING DATABASE TABLE ###
            myt1=sqlite3.connect("schedule.db")

            ### CREATE CURSOR ###
            myc1=myt1.cursor()

            myc1.execute("DELETE FROM mytt WHERE oid="+typeid.get())

            typeid.delete(0,END)

            ### COMMIT CHANGES ###
            myt1.commit()

            ### CLOSE CONNECTIONS ###
            myt1.close()
            deletedone=Label(m_frame,text="DONE",fg="white",bg="#333333")
            deletedone.grid(row=2,column=0,columnspan=2)

        deletebutton=Button(m_frame,text="Delete record",command=lastdelete,bg="#BB86FC")
        deletebutton.grid(row=1,column=0,columnspan=2)

    delete_menu=Menu(m_menu,tearoff=0)
    m_menu.add_cascade(label="Delete",menu=delete_menu)
    delete_menu.add_command(label="Delete Using ID",command=delete)
    #deletedata=Button(monday,text="Delete using ID",command=delete)
    #deletedata.grid(row=0,column=4)


    def edit():
        #topm3=Toplevel()
        #topm3.title("Edit Record")
        for widget in m_frame.winfo_children():
            widget.destroy()

        enterid=Label(m_frame,text="Enter id",fg="white",bg="#333333")
        enterid.grid(row=0,column=0)
        enteridbox=Entry(m_frame,width=20)
        enteridbox.grid(row=0,column=1)

        def clicked1():

            ### CREATING/CONNECTING DATABASE TABLE ###
            myt1=sqlite3.connect("schedule.db")

            ### CREATE CURSOR ###
            myc1=myt1.cursor()

            myid=enteridbox.get()
            myc1.execute("SELECT * FROM mytt WHERE oid =" + myid)
            showthatid=myc1.fetchall()

            ### COMMIT CHANGES ###
            myt1.commit()

            ### CLOSE CONNECTIONS ###
            myt1.close()


            def save():
                ### CREATING/CONNECTING DATABASE TABLE ###
                myt1=sqlite3.connect("schedule.db")

                ### CREATE CURSOR ###
                myc1=myt1.cursor()

                myc1.execute("""UPDATE mytt SET
                            class_name=:cn,
                            class_link=:cl,
                            time_start=:ts,
                            time_final=:tf
                            WHERE oid=:oid""",
                            {
                                'cn':class_name.get(),
                                'cl':class_link.get(),
                                'ts':clickedie.get(),
                                'tf':clickedfe.get(),
                                'oid':myid
                            })

                ### COMMIT CHANGES ###
                myt1.commit()

                ### CLOSE CONNECTIONS ###
                myt1.close()

                donelabel=Label(m_frame,text="DONE !",fg="white",bg="#333333")
                donelabel.grid(row=7,column=1)


            class_name=Entry(m_frame,width=10)
            class_link=Entry(m_frame,width=30)

            clickedie=IntVar()
            droptimei=OptionMenu(m_frame,clickedie,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimei.configure(background='#191919',foreground='white')
            droptimei["menu"].config(bg="#191919",fg="white")

            clickedfe=IntVar()
            droptimef=OptionMenu(m_frame,clickedfe,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimef.configure(background='#191919',foreground='white')
            droptimef["menu"].config(bg="#191919",fg="white")
        
            class_name.grid(row=1,column=0,columnspan=1,padx=10)
            class_link.grid(row=1,column=1,columnspan=2)
            droptimei.grid(row=1,column=3)
            droptimef.grid(row=1,column=4)

            for i in showthatid:
                class_name.insert(0,i[1])
                class_link.insert(0,i[2])
                clickedie.set(i[3])
                clickedfe.set(i[4])

            savebutton=Button(m_frame,text="Save",command=save,bg="#BB86FC")
            savebutton.grid(row=6,column=1)


        okbutton1=Button(m_frame,text="OK",command=clicked1,bg="#BB86FC")
        okbutton1.grid(row=0,column=2)

    edit_menu=Menu(m_menu,tearoff=0)
    m_menu.add_cascade(label="Edit",menu=edit_menu)
    edit_menu.add_command(label="Edit Using ID",command=edit)
    #editdata=Button(monday,text="Edit using ID",command=edit)
    #editdata.grid(row=0,column=5)

    def delete_all():
        ### CREATING/CONNECTING DATABASE TABLE ###
            myt1=sqlite3.connect("schedule.db")

            ### CREATE CURSOR ###
            myc1=myt1.cursor()
            delete_day="Monday"
            myc1.execute("DELETE FROM mytt WHERE day='{}'".format(delete_day))

            ### COMMIT CHANGES ###
            myt1.commit()

            ### CLOSE CONNECTIONS ###
            myt1.close()


    delete_menu.add_command(label="Delete all in Monday",command=delete_all)



def create_a_tt_t():
    tuesday=Toplevel()
    tuesday.title("Tuesday")
    tuesday.configure(background='#212121')

    number_of_classes_label=Label(tuesday,text="Number of Classes :",background='#212121',foreground='white')
    number_of_classes_label.grid(row=0,column=0)
    number_of_classes_entry=Entry(tuesday)
    number_of_classes_entry.grid(row=0,column=1)

    t_frame=Frame(tuesday)
    t_frame.grid(row=1,columnspan=5,pady=(6,0))
    t_frame.configure(background='#333333')

    t_menu=Menu(tuesday,tearoff=0)
    tuesday.config(menu=t_menu)

    def input_classes():
        for widget in t_frame.winfo_children():
            widget.destroy()

        number_of_classes_tuesday=int(number_of_classes_entry.get())
        a=range(1,number_of_classes_tuesday+1)
        class_name_list=[]
        class_link_list=[]
        timei=[]
        timef=[]
        sno=Label(t_frame,text="S.NO",fg="white",background="#333333")
        sno.grid(row=0,column=0)

        name=Label(t_frame,text="Class Name",fg="white",background="#333333")
        name.grid(row=0,column=1)

        linkpaste=Label(t_frame,text="Class Link",fg="white",background="#333333")
        linkpaste.grid(row=0,column=2)

        start_time=Label(t_frame,text="Starting Time",fg="white",background="#333333")
        start_time.grid(row=0,column=3)

        end_time=Label(t_frame,text="Ending Time",fg="white",background="#333333")
        end_time.grid(row=0,column=4)

        for i in a:
            classlabels=Label(t_frame,text="class"+str(i),background='#333333',foreground='white')
            classlabels.grid(row=i,column=0)
            class_name=Entry(t_frame)
            class_name.grid(row=i,column=1)
            class_name_list.append(class_name)
            paste_link=Entry(t_frame)
            paste_link.grid(row=i,column=2)
            class_link_list.append(paste_link)

            clickedi=IntVar()
            droptimei=OptionMenu(t_frame,clickedi,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimei.configure(background='#191919',foreground='white')
            droptimei["menu"].config(bg="#191919",fg="white")
            droptimei.grid(row=i,column=3)

            timei.append(clickedi)

            clickedf=IntVar()
            droptimef=OptionMenu(t_frame,clickedf,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimef.configure(background='#191919',foreground='white')
            droptimef["menu"].config(bg="#191919",fg="white")
            droptimef.grid(row=i,column=4)
            
            timef.append(clickedf)

        def apply():
            ### CREATING/CONNECTING DATABASE TABLE ###
            myt1=sqlite3.connect("schedule.db")

            ### CREATE CURSOR ###
            myc1=myt1.cursor()

            ### CREATE TABLE ###
            myc1.execute("""CREATE TABLE IF NOT EXISTS mytt(day TEXT,class_name TEXT,class_link TEXT,time_start INTEGER,time_final INTEGER)""")

            for i in range(0,number_of_classes_tuesday):
                ### CREATING/CONNECTING DATABASE TABLE ###
                myt1=sqlite3.connect("schedule.db")

                ### CREATE CURSOR ###
                myc1=myt1.cursor()
                ### INSERTING ENETERED DATA INTO TABLE ###
                myc1.execute("INSERT INTO mytt VALUES (:d,:cn,:cl,:ts,:tf)",
                            {
                                'd':"Tuesday",
                                'cn':class_name_list[i].get(),
                                'cl':class_link_list[i].get(),
                                'ts':timei[i].get(),
                                'tf':timef[i].get()
                            })

                ### COMMIT CHANGES ###
                myt1.commit()

                ### CLOSE CONNECTIONS ###
                myt1.close()

                donelabel=Label(t_frame,text="DONE",background="#333333",foreground="white")
                donelabel.grid(row=number_of_classes_tuesday+2,column=2)


        apply=Button(t_frame,text="Apply",command=apply,background='#BB86FC')
        apply.grid(row=number_of_classes_tuesday+1,column=2)


    


        #def show():
            #entry=""
            #for entries in class_name_list:
                #entry = entry + str(entries.get()) + '\n'
                #mylabel=Label(monday,text=entry)
                #mylabel.grid(row=1,column=1)

        #prin=Button(monday,text="click",command=show)
        #prin.grid(row=1,column=0)


    number_of_classes_ok=Button(tuesday,text="OK",command=input_classes,background='#BB86FC')
    number_of_classes_ok.grid(row=0,column=2,padx=15)

    def showdata():
        ### CREATING/CONNECTING DATABASE TABLE ###
        myt1=sqlite3.connect("schedule.db")

        ### CREATE CURSOR ###
        myc1=myt1.cursor()
        
        ### fetching and printing ###
        myc1.execute("SELECT *,oid FROM mytt WHERE day = 'Tuesday'")
        records=myc1.fetchall()

        topt=Toplevel()
        topt.title("Data")
        topt.configure(bg="#191919")

        day=Label(topt,text="Day",fg="white",bg="#191919")
        day.grid(row=0,column=0)

        name=Label(topt,text="Class Name",fg="white",bg="#191919")
        name.grid(row=0,column=1)

        linkpaste=Label(topt,text="Class Link",fg="white",bg="#191919")
        linkpaste.grid(row=0,column=2)

        start_time=Label(topt,text="Starting Time",fg="white",bg="#191919")
        start_time.grid(row=0,column=3)

        end_time=Label(topt,text="Ending Time",fg="white",bg="#191919")
        end_time.grid(row=0,column=4)

        dataid=Label(topt,text="ID",fg="white",bg="#191919")
        dataid.grid(row=0,column=5)


        j=1
        for i in records:
            lab1=Label(topt,text=i[0],fg="white",bg="#191919")
            lab1.grid(row=j,column=0)
            lab2=Label(topt,text=i[1],fg="white",bg="#191919")
            lab2.grid(row=j,column=1)
            lab3=Label(topt,text=i[2],fg="white",bg="#191919")
            lab3.grid(row=j,column=2)
            lab4=Label(topt,text=str(i[3]),fg="white",bg="#191919")
            lab4.grid(row=j,column=3)
            lab5=Label(topt,text=str(i[4]),fg="white",bg="#191919")
            lab5.grid(row=j,column=4)
            lab6=Label(topt,text=str(i[5]),fg="white",bg="#191919")
            lab6.grid(row=j,column=5)
            j=j+1
    
        ### COMMIT CHANGES ###
        myt1.commit()

        ### CLOSE CONNECTIONS ###
        myt1.close()

    file_menu=Menu(t_menu,tearoff=0)
    t_menu.add_cascade(label="File",menu=file_menu)
    file_menu.add_command(label="Show Data",command=showdata)
    #showdatabutton=Button(tuesday,text="Show Data",command=showdata)
    #showdatabutton.grid(row=0,column=3)

    def delete():
        #topt2=Toplevel()
        #topt2.title("Delete entry")
        for widget in t_frame.winfo_children():
            widget.destroy()

        typeidlabel=Label(t_frame,text="Type id",fg="white",bg="#333333")
        typeidlabel.grid(row=0,column=0)
        typeid=Entry(t_frame,width=30)
        typeid.grid(row=0,column=1)
        def lastdelete():
            ### CREATING/CONNECTING DATABASE TABLE ###
            myt1=sqlite3.connect("schedule.db")

            ### CREATE CURSOR ###
            myc1=myt1.cursor()

            myc1.execute("DELETE FROM mytt WHERE oid="+typeid.get())

            typeid.delete(0,END)

            ### COMMIT CHANGES ###
            myt1.commit()

            ### CLOSE CONNECTIONS ###
            myt1.close()
            deletedone=Label(t_frame,text="DONE",fg="white",bg="#333333")
            deletedone.grid(row=2,column=0,columnspan=2)


        deletebutton=Button(t_frame,text="Delete record",command=lastdelete,bg="#BB86FC")
        deletebutton.grid(row=1,column=0,columnspan=2)

    delete_menu=Menu(t_menu,tearoff=0)
    t_menu.add_cascade(label="Delete",menu=delete_menu)
    delete_menu.add_command(label="Delete Using ID",command=delete)
    #deletedata=Button(tuesday,text="Delete using ID",command=delete)
    #deletedata.grid(row=0,column=4)


    def edit():
        #topt3=Toplevel()
        #topt3.title("Edit Record")
        for widget in t_frame.winfo_children():
            widget.destroy()

        enterid=Label(t_frame,text="Enter id",fg="white",bg="#333333")
        enterid.grid(row=0,column=0)
        enteridbox=Entry(t_frame,width=20)
        enteridbox.grid(row=0,column=1)

        def clicked1():

            ### CREATING/CONNECTING DATABASE TABLE ###
            myt1=sqlite3.connect("schedule.db")

            ### CREATE CURSOR ###
            myc1=myt1.cursor()

            myid=enteridbox.get()
            myc1.execute("SELECT * FROM mytt WHERE oid =" + myid)
            showthatid=myc1.fetchall()

            ### COMMIT CHANGES ###
            myt1.commit()

            ### CLOSE CONNECTIONS ###
            myt1.close()


            def save():
                ### CREATING/CONNECTING DATABASE TABLE ###
                myt1=sqlite3.connect("schedule.db")

                ### CREATE CURSOR ###
                myc1=myt1.cursor()

                myc1.execute("""UPDATE mytt SET
                            class_name=:cn,
                            class_link=:cl,
                            time_start=:ts,
                            time_final=:tf
                            WHERE oid=:oid""",
                            {
                                'cn':class_name.get(),
                                'cl':class_link.get(),
                                'ts':clickedie.get(),
                                'tf':clickedfe.get(),
                                'oid':myid
                            })

                ### COMMIT CHANGES ###
                myt1.commit()

                ### CLOSE CONNECTIONS ###
                myt1.close()

                donelabel=Label(t_frame,text="DONE !",fg="white",bg="#333333")
                donelabel.grid(row=7,column=1)


            class_name=Entry(t_frame,width=10)
            class_link=Entry(t_frame,width=30)

            clickedie=IntVar()
            droptimei=OptionMenu(t_frame,clickedie,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimei.configure(background='#191919',foreground='white')
            droptimei["menu"].config(bg="#191919",fg="white")

            clickedfe=IntVar()
            droptimef=OptionMenu(t_frame,clickedfe,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimef.configure(background='#191919',foreground='white')
            droptimef["menu"].config(bg="#191919",fg="white")
        
            class_name.grid(row=1,column=0,columnspan=1,padx=10)
            class_link.grid(row=1,column=1,columnspan=2)
            droptimei.grid(row=1,column=3)
            droptimef.grid(row=1,column=4)

            for i in showthatid:
                class_name.insert(0,i[1])
                class_link.insert(0,i[2])
                clickedie.set(i[3])
                clickedfe.set(i[4])

            savebutton=Button(t_frame,text="Save",command=save,bg="#BB86FC")
            savebutton.grid(row=6,column=1)


        okbutton1=Button(t_frame,text="OK",command=clicked1,bg="#BB86FC")
        okbutton1.grid(row=0,column=2)

    edit_menu=Menu(t_menu,tearoff=0)
    t_menu.add_cascade(label="Edit",menu=edit_menu)
    edit_menu.add_command(label="Edit Using ID",command=edit)
    #editdata=Button(tuesday,text="Edit using ID",command=edit)
    #editdata.grid(row=0,column=5)

    def delete_all():
        ### CREATING/CONNECTING DATABASE TABLE ###
        myt1=sqlite3.connect("schedule.db")

        ### CREATE CURSOR ###
        myc1=myt1.cursor()
        delete_day="Tuesday"
        myc1.execute("DELETE FROM mytt WHERE day='{}'".format(delete_day))

         ### COMMIT CHANGES ###
        myt1.commit()

        ### CLOSE CONNECTIONS ###
        myt1.close()

    delete_menu.add_command(label="Delete all in Tuesday",command=delete_all)




def create_a_tt_w():
    wednesday=Toplevel()
    wednesday.title("Wednesday")
    wednesday.configure(background='#212121')

    number_of_classes_label=Label(wednesday,text="Number of Classes :",background='#212121',foreground='white')
    number_of_classes_label.grid(row=0,column=0)
    number_of_classes_entry=Entry(wednesday)
    number_of_classes_entry.grid(row=0,column=1)

    w_frame=Frame(wednesday)
    w_frame.grid(row=1,columnspan=5,pady=(6,0))
    w_frame.configure(background='#333333')

    w_menu=Menu(wednesday,tearoff=0)
    wednesday.config(menu=w_menu)


    def input_classes():
        for widget in w_frame.winfo_children():
            widget.destroy()
        
        number_of_classes_wednesday=int(number_of_classes_entry.get())
        a=range(1,number_of_classes_wednesday+1)
        class_name_list=[]
        class_link_list=[]
        timei=[]
        timef=[]
        sno=Label(w_frame,text="S.NO",fg="white",background="#333333")
        sno.grid(row=0,column=0)

        name=Label(w_frame,text="Class Name",fg="white",background="#333333")
        name.grid(row=0,column=1)

        linkpaste=Label(w_frame,text="Class Link",fg="white",background="#333333")
        linkpaste.grid(row=0,column=2)

        start_time=Label(w_frame,text="Starting Time",fg="white",background="#333333")
        start_time.grid(row=0,column=3)

        end_time=Label(w_frame,text="Ending Time",fg="white",background="#333333")
        end_time.grid(row=0,column=4)
        for i in a:
            classlabels=Label(w_frame,text="class"+str(i),background='#333333',foreground='white')
            classlabels.grid(row=i,column=0)
            class_name=Entry(w_frame)
            class_name.grid(row=i,column=1)
            class_name_list.append(class_name)
            paste_link=Entry(w_frame)
            paste_link.grid(row=i,column=2)
            class_link_list.append(paste_link)

            clickedi=IntVar()
            droptimei=OptionMenu(w_frame,clickedi,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimei.configure(background='#191919',foreground='white')
            droptimei["menu"].config(bg="#191919",fg="white")
            droptimei.grid(row=i,column=3)
            timei.append(clickedi)

            clickedf=IntVar()
            droptimef=OptionMenu(w_frame,clickedf,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimef.configure(background='#191919',foreground='white')
            droptimef["menu"].config(bg="#191919",fg="white")
            droptimef.grid(row=i,column=4)
            timef.append(clickedf)

        def apply():
            ### CREATING/CONNECTING DATABASE TABLE ###
            myt1=sqlite3.connect("schedule.db")

            ### CREATE CURSOR ###
            myc1=myt1.cursor()

            ### CREATE TABLE ###
            myc1.execute("""CREATE TABLE IF NOT EXISTS mytt(day TEXT,class_name TEXT,class_link TEXT,time_start INTEGER,time_final INTEGER)""")

            for i in range(0,number_of_classes_wednesday):
                ### CREATING/CONNECTING DATABASE TABLE ###
                myt1=sqlite3.connect("schedule.db")

                ### CREATE CURSOR ###
                myc1=myt1.cursor()
                ### INSERTING ENETERED DATA INTO TABLE ###
                myc1.execute("INSERT INTO mytt VALUES (:d,:cn,:cl,:ts,:tf)",
                            {
                                'd':"Wednesday",
                                'cn':class_name_list[i].get(),
                                'cl':class_link_list[i].get(),
                                'ts':timei[i].get(),
                                'tf':timef[i].get()
                            })

                ### COMMIT CHANGES ###
                myt1.commit()

                ### CLOSE CONNECTIONS ###
                myt1.close()

                donelabel=Label(w_frame,text="DONE",background="#333333",foreground="white")
                donelabel.grid(row=number_of_classes_wednesday+2,column=2)


        apply=Button(w_frame,text="Apply",command=apply,background='#BB86FC')
        apply.grid(row=number_of_classes_wednesday+1,column=2)


    


        #def show():
            #entry=""
            #for entries in class_name_list:
                #entry = entry + str(entries.get()) + '\n'
                #mylabel=Label(monday,text=entry)
                #mylabel.grid(row=1,column=1)

        #prin=Button(monday,text="click",command=show)
        #prin.grid(row=1,column=0)


    number_of_classes_ok=Button(wednesday,text="OK",command=input_classes,background='#BB86FC')
    number_of_classes_ok.grid(row=0,column=2,padx=15)

    def showdata():
        ### CREATING/CONNECTING DATABASE TABLE ###
        myt1=sqlite3.connect("schedule.db")

        ### CREATE CURSOR ###
        myc1=myt1.cursor()
        
        ### fetching and printing ###
        myc1.execute("SELECT *,oid FROM mytt WHERE day = 'Wednesday'")
        records=myc1.fetchall()

        topw=Toplevel()
        topw.title("Data")
        topw.configure(bg="#191919")

        day=Label(topw,text="Day",fg="white",bg="#191919")
        day.grid(row=0,column=0)

        name=Label(topw,text="Class Name",fg="white",bg="#191919")
        name.grid(row=0,column=1)

        linkpaste=Label(topw,text="Class Link",fg="white",bg="#191919")
        linkpaste.grid(row=0,column=2)

        start_time=Label(topw,text="Starting Time",fg="white",bg="#191919")
        start_time.grid(row=0,column=3)

        end_time=Label(topw,text="Ending Time",fg="white",bg="#191919")
        end_time.grid(row=0,column=4)

        dataid=Label(topw,text="ID",fg="white",bg="#191919")
        dataid.grid(row=0,column=5)


        j=1
        for i in records:
            lab1=Label(topw,text=i[0],fg="white",bg="#191919")
            lab1.grid(row=j,column=0)
            lab2=Label(topw,text=i[1],fg="white",bg="#191919")
            lab2.grid(row=j,column=1)
            lab3=Label(topw,text=i[2],fg="white",bg="#191919")
            lab3.grid(row=j,column=2)
            lab4=Label(topw,text=str(i[3]),fg="white",bg="#191919")
            lab4.grid(row=j,column=3)
            lab5=Label(topw,text=str(i[4]),fg="white",bg="#191919")
            lab5.grid(row=j,column=4)
            lab6=Label(topw,text=str(i[5]),fg="white",bg="#191919")
            lab6.grid(row=j,column=5)
            j=j+1

        ### COMMIT CHANGES ###
        myt1.commit()

        ### CLOSE CONNECTIONS ###
        myt1.close()

    file_menu=Menu(w_menu,tearoff=0)
    w_menu.add_cascade(label="File",menu=file_menu)
    file_menu.add_command(label="Show Data",command=showdata)
    #showdatabutton=Button(wednesday,text="Show Data",command=showdata)
    #showdatabutton.grid(row=0,column=3)

    def delete():
        #topw2=Toplevel()
        #topw2.title("Delete entry")
        for widget in w_frame.winfo_children():
            widget.destroy()

        typeidlabel=Label(w_frame,text="Type id",fg="white",bg="#333333")
        typeidlabel.grid(row=0,column=0)
        typeid=Entry(w_frame,width=30)
        typeid.grid(row=0,column=1)
        def lastdelete():
            ### CREATING/CONNECTING DATABASE TABLE ###
            myt1=sqlite3.connect("schedule.db")

            ### CREATE CURSOR ###
            myc1=myt1.cursor()

            myc1.execute("DELETE FROM mytt WHERE oid="+typeid.get())

            typeid.delete(0,END)

            ### COMMIT CHANGES ###
            myt1.commit()

            ### CLOSE CONNECTIONS ###
            myt1.close()
            deletedone=Label(w_frame,text="DONE",fg="white",bg="#333333")
            deletedone.grid(row=2,column=0,columnspan=2)


        deletebutton=Button(w_frame,text="Delete record",command=lastdelete,bg="#BB86FC")
        deletebutton.grid(row=1,column=0,columnspan=2)

    delete_menu=Menu(w_menu,tearoff=0)
    w_menu.add_cascade(label="Delete",menu=delete_menu)
    delete_menu.add_command(label="Delete Using ID",command=delete)
    #deletedata=Button(wednesday,text="Delete using ID",command=delete)
    #deletedata.grid(row=0,column=4)

    def edit():
        #topw3=Toplevel()
        #topw3.title("Edit Record")
        for widget in w_frame.winfo_children():
            widget.destroy()

        enterid=Label(w_frame,text="Enter id",fg="white",bg="#333333")
        enterid.grid(row=0,column=0)
        enteridbox=Entry(w_frame,width=20)
        enteridbox.grid(row=0,column=1)

        def clicked1():

            ### CREATING/CONNECTING DATABASE TABLE ###
            myt1=sqlite3.connect("schedule.db")

            ### CREATE CURSOR ###
            myc1=myt1.cursor()

            myid=enteridbox.get()
            myc1.execute("SELECT * FROM mytt WHERE oid =" + myid)
            showthatid=myc1.fetchall()

            ### COMMIT CHANGES ###
            myt1.commit()

            ### CLOSE CONNECTIONS ###
            myt1.close()


            def save():
                ### CREATING/CONNECTING DATABASE TABLE ###
                myt1=sqlite3.connect("schedule.db")

                ### CREATE CURSOR ###
                myc1=myt1.cursor()

                myc1.execute("""UPDATE mytt SET
                            class_name=:cn,
                            class_link=:cl,
                            time_start=:ts,
                            time_final=:tf
                            WHERE oid=:oid""",
                            {
                                'cn':class_name.get(),
                                'cl':class_link.get(),
                                'ts':clickedie.get(),
                                'tf':clickedfe.get(),
                                'oid':myid
                            })

                ### COMMIT CHANGES ###
                myt1.commit()

                ### CLOSE CONNECTIONS ###
                myt1.close()

                donelabel=Label(w_frame,text="DONE !",fg="white",bg="#333333")
                donelabel.grid(row=7,column=1)


            class_name=Entry(w_frame,width=10)
            class_link=Entry(w_frame,width=30)

            clickedie=IntVar()
            droptimei=OptionMenu(w_frame,clickedie,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimei.configure(background='#191919',foreground='white')
            droptimei["menu"].config(bg="#191919",fg="white")

            clickedfe=IntVar()
            droptimef=OptionMenu(w_frame,clickedfe,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimef.configure(background='#191919',foreground='white')
            droptimef["menu"].config(bg="#191919",fg="white")
        
            class_name.grid(row=1,column=0,columnspan=1,padx=10)
            class_link.grid(row=1,column=1,columnspan=2)
            droptimei.grid(row=1,column=3)
            droptimef.grid(row=1,column=4)

            for i in showthatid:
                class_name.insert(0,i[1])
                class_link.insert(0,i[2])
                clickedie.set(i[3])
                clickedfe.set(i[4])

            savebutton=Button(w_frame,text="Save",command=save,bg="#BB86FC")
            savebutton.grid(row=6,column=1)


        okbutton1=Button(w_frame,text="OK",command=clicked1,bg="#BB86FC")
        okbutton1.grid(row=0,column=2)

    edit_menu=Menu(w_menu,tearoff=0)
    w_menu.add_cascade(label="Edit",menu=edit_menu)
    edit_menu.add_command(label="Edit Using ID",command=edit)
    #editdata=Button(wednesday,text="Edit using ID",command=edit)
    #editdata.grid(row=0,column=5)

    def delete_all():
        ### CREATING/CONNECTING DATABASE TABLE ###
        myt1=sqlite3.connect("schedule.db")

        ### CREATE CURSOR ###
        myc1=myt1.cursor()
        delete_day="Wednesday"
        myc1.execute("DELETE FROM mytt WHERE day='{}'".format(delete_day))

        ### COMMIT CHANGES ###
        myt1.commit()

        ### CLOSE CONNECTIONS ###
        myt1.close()

    delete_menu.add_command(label="Delete all in Wednesday",command=delete_all)




def create_a_tt_th():
    thursday=Toplevel()
    thursday.title("Thursday")
    thursday.configure(background="#212121")

    number_of_classes_label=Label(thursday,text="Number of Classes :",background='#212121',foreground='white')
    number_of_classes_label.grid(row=0,column=0)
    number_of_classes_entry=Entry(thursday)
    number_of_classes_entry.grid(row=0,column=1)

    th_frame=Frame(thursday)
    th_frame.grid(row=1,columnspan=5,pady=(6,0))
    th_frame.configure(background='#333333')

    th_menu=Menu(thursday,tearoff=0)
    thursday.config(menu=th_menu)


    def input_classes():
        for widget in th_frame.winfo_children():
            widget.destroy()

        number_of_classes_thursday=int(number_of_classes_entry.get())
        a=range(1,number_of_classes_thursday+1)
        class_name_list=[]
        class_link_list=[]
        timei=[]
        timef=[]
        sno=Label(th_frame,text="S.NO",fg="white",background="#333333")
        sno.grid(row=0,column=0)

        name=Label(th_frame,text="Class Name",fg="white",background="#333333")
        name.grid(row=0,column=1)

        linkpaste=Label(th_frame,text="Class Link",fg="white",background="#333333")
        linkpaste.grid(row=0,column=2)

        start_time=Label(th_frame,text="Starting Time",fg="white",background="#333333")
        start_time.grid(row=0,column=3)

        end_time=Label(th_frame,text="Ending Time",fg="white",background="#333333")
        end_time.grid(row=0,column=4)
        for i in a:
            classlabels=Label(th_frame,text="class"+str(i),background='#333333',foreground='white')
            classlabels.grid(row=i,column=0)
            class_name=Entry(th_frame)
            class_name.grid(row=i,column=1)
            class_name_list.append(class_name)
            paste_link=Entry(th_frame)
            paste_link.grid(row=i,column=2)
            class_link_list.append(paste_link)

            clickedi=IntVar()
            droptimei=OptionMenu(th_frame,clickedi,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimei.configure(background='#191919',foreground='white')
            droptimei["menu"].config(bg="#191919",fg="white")
            droptimei.grid(row=i,column=3)
            timei.append(clickedi)

            clickedf=IntVar()
            droptimef=OptionMenu(th_frame,clickedf,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimef.configure(background='#191919',foreground='white')
            droptimef["menu"].config(bg="#191919",fg="white")
            droptimef.grid(row=i,column=4)
            timef.append(clickedf)

        def apply():
            ### CREATING/CONNECTING DATABASE TABLE ###
            myt1=sqlite3.connect("schedule.db")

            ### CREATE CURSOR ###
            myc1=myt1.cursor()

            ### CREATE TABLE ###
            myc1.execute("""CREATE TABLE IF NOT EXISTS mytt(day TEXT,class_name TEXT,class_link TEXT,time_start INTEGER,time_final INTEGER)""")

            for i in range(0,number_of_classes_thursday):
                ### CREATING/CONNECTING DATABASE TABLE ###
                myt1=sqlite3.connect("schedule.db")

                ### CREATE CURSOR ###
                myc1=myt1.cursor()
                ### INSERTING ENETERED DATA INTO TABLE ###
                myc1.execute("INSERT INTO mytt VALUES (:d,:cn,:cl,:ts,:tf)",
                            {
                                'd':"Thursday",
                                'cn':class_name_list[i].get(),
                                'cl':class_link_list[i].get(),
                                'ts':timei[i].get(),
                                'tf':timef[i].get()
                            })

                ### COMMIT CHANGES ###
                myt1.commit()

                ### CLOSE CONNECTIONS ###
                myt1.close()

                donelabel=Label(th_frame,text="DONE",background="#333333",foreground="white")
                donelabel.grid(row=number_of_classes_thursday+2,column=2)


        apply=Button(th_frame,text="Apply",command=apply,background='#BB86FC')
        apply.grid(row=number_of_classes_thursday+1,column=2)


    


        #def show():
            #entry=""
            #for entries in class_name_list:
                #entry = entry + str(entries.get()) + '\n'
                #mylabel=Label(monday,text=entry)
                #mylabel.grid(row=1,column=1)

        #prin=Button(monday,text="click",command=show)
        #prin.grid(row=1,column=0)


    number_of_classes_ok=Button(thursday,text="OK",command=input_classes,background='#BB86FC')
    number_of_classes_ok.grid(row=0,column=2,padx=15)

    def showdata():
        ### CREATING/CONNECTING DATABASE TABLE ###
        myt1=sqlite3.connect("schedule.db")

        ### CREATE CURSOR ###
        myc1=myt1.cursor()
        
        ### fetching and printing ###
        myc1.execute("SELECT *,oid FROM mytt WHERE day = 'Thursday'")
        records=myc1.fetchall()
        
        topth=Toplevel()
        topth.title("Data")
        topth.configure(bg="#191919")

        day=Label(topth,text="Day",fg="white",bg="#191919")
        day.grid(row=0,column=0)

        name=Label(topth,text="Class Name",fg="white",bg="#191919")
        name.grid(row=0,column=1)

        linkpaste=Label(topth,text="Class Link",fg="white",bg="#191919")
        linkpaste.grid(row=0,column=2)

        start_time=Label(topth,text="Starting Time",fg="white",bg="#191919")
        start_time.grid(row=0,column=3)

        end_time=Label(topth,text="Ending Time",fg="white",bg="#191919")
        end_time.grid(row=0,column=4)

        dataid=Label(topth,text="ID",fg="white",bg="#191919")
        dataid.grid(row=0,column=5)


        j=1
        for i in records:
            lab1=Label(topth,text=i[0],fg="white",bg="#191919")
            lab1.grid(row=j,column=0)
            lab2=Label(topth,text=i[1],fg="white",bg="#191919")
            lab2.grid(row=j,column=1)
            lab3=Label(topth,text=i[2],fg="white",bg="#191919")
            lab3.grid(row=j,column=2)
            lab4=Label(topth,text=str(i[3]),fg="white",bg="#191919")
            lab4.grid(row=j,column=3)
            lab5=Label(topth,text=str(i[4]),fg="white",bg="#191919")
            lab5.grid(row=j,column=4)
            lab6=Label(topth,text=str(i[5]),fg="white",bg="#191919")
            lab6.grid(row=j,column=5)
            j=j+1

        ### COMMIT CHANGES ###
        myt1.commit()

        ### CLOSE CONNECTIONS ###
        myt1.close()

    file_menu=Menu(th_menu,tearoff=0)
    th_menu.add_cascade(label="File",menu=file_menu)
    file_menu.add_command(label="Show Data",command=showdata)
    #showdatabutton=Button(thursday,text="Show Data",command=showdata)
    #showdatabutton.grid(row=0,column=3)

    def delete():
        #topth2=Toplevel()
        #topth2.title("Delete entry")
        for widget in th_frame.winfo_children():
            widget.destroy()

        typeidlabel=Label(th_frame,text="Type id",fg="white",bg="#333333")
        typeidlabel.grid(row=0,column=0)
        typeid=Entry(th_frame,width=30)
        typeid.grid(row=0,column=1)
        def lastdelete():
            ### CREATING/CONNECTING DATABASE TABLE ###
            myt1=sqlite3.connect("schedule.db")

            ### CREATE CURSOR ###
            myc1=myt1.cursor()

            myc1.execute("DELETE FROM mytt WHERE oid="+typeid.get())

            typeid.delete(0,END)

            ### COMMIT CHANGES ###
            myt1.commit()

            ### CLOSE CONNECTIONS ###
            myt1.close()
            deletedone=Label(th_frame,text="DONE",fg="white",bg="#333333")
            deletedone.grid(row=2,column=0,columnspan=2)


        deletebutton=Button(th_frame,text="Delete record",command=lastdelete,bg="#BB86FC")
        deletebutton.grid(row=1,column=0,columnspan=2)

    delete_menu=Menu(th_menu,tearoff=0)
    th_menu.add_cascade(label="Delete",menu=delete_menu)
    delete_menu.add_command(label="Delete Using ID",command=delete)
    #deletedata=Button(thursday,text="Delete using ID",command=delete)
    #deletedata.grid(row=0,column=4)

    def edit():
        #topth3=Toplevel()
        #topth3.title("Edit Record")
        for widget in th_frame.winfo_children():
            widget.destroy()

        enterid=Label(th_frame,text="Enter id",fg="white",bg="#333333")
        enterid.grid(row=0,column=0)
        enteridbox=Entry(th_frame,width=20)
        enteridbox.grid(row=0,column=1)

        def clicked1():

            ### CREATING/CONNECTING DATABASE TABLE ###
            myt1=sqlite3.connect("schedule.db")

            ### CREATE CURSOR ###
            myc1=myt1.cursor()

            myid=enteridbox.get()
            myc1.execute("SELECT * FROM mytt WHERE oid =" + myid)
            showthatid=myc1.fetchall()

            ### COMMIT CHANGES ###
            myt1.commit()

            ### CLOSE CONNECTIONS ###
            myt1.close()


            def save():
                ### CREATING/CONNECTING DATABASE TABLE ###
                myt1=sqlite3.connect("schedule.db")

                ### CREATE CURSOR ###
                myc1=myt1.cursor()

                myc1.execute("""UPDATE mytt SET
                            class_name=:cn,
                            class_link=:cl,
                            time_start=:ts,
                            time_final=:tf
                            WHERE oid=:oid""",
                            {
                                'cn':class_name.get(),
                                'cl':class_link.get(),
                                'ts':clickedie.get(),
                                'tf':clickedfe.get(),
                                'oid':myid
                            })

                ### COMMIT CHANGES ###
                myt1.commit()

                ### CLOSE CONNECTIONS ###
                myt1.close()

                donelabel=Label(th_frame,text="DONE !",fg="white",bg="#333333")
                donelabel.grid(row=7,column=1)


            class_name=Entry(th_frame,width=10)
            class_link=Entry(th_frame,width=30)

            clickedie=IntVar()
            droptimei=OptionMenu(th_frame,clickedie,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimei.configure(background='#191919',foreground='white')
            droptimei["menu"].config(bg="#191919",fg="white")

            clickedfe=IntVar()
            droptimef=OptionMenu(th_frame,clickedfe,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimef.configure(background='#191919',foreground='white')
            droptimef["menu"].config(bg="#191919",fg="white")
        
            class_name.grid(row=1,column=0,columnspan=1,padx=10)
            class_link.grid(row=1,column=1,columnspan=2)
            droptimei.grid(row=1,column=3)
            droptimef.grid(row=1,column=4)

            for i in showthatid:
                class_name.insert(0,i[1])
                class_link.insert(0,i[2])
                clickedie.set(i[3])
                clickedfe.set(i[4])

            savebutton=Button(th_frame,text="Save",command=save,bg="#BB86FC")
            savebutton.grid(row=6,column=1)


        okbutton1=Button(th_frame,text="OK",command=clicked1,bg="#BB86FC")
        okbutton1.grid(row=0,column=2)


    edit_menu=Menu(th_menu,tearoff=0)
    th_menu.add_cascade(label="Edit",menu=edit_menu)
    edit_menu.add_command(label="Edit Using ID",command=edit)
    #editdata=Button(thursday,text="Edit using ID",command=edit)
    #editdata.grid(row=0,column=5)

    def delete_all():
        ### CREATING/CONNECTING DATABASE TABLE ###
        myt1=sqlite3.connect("schedule.db")

        ### CREATE CURSOR ###
        myc1=myt1.cursor()
        delete_day="Thursday"
        myc1.execute("DELETE FROM mytt WHERE day='{}'".format(delete_day))

        ### COMMIT CHANGES ###
        myt1.commit()

        ### CLOSE CONNECTIONS ###
        myt1.close()

    delete_menu.add_command(label="Delete all in Thursday",command=delete_all)




def create_a_tt_f():
    friday=Toplevel()
    friday.title("Friday")
    friday.configure(background='#212121')

    number_of_classes_label=Label(friday,text="Number of Classes :",background='#212121',foreground='white')
    number_of_classes_label.grid(row=0,column=0)
    number_of_classes_entry=Entry(friday)
    number_of_classes_entry.grid(row=0,column=1)

    f_frame=Frame(friday)
    f_frame.grid(row=1,columnspan=5,pady=(6,0))
    f_frame.configure(background='#333333')

    f_menu=Menu(friday,tearoff=0)
    friday.config(menu=f_menu)


    def input_classes():
        for widget in f_frame.winfo_children():
            widget.destroy()

        number_of_classes_friday=int(number_of_classes_entry.get())
        a=range(1,number_of_classes_friday+1)
        class_name_list=[]
        class_link_list=[]
        timei=[]
        timef=[]
        sno=Label(f_frame,text="S.NO",fg="white",background="#333333")
        sno.grid(row=0,column=0)

        name=Label(f_frame,text="Class Name",fg="white",background="#333333")
        name.grid(row=0,column=1)

        linkpaste=Label(f_frame,text="Class Link",fg="white",background="#333333")
        linkpaste.grid(row=0,column=2)

        start_time=Label(f_frame,text="Starting Time",fg="white",background="#333333")
        start_time.grid(row=0,column=3)

        end_time=Label(f_frame,text="Ending Time",fg="white",background="#333333")
        end_time.grid(row=0,column=4)
        for i in a:
            classlabels=Label(f_frame,text="class"+str(i),background='#333333',foreground='white')
            classlabels.grid(row=i,column=0)
            class_name=Entry(f_frame)
            class_name.grid(row=i,column=1)
            class_name_list.append(class_name)
            paste_link=Entry(f_frame)
            paste_link.grid(row=i,column=2)
            class_link_list.append(paste_link)

            clickedi=IntVar()
            droptimei=OptionMenu(f_frame,clickedi,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimei.configure(background='#191919',foreground='white')
            droptimei["menu"].config(bg="#191919",fg="white")
            droptimei.grid(row=i,column=3)
            timei.append(clickedi)

            clickedf=IntVar()
            droptimef=OptionMenu(f_frame,clickedf,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimef.configure(background='#191919',foreground='white')
            droptimef["menu"].config(bg="#191919",fg="white")
            droptimef.grid(row=i,column=4)
            timef.append(clickedf)

        def apply():
            ### CREATING/CONNECTING DATABASE TABLE ###
            myt1=sqlite3.connect("schedule.db")

            ### CREATE CURSOR ###
            myc1=myt1.cursor()

            ### CREATE TABLE ###
            myc1.execute("""CREATE TABLE IF NOT EXISTS mytt(day TEXT,class_name TEXT,class_link TEXT,time_start INTEGER,time_final INTEGER)""")

            for i in range(0,number_of_classes_friday):
                ### CREATING/CONNECTING DATABASE TABLE ###
                myt1=sqlite3.connect("schedule.db")

                ### CREATE CURSOR ###
                myc1=myt1.cursor()
                ### INSERTING ENETERED DATA INTO TABLE ###
                myc1.execute("INSERT INTO mytt VALUES (:d,:cn,:cl,:ts,:tf)",
                            {
                                'd':"Friday",
                                'cn':class_name_list[i].get(),
                                'cl':class_link_list[i].get(),
                                'ts':timei[i].get(),
                                'tf':timef[i].get()
                            })

                ### COMMIT CHANGES ###
                myt1.commit()

                ### CLOSE CONNECTIONS ###
                myt1.close()

                donelabel=Label(f_frame,text="DONE",background="#333333",foreground="white")
                donelabel.grid(row=number_of_classes_friday+2,column=2)


        apply=Button(f_frame,text="Apply",command=apply,background='#BB86FC')
        apply.grid(row=number_of_classes_friday+1,column=2)


    


        #def show():
            #entry=""
            #for entries in class_name_list:
                #entry = entry + str(entries.get()) + '\n'
                #mylabel=Label(monday,text=entry)
                #mylabel.grid(row=1,column=1)

        #prin=Button(monday,text="click",command=show)
        #prin.grid(row=1,column=0)


    number_of_classes_ok=Button(friday,text="OK",command=input_classes,background='#BB86FC')
    number_of_classes_ok.grid(row=0,column=2,padx=15)

    def showdata():
        ### CREATING/CONNECTING DATABASE TABLE ###
        myt1=sqlite3.connect("schedule.db")

        ### CREATE CURSOR ###
        myc1=myt1.cursor()
        
        ### fetching and printing ###
        myc1.execute("SELECT *,oid FROM mytt WHERE day = 'Friday'")
        records=myc1.fetchall()
        

        topf=Toplevel()
        topf.title("Data")
        topf.configure(bg="#191919")

        day=Label(topf,text="Day",fg="white",bg="#191919")
        day.grid(row=0,column=0)

        name=Label(topf,text="Class Name",fg="white",bg="#191919")
        name.grid(row=0,column=1)

        linkpaste=Label(topf,text="Class Link",fg="white",bg="#191919")
        linkpaste.grid(row=0,column=2)

        start_time=Label(topf,text="Starting Time",fg="white",bg="#191919")
        start_time.grid(row=0,column=3)

        end_time=Label(topf,text="Ending Time",fg="white",bg="#191919")
        end_time.grid(row=0,column=4)

        dataid=Label(topf,text="ID",fg="white",bg="#191919")
        dataid.grid(row=0,column=5)


        j=1
        for i in records:
            lab1=Label(topf,text=i[0],fg="white",bg="#191919")
            lab1.grid(row=j,column=0)
            lab2=Label(topf,text=i[1],fg="white",bg="#191919")
            lab2.grid(row=j,column=1)
            lab3=Label(topf,text=i[2],fg="white",bg="#191919")
            lab3.grid(row=j,column=2)
            lab4=Label(topf,text=str(i[3]),fg="white",bg="#191919")
            lab4.grid(row=j,column=3)
            lab5=Label(topf,text=str(i[4]),fg="white",bg="#191919")
            lab5.grid(row=j,column=4)
            lab6=Label(topf,text=str(i[5]),fg="white",bg="#191919")
            lab6.grid(row=j,column=5)
            j=j+1

        ### COMMIT CHANGES ###
        myt1.commit()

        ### CLOSE CONNECTIONS ###
        myt1.close()

    file_menu=Menu(f_menu,tearoff=0)
    f_menu.add_cascade(label="File",menu=file_menu)
    file_menu.add_command(label="Show Data",command=showdata)
    #showdatabutton=Button(friday,text="Show Data",command=showdata)
    #showdatabutton.grid(row=0,column=3)

    def delete():
        #topf2=Toplevel()
        #topf2.title("Delete entry")
        for widget in f_frame.winfo_children():
            widget.destroy()

        typeidlabel=Label(f_frame,text="Type id",fg="white",bg="#333333")
        typeidlabel.grid(row=0,column=0)
        typeid=Entry(f_frame,width=30)
        typeid.grid(row=0,column=1)
        def lastdelete():
            ### CREATING/CONNECTING DATABASE TABLE ###
            myt1=sqlite3.connect("schedule.db")

            ### CREATE CURSOR ###
            myc1=myt1.cursor()

            myc1.execute("DELETE FROM mytt WHERE oid="+typeid.get())

            typeid.delete(0,END)

            ### COMMIT CHANGES ###
            myt1.commit()

            ### CLOSE CONNECTIONS ###
            myt1.close()
            deletedone=Label(f_frame,text="DONE",fg="white",bg="#333333")
            deletedone.grid(row=2,column=0,columnspan=2)


        deletebutton=Button(f_frame,text="Delete record",command=lastdelete,bg="#BB86FC")
        deletebutton.grid(row=1,column=0,columnspan=2)

    delete_menu=Menu(f_menu,tearoff=0)
    f_menu.add_cascade(label="Delete",menu=delete_menu)
    delete_menu.add_command(label="Delete Using ID",command=delete)
    #deletedata=Button(friday,text="Delete using ID",command=delete)
    #deletedata.grid(row=0,column=4)

    def edit():
        #topf3=Toplevel()
        #topf3.title("Edit Record")
        for widget in f_frame.winfo_children():
            widget.destroy()

        enterid=Label(f_frame,text="Enter id",fg="white",bg="#333333")
        enterid.grid(row=0,column=0)
        enteridbox=Entry(f_frame,width=20)
        enteridbox.grid(row=0,column=1)

        def clicked1():

            ### CREATING/CONNECTING DATABASE TABLE ###
            myt1=sqlite3.connect("schedule.db")

            ### CREATE CURSOR ###
            myc1=myt1.cursor()

            myid=enteridbox.get()
            myc1.execute("SELECT * FROM mytt WHERE oid =" + myid)
            showthatid=myc1.fetchall()

            ### COMMIT CHANGES ###
            myt1.commit()

            ### CLOSE CONNECTIONS ###
            myt1.close()


            def save():
                ### CREATING/CONNECTING DATABASE TABLE ###
                myt1=sqlite3.connect("schedule.db")

                ### CREATE CURSOR ###
                myc1=myt1.cursor()

                myc1.execute("""UPDATE mytt SET
                            class_name=:cn,
                            class_link=:cl,
                            time_start=:ts,
                            time_final=:tf
                            WHERE oid=:oid""",
                            {
                                'cn':class_name.get(),
                                'cl':class_link.get(),
                                'ts':clickedie.get(),
                                'tf':clickedfe.get(),
                                'oid':myid
                            })

                ### COMMIT CHANGES ###
                myt1.commit()

                ### CLOSE CONNECTIONS ###
                myt1.close()

                donelabel=Label(f_frame,text="DONE !",fg="white",bg="#333333")
                donelabel.grid(row=7,column=1)


            class_name=Entry(f_frame,width=10)
            class_link=Entry(f_frame,width=30)

            clickedie=IntVar()
            droptimei=OptionMenu(f_frame,clickedie,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimei.configure(background='#191919',foreground='white')
            droptimei["menu"].config(bg="#191919",fg="white")

            clickedfe=IntVar()
            droptimef=OptionMenu(f_frame,clickedfe,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
            droptimef.configure(background='#191919',foreground='white')
            droptimef["menu"].config(bg="#191919",fg="white")
        
            class_name.grid(row=1,column=0,columnspan=1,padx=10)
            class_link.grid(row=1,column=1,columnspan=2)
            droptimei.grid(row=1,column=3)
            droptimef.grid(row=1,column=4)

            for i in showthatid:
                class_name.insert(0,i[1])
                class_link.insert(0,i[2])
                clickedie.set(i[3])
                clickedfe.set(i[4])

            savebutton=Button(f_frame,text="Save",command=save,bg="#BB86FC")
            savebutton.grid(row=6,column=1)


        okbutton1=Button(f_frame,text="OK",command=clicked1,bg="#BB86FC")
        okbutton1.grid(row=0,column=2)


    edit_menu=Menu(f_menu,tearoff=0)
    f_menu.add_cascade(label="Edit",menu=edit_menu)
    edit_menu.add_command(label="Edit Using ID",command=edit)
    #editdata=Button(friday,text="Edit using ID",command=edit)
    #editdata.grid(row=0,column=5)

    def delete_all():
        ### CREATING/CONNECTING DATABASE TABLE ###
        myt1=sqlite3.connect("schedule.db")

        ### CREATE CURSOR ###
        myc1=myt1.cursor()
        delete_day="Friday"
        myc1.execute("DELETE FROM mytt WHERE day='{}'".format(delete_day))

        ### COMMIT CHANGES ###
        myt1.commit()

        ### CLOSE CONNECTIONS ###
        myt1.close()

    delete_menu.add_command(label="Delete all in Friday",command=delete_all)





def today_schedule():
    today=Tk()
    today.title(day_now + " Schedule")
    today.configure(background='#212121')

    ### CREATING/CONNECTING DATABASE TABLE ###
    myt1=sqlite3.connect("schedule.db")

    ### CREATE CURSOR ###
    myc1=myt1.cursor()
    
    ### fetching and printing ###
    myc1.execute("SELECT * FROM mytt WHERE day = '{}'".format(day_now))
    records=myc1.fetchall()

    cn=[]
    cl=[]
    ts=[]
    te=[]
    for record in records:
        cn.append(record[1])
        cl.append(record[2])
        ts.append(record[3])
        te.append(record[4])
        #print(cn)
        #print(cl)
    
    if len(cn)==0:
        noclass=Label(today,text="NO CLASSES TODAY",font=("default",15),background='#212121',foreground='white')
        noclass.pack(padx=20,pady=20)

    new=1
    buttons=[]
    def linkexecute(a):
        webbrowser.open(cl[a],new=new)

    def runagain():
        datetimeinfo=datetime.datetime.now()
        nowhour=datetimeinfo.hour
        nowminute=datetimeinfo.minute
        nowtime=nowhour+(nowminute/60)
        
        for i in range(0,len(cn)):
            b=Button(today,text=cn[i],command=lambda i=i:linkexecute(i),padx=10,background='#BB86FC',font=("default",10,"bold"))
            b.grid(row=i,column=0,padx=20,pady=10)
            buttons.append(b)
            timelabel=Label(today,text=str(ts[i])+"-"+str(te[i]),background='#212120',foreground='white',font=("default",10,"bold"))
            timelabel.grid(row=i,column=1)

            if nowtime>=ts[i] and nowtime<te[i]:
                markerlabel=Label(today,bg="green",padx=10,pady=3)
                markerlabel.grid(row=i,column=2,padx=20)
            else:
                markerlabel1=Label(today,bg="gray",padx=10,pady=3)
                markerlabel1.grid(row=i,column=2,padx=20)

        global var
        var=today.after(20000,runagain)
    
    def quit():
        """Cancel all scheduled callbacks and quit."""
        today.after_cancel(var)
        today.destroy()

    today.protocol('WM_DELETE_WINDOW', quit)


    ### COMMIT CHANGES ###
    myt1.commit()

    ### CLOSE CONNECTIONS ###
    myt1.close()

    runagain()






def savetxt():
    text_file=open("mytext.txt",'w')
    text_file.write(my_text.get(1.0,END))

    donelabel_txt=Label(root,text="DONE",background='#212121',foreground='white')
    donelabel_txt.place(x=330,y=445)

    def update():
        donelabel_txt.config(text='')
    donelabel_txt.after(5000,update)



def savetxt_keyboard_binding(event):
    text_file=open("mytext.txt",'w')
    text_file.write(my_text.get(1.0,END))

    donelabel_txt_keyboard_bind=Label(root,text="DONE",background='#212121',foreground='white')
    donelabel_txt_keyboard_bind.place(x=330,y=445)

    def update():
        donelabel_txt_keyboard_bind.config(text='')
    donelabel_txt_keyboard_bind.after(5000,update)


def right_click_popup(event):
    right_click_menu.tk_popup(event.x_root,event.y_root)


def copytext():
    try:
        selected=my_text.selection_get()
        pyperclip.copy(selected)
    except:
        pass


def pastetext():
    input_text=pyperclip.paste()
    position=my_text.index(INSERT)
    my_text.insert(position,input_text)



def gotolink():
    try:
        selected_link=my_text.selection_get()
        n=1
        url_text=str(selected_link)
        webbrowser.open(url_text,new=n)
    except:
        pass


def bold_text():
    bold_font=font.Font(my_text,my_text.cget("font"))
    bold_font.configure(weight="bold")
    my_text.tag_configure("bold",font=bold_font)

    current_tags=my_text.tag_names("sel.first")
    if "bold" in current_tags:
        my_text.tag_remove("bold","sel.first","sel.last")
    else:
        my_text.tag_add("bold","sel.first","sel.last")


def overstrike_text():
    strike_font=font.Font(my_text,my_text.cget("font"))
    strike_font.configure(slant="italic",overstrike=1)
    my_text.tag_configure("strike",font=strike_font)

    current_tags=my_text.tag_names("sel.first")
    if "strike" in current_tags:
        my_text.tag_remove("strike","sel.first","sel.last")
    else:
        my_text.tag_add("strike","sel.first","sel.last")




### CREATE TT BUTTON ###
creatett_m=Button(root,text="Timetable for Monday",pady=10,command=create_a_tt_m,padx=10,background='#03DAC6',foreground='black',font=("default",9,"bold"))
creatett_m.place(x=10,y=10)

### CREATE TT BUTTON ###
creatett_t=Button(root,text="Timetable for Tuesday",pady=10,command=create_a_tt_t,padx=5,background='#03DAC6',foreground='black',font=("default",9,"bold"))
creatett_t.place(x=259,y=10)

### CREATE TT BUTTON ###
creatett_w=Button(root,text="Timetable for Wednesday",pady=10,command=create_a_tt_w,padx=3,background='#03DAC6',foreground='black',font=("default",9,"bold"))
creatett_w.place(x=10,y=60)

### CREATE TT BUTTON ###
creatett_th=Button(root,text="Timetable for Thursday",pady=10,command=create_a_tt_th,padx=2,background='#03DAC6',foreground='black',font=("default",9,"bold"))
creatett_th.place(x=259,y=60)

### CREATE TT BUTTON ###
creatett_f=Button(root,text="Timetable for Friday",padx=10,pady=10,command=create_a_tt_f,background='#03DAC6',foreground='black',font=("default",9,"bold"))
creatett_f.place(x=10,y=110)

### RUN BUTTON ###
run=Button(root,text="Run",padx=5,pady=5,command=today_schedule,bg="#33f180",font=("default",11,"bold"))
run.place(x=188,y=20)



myframe=Frame(root)

scroll_y=Scrollbar(myframe)
scroll_y.pack(side=RIGHT,fill=Y)

### TEXT BOX ###
my_text=Text(myframe,width=47,height=16,font=("default",11),border=2,fg="#000000",yscrollcommand=scroll_y.set,background='black',foreground='white')
my_text.configure(insertbackground='white')
my_text.pack()  

scroll_y.config(command=my_text.yview)

### CONFIGURING OUR TEXT BOX ###
text_file=open("mytext.txt",'r')
stuff=text_file.read()

my_text.insert(END,stuff)
text_file.close()

myframe.place(x=10,y=160)

### SAVE BUTTON FOR OUR TEXT ###
savetxtbutton=Button(root,text="SAVE",command=savetxt,background='#BB86FC',font=('default',9,'bold'))
savetxtbutton.place(x=187,y=440)


root.bind("<Control_L><s>",savetxt_keyboard_binding)
root.bind("<Control_R><s>",savetxt_keyboard_binding)



my_menu=Menu(root,tearoff=0)
root.config(menu=my_menu)

file_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Save",command=savetxt)
file_menu.add_command(label="Exit",command=root.quit)

day_list=["Monday","Tuesday","Wednesday","Thursday","Friday"]
def delete_tt():
    for i in day_list:
        ### CREATING/CONNECTING DATABASE TABLE ###
        myt1=sqlite3.connect("schedule.db")

        ### CREATE CURSOR ###
        myc1=myt1.cursor()
        myc1.execute("DELETE FROM mytt WHERE day='{}'".format(i))

        ### COMMIT CHANGES ###
        myt1.commit()

        ### CLOSE CONNECTIONS ###
        myt1.close()


delete_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Delete",menu=delete_menu)
delete_menu.add_command(label="Delete my timetable",command=delete_tt)


right_click_menu=Menu(myframe,tearoff=False)

right_click_menu.add_command(label="Copy",command=copytext)
right_click_menu.add_command(label="Paste",command=pastetext)
right_click_menu.add_command(label="Go To",command=gotolink)
right_click_menu.add_separator()
right_click_menu.add_command(label="Bold",command=bold_text)
right_click_menu.add_command(label="Overstrike",command=overstrike_text)
my_text.bind("<Button-3>",right_click_popup)







def credentials():
    creds=Toplevel()
    creds.title("Credentials")
    creds.geometry("280x100")
    creds.configure(background='#212121')

    gmail=Label(creds,text="Gmail id",fg="white",background="#333333")
    gmail.place(x=0,y=10)
    gmail_entry=Entry(creds,width=30)
    gmail_entry.place(x=90,y=10)
    password=Label(creds,text="Gmail Password",fg="white",background="#333333")
    password.place(x=0,y=40)
    password_entry=Entry(creds,show="\u2022",width=30)
    password_entry.place(x=90,y=40)

    creds_menu=Menu(creds,tearoff=0)
    creds.config(menu=creds_menu)


    def save_creds():
        ### CREATING/CONNECTING DATABASE TABLE ###
        myt1=sqlite3.connect("schedule.db")

        ### CREATE CURSOR ###
        myc1=myt1.cursor()

        ### CREATE TABLE ###
        myc1.execute("""CREATE TABLE IF NOT EXISTS mycreds(mail_id TEXT,password TEXT)""")

        ### INSERTING ENETERED DATA INTO TABLE ###
        myc1.execute("INSERT INTO mycreds VALUES (:m,:p)",
                    {
                        'm':gmail_entry.get(),
                        'p':password_entry.get()
                    })

        ### COMMIT CHANGES ###
        myt1.commit()

        ### CLOSE CONNECTIONS ###
        myt1.close()


        gmail_entry.delete(0,END)
        password_entry.delete(0,END)

    save_creds_btn=Button(creds,text="Save",command=save_creds,padx=10,background='#BB86FC',font=("default",10,"bold"))
    save_creds_btn.place(x=120,y=65)


    def delete_creds():
        ### CREATING/CONNECTING DATABASE TABLE ###
        myt1=sqlite3.connect("schedule.db")

        ### CREATE CURSOR ###
        myc1=myt1.cursor()
        myc1.execute("DELETE FROM mycreds")

        ### COMMIT CHANGES ###
        myt1.commit()

        ### CLOSE CONNECTIONS ###
        myt1.close()

    delete_menu=Menu(creds_menu,tearoff=0)
    creds_menu.add_cascade(label="Delete",menu=delete_menu)
    delete_menu.add_command(label="Delete creds",command=delete_creds)


    




### Credentials Button ###
credentials_btn=Button(root,text="Credentials",command=credentials,padx=5,pady=8,background='#03DAC6',foreground='black',font=("default",9,"bold"))
credentials_btn.place(x=288,y=110)

### AUTOMATE BUTTON ###
automate_btn=Button(root,text="AUTO",command=clickme,padx=4,pady=5,bg="#ff5959",font=("default",11,"bold"))
automate_btn.place(x=184,y=90)



root.mainloop()