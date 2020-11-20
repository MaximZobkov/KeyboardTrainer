from flask import Flask, render_template
from flask_login import LoginManager
# import requests
from random import choice
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clavatrainer.ru'
db_session.global_init("db/blogs.sqlite")


@app.route("/")
def main_page():
    string_before = ""
    string = ''
    symbol_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя     "
    for i in range(120):
        string_before += choice(symbol_rus)
    count = 0
    for x in string_before:
        if x == ' ':
            count += 1
        if x != ' ' or count < 2:
            string += x
            count = 0
    return render_template("index.html", symbol=symbol_rus, string=string.strip())


@app.route("/words_trainer")
def words():
    loops = 5
    string_array = []
    array = ['агнец', 'адам', 'адрес', 'азарт', 'азы', 'аист', 'айва', 'акт', 'актер', 'алеть', 'аллея', 'алмаз',
             'алый', 'альпы', 'альфа', 'амур', 'балл', 'балет', 'бант', 'бард', 'барс', 'бас', 'батик', 'бег', 'бедро',
             'без', 'бей', 'белая', 'белка', 'белла', 'белье', 'берег', 'вал', 'вальс', 'вам', 'верх', 'вдали', 'вдох',
             'вдруг', 'веда', 'ведет', 'ведь', 'веер', 'везде', 'венец', 'венок', 'вера', 'верба', 'гамма', 'где',
             'геба', 'ген', 'гибка', 'гимн', 'глаза', 'гляди', 'голая', 'голос', 'горит', 'град', 'грань', 'греза',
             'грех', 'гроза', 'дает', 'даже', 'дама', 'дар', 'девиз', 'демон', 'день', 'джин', 'дивно', 'дикая', 'для',
             'днепр', 'до', 'дождь', 'дочь', 'драма', 'ева', 'едва', 'ее', 'ежик', 'еле', 'ель', 'емкий', 'если',
             'есть', 'еще', 'жадно', 'жажда', 'жанр', 'жара', 'жизнь', 'жрица', 'завет', 'загар', 'закат', 'закон',
             'залив', 'запад', 'запах', 'заря', 'заряд', 'зачем', 'звать', 'звено', 'звук', 'здесь', 'земля', 'зерно',
             'ива', 'игра', 'идеал', 'идея', 'идол', 'идти', 'из', 'извив', 'извне', 'изгиб', 'излет', 'излом', 'изо',
             'иисус', 'икона', 'или', 'как', 'какая', 'каноэ', 'кара', 'квант', 'ключ', 'книга', 'когда', 'кожа',
             'коза', 'конец', 'копия', 'крем', 'кроха', 'крыло', 'куда', 'ласка', 'лед', 'лента', 'лепет', 'лето',
             'лиана', 'лик', 'лилия', 'лимон', 'линза', 'линия', 'лира', 'лиса', 'лист', 'лихой', 'лицо', 'маг',
             'магия', 'магма', 'мазок', 'май', 'мак', 'мама', 'манго', 'мания', 'марта', 'мать', 'маяк', 'между',
             'мекка', 'мера', 'месса', 'набор', 'напев', 'напор', 'не', 'нега', 'ничто', 'нота', 'ночь', 'нюанс',
             'няня', 'оазис', 'обвал', 'обе', 'обет', 'облик', 'облом', 'образ', 'обруч', 'обрыв', 'обряд', 'овал',
             'огонь', 'ода', 'озеро', 'озноб', 'ой', 'пава', 'палцы', 'памир', 'парус', 'пение', 'перед', 'песня',
             'пик', 'пир', 'пить', 'пища', 'пламя', 'племя', 'плен', 'плеск', 'плод', 'равно', 'рад', 'ради', 'раз',
             'разве', 'разум', 'рай', 'рампа', 'рана', 'ранее', 'расти', 'раут', 'ребро', 'резко', 'рейд', 'рейс',
             'сага', 'сад', 'салат', 'салки', 'салют', 'самая', 'самба', 'сан', 'сани', 'сахар', 'сбор', 'сброс',
             'свет', 'свеча', 'свита', 'свод', 'тайна', 'так', 'такт', 'там', 'танго', 'танец', 'таять', 'твой',
             'театр', 'тело', 'тема', 'тембр', 'тень', 'титул', 'тихая', 'то', 'убор', 'увы', 'угар', 'удача', 'уж',
             'ужин', 'узор', 'узы', 'ум', 'уметь', 'ура', 'успех', 'уста', 'устье', 'утеха', 'уют', 'фаза', 'факел',
             'факт', 'фант', 'фарт', 'фасон', 'фата', 'фаянс', 'ферзь', 'фея', 'фиджи', 'фильм', 'финал', 'финик',
             'финиш', 'флаг', 'халва', 'хаос', 'хвала', 'химия', 'хит', 'хлеб', 'хмель', 'ход', 'холст', 'хор', 'хотя',
             'храм', 'хурма', 'цапля', 'цвет', 'целый', 'цель', 'цена', 'центр', 'цепь', 'цикл', 'цирк', 'цифра',
             'цокот', 'чарка', 'чары', 'час', 'часы', 'чаша', 'чаще', 'через', 'черты', 'чета', 'число', 'чрез', 'что',
             'чтобы', 'чу', 'чуть', 'чую', 'шаг', 'шалаш', 'шаль', 'шанс', 'шар', 'шарм', 'шатер', 'швея', 'шейх',
             'шел', 'шелк', 'шепот', 'шея', 'шип', 'шить', 'шифр', 'щебет', 'щедро', 'щека', 'щелк', 'щит', 'экран',
             'элита', 'эльф', 'эмаль', 'эней', 'эол', 'эпос', 'эпоха', 'эрос', 'эрот', 'эскиз', 'эссе', 'эта', 'этаж',
             'этап', 'этика', 'юбка', 'юг', 'юмор', 'юный', 'явно', 'ягода', 'ядро', 'язык', 'яйцо', 'якобы', 'якорь',
             'ялик', 'ямка', 'яркий', 'ясень', 'ясли', 'ясно', 'яства', 'яхонт', 'яхта']
    for i in range(loops):
        element = choice(array) + ' '
        string_array += [(element * 20).strip()]
    string = string_array[0]
    print(string_array)
    return render_template("index.html", string=string.strip(), loops=loops, str_arr=string_array)


def main():
    app.run()


if __name__ == '__main__':
    main()
