import os
import smtplib
from random import randint


sender = '' #Adresse mail de l'envoyeur
pw = '' #Mot de passe de cette adresse mail


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, pw)
message = 'Ho ! Ho ! Ho ! Ton secret receiver est '

def confirmation(rep):
    rep = rep.lower()
    return rep == 'non' or rep == 'n'

def dico_create(mail_list):
    '''
    Prends en paramètre la liste des mails.
    Organise en dictionnaire.
    Retourne un dictionnaire de mails
    '''
    a = len(mail_list)
    j = 0
    dico_mail = {}
    # Création dico
    while j < a:
        dico_mail[mail_list[j]] = ''
        j += 1
    return dico_mail

rep  = True
while rep: #input de la liste de mails    
    mail_list = input('Entrez la liste des e-mails séparés d\'une virgule et un espace: ')
    print(mail_list)
    print('--------------------------------------------------------------')
    reponse = input('Confirmer ? (o/n)')
    rep = confirmation(reponse)


print('**************************************************')
mail_list = mail_list.split(', ') #sépare les mails et créé un tableau
mail_dico = dico_create(mail_list) #créé le dictionnaire à partir du tableau

i = 0
n = len(mail_list)

while i < n:
    keys = list(mail_dico.keys()) 
    values = list(mail_dico.values())
    receiver = mail_list[i]
    msg = message
    nb = randint(0, n - 1)
    while i == nb  or values[nb] == mail_list[i] or mail_list[nb] in values: #Le receveur ne doit pas avoir déjà une adresse associé ou avoir comme receveur son envoyeur
        nb = randint(0, n - 1) #Choisit un mail au hasard
    msg += mail_list[nb]
    mail_dico[mail_list[i]] = mail_list[nb]
    server.sendmail(sender, receiver, msg) #Envoie le mail
    i += 1
server.quit()

print('Félicitations ! Les mails ont été envoyé aux adresses aléatoirement.\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n\tJoyeux Noël !\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*')

os.system('pause')