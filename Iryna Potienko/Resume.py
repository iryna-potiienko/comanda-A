from tkinter import *
root=Tk()

lab=Label(root,text='Резюме',font="Arial 18",fg='blue')
la=Label(root,text='Особисті дані',font='Calibri 14',fg='green')
labe=Label(root,text='ПІБ')
ent=Entry(root,width=80)
labe1=Label(root,text='Дата народження:')
ent1=Entry(root)
labe2=Label(root,text='Місце проживання (адреса):')
ent2=Entry(root,width=80)
lab1=Label(root,text='Сімейний стан:')
var=IntVar()
var.set(0)
rad0=Radiobutton(root,text='Одружений',variable=var,value=0)
rad1=Radiobutton(root,text='Неодружений', variable=var,value=1)
labe3=Label(root,text='Контактний телефон:')
ent3=Entry(root)
labe4=Label(root,text='e-mail')
ent4=Entry(root)
labe5=Label(root,text='Посада:')
ent5=Entry(root,width=80)
lab3=Label(root,text='Мета',font='Calibri 14', fg='green')
lab2=Label(root,text='Опишіть мету отримання посади та пошуку роботи.')
tex=Text(root,width=80,height=2,wrap=WORD)
lab4=Label(root,text='Досвід роботи',font='Calibri 14',fg='green')
labe6=Label(root,text='Назва компанії, посада, період роботи:')
ent6=Text(root,wrap=WORD,width=80,height=3)
lab5=Label(root,text='Освіта',font='Calibri 14',fg='green')
labe7=Label(root,text='Навчальний заклад, ступінь, спеціальність, період навчання')
tex2=Text(root,width=80,height=4,wrap=WORD)
lab6=Label(root,text='Додаткова інформація',font='Calibri 14',fg='green')
labe8=Label(root,text='Особисті якості, рекомендації')
ent7=Text(root,width=80,height=2,wrap=WORD)
c1=IntVar()
c2=IntVar()
c1=Checkbutton(root,text='Водійські права')
c2=Checkbutton(root,text='Закордонний паспорт')
but=Button(root,text='Надіслати резюме',bg='lightgreen',font='13')

lab.pack()
la.pack()
labe.pack()
ent.pack()
labe1.pack()
ent1.pack()
labe2.pack()
ent2.pack()
lab1.pack()
rad0.pack()
rad1.pack()
labe3.pack()
ent3.pack()
labe4.pack()
ent4.pack()
labe5.pack()
ent5.pack()
lab3.pack()
lab2.pack()
tex.pack()
lab4.pack()
labe6.pack()
ent6.pack()
lab5.pack()
labe7.pack()
tex2.pack()
lab6.pack()
labe8.pack()
ent7.pack()
c1.pack()
c2.pack()
but.pack()

root.mainloop()