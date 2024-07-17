@echo off
setlocal

REM Definir el comando que quieres ejecutar
set COMMAND=python kahoot.py

REM Definir el número de instancias que deseas ejecutar
set NUM_INSTANCIAS=15

REM Bucle para ejecutar el comando en múltiples instancias minimizadas
for /l %%i in (1,1,%NUM_INSTANCIAS%) do (
    start /min cmd /c "%COMMAND%"
)

endlocal