from instabot import Bot
import random
import csv
import config as cf

###################################### HELPER FUNCTIONS ######################################
def listLoad(archivo):
    file = []
    dialect = csv.excel()
    dialect.delimiter=","
    with open(cf.data_dir + archivo, encoding="utf-8") as csvfile:
        input_file = csv.DictReader(csvfile,dialect=dialect)
        for element in input_file:
            file.append(element)
    return file    
##############################################################################################

###################################### SETUP #################################################
login = "login.csv"
bot = Bot(max_follows_per_day=173, max_unfollows_per_day=181, 
              max_followers_to_follow=2500, min_followers_to_follow=100,
              follow_delay=random.randint(300, 600), unfollow_delay=random.randint(300, 600))
credentials = listLoad(login)[0]
##############################################################################################

bot.login(username = credentials["username"], password = credentials["password"])

