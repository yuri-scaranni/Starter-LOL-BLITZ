import os, subprocess as sub
from time import sleep

#Busca o caminho independente da máquina e concatena com o caminho padrão dos programas
lol = (os.environ['SYSTEMDRIVE'] + '\Riot Games\League of Legends\LeagueClient.exe')
blitz = (os.environ['USERPROFILE'] + '\AppData\Local\Programs\Blitz\Blitz.exe')

#Verifica se o programa já se encontra rodando.
def running_or_not(programa):
    #Verifica dentro das tarefas do windows.
    processo = sub.getoutput(f'TASKLIST /SVC /FI "IMAGENAME eq {programa}')
    if f'{programa}' in processo:
        return True
    return False

#LOL off e BLITZ off, inicia os 2 com um intervalo de 30 segundos.
if running_or_not('LeagueClient.exe') is False and running_or_not('Blitz.exe') is False:
    os.startfile(lol)
    sleep(30)
    os.startfile(blitz)

#LOL on e BLITZ off, inicia apenas o blitz.
elif running_or_not('LeagueClient.exe') is True and running_or_not('Blitz.exe') is False:
    os.startfile(blitz)

#LOL off e BLITZ on, inicia apenas o LOL.
elif running_or_not('LeagueClient.exe') is False and running_or_not('Blitz.exe') is True:
    os.startfile(lol)

else:
    pass


