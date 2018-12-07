# Удаленное управление

Удаленное управление PTZ-камерами и приложением **TrueConf Weathervane**

# Что требуется

1. Установленное приложение [TrueConf Weathervane](https://trueconf.ru/products/weathervane.html) версии 4.* или выше
2. Python версии 3.* и установленный flask 

# Первый запуск

В файле **wv_remotecontrol.py** установите следующие константы:

- WV_PATH - расположение исполняемого файла [TrueConf Weathervane](https://trueconf.ru/products/weathervane.html)
- FLASK_HOST - ваш IP
- FLASK_PORT - порт (можно оставить 5000)
- PRESET_COUNT - количество "пресетов" (строк) установленных в приложении [TrueConf Weathervane](https://trueconf.ru/products/weathervane.html)

# Как использовать

Откройте в браузере страницу http://<FLASK_HOST>:<FLASK_PORT> и по нажатию кнопок с номерами соотв. пресеты будут активироваться в приложении [TrueConf Weathervane](https://trueconf.ru/products/weathervane.html)

![wv41](https://user-images.githubusercontent.com/33928051/49642618-a9d6e680-fa24-11e8-9c8a-8df292f723a3.png)
