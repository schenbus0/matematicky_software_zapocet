Seminární práce: Matematický software
(Kl/MSW)Autor: Marek Schönbauer

Úloha 1: Lineární a nelineární oscilátory
  A) Lineární oscilátor
    Rozdíl mezi tlumeními:
      Slabé (underdamped): Systém kmitá kolem rovnovážné polohy, ale jeho amplituda exponenciálně klesá.
      Kritické (critical): Systém se vrátí do rovnovážné polohy v nejkratším možném čase bez jediné oscilace (překmitu).
      Silné (overdamped): Systém je přetlučený, neosciluje a vrací se do rovnováhy velmi pomalu (pohyb v hustém médiu).
    Změna tlumení o několik procent: Přechod mezi režimy je kvalitativně ostrý v bodě kritického tlumení (překmit buď nastane, nebo nenastane). Matematické kořeny se sice mění spojitě, ale fyzikální chování vykazuje jasný zlom.
    Mechanismus rezonance: Nastává, když se frekvence vnějšího buzení přiblíží vlastní frekvenci oscilátoru. Vnější síla dodává energii ve správný moment (ve fázi), což vede k dramatickému nárůstu amplitudy.
    Symbolická matematika: Ano, lineární diferenciální rovnice lze řešit analyticky pomocí knihovny sympy a její funkce dsolve().
  B) Duffingův oscilátor
    Chaotické chování: Ano, pro doporučené parametry ($\delta=0.2, \alpha=-1, \beta=1, \gamma=0.3, \omega=1.2$) se systém chová chaoticky. Je extrémně citlivý na počáteční podmínky.  
    Malá vs. velká počáteční podmínka: Potenciál má dvě studny ($\alpha = -1$). Malá počáteční podmínka drží oscilátor zamčený v jedné studni. Velká počáteční podmínka mu dodá energii na chaotické přeskakování mezi oběma studnami.  
    Zvýšení buzení $\gamma$ a počet atraktorů: Zvýšením $\gamma$ dochází k bifurkacím (zdvojování periody). Počet a tvar atraktorů se mění, systém přechází mezi okny periodicity a čistým chaosem.
  C) Van der Polův oscilátor
    Tvar limitního cyklu ($\mu=1 \to \mu=10$): Pro $\mu=1$ je cyklus hladký a eliptický. Pro $\mu=10$ se mění na hranatý tvar typický pro relaxační oscilace. 
    Rychlé skoky a pomalé fáze: Nelineární tlumení mění znaménko. Když je poloha $|x| > 1$, systém energii tlumí (pomalá fáze). Když klesne pod $|x| < 1$, tlumení začne energii dodávat, což způsobí rychlý skok do opačného stavu.
    Vliv počátečních podmínek a atraktory: Model má pouze jeden stabilní atraktor (limitní cyklus). Počáteční podmínky mají vliv jen na krátký přechodový děj, nakonec všechny trajektorie skončí na stejném limitním cyklu.
    
Úloha 2: Programová implementace SIR modelu
  Simulovali jsme šíření 5 různých infekčních nemocí s konstantní incidencí na populaci o velikosti 100 000 jedinců.
  Interpretace výsledků simulace:
    Vrchol epidemie: U vysoce nakažlivých nemocí (Spalničky, Plané neštovice) nastává vrchol velmi brzy (během 10–20 dnů) a je extrémně vysoký. U méně nakažlivých (Chřipka) nastává vrchol podstatně později a je plošší.
    Doba trvání epidemie: Agresivní epidemie s vysokým $R_0$ (Spalničky) proletí populací bleskově a rychle skončí, protože jim dojdou náchylní lidé. Nemoci s nízkým $R_0$ (Chřipka) trvají v populaci mnohem déle.
    Konečná bilance (kdo onemocní): U Spalniček onemocní téměř 100 % populace (křivka $S$ klesne k nule). U Chřipky se velká část populace vůbec nenakazí, protože se epidemie zastaví díky kolektivní imunitě dříve, než se nakazí všichni.
    
Úloha 3: Vytvoření vlastního modelu (Lotka-Volterra)Zvolil jsem model Lotka-Volterra (Dravec-Kořist) implementovaný pomocí soustavy dvou obyčejných diferenciálních rovnic.  
  Princip: Model popisuje dynamiku mezi populací zajíců (kořist) a lišek (dravci).
  Výsledek: Simulace ukazuje stabilní, periodicky se opakující cykly. Přemnožení kořisti vede k přemnožení dravců, ti kořist vyloví, začnou hladovět, jejich populace klesne a cyklus začíná nanovo.
