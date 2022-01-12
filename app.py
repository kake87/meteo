from flask import Flask, render_template,session, redirect, url_for, escape, request

# Flask - сам фреймворк Фласка, 
# render_template - отвечает за отрисовку html страниц в папке template
# redirect - отвечает за перенаправление на другую страницу
# url_for - создание URL
# escape - выход из сессии
# request - работа с GET/POST запросами, обычно используется при создании форм



# 1. Необходимо создать инициализирующее приложение. 
# Данная конструкция общепринята и если заменить __name__ на что-то другое то корректная работа
# не гарантируется
app = Flask(__name__)


# 2.  Главная страница. Декоратор app.route всегда применяется при создании новой страницы
# В качестве аргумента принимает название страницы в строковом виде
# Конкретно в данном случае название опущено, так как мы генерируем главную страницу
@app.route('/')
def index():
    """Вывод главной страницы
    'username' берется из функции и страницы login
    В нашей конструкции происходит редирект на страницу content если пользователь
    ввел логин

    Returns:
        если введен username: [redirect to content page]
        если не введен: [вывод сообщения о том что вы не вошли]
    """

    if 'username' in session:
        return  redirect('/content')
    return 'Вы не вошли под своим логином </br><a href="/login">Страница входа<a/>'



@app.route('/user/<username>')
def user(username):
    username = 'Kanat'
    return "<h1>Hello {username}</h1>".format(username)

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
    <form action="" method="post">
        <p><input type=text name=username>
        <p><input type=submit value=Login>
    </form>'''


@app.route('/logout')
def logout():
# удалить из сессии имя пользователя, если оно там есть
    session.pop('username', None)
    return redirect(url_for('index'))
    
@app.route('/content')
def content():
    return render_template('/content.html')


@app.route('/info')
def info():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

# set the secret key. keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


#3 Данная конструция нужна чтобы наш скрипт был постоянно запущен
# При такой конструкции нет необходимости прописывать в консоли flask run
if __name__ == '__main__':
    debug=True
    app.run()