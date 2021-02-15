
# Biblioteques
import yagmail
import time
import random

# Paràmetres
període = 3600 # Temps entre repeticions en segons
marge = 10 # Percentatge sobre 'període', de manera que el temps d'espera real serà de 'període' +/- 'marge'
lletres = open( 'missatges.txt', 'r' ) # Accedim a l'arxiu amb els missatges
ruta_imatges = '/ruta/comuna/a/totes/les/imatges/'
yag = yagmail.SMTP( 'elmeucompte' )
destinatari = 'estimada@meva.com'

# Càlculs
lInf = període * ( 1 - marge / 100 )
lSup = període * ( 1 + marge / 100 )

# Principal
while True:

    # Temps d'espera
    espera = random.uniform( lInf, lSup )
    time.sleep( espera )

    # Assumpte i missatge
    assumpte = lletres.readline()
    missatge = lletres.readline()
    imatge = ruta_imatges + lletres.readline().strip()

    # Enviament
    yag.send(
        to = destinatari,
        subject = assumpte,
        contents = missatge,
        attachments = imatge
    )
    
    continua = lletres.readline()
    if not continua:
        break

lletres.close()
