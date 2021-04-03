# Обрезка ссылок с помощью Битли

Cокращающий ссылки проект.

### Как установить

Для работы кода необходимо создать файл .env и поместить туда токен bitly.
```
BIT.LY_TOKEN=17c09e22ad155405159ca1977542fecf00231da7
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

### пример работы

```
D:\ZeazyGame\devman\bitly>python main.py https://www.youtube.com/watch?v=wdTeeMF7L7U
https://bit.ly/3lY2YVy
```