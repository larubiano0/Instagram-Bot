from instabot import Bot
import random
import csv
import config as cf
import sys

###################################### HELPER FUNCTIONS ######################################
def listLoad(archivo):
    file = []
    dialect = csv.excel()
    dialect.delimiter=","
    print(cf.data_dir)
    with open(cf.data_dir + archivo, encoding="utf-8") as csvfile:
        input_file = csv.DictReader(csvfile,dialect=dialect)
        for element in input_file:
            file.append(element)
    return file

def printMenu():
    print("\n"*5 +"Bienvenido")
    print("0- Salir")
    print("1- Login")
    print("2- Mandar mensaje")
    print("3- Subir historias con las fotos en la carpeta fotos")
    print("\n")
##############################################################################################

###################################### SETUP #################################################
login = "login.csv"
bot = Bot(max_follows_per_day=173, max_unfollows_per_day=181, 
              max_followers_to_follow=2500, min_followers_to_follow=100,
              follow_delay=random.randint(300, 600), unfollow_delay=random.randint(300, 600))
credentials = listLoad(login)[0]
##############################################################################################

###################################### MENU PRINCIPAL #################################################

while True:
    printMenu()
    inputs = int(input('Seleccione una opción para continuar\n\n'))
    if inputs == 1:
        bot.login(username = credentials["username"], password = credentials["password"])
    elif inputs == 2:
        mensaje = input("Ponga su mensaje: ")
        usuario = input("Escriba a quien le quiere mandar el mensaje: ")
        bot.send_message(mensaje,[usuario])
    else:
        bot.logout()
        sys.exit(0)



#######################################################################################################