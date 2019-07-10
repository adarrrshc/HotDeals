
# -*- coding: utf-8 -*-
import requests
from telegram.ext import Updater,CommandHandler
import json
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup 
from bs4 import BeautifulSoup
import datetime
import random


global bot_token
global updater
global dispatcher
global jq
global admin_id
global sub_job_check

sub_job_check=0


bot_token=''
updater=Updater(token='')
dispatcher = updater.dispatcher
jq = updater.job_queue
admin_id=00000000


hd_text=""
up_text=""




def init_bknd():
    global hd_text
    global up_text
    #HD  'fashion','tech','dailyneeds  , mobile , accessories , laptop   bonus 

    

    global category
    category="tech"
    #mobile,fashion,accessories,dailyneeds,laptop,tech

    url=""
    res=requests.get(url)
    json_data = json.loads(res.text)

    global dealsList
    dealsList=[]

    for i in range(len(json_data)):
        dealName=json_data[i]['name'].replace("[","-").replace("]","-")
        dealLink=json_data[i]['DealLink']['url']
        dealImageUrl=json_data[i]['featuredImage']
        dealCategory=json_data[i]['category']
        try:
            dealPrice=str(json_data[i]['price'])
            dealOldPrice=str(json_data[i]['oldPrice'])
            dealPercent=" -"+str(int((float(dealPrice)/float(dealOldPrice))*100))+"% off"
        except:
            dealPrice=""
            dealOldPrice=""
            dealPercent=""
    
        #print(dealPrice)
        finalDeal=str(i+1) + "." + "[" + dealName +dealPercent + "]" + "(" + dealLink + ")"
        dealsList.append(finalDeal)
        #print("\n\n"+dealName+"\n"+dealLink+"\n"+dealImageUrl+"\n"+dealCategory+"\n"+dealPrice+"\n"+dealOldPrice+"\n"+dealPercent+"\n\n")
    #print(dealsList)


    
    hd_text="*HOT DEALS*\n"
    for i in dealsList:
        hd_text=hd_text+i+"\n\n"
    hd_text=hd_text+"@hotdealsbot"




def fetchDeals():
    global category
    global hd_text
    #mobile,fashion,accessories,dailyneeds,laptop,tech

    url=""
    res=requests.get(url)
    json_data = json.loads(res.text)

    global dealsList
    dealsList=[]

    for i in range(len(json_data)):
        dealName=json_data[i]['name'].replace("[","-").replace("]","-")
        dealLink=json_data[i]['DealLink']['url']
        dealImageUrl=json_data[i]['featuredImage']
        dealCategory=json_data[i]['category']
        try:
            dealPrice=str(json_data[i]['price'])
            dealOldPrice=str(json_data[i]['oldPrice'])
            dealPercent=" -"+str(int((float(dealPrice)/float(dealOldPrice))*100))+"% off"
        except:
            dealPrice=""
            dealOldPrice=""
            dealPercent=""
    
        #print(dealPrice)
        finalDeal=str(i+1) + "." + "[" + dealName +dealPercent + "]" + "(" + dealLink + ")"
        dealsList.append(finalDeal)
        #print("\n\n"+dealName+"\n"+dealLink+"\n"+dealImageUrl+"\n"+dealCategory+"\n"+dealPrice+"\n"+dealOldPrice+"\n"+dealPercent+"\n\n")

    #print(dealsList)
    hd_text="*HOT DEALS IN "+category.upper()+"*\n"
    for i in dealsList:
        hd_text=hd_text+i+"\n\n"
    hd_text=hd_text+"@hotdealsbot"
    







def start(bot, update):
    global user_data
    flag=0
    for ud in user_data:
        if(int(ud[0])==update.message.chat_id):
            flag=1
            break
    if(flag==0):
        user_data.append([update.message.chat_id])
                                    #userid     HD  'fashion','tech','dailyneeds  , mobile , accessories , laptop   bonus                
    print("inside start\n")
    bot.send_message(chat_id=update.message.chat_id, text="*Iam the Hottest Bot in Town!*",parse_mode='Markdown')

    bot.send_message(chat_id=update.message.chat_id, text="Choose Option.", reply_markup=ReplyKeyboardMarkup(keyboard=[  ["/HotDeals"],["/Category"],["/Bonus"] ] ),one_time_keyboard=False)





         
                 


def choose_option_bknd(bot,update):
    global hd_text
    global up_text
    global category

    bot.send_message(chat_id=admin_id, text="Bump!\n"+update.message.text+"\n*"+str(update.message.from_user.full_name)+"*\n@"+str(update.message.from_user.username),parse_mode='Markdown', disable_web_page_preview=True)
    
    if((update.message.text).lower()=="/hotdeals"):
        fetchDeals()

        bot.send_message(chat_id=update.message.chat_id,text=hd_text,parse_mode='Markdown', disable_web_page_preview=True)

    elif((update.message.text).lower()=="/category"):                                                                                             
        #mobile,fashion,accessories,dailyneeds,laptop,tech
        bot.send_message(chat_id=update.message.chat_id, text="Choose Category.", reply_markup=ReplyKeyboardMarkup(keyboard=[  ["/tech"],["/fashion"],["/accessories"],["/dailyneeds"],["/laptop"],["/mobile"] ] ),one_time_keyboard=False)
        

    elif((update.message.text).lower()=="/bonus"):
        bot.send_message(chat_id=update.message.chat_id,text="*BONUS*\n@jugaadlife -Best Loots and Deals\n@GooUrlBot -ShortLink-shorten your links\n@driveuploadbot -Google Drive Uploader\n@fakemailbot -for fake mail\n@uploadbot -upload remote files to telegram\n\n@hotdealsbot",parse_mode='Markdown', disable_web_page_preview=True)
    
        
def categoryChooser(bot,update):
    global category
    global hd_text
   

    if((update.message.text).lower()=="/tech"):

        category="tech"
        bot.send_message(chat_id=update.message.chat_id, text="Selected "+category+"!")

    elif((update.message.text).lower()=="/fashion"):

        category="fashion"
        bot.send_message(chat_id=update.message.chat_id, text="Selected "+category+"!")
    elif((update.message.text).lower()=="/accessories"):

        category="accessories"    
        bot.send_message(chat_id=update.message.chat_id, text="Selected "+category+"!")
    elif((update.message.text).lower()=="/dailyneeds"):

        category="dailyneeds"       
        bot.send_message(chat_id=update.message.chat_id, text="Selected "+category+"!")
    elif((update.message.text).lower()=="/laptop"):

        category="laptop" 
        bot.send_message(chat_id=update.message.chat_id, text="Selected "+category+"!")
    elif((update.message.text).lower()=="/mobile"):

        category="mobile"       
        bot.send_message(chat_id=update.message.chat_id, text="Selected "+category+"!")
    
    fetchDeals()
    bot.send_message(chat_id=update.message.chat_id,text=hd_text,parse_mode='Markdown', disable_web_page_preview=True)
    bot.send_message(chat_id=update.message.chat_id, text="Choose Option.", reply_markup=ReplyKeyboardMarkup(keyboard=[  ["/HotDeals"],["/Category"],["/Bonus"] ] ),one_time_keyboard=False)







def stoprepeatpost(bot,update,job_queue):
    global sub_job
    global sub_job_check
    sub_job_check=0
    print("killed")
    bot.send_message(chat_id=admin_id,text="killed",parse_mode='Markdown', disable_web_page_preview=True)
    sub_job.schedule_removal()
    

def repeatpost(bot,update):
    global sub_job
    timeinseconds=0.5*60*60
    sub_job=jq.run_repeating(telegram_scraper, interval=timeinseconds, first=0,context=update.message.chat_id)



def sub_job_checker(bot,update):
    global sub_job_check
    global admin_id
    print("subjobchecker")

    if(sub_job_check==0):
        bot.send_message(chat_id=admin_id,text="NOT RUNNING ---",parse_mode='Markdown', disable_web_page_preview=True)
    elif(sub_job_check==1):
        bot.send_message(chat_id=admin_id,text="RUNNING SMOOTH +++",parse_mode='Markdown', disable_web_page_preview=True)




global oldDeal
oldDeal=""

def telegram_scraper(bot,update):
    global oldDeal
    global sub_job_check
    sub_job_check=1

    
    
    #print(catchy_terms[0])
    a=datetime.datetime.now()
    hour=int(str(a.time()).split(":")[0])
    print("\n\nHour:"+str(hour))
    if(hour>=1 and hour<=18):
    #if(hour>=1 and hour<=24):
        print("TIME TO POST()")
        try:
            
            url="https"

            #tgme_widget_message_wrap js-widget_message_wrap
            r=requests.get(url)

            soup = BeautifulSoup(r.text.replace("<br/>","\n"), 'html.parser')
            non_link_text=""
            shortened_link=""
            full_text=""
            try:
                mydivs2 = soup.select("div.tgme_widget_message_text")
                i=mydivs2[-1]
                try:
                    link=i.select("a")[0]["href"]
                    full_text=i.text
                    non_link_text=full_text.replace(link,"Link below")
                    #print("unredirecting\n")
                    unredirected_link=requests.get(link).url
                except Exception as e:
                    print(e)
                    link=""
                    non_link_text=i.get_text()
                    unredirected_link=""
            except Exception as e:
                print(e)
                print("not a text deal!")

            finalDeal = non_link_text.replace("Link below",unredirected_link)
            #finalDeal = percentage+title + "\n\n" +  str(real_link)

            if(oldDeal!=finalDeal and (non_link_text!="" or shortened_link!="")):
                print("posting from TelegramChannel")
                finalDeall=finalDeal
                bot.send_message(chat_id=admin_id,text="Posting on channel from IHDeals😍",parse_mode='HTML', disable_web_page_preview=True)
                #bot.send_message(chat_id="@bot_test00",text=finalDeall,parse_mode="HTML", disable_web_page_preview=False)
                bot.send_message(chat_id="@jugaadlife",text=finalDeall,parse_mode="HTML", disable_web_page_preview=False)
            else:
                print("IHDeals out of deals")
                lootalert(bot,update)
                # oldDeal=finalDeal
                # postonchannel(bot,update)
            oldDeal=finalDeal
        except Exception as e:
            bot.send_message(chat_id=admin_id,text="Exception @ Telegram scraper\n"+str(e),parse_mode='Markdown', disable_web_page_preview=True)
            print(e)
    else:
        print("Early morning,People sleep")
        bot.send_message(chat_id=admin_id,text="Early morning,ppl sleep",parse_mode='Markdown', disable_web_page_preview=True)


global oldDealLootaltert
oldDealLootaltert=""


def lootalert(bot,update):
    global oldDealLootaltert
    
    
    print("\n\nTIME TO POST(Lootalert)")
    try:
        url = ""
        res = requests.get(url)
        json_data = json.loads(res.text)
        i = 0
        dealName = json_data[i]['name']
        dealLink = json_data[i]['DealLink']['url']
        dealImageUrl = json_data[i]['featuredImage']
        dealCategory = json_data[i]['category']
        try:
            dealPrice = str(json_data[i]['price'])
            dealOldPrice = str(json_data[i]['oldPrice'])
            dealPercent = str(int(((float(dealOldPrice)-float(dealPrice))/float(dealOldPrice))*100))+"% off -"
        except:
            dealPrice = ""
            dealOldPrice = ""
            dealPercent = ""

        # print(dealPrice)


        finalDeal = dealPercent+dealName + "\n\n" + str(dealLink)

   

        if(oldDealLootaltert!=finalDeal):
            print("posting from lootalert")
            finalDeall=finalDeal
            bot.send_message(chat_id=admin_id,text="Posting on channel from lootalert⚡️",parse_mode='Markdown', disable_web_page_preview=True)
            #bot.send_message(chat_id="@bot_test00",text=finalDeall,parse_mode="HTML", disable_web_page_preview=False)
            bot.send_message(chat_id="@jugaadlife",text=finalDeall,parse_mode="HTML", disable_web_page_preview=False)
        else:
            print("lootalert out of deals")
            bot.send_message(chat_id=admin_id,text="No new Deals",parse_mode='Markdown', disable_web_page_preview=True)
            # oldDeal=finalDeal
            # postonchannel(bot,update)
        oldDealLootaltert=finalDeal
    except Exception as e:
        print(e)
        bot.send_message(chat_id=admin_id,text="Exception @ Lootalert\n"+str(e),parse_mode='Markdown', disable_web_page_preview=True)
    








def generate(bot,update,args):

    category_dict={
        "1":"tech",
        "2":"fashion",
        "3":"accessories",
        "4":"dailyneeds",
        "5":"laptop",
        "6":"mobile"
    }
    print("insideGen")
    num=int(args[1])-1
    print(num)
    try:
        category=str(category_dict[str(args[0])])
    except:
        category="tech"
    #mobile,fashion,accessories,dailyneeds,laptop,tech
    print(category)
    url=""
    res=requests.get(url)
    json_data = json.loads(res.text)

    global dealsList
    dealsList=[]
    for i in range(len(json_data)):
        if(int(num)==int(i)):
            print("inside",i)
            dealName=json_data[i]['name'].replace("/","")
            dealLink=json_data[i]['DealLink']['url']
            dealLinkBKP=dealLink
            
                
            dealImageUrl=json_data[i]['featuredImage']
            dealCategory=json_data[i]['category']
            try:
                if(int(args[2])==1):
                    oxideallink=""
                    res=requests.get(oxideallink)
                    dealLink=res.text
                    dealPrice=str(json_data[i]['price'])
                    dealOldPrice=str(json_data[i]['oldPrice'])
                    print(dealPrice," : ",dealOldPrice)
                    dealPercent=str(int((float(dealPrice)/float(dealOldPrice))*100))+"% off-"
                
            except Exception as e:
                print(e)
                dealPrice=""
                dealOldPrice=""
                dealPercent=""

            try:
                finalDeal=str(dealPercent+dealName+"\n\n")
                finalDealLink="["+dealLinkBKP+"]("+dealLink+")"
            except Exception as e:
                print(e)
                finalDeal=dealPercent+dealName+"\n\n"
                finalDealLink=dealLinkBKP
            #print("\n\n"+dealName+"\n"+dealLink+"\n"+dealImageUrl+"\n"+dealCategory+"\n"+dealPrice+"\n"+dealOldPrice+"\n"+dealPercent+"\n\n")

    print(finalDeal)
    bot.send_message(chat_id=update.message.chat_id, text=finalDeal+ finalDealLink,parse_mode="HTML")
    # #print(dealsList)
    # hd_text="*HOT DEALS IN "+category.upper()+"*\n"
    # for i in dealsList:
    #     hd_text=hd_text+i+"\n\n"
    # hd_text=hd_text+"@hotdealsbot"





#handlers
start_handler = CommandHandler('start', start)



#dispatchers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(CommandHandler(["HotDeals","UpcomingDeals","Bonus",'hotdeals','upcomingdeals','bonus', 'category'],choose_option_bknd))
dispatcher.add_handler(CommandHandler(['fashion','tech','dailyneeds','mobile','accessories','laptop'],categoryChooser))


dispatcher.add_handler(CommandHandler("repeatpost",repeatpost))
dispatcher.add_handler(CommandHandler("generate",generate,pass_args=True))
dispatcher.add_handler(CommandHandler("stoprepeatpost",stoprepeatpost,pass_job_queue=True))
dispatcher.add_handler(CommandHandler("subjobchecker",sub_job_checker))



updater.start_polling()

if __name__ == "__main__":
    init_bknd()
    try:
        sub_job_check=1
        timeinseconds=0.3*60*60

        sub_job=jq.run_repeating(telegram_scraper, interval=timeinseconds, first=0)
        updater.bot.send_message(chat_id=admin_id, text="Bot Started,Repeat Post Started!",parse_mode="Markdown")
        print("started")
    except Exception as e:
        print(e)


    



