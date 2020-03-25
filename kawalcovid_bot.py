#!/usr/bin/env python
import logging
import telegram
import requests
import json
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

reply_keyboard = [['INFO', 'GEJALA', 'TIPS'],
                  ['POSITIF', 'SEMBUH', 'MENINGGAL']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

reply_keyboard2 = [['MENU'],['SELESAI']]
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=True)

def facts_to_str(user_data):
    facts = list()

    for key, value in user_data.items():
        facts.append('{} - {}'.format(key, value))

    return "\n".join(facts).join(['\n', '\n'])


def start(update, context):
    update.message.reply_text(
        "Halo kak, saya *kawalcovid_bot*. "
        "Saya robot yang menyajikan informasi terkait perkembangan terbaru Covid-19.",
        reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)

    update.message.reply_text(
        "Pilih informasi yang kakak ingin tau\n"
        "*INFO* --> Informasi umum tentang Covid-19\n"
        "*GEJALA* --> Informasi Gejala Covid-19\n"
	"*TIPS* --> Informasi Tips Pencegahan Covid-19\n"
        "*POSITIF* --> Informasi Pasien Positif Corona :(\n"
        "*SEMBUH* --> Informasi Pasien Corona yang Sudah Sembuh :)\n"
        "*MENINGGAL* --> Informasi Pasien Corona yang Sudah Meninggal :'(\n"
        "Pilih salah satu menu diatas dengan klik tombol yang sudah saya sediakan, atau kakak juga bisa ketik sendiri jika ingin.\n\n"
        "Saya *kawalcovid_bot* siap membantu. ",
        reply_markup=markup,parse_mode=telegram.ParseMode.MARKDOWN)
        
    return CHOOSING


def regular_choice(update, context):
    x = update.message.text.upper()
    context.user_data['choice'] = x
    if x == 'POSITIF':
        try:
            r = requests.get('https://api.kawalcorona.com/indonesia/')
            data = json.loads(r.content)
            positif = data[0]['positif']
            update.message.reply_text("Total Positif Corona di Indonesia :* {} *".format(positif)+
            "\n\nSudah banyak yang positif kak :(\nUntuk informasi sebaran corona lengkapnya bisa cek di web ini ya kak https://kawalcorona.com/ \n\nKlik *MENU* untuk mendapatkan informasi lainnya, atau klik *SELESAI* jika sudah cukup.",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)

        except:
            update.message.reply_text(
                "Untuk informasi sebaran corona lengkapnya bisa cek di web ini ya kak https://kawalcorona.com/ \n\nKlik *MENU* untuk mendapatkan informasi lainnya, atau klik *SELESAI* jika sudah cukup.",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'INFO':
        update.message.reply_text(
            "Virus Corona (Covid-19) adalah jenis baru dari coronavirus yang menular ke manusia. Virus ini bisa menyerang siapa saja, baik bayi, anak-anak, orang dewasa, lansia, ibu hamil, maupun ibu menyusui. \n\n" 
            "Infeksi virus ini disebut COVID-19 dan pertama kali ditemukan di kota Wuhan, Cina, pada akhir Desember 2019. Virus ini menular dengan cepat dan telah menyebar ke wilayah lain di Cina dan ke beberapa negara, termasuk Indonesia. \n\n"
            "Coronavirus adalah kumpulan virus yang bisa menginfeksi sistem pernapasan. Pada banyak kasus, virus ini hanya menyebabkan infeksi pernapasan ringan, seperti flu. Namun, virus ini juga bisa menyebabkan infeksi pernapasan berat, seperti infeksi paru-paru (pneumonia), Middle-East Respiratory Syndrome (MERS), dan Severe Acute Respiratory Syndrome (SARS). \n\n"

            "Sumber : https://www.alodokter.com/virus-corona \n\nKlik *MENU* untuk mendapatkan informasi lainnya, atau klik *SELESAI* jika sudah cukup.",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'GEJALA':
        update.message.reply_text(
            "Infeksi virus Corona atau COVID-19 bisa menyebabkan penderitanya mengalami gejala flu, seperti demam, pilek, batuk, sakit tenggorokan, dan sakit kepala; atau gejala penyakit infeksi pernapasan berat, seperti demam tinggi, batuk berdahak bahkan berdarah, sesak napas, dan nyeri dada.  \n\n Namun, secara umum ada 3 gejala umum yang bisa menandakan seseorang terinfeksi virus Corona, yaitu: \n"
            " - Demam (suhu tubuh di atas 38 derajat Celcius)  \n"
            " - Batuk  \n"
            " - Sesak nafas  \n\n"
            "Menurut penelitian, gejala COVID-19 muncul dalam waktu 2 hari sampai 2 minggu setelah terpapar virus Corona. \n\n"
            "Sumber : https://www.alodokter.com/virus-corona \n\nKlik *MENU* untuk mendapatkan informasi lainnya, atau klik *SELESAI* jika sudah cukup.",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'TIPS':
        update.message.reply_text(
            "Sampai saat ini, belum ada vaksin untuk mencegah infeksi virus Corona atau COVID-19. Oleh sebab itu, cara pencegahan yang terbaik adalah dengan menghindari faktor-faktor yang bisa menyebabkan Anda terinfeksi virus ini, yaitu: \n"
            "- Hindari bepergian ke tempat-tempat umum yang ramai pengunjung (social distancing).\n"
            "- Gunakan masker saat beraktivitas di tempat umum atau keramaian. \n"
            "- Rutin mencuci tangan dengan air dan sabun atau hand sanitizer yang mengandung alkohol minimal 60% setelah beraktivitas di luar rumah atau di tempat umum. \n"
            "- Jangan menyentuh mata, mulut, dan hidung sebelum mencuci tangan. \n"
            "- Hindari kontak dengan hewan, terutama hewan liar. Bila terjadi kontak dengan hewan, cuci tangan setelahnya. \n"
            "- Masak daging sampai benar-benar matang sebelum dikonsumsi.\n"
            "- Tutup mulut dan hidung dengan tisu saat batuk atau bersin, kemudian buang tisu ke tempat sampah.\n"
            "- Hindari berdekatan dengan orang yang sedang sakit demam, batuk, atau pilek.\n"
            "- Jaga kebersihan benda yang sering disentuh dan kebersihan lingkungan.\n"
            "Sumber : https://www.alodokter.com/virus-corona \n\nKlik *MENU* untuk mendapatkan informasi lainnya, atau klik *SELESAI* jika sudah cukup.",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'SEMBUH':
        try:
            r = requests.get('https://api.kawalcorona.com/indonesia/')
            data = json.loads(r.content)
            sembuh = data[0]['sembuh']
            update.message.reply_text("Total Pasien Corona yang Sudah Sembuh di Indonesia :* {} *".format(sembuh)+
            "\n\nAlhamdulillah.. Sudah banyak yang sembuh kak, mari kita support tenaga medis untuk menyelamatkan pasien lainnya :)\nUntuk informasi sebaran corona lengkapnya bisa cek di web ini ya kak https://kawalcorona.com/ \n\nKlik *MENU* untuk mendapatkan informasi lainnya, atau klik *SELESAI* jika sudah cukup.",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)

        except:
            update.message.reply_text(
                "Untuk informasi sebaran corona lengkapnya bisa cek di web ini ya kak https://kawalcorona.com/ \n\nKlik *MENU* untuk mendapatkan informasi lainnya, atau klik *SELESAI* jika sudah cukup.",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'MENINGGAL':
        try:
            r = requests.get('https://api.kawalcorona.com/indonesia/')
            data = json.loads(r.content)
            meninggal = data[0]['meninggal']
            update.message.reply_text("Total Pasien Corona yang Sudah Meninggal di Indonesia :* {} *".format(meninggal)+
            "\n\nSudah banyak yang meninggal kak, kakak jaga kesehatan ya :'(\nUntuk informasi sebaran corona lengkapnya bisa cek di web ini ya kak https://kawalcorona.com/ \n\nKlik *MENU* untuk mendapatkan informasi lainnya, atau klik *SELESAI* jika sudah cukup.",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)

        except:
            update.message.reply_text(
                "Untuk informasi sebaran corona lengkapnya bisa cek di web ini ya kak https://kawalcorona.com/ \n\nKlik *MENU* untuk mendapatkan informasi lainnya, atau klik *SELESAI* jika sudah cukup.",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
    elif x == 'SELESAI':
        update.message.reply_text(
            "Terimakasih kak, ketik /start untuk memulai kembali. \nTetap jaga kesehatan ya kak, jaga pola makan juga kak, karna aku gk bisa selalu jagain kakak. Oh ya, jangan keluar rumah jika tidak penting ya kak. \n\n"
            "#StayAtHome\n"
            "#LawanCorona",parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        update.message.reply_text(
            "Klik *MENU* untuk mendapatkan informasi lainnya, atau klik *SELESAI* jika sudah cukup. ",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
    return CHOOSING

def done(update, context):
    update.message.reply_text("Terimakasih!")
    user_data.clear()
    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("token:nyadisini", use_context=True)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [MessageHandler(Filters.regex('^(POSITIF|INFO|GEJALA|TIPS|SEMBUH|MENINGGAL|SELESAI)$'),
                                      regular_choice),
                       MessageHandler(Filters.text,
                                      start)
                       ],

            TYPING_CHOICE: [MessageHandler(Filters.text,
                                           regular_choice)
                            ],
        },

        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)]
    )  
    dp.add_handler(conv_handler)
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
