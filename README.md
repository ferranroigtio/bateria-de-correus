
# Bateria de correus
Programa per enviar una sèrie de correus electrònics, d'un en un, cada certa estona. Jo el vaig crear per enviar un missatge romàntic cada hora a la meva xicota durant tot un dia de sant Valentí. Li va fer moltíssima il·lusió. Llàstima que ens separaven més de mil quilòmetres; si no, aquella nit hi hauria hagut molta festa.

Tanmateix, es pot fer servir per qualsevol altre propòsit que requereixi de repetir la tasca d'enviar un correu amb continguts diferents cada vegada.

## Com funciona
Llegiu aquesta secció per entendre com fer servir el programa

### Biblioteques
El primer que cal fer és instal·lar les biblioteques `yagmail` i `keyring`. La biblioteca `keyring` es fa servir de manera implícita a l'hora de configurar un compte a `yagmail`. Podeu instal·lar-les alhora des de *Terminal* amb la següent instrucció, sempre i quan hàgiu navegat fins a la ubicació de `requisits.txt`:

```bash
`pip install -r requisits.txt`
````

El programa també fa servir les biblioteques `time` i `random`, que són mòduls estàndards de *Python* i ja venen instal·lats.

### Yagmail
En segon lloc, cal configurar `yagmail`. La biblioteca `yagmail` serveix per enviar correus des d'un compte de *Gmail*. Un cop configurat el compte, enviar correus és senzillíssim, només cal referir destinatari, assumpte, continguts i adjunts i donar la instrucció d'enviar.

Per configurar un compte en un entorn *Mac*, entreu a *Python* des de *Terminal* i doneu les instruccions següents:

```python
    >>> import yagmail
    >>> yagmail.register( 'elmeucompte@gmail.com', 'contrasenya' )
```

Així, quedarà guardat l'inici de sessió de manera segura.

Aquesta informació queda emmagatzemada a l'aplicació *Accés a Clauers* de *Mac*. Podria ser que la primera vegada que executeu ` yagmail.SMTP( 'elmeucompte' )` *Accés a Clauers* us demani confirmació perquè *Python* pugui accedir a les credencials. Podeu clicar `Permetre-ho sempre` perquè no ho torni a demanar.

Si entreu a *Accés a Clauers* i cerqueu `yagmail`, trobareu tots els inicis de sessió vinculats a aquest mètode. Si no els necessiteu, els podeu eliminar des d'*Accés a Clauers* o des de *Terminal* amb:

```python
    >>> import keyring
    >>> keyring.delete_password( 'yagmail', 'elmeucompte' )
```
    
És possible que hàgiu d'habilitar *Less secure app access* a la configuració del vostre compte de *Gmail*.

### Personalització
Ara cal aportar els continguts dels missatges que vulgueu enviar. Si voleu afegir-hi adjunts, com ara fotografies, també és el moment d'arreplegar-los. Si no voleu adjuntar res, haureu de comentar les línies corresponents del programa.

Els missatges s'escriuen tots a l'arxiu `missatges.txt`. Cada missatge consta de quatre línies:
1.  La primera línia és l'assumpte del missatge
2.  La segona línia és el cos del missatge. Com que vaig pensar el programa per enviar frases romàntiques, no vaig implementar la impressió de paràgrafs diferents
3.  La tercera línia és el nom de l'adjunt
4.  La quarta línia és un salt de línia per visualitzar millor els diferents correus

Els adjunts s'han d'agrupar tots en un mateix directori. La ruta d'aquest directori s'especificarà entre els paràmetres del programa principal `enviador.py`.

Per últim, només queda personalitzar el programa principal `enviador.py`. Bàsicament, els paràmetres que caldrà ajustar seran els següents:
-   `període`. El temps entre repeticions en segons
-   `marge`. Un percentatge de `període` perquè les repeticions no siguin a intervals exactes, sinó que tinguin una certa desviació aleatòria. En definitiva, el temps d'espera entre correu i correu estarà contingut en l'interval

    <img src="https://render.githubusercontent.com/render/math?math=p\cdot\left(1\pm\frac{m}{100}\right)">

    on *p* representa `període` i *m* representa `marge`.

-   `missatges.txt`. L'arxiu amb els missatges
-   `ruta_imatges`. La ruta al directori dels adjunts
-   `elmeucompte`. El compte de *Gmail* que heu configurat a `yagmail`. Un cop configurat, ja no cal afegir `@gmail.com`
-   `destinatari`. L'adreça electrònica on adreceu els correus. No cal que sigui de *Gmail* i, per tant, cal especificar l'adreça sencera.
