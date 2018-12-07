# Удаленное управление

Удаленное управление PTZ-камерами и приложением TrueConf Weathervane

# Что требуется

1. Установленное приложение TrueConf Weathervane
2. Python версии 3.* и установленный flask 

# Первый запуск

В файле wv_remotecontrol.py установите константы 

WV_PATH - расположение исполняемого файла TrueConf Weathervane
FLASK_HOST - ваш IP
FLASK_PORT - порт (можно оставить 5000)
PRESET_COUNT - количество "пресетов" (строк) установленных в приложении TrueConf Weathervane

# Как использовать

Откройте в браузере страницу http://<FLASK_HOST>:<FLASK_PORT> и по нажатию кнопок с номерами соотв. пресеты будут активироваться в приложении TrueConf Weathervane
