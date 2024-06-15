### Projekat Analize Proizvoda Sephore

#### Pregled

Ovaj projekat je posvećen analizi raznolikog asortimana proizvoda koje nudi Sephora a koja obuhvata detaljno proučavanje recenzija, povratnih informacija i karakteristika proizvoda kako bismo bolje razumeli potrebe i preferencije potrošača.

#### Opis Tabela

Projekat koristi nekoliko ključnih tabela koje sadrže različite tipove podataka, svaka sa specifičnom svrhom u okviru analize:

1. **Proizvodi (Products):** Ova tabela sadrži osnovne informacije o svakom proizvodu, uključujući naziv, cenu, dostupnost, i ekskluzivnost za Sephoru. Pored toga, informacije o kategoriji i podkategoriji proizvoda omogućavaju detaljnije segmentiranje u analizi.

2. **Varijacije (Variations):** Varijacije proizvoda, kao što su veličine i boje, zabeležene su u ovoj tabeli. Ove informacije su korisne za analizu preferencija potrošača u pogledu specifičnih verzija proizvoda.

3. **Recenzije (Reviews):** Tabela recenzija sadrži detalje kao što su ocena, tekst recenzije, datum slanja, i identifikacija autora recenzije. Ove informacije su ključne za razumevanje korisničkog doživljaja i zadovoljstva proizvodima.

4. **Autori (Authors):** Sadrži demografske podatke o autorima recenzija, uključujući tip kože, ton kože, i druge relevantne osobine koje mogu uticati na percepciju proizvoda.

5. **Statistike Povratnih Informacija (Feedback Statistics):** Ova tabela pruža kvantitativne podatke o povratnim informacijama na recenzije, uključujući broj pozitivnih i negativnih povratnih informacija, kao i ukupan broj povratnih informacija koje su recenzije primile.

#### Ciljevi Analize Tabela

- **Optimizacija Asortimana Proizvoda:** Analizom podataka iz ovih tabela, projekat teži da identifikuje koje proizvode korisnici najviše cene, kao i one koji možda zahtevaju poboljšanja ili prilagođavanja.
- 
- **Personalizacija Ponude:** Upotrebom demografskih podataka o autorima recenzija, moguće je personalizovati ponudu proizvoda kako bi se bolje uskladila sa specifičnim potrebama i preferencijama različitih grupa potrošača.

#### Implementacija i Vizualizacija

Rezultati analize će biti predstavljeni kroz seriju izveštaja i vizualizacija koje će olakšati interpretaciju podataka i donošenje odluka na osnovu analize. Vizualizacije mogu uključiti grafikone popularnosti proizvoda, toplote ocena, i trendove povratnih informacija, kao i druge relevantne statističke prikaze.

Ove detaljne analize i izveštaji pomoći će Sephori da bolje razume svoje potrošače, optimizuje svoj asortiman proizvoda, i efikasno adresira bilo koje probleme u ponudi, sve sa ciljem unapređenja korisničkog iskustva i jačanja tržišne pozicije.

#### Izazovi sa Performansama

Tokom analize, primetili smo da dolazi do predugog vremena obrade upita, što direktno utiče na brzinu dobijanja rezultata i generalno usporava proces analize. Ovo je posebno bilo izraženo prilikom složenih upita koji zahtevaju pridruživanje velikog broja tabela i obradu velike količine podataka.

#### Refaktorisanje Seme i Korišćenje Indeksa

Kao odgovor na ove izazove, preduzeli smo nekoliko koraka za optimizaciju naše baze podataka:

1. **Integracija Tabela FeedbackStatistics i Reviews:**
   - Povratne informacije o recenzijama, koje su prethodno bile odvojene, integrisane su direktno u dokumente recenzija. Ovo smanjuje potrebu za izvršavanjem složenih upita za prikupljanje i analizu povratnih informacija, čime se povećava brzina obrade podataka.

2. **Integracija Tabela Variations u Products:**
   - Varijacije proizvoda, kao što su veličine i boje, ranije su skladištene kao zasebne kolekcije. Integracijom ovih podataka direktno u dokumente proizvoda, eliminisana je potreba za pridruživanjem podataka prilikom upita, što rezultira bržim vremenima odgovora.

3. **Odvojivanje Autora iz Recenzija:**
   - Autori recenzija, koji su ranije bili ugrađeni direktno u dokumente recenzija, izdvojeni su u zasebnu kolekciju. Ovo odvajanje omogućava efikasnije upravljanje autorima i njihovim profilima, kao i bolju skalabilnost prilikom ažuriranja podataka o autorima.

4. **Implementacija Indeksa:**
   - Uvedeni su indeksi na ključne kolone koje se često koriste u upitima, kao što su ID proizvoda, ID autora recenzija, i datum slanja recenzije,kao i kombinovani indek (skin_type . Ovo je drastično poboljšalo performanse upita, smanjujući vreme potrebno za pretragu i sortiranje podataka.
   - Posebna pažnja je posvećena indeksiranju polja koja učestvuju u operacijama pridruživanja i filtriranja, što je rezultiralo znatno bržim vremenima odziva prilikom izvršavanja složenih analitičkih upita.
   - ![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/9eece655-d738-4861-9f53-ed8a20166eaa)



#### Očekivani Rezultati

Projekat će omogućiti dublji uvid u preferencije i ponašanje potrošača Sephore, identifikovati ključne faktore koji utiču na zadovoljstvo korisnika, i pomoći u optimizaciji asortimana proizvoda. Rezultati će biti ključni za strategije poboljšanja proizvoda i prilagođavanja ponude prema specifičnim potrebama i željama kupaca.

### Zadatak 6: Analiza Proizvoda za Njegu Lica Brendiranih za Sephoru

**Cilj Analize:**

Cilj ove analize je identifikovati proizvode iz kategorije "Face Creams" koji su ekskluzivni za Sephoru, imaju visoku prosečnu ocenu (preko 4.5), dostupni su na sniženju, i nude varijacije po veličini. Dodatni uslov je da su ovi proizvodi preporučeni od strane korisnika, što dodatno potvrđuje njihov kvalitet i prihvaćenost na tržištu.

### Detalji Analize:

Analiza obuhvata sledeće korake:

1. **Konverzija Cena:** Prvo se konvertuje prikazana cena iz tekstualnog formata u numerički, kako bi se omogućilo precizno upoređivanje i filtriranje cena.
   
2. **Filtriranje po Ocenama i Dostupnosti:** Proizvodi se filtriraju tako da su isključivo oni čija je ocena viša od 4.5, koji su ekskluzivni za Sephoru, i koji su na sniženju (tj. prodajna cena je niža od originalne).

3. **Varijacije Proizvoda:** Pridružuju se informacije o varijacijama za svaki proizvod, sa posebnim fokusom na varijacije veličine, što je važno za kupce koji traže specifične količine ili pakovanja.

4. **Pridruživanje Recenzija:** Analiziraju se recenzije koje su korisnici označili kao preporučene, što dodatno potvrđuje visok kvalitet i zadovoljstvo korisnika sa proizvodom.

5. **Grupisanje i Izlistavanje Informacija:** Rezultati se grupišu po proizvodu, pri čemu se izlistavaju naziv proizvoda, snižena i originalna cena, varijacije, i detalji recenzija koje uključuju ocene.

6. **Prezentacija Rezultata:** :
   ![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/bbdae4ac-62e7-4ff4-9ab1-c590f92124b6)

   **Explain pre optimizacije:**
   
![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/9ab394d5-b3ac-4140-aa9a-3313f64e95aa)

   **Explain nakon optimizacije:**
   
![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/d48dc24c-7364-4ee1-9fef-69823a7e9aae)


![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/ac072d20-b5b6-4ed8-8432-f04146adcacb)



### Zadatak 7: Analiza Najuticajnijih Recenzija

**Cilj Analize:**

Ova analiza ima za cilj da identifikuje 1000 najuticajnijih recenzija poslatih između 1. februara i 1. aprila 2023. godine. Da bi recenzija bila klasifikovana kao uticajna, ona mora biti označena kao korisna i mora imati najmanje 5 povratnih informacija. Pored identifikacije, analiza uključuje i izračunavanje procenta pozitivnih i negativnih povratnih informacija za svaku recenziju, što omogućava bolje razumevanje reakcija korisnika na proizvode.

### Detalji Analize:

1. **Vremenski Okvir:** Recenzije poslate između 1. februara i 1. aprila 2023.
   
2. **Kriterijumi za Uticajnost:** Recenzije moraju biti označene kao korisne i imati više od 5 povratnih informacija.

3. **Izračunavanje Procenta Povratnih Informacija:** Za svaku recenziju izračunavaju se procenti pozitivnih i negativnih povratnih informacija kako bi se analiziralo kako korisnici percipiraju kvalitet proizvoda.

4. **Rangiranje po Vremenu Slanja:** Recenzije se rangiraju na osnovu vremena slanja, počevši od najranije, što omogućava pregled trendova i promena u mišljenju korisnika tokom vremena.
5. **Prezentacija**
   ![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/9d5b504a-b2b6-441b-abfa-873cdc6a2466)

![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/d49d0c92-0537-4f9b-bc94-8d8410e2ade4)

**Metabase grafici**
![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/599e2d61-3f5d-4d04-8d64-d58d6464f4ee)
![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/166dd849-8f8a-4cda-8a6a-3b553a7e0181)



### Zaključak:

Ovom analizom dobijamo jasan uvid u koje recenzije imaju najveći uticaj među potrošačima, što može poslužiti kao dragocen alat za unapređenje proizvoda i marketinških strategija. Identifikacija recenzija sa visokom ocenom korisnosti i značajnim brojem povratnih informacija pomaže u razumevanju šta korisnici cene kod proizvoda, a visoki procenti pozitivnih povratnih informacija mogu istaći proizvode koji su dobro prihvaćeni na tržištu.


### Zadatak 8: Identifikacija Najuticajnijih Autora Recenzija na Osnovu Tipa Kože

**Cilj Analize:**

Cilj ove analize je identifikovati autore sa svetlim tonom kože i suvim tipom kože koji su napisali visoko ocenjene recenzije (ocena veća od 4). Analiza se fokusira na recenzije koje su korisnici označili kao korisne i koje imaju više pozitivnih nego negativnih povratnih informacija. Krajnji cilj je prikazati autore čije recenzije dobijaju najviše pozitivnih povratnih informacija, kako bi se prepoznali oni koji ostavljaju najuticajnije i najkorisnije recenzije.

### Detalji Analize:

1. **Selekcija Autora:** Identifikacija autora sa 'light' tonom kože i 'dry' tipom kože.

2. **Pridruživanje i Analiza Recenzija:** Pridruživanje recenzija ovim autorima i filtriranje recenzija sa ocenama većim od 4.

3. **Pridruživanje Povratnih Informacija:** Analiza povratnih informacija za svaku recenziju kako bi se osiguralo da su označene kao korisne i da imaju više pozitivnih nego negativnih povratnih informacija.

4. **Kvantifikacija Uticaja:** Izračunavanje ukupnog broja pozitivnih povratnih informacija koje su recenzije svakog autora primile.

5. **Rangiranje Autora:** Sortiranje autora prema ukupnom broju pozitivnih povratnih informacija kako bi se identifikovali oni koji ostavljaju najkvalitetnije recenzije.
6. **Prezentacija**
      ![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/783e7704-4006-45c9-81d8-8a381879b8df)

![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/7608885a-c1b9-461b-9584-e576c62e1074)

![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/eda07538-cb92-43cc-b576-a0191114b176)



### Zaključak:

Rezultati ove analize pružaju dragocene uvide u to koji autori konzistentno pišu uticajne i korisne recenzije za proizvode koji su popularni među korisnicima sa svetlim tonom kože i suvim tipom kože. Ovo može pomoći u ciljanom marketingu i razvoju proizvoda koji će najbolje odgovarati potrebama ove demografske grupe.

### Zadatak 9: Analiza Proizvoda za Njegu Kože sa Negativnim Recenzijama

**Cilj Analize:**

Cilj ove analize je da identifikuje proizvode iz kategorija 'Skincare' i 'Cleansers' koji su primili negativne preporuke od korisnika sa masnom kožom. Fokus je na proizvodima čija je srednja vrednost ocena ispod 4, što ukazuje da se generalno ne smatraju dovoljno dobrim. Ova analiza će pomoći u identifikovanju proizvoda koji možda zahtevaju poboljšanja ili posebnu pažnju u razvoju i marketingu.

### Detalji Analize:

- **Selekcija Proizvoda:** Izdvajanje proizvoda koji spadaju u kategorije 'Skincare' i 'Cleansers'.
- **Pridruživanje Recenzija:** Povezivanje ovih proizvoda sa recenzijama koje su ostavili korisnici.
- **Filtriranje po Preporukama:** Fokusiranje na recenzije koje nisu preporučene od strane korisnika.
- **Analiza Tipa Kože:** Dalje filtriranje recenzija kako bi se osiguralo da potiču od korisnika sa masnom kožom.
- **Izračunavanje Prosečne Ocene:** Proizvodi se grupišu po identifikatoru, pri čemu se izračunava srednja vrednost ocena za svaki proizvod.
- **Selekcija Proizvoda sa Niskim Ocenama:** Izdvajanje proizvoda čija je prosečna ocena ispod 4.
- **Sortiranje po Relevanciji:** Proizvodi se rangiraju prema ukupnom broju recenzija, sa onima koji imaju najviše recenzija na vrhu liste, što ukazuje na njihovu veću tržišnu relevantnost.
### Zaključak:

Rezultati ove analize pružiće vredne uvide u performanse određenih proizvoda u realnim uslovima korišćenja. Identifikovanje proizvoda sa niskim prosečnim ocenama i negativnim recenzijama od specifičnih korisnika omogućiće Sephori da preispita i potencijalno unapredi formulacije ili pristupe marketinškim strategijama za ove proizvode. Ovo će, nadalje, doprineti poboljšanju zadovoljstva korisnika i jačanju brenda na tržištu. :
![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/97d874ea-b67d-44f0-a632-d5ede224731d)

![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/7ad24568-794a-4f58-9ef7-6edbb5201fe7)


![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/fe3bdb02-21ad-4f83-ba63-e2e63ff584c7)


### Zadatak 10: Analiza Kvalitetnih Proizvoda po Povoljnim Cenama

**Cilj Analize:**

Istražite asortiman proizvoda koji spajaju visoku ocenu korisničkog zadovoljstva s pristupačnošću. Fokusirajte se na proizvode čija se cena kreće u opsegu od 30 do 60 dolara i koji imaju ocene veće od 4, što ukazuje na visok kvalitet brenda Causalie, koji su dostupni ne samo na sajtu. Dodatno, izračunajte i analizirajte sledeće pokazatelje za svaki proizvod:
- **Prosečna Ocena:** Reflektuje generalno korisničko zadovoljstvo.
- **Ukupan Broj Recenzija:** Daje uvid u popularnost i pouzdanost ocena.
- **Procenat Recenzija po Tipu Kože:** Omogućava razumevanje kako različiti tipovi kože reaguju na proizvod.

**Konačni Korak:**
Sortirajte dobijene rezultate po ceni, od najniže ka najvišoj, kako bi se omogućilo lakše identifikovanje najisplativijih opcija.

### Zakljucak:

Ovaj detaljan pristup omogućava ne samo identifikaciju proizvoda koji nude najbolji odnos cene i kvaliteta, već i dublje razumevanje preferencija potrošača zasnovano na tipu kože, čime se olakšava ciljano pozicioniranje proizvoda na tržištu.

**Prezentacija**
![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/182c5cbe-6bb1-4271-bd7a-801620e95841)

![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/c96b17f0-6f55-4eab-9752-491e1b82bd06)
![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/1cb12eb0-df30-464b-a164-13cf415b9bec)
![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/15297a12-bf57-43ac-88b9-048ac0911fb6)








