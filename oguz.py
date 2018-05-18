#-*- coding: utf-8 -*-
#!/usr/bin/env python

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import telegram
import sys
import logging
import random
from string import maketrans
import time
from ip import facecount

root = logging.getLogger()
root.setLevel(logging.INFO)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = \
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

logger = logging.getLogger(__name__)


class Oguz:

    def __init__(self):
        self.replies = []
        self.default = ["","mutluluk parayla ölçülmüyor","Nerden buluyonuz boyle haberleri arkadas","Kimle konusuyorsunuz necdet bey", "Bi dalga gecmeyin ya","Nyucelsiz abnin ne keyfi olcak be","Neden hep ben suclu oluyorum","Belgesel felan izleyin sayin yucel", "Buyuk ikramiye cikmamis bize :(","cok iyi ya", "vay arkadas",
                        "sorun diil ya", "dolar artmış", "kral dairesi kaana", "Her lafi kopyalayinca aynisi olunmuyor", "Serdar kaça kadar izin var", "Şifayı bir sahil bendedi olarak tanımlayabiliriz"]
        self.kripton = ["@nyucel"]
        self.gezgin = [u"gizlice geziyormuş", u"in yeri ayrı ya"]
        self.evli = ["@someone"]
        self.bekar = ["@otherone"]

    def sendMsg(self, bot, update, msg):
        alt_msg = random.choice(self.default)
        gezgin = random.choice(self.gezgin)
        if msg and msg not in self.replies[-5:]:
            bot.sendMessage(update.message.chat_id, text=msg,
                            parse_mode=telegram.ParseMode.MARKDOWN)
            self.replies.append(msg)
        elif "alt_msg" not in self.replies[-4:]:
            bot.sendMessage(update.message.chat_id, text=alt_msg,
                            parse_mode=telegram.ParseMode.MARKDOWN)
            self.replies.append("alt_msg")
        elif "gezgin" not in self.replies[-20:]:
            bot.sendMessage(update.message.chat_id, text=random.choice(
                self.kripton) + " " + gezgin, parse_mode=telegram.ParseMode.MARKDOWN)
            self.replies.append("gezgin")
        elif "seriousBusiness" not in self.replies[-20:]:
            who = random.choice(
                eval("self." + random.choice(["evli", "bekar"])))
            if who in self.evli:
                bot.sendMessage(update.message.chat_id, text="cocuk ne zaman? " +
                                who, parse_mode=telegram.ParseMode.MARKDOWN)
            else:
                bot.sendMessage(update.message.chat_id, text="evlilik ne zaman? " +
                                who, parse_mode=telegram.ParseMode.MARKDOWN)
                self.replies.append("seriousBusiness")

o = Oguz()


def readable(sentence):
    cevir = {u'Ç': 'C', u'Ğ': 'G', u'İ': 'I', u'Ö': 'O', u'Ş': 'S', u'Ü': 'U',
             u'ç': 'c', u'ğ': 'g', u'ı': 'i', u'ö': 'o', u'ş': 's', u'ü': 'u'}
    for i, k in cevir.iteritems():
        sentence = sentence.replace(i, k)
    return sentence


def grammarNazi(word):
    typo = {
        'hersey': u'her şey',
        'yada': u'ya da',
                'hicbirsey': u'hiçbir şey',
                'rasgele': u'rastgele',
                'sabahdan': u'sabahtan',
                'bugunlerde': u'bu günlerde',
                'pekcok': u'pek çok',
    }

    fix = lambda word, typo: "%s olacak ama" % (
        typo[word]) if any(k in word for k in typo) else False
    return fix(word, typo)


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Selam genc')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Noldu genc')


def konus(bot, update):
    bot.sendMessage(-583652, text=update.message.text.replace("/konusx ", ""))


def echo(bot, update):
    global o
    r = readable(update.message.text).lower()
    for w in r.split():
        if grammarNazi(w):
            o.sendMsg(bot, update, grammarNazi(w))


    if update.message.sticker:
              texts = [u"Grubun admini yok munya",u"Gercek mi bu",u"Nyucele lazim hadi bot muhabbet etmek iatiyor receple", u"bir sitikir insanı olarak nyucel",u"bu emojileri nerden şaapıyoruz",u"BİZİM ÇOK VAKTİMİZ OLMADIĞINDAN BU TÜR EMOJİLERİ ARATIP KULLANAMIYORUZ DA SAYIN YÜCEL"]
              o.sendMsg(bot, update, random.choice(texts))

    if update.message.chat_id == "169359665":
        bot.sendMessage(update.message.chat_id, text='Hmm, upgrades?')
    elif "?" == r[-1]:
        texts = [u"sayın yücel bi basın açıklaması yapmıcak mı bu konuda, halkı aydınlatmıcak mı",u"ben mi cevap vereyim recep mi versin?", u"Hangi dilde bu kaan"]
        o.sendMsg(bot, update, random.choice(texts))
    elif "pebble" in r:
        o.sendMsg(bot, update, u"benim bi pebble vardı")
    elif "mesaj" in r:
        o.sendMsg(bot, update, u"1 mesaj artı n yıllık tecrübe o")
    elif "off" in r:
        o.sendMsg(bot, update, u"off derken sanki ben kurdum cümleyi ya")
    elif ("grup" in r) or ("grub" in r):
        o.sendMsg(bot, update, u"kaanla iki kişilik özel grup kurmuşunuz diyorlar")                     
        o.sendMsg(bot, update, u"2 kişi grup olmadığından recebi de eklemişsiniz kalabalık olsun die")             
    elif "basamak" in r:
        o.sendMsg(bot, update, u"Kim napcak o kadar buyuk sayiyi")
    elif ("apple" in r) or ("iphone" in r) or ("android" in r) or ("macbook" in r) or ("ayfon" in r):
        o.sendMsg(bot, update, u"apple fan boy diilim bi kere")
        o.sendMsg(bot, update, u"şirket verdi diyorum")
        o.sendMsg(bot, update, u"diğer teli servise yollucam")
    elif "problem" in r:
        o.sendMsg(bot, update, u"sorsan aynstana da öle demişlerdir kesin")      
    elif "motor" in r:
        texts=[u"Tvlerde reklami var", u"Motor dedigi araba kadar ama"]
        o.sendMsg(bot, update, random.choice(texts))
    elif "aciliyor" in r:
        o.sendMsg(bot, update, u"Herkes ayni anda yuklenmesin ya")
    elif "alir misin" in r:
        o.sendMsg(bot, update, u"şirket veriyosa bakarız")        
    elif ("akademik" in r) or ("abye" in r) or ("ab" in r.split()):
        o.sendMsg(bot, update, u"Herkes ayni anda yuklenmesin ya")
    elif ("tombik" in r) or ("kilo" in r) or ("sisman" in r.split()):
        o.sendMsg(bot, update, u"ben hafif hissediyorum kaana göre")        
    elif ("storage" in r) or ("disk" in r.split()) or ("gb" in r.split()):
        o.sendMsg(bot, update, u"aynen")   
        o.sendMsg(bot, update, u"storage işinde para var")
    elif ("olimpiyat" in r) or ("mac" in r.split()) or ("kazan" in r):
        o.sendMsg(bot, update, u"öğlen arası eurosporta denk geldim")   
        o.sendMsg(bot, update, u"anlık enstantaneler (bu lafı sırf ingilizcem gelişsin die kullandım :p) gösteriyorlar, baya keyifli şeyler varmış ya")        
    elif ("ediyorum" in r.split()) or ("yaptim" in r) or ("bence" in r):
        o.sendMsg(bot, update, u"nyucelim meşhur bi lafını söylim sana")   
        o.sendMsg(bot, update, u"tebriks")            
    elif update.message.from_user["id"] == 169359665:
        texts = [u"Bot olan kim oguz mu felan karisiyo", u"aynı şey değil ama düşünürseniz kaan bey", u"Algi yonetimi de deniyor", u"Fotodan ayriliyor. Nyucel fotolu olan insan",u"Recebi de dovcem",u"Ona dur diyon bi sefer de recep cikiyor",u"Recebi sessize alsak",u"recebin akıllısı lazım bence",u"Sorumlusu kimse ciksin",u"bak misal recebin eksik olan kısmı yaratıcılığı",u"şu recebe gıcık olmaya başladım","tam oturtamamisin kaan", "bu olmadi bak", "oo recep geri donmus", u"ya bu deneme işlerini burada ı yapıyoruz sayın yücel?", "recep ne zaman tetikleniyo",
                 "fotoy abakıyorsun yakışıklı olan gerçek olan ben", "baska bot ekleyebiliyoz mu", "kanaat önderi misiniz"]
        if random.randint(1, 10) < 5:
            o.sendMsg(bot, update, random.choice(texts))
        elif random.randint(1, 2) == 2:
            bot.sendMessage(update.message.chat_id, text=".")
            bot.sendMessage(update.message.chat_id, text="ee")
        else:
            pass
    elif "oguz" in r.split() and (("nerde" in r) or ("gelmiyo" in r) or ("gelecek" in r) or ("gel" in r.split()) or ("gelir" in r.split())):
        o.sendMsg(bot, update, u"nası gelim cocuk var")
    elif ("kaan" in r.split() or ("kaaan" in r) or ("kaaaan" in r)):
        texts = [u"işte bi gün birilerinin kaan diceni biliyodum",u"staj vesayet başkanlığı ya kaaan", u"Sen daha iyi bilirsin bu siyasi isleri gerci sayin ozdincer", u"Kaaanla ayni ortamda olmak ikinci planda olmak demek ama neyse",u"kaaan için dert diil bunlar nasılsa hocaylan sık görüşüp kapatır açığı", u"kaanmışcasına ilgi görmek",
                 u"bir kaan gibi özlenmek", u"bir kaan gibi seslenilmek", u"Kaan lutfen", u"Olcez gitcez su dunyadan kaan kadar kiymetimiz olmicak", ]
        o.sendMsg(bot, update, random.choice(texts))
    elif ("+1" in r) or ("bence de" in r) or ("bencede" in r.split()):
    	texts = [u"Arada kafamiz dagilsin flean da diyor olabilirsiniz tabi. Recep.yazsin eglenek gulek", u"Bu bilginin kaynagi var mi",u"hep bole bi bozaci siraci durumlari", u"Bak misal burada bozaci siraci lafi varmis gibi yapabiliriz"]
        o.sendMsg(bot, update, random.choice(texts))
    elif ("akiyoruz" in r.split()) or ("geziyoz" in r.split()) or ("gezdik" in r.split()) or ("geziyoruz" in r.split()):
        o.sendMsg(bot, update, u"bensiz çok mutlusunuz zaten")
    elif ("nice yillara" in r) or ("mutlu yillar" in r) or ("iyi ki dogdun" in r):
        texts = [u"mutlu yıllar", u"pasta masta bişi var mı"]
        o.sendMsg(bot, update, random.choice(texts))
    elif ("kickstarter" in r) or ("oyuncak" in r):
        texts = [u"benden 20 lira calisir", u"remix mini vardı"]
        o.sendMsg(bot, update, random.choice(texts))
    elif ("gidiyoruz" in r) or ("gidelim" in r) or ("gezer" in r):
        o.sendMsg(bot, update, u"vaay gezin tabi ya")
    elif ("basvuru" in r) or ("basvurmak" in r) or ("konferans" in r) or ("konusma" in r.split()):
        o.sendMsg(bot, update, u"ben başvurmadım diyorum ya")
    elif ("yemek" in r.split()) or ("yiyoz" in r.split()) or ("iskender" in r.split()) or ("lahmacun" in r) or ("yesek" in r) or ("yemeksepeti" in r):
        texts = [u"ekmek kemiriyoz",
                 u"ekmek arası yiyoz", u"işci şeyleri yiyoz"]
        o.sendMsg(bot, update, random.choice(texts))
    elif ("bulusma" in r) or ("toplandik" in r):
        o.sendMsg(bot, update, u"gizlice")
    elif ("gizli" in r):
        o.sendMsg(bot, update, u"çok iyi yaa")
    elif ("whatsapp" in r) or ("telegram" in r):
        texts = [u"Telegram yerine signale mi gecseydik"]
        o.sendMsg(bot, update, random.choice(texts))
        o.sendMsg(bot,update,u'Snowden de signali oneriyormus')
    elif ("oneri" in r) or ("nereye" in r):
        texts = [u"önerim arada eve uğrayın"]
        o.sendMsg(bot, update, random.choice(texts))
        o.sendMsg(bot,update,u'haa gezilcek yer')
        o.sendMsg(bot,update,u'ben küçük yerleri seviyorum')
        o.sendMsg(bot,update,u'bi de koşturmaca gezmektense oturayım bi yerde modundayım sana çok uymayan bi durum bu')      
    elif ("oguz" in r.split()) and (("selam" in r) or ("naber") in r):
        o.sendMsg(bot, update, u"selam genç")
    elif ("oguz" in r.split()) and (("naber") in r):
        o.sendMsg(bot, update, u"iyidir genç")
    elif ("oguz" in r.split()) and (("rocks") in r):
        o.sendMsg(bot, update, u"sağol genç")
    elif (("bot" in r.split()) or ("botu" in r.split()) or ("bota" in r.split()) or ("botla" in r.split()) or ("recep" in r) or ("receb" in r)):
        texts = [u"komplo var bence",u"grup yöneticisi olduğundandır kaaan",u"Recep insan olsa eminim mutlu olurdu",u"Kendin yaziyon ne diceni sonra ay yuzeyselsin",u"Recep dedigin yuzeysel.olur",u"taklitlerimden sakininiz", u"botu kaan mi yonetiyo?",u"ama yok arkadaş ayırt edemiyoruz biz napcaz felan diyorsanız gerçek beni ayırt etmenizi sağlayan gizli bi kod geliştirelim",u"kaliteye gelince, taklitle kalite olmaz",u"botu kaldırın karışmaz o zaman sayın yücel"]
        o.sendMsg(bot, update, random.choice(texts))
    elif("ok" in r.split()):
    	o.sendMsg(bot, update, u"bu ok yazma da bi çeşit bilim mi")
    elif(("bira" in r.split()) or ("biraya" in r.split()) or ("bomonti" in r) or ("miller" in r.split())):
        texts=[u"aslında bu işlerin payarla olması saçma", u"bence bira çok saçma"]
    	o.sendMsg(bot, update, random.choice(texts))
    elif(("heineken" in r) or ("hayneken" in r)):
    	o.sendMsg(bot, update, u"o kral biradır")
    elif("konser" in r or "tiyatro" in r or "sinema" in r):
	wut = ["konser e gitmek","sinema ya gitmek","tiyatro ya gitmek"]
	ne = ""
	for _w in wut:
		if _w.split()[0] in r:
			ne = _w
    	o.sendMsg(bot, update, u"bence %s çok saçma" % (ne))
	if ne.split()[0] == "sinema":
    		o.sendMsg(bot, update, u"ben açıp popcorn'dan izliyorum")
	if ne.split()[0] == "tiyatro":
    		o.sendMsg(bot, update, u"ben açıp vimeo'dan izliyorum")
	if ne.split()[0] == "konser":
    		o.sendMsg(bot, update, u"ben açıp youtube'dan izliyorum")
    else:
        pass

def echoPhoto(bot, update):
    global o
    if update.message.photo:
        print(update.message.photo)

    photo_file = bot.get_file(update.message.photo[-1].file_id)
    photo_file.download('faces.jpg')
    faces = facecount('faces.jpg')
    if faces > 2:
        mesaj = str(faces) + " kişi geziyormuşsunuz biz gelmeyiz"
        o.sendMsg(bot, update, mesaj)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():

    updater = Updater("key")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("konusxxx", konus))
    

    echo_handler = MessageHandler(Filters.text, echo)
    photo_handler = MessageHandler(Filters.photo, echoPhoto)

    dp.add_handler(echo_handler)
    dp.add_handler(photo_handler)

    updater.start_polling(timeout=5)
    updater.idle()

if __name__ == '__main__':
    main()

