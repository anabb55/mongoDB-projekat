
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

3. **Izdvajanje Autora iz Recenzija:**
   - Autori recenzija, koji su ranije bili ugrađeni direktno u dokumente recenzija, izdvojeni su u zasebnu kolekciju. Ovo odvajanje omogućava efikasnije upravljanje autorima i njihovim profilima, kao i bolju skalabilnost prilikom ažuriranja podataka o autorima.

4. **Implementacija Indeksa:**
   - Uvedeni su indeksi na ključne kolone koje se često koriste u upitima, kao što su ID proizvoda, ID autora recenzija, i datum slanja recenzije,kao i kombinovani indeks(skin_type,skin_tone) . Ovo je drastično poboljšalo performanse upita, smanjujući vreme potrebno za pretragu i sortiranje podataka.
   - Posebna pažnja je posvećena indeksiranju polja koja učestvuju u operacijama pridruživanja i filtriranja, što je rezultiralo znatno bržim vremenima odziva prilikom izvršavanja složenih analitičkih upita.
   - ![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/9eece655-d738-4861-9f53-ed8a20166eaa)

#### Očekivani Rezultati

Projekat će omogućiti dublji uvid u preferencije i ponašanje potrošača Sephore, identifikovati ključne faktore koji utiču na zadovoljstvo korisnika, i pomoći u optimizaciji asortimana proizvoda. Rezultati će biti ključni za strategije poboljšanja proizvoda i prilagođavanja ponude prema specifičnim potrebama i željama kupaca.



### Zadatak 1: Analiza udela komentara za proizvode u kategoriji "Treatments"

[Upit pre optimizcije](https://github.com/anabb55/mongoDB-projekat/blob/main/Queries/query1.txt) | [Upit nakon optimizacije](https://github.com/anabb55/mongoDB-projekat/blob/main/Queries/query1-optimized.txt)

**Cilj Analize:**

Cilj ove analize je izračunati udeo komentara koje su ostavile osobe čiji je tip kože "dry" u odnosu na ukupan broj komentara koji se odnose na proizvode iz sekundarne kategorije "Treatments" i čija je cena manja od 50 USD. Pomoću ovog upita dobijamo uvid u to koliko osobe sa suvom kožom komentarišu jeftinije Treatments proizvode.

### Detalji Analize:

1. **Spajanje Komentara sa Proizvodima:**

Komentari iz kolekcije reviews1 se spajaju sa informacijama o proizvodima iz kolekcije products1 pomoću product_id. Ovo povezuje svaki komentar sa odgovarajućim proizvodom.


2. **Filtriranje po Sekundarnoj Kategoriji i Ceni:**

Nakon spajanja, filtriraju se proizvodi iz kategorije "Treatments" čija je cena manja od 50 USD. Time se osigurava analiza samo relevantnih proizvoda.


3. **Spajanje Komentara sa Autorima:**

Filtrirani komentari se spajaju sa informacijama o autorima iz kolekcije authors pomoću stranog kljuca. Ovaj korak omogućava pristup informacijama o tipu kože autora komentara.


4. **Grupisanje po Tipu Kože:**

Komentari se grupišu prema tipu kože autora (skin_type), a za svaki tip kože se računa ukupan broj komentara (total_reviews).


5. **Izračunavanje Ukupnog Broja Komentara i Komentara za "Dry" Tip Kože:**

Komentari se ponovo grupišu kako bi se izračunao ukupan broj komentara (total_reviews) i broj komentara od korisnika sa "dry" tipom kože (dry_skin_reviews).


6. **Izračunavanje Udela:**

Na kraju se računa udeo komentara koje su ostavili korisnici sa "dry" tipom kože u odnosu na ukupan broj komentara. Ako nema komentara, udeo se postavlja na 0 kako bi se izbegla greška deljenja sa nulom.

**Optimizacija je postignuta uz pomoć narednih koraka:**

1. **Filtriranje podataka pre spajanja:**
Upit je optimizovan tako što je prvo izvršeno filtriranje proizvoda koji se prodaju samo online, smanjujući količinu podataka koji se dalje obrađuju. Ovo unapred filtriranje omogućava da se u kasnijim fazama upita radi sa manjim skupom podataka, što ubrzava celokupan proces. Promena redosleda oepracija u agregacionom pipeline-u dovodi do ynatno bržeg izvršavanja upita

2. **Indeks na Stranom Ključu product_id u Recenzijama:**
Dodavanje indeksa na polje product_id u kolekciji reviews_final značajno ubrzava operacije spajanja (joins) između proizvoda i njihovih recenzija. Indeks na stranom kljucu omogućava da se brzo pronađu i spoje relevantni dokumenti, čime se drastično smanjuje vreme pretrage i povećava efikasnost upita.

```javascript
   db.reviews_final.createIndex({ product_id: 1 });
   ```

  **Explain plan pre optimizacije:**
  
![query1-initial](https://github.com/anabb55/mongoDB-projekat/assets/75089113/f0c582b1-ee04-45d1-af6f-357ea32e4ff5)

**Explain plan nakon optimizacije:**

![query1-optimized](https://github.com/anabb55/mongoDB-projekat/assets/75089113/ac2f6898-97a4-4252-8cd1-2462672c7751)

**Grafički prikaz rezultata uz pomoć alata Metabase:**

![query1Metabase](https://github.com/anabb55/mongoDB-projekat/assets/75089113/48ef4191-955a-4bf0-b0f4-5c53f97c5ee5)     ![query11Metabase](https://github.com/anabb55/mongoDB-projekat/assets/75089113/0cfd21cd-82ef-4d89-bdda-7358b6c14142)



### Zadatak 2: Rangiranje proizvoda koji se prodaju samo online po negativnim feedback-ovima na njihove komentare
[Upit pre optimizacije](https://github.com/anabb55/mongoDB-projekat/blob/main/Queries/query2.txt) | [Upit nakon optimizacije](https://github.com/anabb55/mongoDB-projekat/blob/main/Queries/query2-optimized.txt)

**Cilj Analize:**

Cilj  analize je rangiranje proizvoda koji se isključivo prodaju online i koji su ocenjeni u periodu od 01.01.2018. do 01.01.2023. prema broju negativnih feedback-ova na komentare koje se odnose na njih. Za svaki proizvod je potrebno prikazati naziv proizvoda, naziv brenda, primarnu kategoriju i broj negativnih komentara. Komentari se prate dugoročno(period od 5 godina) kako bi se uočila neka pravilnost.

### Detalji Analize:

1. **Filtriranje Proizvoda koji se Prodaju Samo Online:**
Proizvodi se filtriraju kako bi se identifikovali samo oni koji su dostupni isključivo putem online prodaje.

2. **Spajanje sa Komentarima:**
Komentari koje su korisnici ostavili za proizvode se spajaju sa odgovarajućim proizvodima koristeći identifikator proizvoda (product_id).

3. **Filtriranje po Datumu Ocene:**
Nakon spajanja, komentari se dodatno filtriraju kako bi se obuhvatili samo oni koji su ostavljeni u definisanom vremenskom periodu (od 1. januara 2018. do 1. januara 2023.). Ovo ograničenje datuma je ključno za fokusiranje analize na relevantne podatke.

4. **Grupisanje i Agregacija Podataka:**
Komentari se grupišu po svakom proizvodu radi izračunavanja ukupnog broja negativnih feedback-ova (total_neg_feedback_count) i ukupnog broja komentara (review_count). Ove agregirane informacije pružaju statistički pregled zadovoljstva korisnika i potencijalnih problema sa proizvodima.

5. **Rangiranje Proizvoda:**
Konačno, proizvodi se rangiraju u opadajućem redosledu prema ukupnom broju negativnih feedback-ova. Ovo rangiranje pomaže u identifikaciji proizvoda koji možda imaju najviše problema ili nezadovoljstva među korisnicima, što može biti pokazatelj potrebe za poboljšanjima ili dodatnim istraživanjem.

**Optimizacija je postignuta uz pomoć narednih koraka:**

1. **Uvođenje Šablona Proširene Reference i Eliminisanje Lookupa:**
Prethodno su FeedbackStatistics bili smešteni u zasebnoj kolekciji, što je zahtevalo dodatni lookup prilikom spajanja podataka. Uvođenjem šablona proširene reference, FeedbackStatistics su sada integrisani direktno unutar dokumenata recenzija. Ova promena eliminiše potrebu za dodatnim lookup operacijama, smanjujući složenost upita i ubrzavajući izvršavanje.FeedbackStatistics prirodno pripadaju recenzijama, čineći strukturu podataka logičnijom i koherentnijom.

2. **Indeks na Stranom Ključu product_id u Recenzijama:**
Kao i u prethodnom upitu imamo indeks na stranom ključu. Dodavanje indeksa na polje product_id u kolekciji reviews_final značajno ubrzava operacije spajanja (joins) između proizvoda i njihovih recenzija. Indeks na stranom kljucu omogućava da se brzo pronađu i spoje relevantni dokumenti, čime se drastično smanjuje vreme pretrage i povećava efikasnost upita.

**Explain plan pre optimizacije:**

![query2-initial](https://github.com/anabb55/mongoDB-projekat/assets/75089113/02201a51-ca8e-433f-bcf9-134f71348382)

**Explain plan nakon optimizacije:**

![query2-optimized](https://github.com/anabb55/mongoDB-projekat/assets/75089113/d28725ed-4e47-4e22-a185-bfdedc2e678a)

**Grafički prikaz rezultata uz pomoć alata Metabase:**

![query2Metabase](https://github.com/anabb55/mongoDB-projekat/assets/75089113/ccd98c28-6a72-4289-b332-0484a3bf78e5)

![query22Metabase](https://github.com/anabb55/mongoDB-projekat/assets/75089113/b9b6aa94-e2ab-4118-85b8-7668eb63cdb1)


### Zadatak 3: Identifikacija Vodećih Brendova za Cleansers Proizvode kod Osoba sa Normalnom Kožom
[Upit pre optimizacije](https://github.com/anabb55/mongoDB-projekat/blob/main/Queries/query3.txt) | [Upit nakon optimizacije] (https://github.com/anabb55/mongoDB-projekat/blob/main/Queries/query3-optimized.txt)

**Cilj Analize:**
Cilj ove analize je identifikovati 10 brendova koji imaju najviše komentara od korisnika sa normalnim tipom kože za proizvode iz sekundarne kategorije "Cleansers". Pored toga, potrebno je izračunati broj proizvoda iz kategorije "Cleansers" koji pripadaju svakom brendu, kao i ukupni broj komentara za te proizvode. Ova analiza pruža uvid u popularnost proizvoda određenih brendova među korisnicima sa normalnim tipom kože.

### Detalji Analize:

Analiza obuhvata sledeće korake:

1. **Filtriranje po Kategoriji Proizvoda:** Prvo se vrši filtriranje proizvoda koji pripadaju sekundarnoj kategoriji "Cleansers".

2. **Spajanje sa Komentarima:** Komentari iz kolekcije reviews_final se spajaju sa odgovarajućim proizvodima koristeći product_id.

3. **Filtriranje po Tipu Kože:** Samo komentari korisnika sa "normal" tipom kože se uzimaju u obzir.

4. **Grupisanje po Brendovima:** Komentari se grupišu po brand_id kako bi se izračunao ukupan broj komentara za Cleansers proizvode svakog brenda.

5. **Sortiranje i Limitiranje Rezultata:** Brendovi se sortiraju po ukupnom broju komentara u opadajućem redosledu, prikazujući samo top 10 brendova.

**Optimizacija je postignuta uz pomoć narednih koraka:**

1. **Efikasnije korišćenje polja u agregaciji:**
 U optimizovanom upitu se koriste samo neophodna polja za grupisanje i projekciju, dok prethodni upit koristi veći broj polja u dodavanju novih polja ($addFields) i projekciji, što može povećati složenost i vreme izvršavanja.

2. **Uklanjanje nepotrebnih projekcija:**
 Optimizovani upit izbegava nepotrebne projekcije ($project) koje su bile prisutne u prethodnom upitu, čime se smanjuje broj operacija i potreban resurs.

3. **Indeks na Stranom Ključu product_id u Recenzijama**

**Explain plan pre optimizacije**
![query3-initial](https://github.com/anabb55/mongoDB-projekat/assets/75089113/6317b7b0-a293-4984-bcac-58e874d430c1)

**Explain plan nakon optimizacije**
![query3-optimized](https://github.com/anabb55/mongoDB-projekat/assets/75089113/54660d03-7fe7-447e-97ce-b4f0c1c54f29)

**Grafički prikaz rezultata uz pomoć alata Metabase:**
![query3Metabase](https://github.com/anabb55/mongoDB-projekat/assets/75089113/3883ec09-802c-4ebd-bfa8-a5d5b64eba89)
![query33Metabase](https://github.com/anabb55/mongoDB-projekat/assets/75089113/61aaa9d9-75d6-4171-9e00-83735de9a343)






### Zadatak 6: Analiza Proizvoda za Njegu Lica Brendiranih za Sephoru
[Upit pre optimizacije](https://github.com/anabb55/mongoDB-projekat/blob/main/Queries/query6.txt)| [Upit nakon optimizacije](https://github.com/anabb55/mongoDB-projekat/blob/main/Queries/query6Opt.txt)


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

Izvršavanje upita je značajno ubrzano zahvaljujući sledećim optimizacijama:

1. **Ugnježdenje Varijacija u Proizvodima**:
   - Prethodno su varijacije bile u zasebnoj kolekciji, što je zahtevalo dodatni `lookup` prilikom spajanja podataka. Sada su varijacije integrisane direktno unutar dokumenata proizvoda, eliminisajući potrebu za dodatnim `lookup` operacijama. Ova promjena smanjuje složenost upita i ubrzava izvršavanje, jer MongoDB više ne mora pretraživati dodatnu kolekciju za podatke o varijacijama.

2. **Indeks na Stranom Ključu `product_id` u Recenzijama**:
   - Dodavanje indeksa na polje `product_id` u kolekciji `reviews_final` značajno ubrzava operacije spajanja (joins) između proizvoda i njihovih recenzija. Indeksi omogućavaju MongoDB-u da brzo pronađe i spoji relevantne dokumente, čime se drastično smanjuje vreme pretrage i povećava efikasnost upita.

   ```javascript
   db.reviews_final.createIndex({ product_id: 1 });
   ```

3. **Precizno Postavljanje Tipova Podataka u Refaktorisanoj Šemi**:
   - Prilikom refaktorisanja šeme baze podataka, pažljivo su postavljeni odgovarajući tipovi podataka (npr. string, int, double) za svako polje. Ova optimizacija eliminiše potrebu za dodatnim koracima konverzije tipova podataka tokom izvršavanja upita. Sada MongoDB može direktno raditi sa podacima u njihovim odgovarajućim formatima, čime se poboljšava brzina i efikasnost obrade podataka.
     
![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/ac072d20-b5b6-4ed8-8432-f04146adcacb)





### Zadatak 7: Analiza Najuticajnijih Recenzija
[Upit pre optimizacije](https://github.com/anabb55/mongoDB-projekat/blob/main/Queries/query7.txt
)| [Upit nakon optimizacije](https://github.com/anabb55/mongoDB-projekat/blob/main/Queries/query7-opt)


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

U nedavnom slučaju optimizacije, primetili smo da je dodavanje indeksa značajno poboljšalo performanse upita. Konkretno, dva ključna koraka su dovela do značajnog smanjenja vremena izvršavanja upita na samo 90 ms:

1. **Indeksi na Stranim Ključevima**: 
   - Dodavanje indeksa na polja koja se koriste za `lookup` operacije, kao što su strani ključevi, omogućava brže povezivanje podataka između kolekcija.
   - Ovo optimizuje operacije spajanja (joins) koje su često glavni faktor usporavanja upita u MongoDB-u.

2. **Indeks na Polju `submission_time`**:
   - Kreiranje indeksa na polju `submission_time` dodatno je poboljšalo performanse upita. 
   - Pošto je ovo polje često korišćeno u filtriranju rezultata prema vremenskom okviru, indeksiranje omogućava brže pretraživanje i sortiranje podataka na osnovu vremenskih kriterijuma.
3. **Ugnježdenje feedbackStatistic** unutar recenzije eliminisalo je potrebu za dodatnim lookup operacijama, što je dodatno smanjilo složenost i vreme izvršavanja upita.

Kombinacijom ovih optimizacija, vreme izvršavanja upita je smanjeno sa potencijalno visokih vrednosti na samo 90 ms, čineći upite efikasnijim i bržim.

---

**Metabase grafici**
![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/599e2d61-3f5d-4d04-8d64-d58d6464f4ee)
![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/166dd849-8f8a-4cda-8a6a-3b553a7e0181)



### Zaključak:

Ovom analizom dobijamo jasan uvid u koje recenzije imaju najveći uticaj među potrošačima, što može poslužiti kao dragocen alat za unapređenje proizvoda i marketinških strategija. Identifikacija recenzija sa visokom ocenom korisnosti i značajnim brojem povratnih informacija pomaže u razumevanju šta korisnici cene kod proizvoda, a visoki procenti pozitivnih povratnih informacija mogu istaći proizvode koji su dobro prihvaćeni na tržištu.


### Zadatak 8: Identifikacija Najuticajnijih Autora Recenzija na Osnovu Tipa Kože

[Upit pre optimizacije](https://github.com/anabb55/mongoDB-projekat/blob/main/Queries/query8.txt
)| [Upit nakon optimizacije](https://github.com/anabb55/mongoDB-projekat/blob/main/Queries/query8-opt)

**Cilj Analize:**

Cilj ove analize je identifikovati autore sa svetlim tonom kože i suvim tipom kože koji su napisali visoko ocenjene recenzije (ocena veća od 4). Analiza se fokusira na recenzije koje su korisnici označili kao korisne i koje imaju više pozitivnih nego negativnih povratnih informacija. Krajnji cilj je prikazati autore čije recenzije dobijaju najviše pozitivnih povratnih informacija, kako bi se prepoznali oni koji ostavljaju najuticajnije i najkorisnije recenzije.

### Detalji Analize:

1. **Selekcija Autora:** Identifikacija autora sa 'light' tonom kože i 'dry' tipom kože.

2. **Pridruživanje i Analiza Recenzija:** Pridruživanje recenzija ovim autorima i filtriranje recenzija sa ocenama većim od 4.

3. **Pridruživanje Povratnih Informacija:** Analiza povratnih informacija za svaku recenziju kako bi se osiguralo da su označene kao korisne i da imaju više pozitivnih nego negativnih povratnih informacija.

4. **Kvantifikacija Uticaja:** Izračunavanje ukupnog broja pozitivnih povratnih informacija koje su recenzije svakog autora primile.

5. **Rangiranje Autora:** Sortiranje autora prema ukupnom broju pozitivnih povratnih informacija kako bi se identifikovali oni koji ostavljaju najkvalitetnije recenzije.
6. **Prezentacija**
![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/49636a4b-2721-4643-85ba-7463b75f7380)
**Explain pre optimizacije:**
Upit traje predugo zbog velike količine podataka!


**Explain nakon optimizacije:**
![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/3ca90108-56e4-4a4c-831b-b1debb9fc918)
Da bi se bolje razumelo kako su optimizacije doprinele bržem izvršavanju upita, sledeća objašnjenja ističu ključne promene koje su implementirane:

---

Izvršavanje upita je značajno ubrzano zahvaljujući sledećim optimizacijama:

1. **Dodavanje Indeksa na Polje `author_id` u Kolekciji Recenzija**:
Indeks na `author_id` omogućava MongoDB-u da brzo pronađe sve recenzije koje pripadaju određenom autoru, značajno smanjujući vreme pretrage.

   ```javascript
   db.reviews_final.createIndex({ author_id: 1 });
   ```

2. **Ugnježdenje `feedbackStatistic` unutar Recenzija**:
   - Pre restrukturiranja, podaci o povratnim informacijama (`feedbackStatistic`)  bili su smešteni u zasebnoj kolekciji, što je zahtevalo dodatne `lookup` operacije za njihovo povezivanje sa recenzijama. Sada su `feedbackStatistic` podaci integrisani direktno unutar dokumenata recenzija. 
   - **Prednosti**: Ovo eliminiše potrebu za dodatnim `lookup` operacijama i omogućava direktan pristup informacijama o povratnim informacijama unutar svake recenzije. Time se smanjuje složenost upita i ubrzava proces pristupa podacima.
---

Ovaj tekst detaljno objašnjava kako su specifične optimizacije doprinele bržem izvršavanju upita u MongoDB-u.
![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/eda07538-cb92-43cc-b576-a0191114b176)



### Zaključak:

Rezultati ove analize pružaju dragocene uvide u to koji autori konzistentno pišu uticajne i korisne recenzije za proizvode koji su popularni među korisnicima sa svetlim tonom kože i suvim tipom kože. Ovo može pomoći u ciljanom marketingu i razvoju proizvoda koji će najbolje odgovarati potrebama ove demografske grupe.

### Zadatak 9: Analiza Proizvoda za Njegu Kože sa Negativnim Recenzijama

[Upit pre optimizacije](https://github.com/anabb55/mongoDB-projekat/blob/main/Queries/query9.txt
)| [Upit nakon optimizacije](https://github.com/anabb55/mongoDB-projekat/blob/main/Queries/query9-opt)

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

**Explain pre optimizacije:**
Upit traje predugo zbog velike količine podataka!
![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/7ad24568-794a-4f58-9ef7-6edbb5201fe7)
---

Izvršavanje upita je značajno ubrzano zahvaljujući sledećim optimizacijama:

1. **Dodavanje Indeksa na Polje `author_id` u Kolekciji Recenzija**:
Indeks na `author_id` omogućava MongoDB-u da brzo pronađe sve recenzije koje pripadaju određenom autoru, značajno smanjujući vreme pretrage.

   ```javascript
   db.reviews_final.createIndex({ author_id: 1 });
   ```

2. **Dodavanje Indeksa na Polje `product_id` u Kolekciji Recenzija**:
Indeks na `product_id` omogućava MongoDB-u da brzo pronađe sve recenzije koje pripadaju određenom proizvodu, značajno smanjujući vreme pretrage.

   ```javascript
   db.reviews_final.createIndex({ product_id: 1 });
---

![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/fe3bdb02-21ad-4f83-ba63-e2e63ff584c7)


### Zadatak 10: Analiza Kvalitetnih Proizvoda po Povoljnim Cenama

[Upit pre optimizacije](https://github.com/anabb55/mongoDB-projekat/blob/main/Queries/query10.txt
)| [Upit nakon optimizacije](https://github.com/anabb55/mongoDB-projekat/blob/main/Queries/query10-opt)

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
**Explain pre optimizacije:**
Upit traje predugo zbog velike količine podataka!
![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/c96b17f0-6f55-4eab-9752-491e1b82bd06)

![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/1cb12eb0-df30-464b-a164-13cf415b9bec)
![image](https://github.com/anabb55/mongoDB-projekat/assets/109462923/15297a12-bf57-43ac-88b9-048ac0911fb6)








