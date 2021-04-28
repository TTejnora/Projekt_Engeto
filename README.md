# Projekt_Engeto

**Popis projektu**

Tento projekt slouží k extrahování výsledk? z parlamentních voleb v roce 2017. Odkaz na stránky s výsledky - https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ.

**Instalace knihoven**

Knihovny, které jsou použity v kódu jsou uloženy v souboru requirements.txt. 
Pro instalaci doporučuji použít nové virtuální prostředí s nainstalovaným manažerem spustit následnovně:
postup pro win10:

pip install -r requirements.txt

**Ukázka projektu**
Výsledky hlasování pro okres Cheb:
1.argument 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=5&xnumnuts=4101'
2.argument Cheb.csv

Spuštění programu
py Projekt_ElectionScrap "odkaz-uzemniho-celku"  soubor-k-ulozeni-dat.csv

Vykoná se stažení dat ze zadaného odkazu do souboru s daným jménem. Soubor musí mít příponu .csv .

Ukázka projektu

![image](https://user-images.githubusercontent.com/78930457/116456881-0d1a7b00-a863-11eb-8b16-050a44c084ac.png)

Ukázka výstupních dat:
![image](https://user-images.githubusercontent.com/78930457/116458277-bd3cb380-a864-11eb-9399-7f1a5d5ea013.png)

