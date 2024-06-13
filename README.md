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
   - Uvedeni su indeksi na ključne kolone koje se često koriste u upitima, kao što su ID proizvoda, ID autora recenzija, i datum slanja recenzije,kao i rating . Ovo je drastično poboljšalo performanse upita, smanjujući vreme potrebno za pretragu i sortiranje podataka.
   - Posebna pažnja je posvećena indeksiranju polja koja učestvuju u operacijama pridruživanja i filtriranja, što je rezultiralo znatno bržim vremenima odziva prilikom izvršavanja složenih analitičkih upita.


#### Očekivani Rezultati

Projekat će omogućiti dublji uvid u preferencije i ponašanje potrošača Sephore, identifikovati ključne faktore koji utiču na zadovoljstvo korisnika, i pomoći u optimizaciji asortimana proizvoda. Rezultati će biti ključni za strategije poboljšanja proizvoda i prilagođavanja ponude prema specifičnim potrebama i željama kupaca.

