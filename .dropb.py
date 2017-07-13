#!/usr/bin/evn python3

__author__ = 'Zwdeff'
__version__ = '0.1'

# [GitHub] https://www.github.com/Xdwnff-04x
# [Telegram - Channel] https://telegram.me/ZWDChannel
# 
# [Description]
#   Progama para configurar o dropbear em sua VPS.
#   Porta 443 serar ativada por padrao.
# [License]
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

import os
import sys
import time
from os import system
from time import *
from sys import*
import fileinput

n0='\033[90m'
u1='\033[31m'
u2='\033[32m'
u3='\033[33m'
u4='\033[34m'
u5='\033[35m'
u6='\033[36m'
u0='\033[m'

__banner__ =n0+'''
     _                 _
  __| |_ __ ___  _ __ | |__   ___  __ _ _ __
 / _` | '__/ _ \| '_ \| '_ \ / _ \/ _` | '__|
| (_| | | | (_) | |_) | |_) |  __/ (_| | |
 \__,_|_|  \___/| .__/|_.__/ \___|\__,_|_|
                |_|
   | Configurar Dropbear |By: %s
''' % __author__ + u0

print(__banner__)

def case():
  try:
     dp = input(u2+'Deseja mesmo fazer instalacao Dropbear [y/n] :: ' + u0)
     if dp == 'y' or dp == 'Y':
 	    print(u3+'Instalando Dropbear. Aguarde ..' + u0)
 	    system('apt-get update 1> /dev/null')
 	    system('apt-get install dropbear -y 1> /dev/null')
 	    def retur():
 	        print(u1+'Recomendado Porta: 80' + u0)
 	        # Porta para utilizar no Dropbear ...
 	        P = input(u3+'Porta para utilizar no Dropbear :: ' + u0)
 	        if P == '443':
 	           print(u1+'Porta 443. Ja vem ativada por Padrao' + u0)
 	           retur()
 	           
 	        # Adicionando nova configuracao no arquivo /etc/default/dropbear ...
 	        system('''echo '# Dropbear By: ZWR Channel' > /etc/default/dropbear''')
 	        system('''echo 'NO_START=0' >> /etc/default/dropbear''')
 	        system('''echo 'DROPBEAR_PORT=%s' >> /etc/default/dropbear''' % P)
 	        system('''echo 'DROPBEAR_EXTRA_ARGS="-p 443"'\
 	                >> /etc/default/dropbear''')
 	                
 	        # Retirando Porta 80 do squid ...
 	        if os.path.isfile('/etc/squid/squid.conf') == True:
 	           for i, line in enumerate(fileinput.input('/etc/squid/squid.conf', inplace=1)):
 	               sys.stdout.write(line.replace('http_port 80\n', ''))
 	           system('service squid restart')
 	           
 	        # Retirando Porta 80 do squid3 ...
 	        if os.path.isfile('/etc/squid3/squid.conf') == True:
 	           for i, line in enumerate(fileinput.input('/etc/squid3/squid.conf', inplace=1)):
 	               sys.stdout.write(line.replace('http_port 80\n', ''))
 	               system('service squid3 restart')
 	               
 	        # Retirando Porta 443 do sshd ...
 	        for i, line in enumerate(fileinput.input('/etc/ssh/sshd_config', inplace=1)):
 	               sys.stdout.write(line.replace('Port 443\n', ''))

 	        # Reiniciando servico sshd ...
 	        system('service ssh restart')
 	        # Reiniciando servido dropbear...
 	        system('service dropbear restart')
 	        # Dropbear instalado com sucesso ...
 	        print(u3+'Concluido. Dropbear configurado nas portas: %s/443' % P + u0)
 	        print(u1+'Going Out ..' + u0)
 	        sleep(2)
 	        exit()
 	    retur()
     elif dp == 'n' or dp == 'N':
        print(u1+'Going Out ..' + u0)
        sleep(2)
        exit()
        
     else:
        case()
  except KeyboardInterrupt:
     print(u1+'\nGoing Out ..' + u0)
     sleep(2)
     exit()
if __name__ == '__main__':
   case()