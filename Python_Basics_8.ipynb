{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 8. Error handling\n",
    "- active and passive error handling, `try`, `except`, `else`, `finally`\n",
    "- errors & exceptions, `raise`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 8.1 Ošetření chyb\n",
    "- Aktivní - pomocí podmínek `if, elif, else` = řeším jednoduché a jasně definovatelné chyby\n",
    "- Pasivní - pomocí `try-except` = pokud není žádný jednoduchý způsob, jak chybu zachytit pomocí \"if, elif, else\"\n",
    "- pro vyjímečné situace :)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# v TRY zkusíme tady provést to, co chceme = načíst vstup a přetypovat na číslo (int)\n",
    "try:\n",
    "    cis1 = int(input(\"zadej číslo: \"))\n",
    "    cis2 = int(input(\"zadej číslo: \"))\n",
    "    seznam_cisel = [cis1, cis2]\n",
    "\n",
    "    print(cis1*cis2)\n",
    "    print(seznam_cisel[3])\n",
    "\n",
    "# v \"EXCEPT\" se připravíme na to, co se stane, pokud se věci v \"TRY\" nepodaří (= skončí chybou)\n",
    "# zde odhadujeme, že uživatel zadá omylem text (string) místo čísel\n",
    "# \"except\" lze nechat bez specifikace pro JAKOUKOLIV chybu\n",
    "# je možné mít VÍCE exceptů = pro VÍCE druhů chyb\n",
    "except ValueError:\n",
    "    print(\"zadej číslo, ne text!!!\")\n",
    "    # nezobrazí se \"ValueError\" ale to, co je v \"except\" = \"zadej číslo, ne text!!!\"\n",
    "\n",
    "except IndexError:\n",
    "    print(\"Mimo seznam kamaráde!\")\n",
    "\n",
    "# p.s. často musíme nechat program cíleně spadnout a odhalit druh chyby = a následně ji \"ošetřit\" v \"except\"\n",
    "\n",
    "\n",
    "# NEPOVINNÉ bloky ELSE & FINALLY\n",
    "\n",
    "else: # vykoná se, když se nespustí žádný \"except\"\n",
    "    print(\"Tohle se udělá, pokud nenastane žádný problém v bloku try\")\n",
    "\n",
    "# \"finally\" není povinné, ale pokud jej použijeme, provede se vždycky :)\n",
    "finally:\n",
    "    print(\"vždycky se rozluč !\")\n",
    "\n",
    "# po vykonání bloků TRY, EXCEPT, FINALLY program pokračuje dál \n",
    "# tzn. i v případě, že byla jedna či více chyb (a proběhly bloky EXCEPT)\n",
    "\n",
    "# pokud bychom to pomocí \"try/except/finally\" neřešili, program s chybou spadne :( "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 8.2. Chyby a výjimky\n",
    "- chyby (`Errors`) - obecný problém, který způsobuje, že program selže - nelze ošetřit v bloku TRY-EXCEPT:\n",
    "    - SyntaxError\n",
    "    - RuntimeError\n",
    "    - IndentationError etc. \n",
    "- výjimky (`Exceptions`) - jsou druhy chyb, které můžeme v programu zachytit a zpracovat v bloku TRY-EXCEPT: \n",
    "    - IndexError\n",
    "    - TypeError\n",
    "    - ZeroDivisionError\n",
    "    - ValueError\n",
    "    - NameError\n",
    "    - FileNotFoundError, ...\n",
    "- výjimky můžeme sami vyvolat pomocí `raise`\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# CUSTOM ERRORS - vyvolávání \"vyjímek\"\n",
    "# vlastně vyberu, v kterém případě program nahlásí ERROR\n",
    "\n",
    "# vyvolání \"obecné\" vyjímky s vysvětlujícím textem\n",
    "if cis1 < 0:\n",
    "  raise Exception(\"Zadané číslo musí být kladné\")\n",
    "\n",
    "# vyvolání konkrétní vyjímky = ValueError s vysvětlujícím textem\n",
    "if not isinstance(cis2, int): # to je ekvivalent: if isinstance(cis2, int) == False:\n",
    "    raise ValueError(\"Neplatná hodnota - musí být zadáno CELÉ číslo\")\n",
    "\n",
    "# vyvolání konkrétní vyjímky = ValueError\n",
    "def check_age(age):\n",
    "    if age < 0:\n",
    "        raise ValueError(\"Věk nemůže být záporný!\")\n",
    "    elif age > 120:\n",
    "        raise ValueError(\"Věk přesahuje realistickou hranici!\")\n",
    "    return f\"Věk je {age}\"\n",
    "\n",
    "try:\n",
    "    print(check_age(-5))  # Vyvolá ValueError\n",
    "except ValueError as e:\n",
    "    print(f\"Chyba: {e}\")\n",
    "\n",
    "# díky blokům TRY-EXCEPT-FINALLY snáze zachytíme zpracujeme chyby na jednom místě "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## practise\n",
    "- budeme chtít od uživatele získat jméno, příjmení, adresu (=město) a věk\n",
    "- pomocí využití try a except zajisti následující (jinak vyvolej chyby či vyjímky):\n",
    "    - jméno a příjmení bude vždy string, složený z písmen bez mezer\n",
    "    - věk bude vždy číslo\n",
    "    - adresa bude jakékoliv město ze seznamu: [Praha, Brno, Ostrava, Plzeň, Liberec]\n",
    "\n",
    "- doporučení:\n",
    "    - můžeš využít i metody stringů :)\n",
    "    - řeš dané případy (jméno, věk, adresa) v separátních try / except blocích\n",
    "    - zkus cíleně zadávat špatné hodnoty = zjistíš, jaké chyby se vyvolají\n",
    "\n",
    "- challenge:\n",
    "    - s využitím bloků else a finally zajisti, aby program (skript) informoval:\n",
    "        - pokud vše proběhlo bez chyb\n",
    "        - pokud se vyskytly chyby, tak podat informaci o všech výskytech chyb (např. vyvolané chyby někam ulož a pak proveď výpis)\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
