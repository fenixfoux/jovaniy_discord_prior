Скриптик для отслеживания и изменения текущего приоритет для процесса 
дискорда у которого с недавних пор появилась проблема что, его приоритет с временем 
устанавливается в "низкий" и в итоге чего он зависает и/или вылетает. 

Каждые 30сек проверяет приоритет, и устанавливает значение как "Высокий"

"в текущем готовом .exe файле в папке dist указан дискорд", для его работы достаточно 
просто скачать его и запустить, будет работать до выключения Windows. 

Для автоматического запуска скрипта каждый раз при запуске Windows необходимо:
    - скачать папку "jovaniy_discord_lag_watcher" и сохранить её на диск "С"
    - файл "discord_priority_watcher.bat" вырезать и сохранить в папку по адресу "C:\Users\your_user_name\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    - готово, теперь при каждом запуске Windows скрипт будет запускаться и фоново работать.

A script for tracking and changing the current priority for
the discord process, which has recently had a problem that its priority is
set to "low" over time and as a result it freezes and/or crashes. 

Checks the priority every 30 seconds, and sets the value as "High"

"in the current built .exe file in the dist folder is set the 'discord' process", 
for it to work, just download it and run it, it will work until Windows is turned off. 

To run the script automatically every time Windows starts, you need to:
    - download the folder "jovani_discord_lag_watcher" and save it to disk "C"
    - file "discord_priority_watcher.bat" cut and save to a folder at the address "C:\Users\your_user_name\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    - done, now every time Windows starts, the script will run and run in the background.