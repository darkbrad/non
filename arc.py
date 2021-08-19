import os
import csv
import telebot
bot = telebot.TeleBot('1944929243:AAF0JWnh7DHHGnPETjHzKP-FFXCBVjEAXAc')

dire='C:/Users/fdm19/Downloads/машины'
filelist=os.listdir(dire)
print(filelist)
@bot.message_handler(content_types=['text'])
def start_command(message):

    if message.text=='/start':
        bot.send_message(message.chat.id, "Send car number")
    elif type(message.text)==str:
        bot.send_message( message.chat.id, " Pls wait for answer" )
        counter=0
        for i in filelist:
            with open( "C:/Users/fdm19/Downloads/машины/" + i, encoding='utf-8', newline='' ) as o:
                myData = csv.reader( o )

                for row1 in myData:
                    if len( row1 ) == 1:
                        a = row1[0].split( ';' )
                    elif len( row1 ) == 2:
                        b = row1[1].split( ';' )
                        c = row1[0].split( ';' )
                        c[3] = c[3] + b[0]
                        b = b[1:len( b )]
                        a = c + b
                    if message.text in a:
                        for elem in a:
                            print( elem, end=' ' )
                            bot.send_message( message.chat.id, elem )
                            print( a )

                            print( myData.line_num )
                    counter=counter+1
                if counter==10984257:
                    bot.send_message( message.chat.id, "The search has not given any results" )

bot.polling()