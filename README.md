# StudentEnrollmentApp

OSS Split  
Marina Rodić, viši predavač  
Godina 2022./2023.  


Some functionalities:  
![cover](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/c69efcea-1546-4ab9-9906-e2d61e6ed312)
![login](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/1d8e8418-d379-4b5c-8b54-c191a1cd1c69)
![admin](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/385b8c6e-b4c6-45c0-aa07-3e5523160508)
![add](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/fea61767-444d-4f09-a9ee-62762b9cf44b)
![remove](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/e3bf285b-68f4-488c-a67f-9fc96023f82c)
![subjects](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/9e51d289-3cd0-44e0-8bf9-54c51e423618)
![professor](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/fddad0ea-eb06-436f-8b11-a997ecfb72c5)
![students](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/3ead5abe-6383-4574-8bf7-ec8d761314c9)
![user](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/c80bc8b1-74e3-4d29-a980-a4ded69eb9b4)











Zadatak za projekt  
Izraditi sustav za upis studenata. Sustav ce se sastojati od tri uloge: student, profesor i administrator.

Uloga administrator:
- autentikacija
- pregled i promjena liste predmeta
- dodavanje novog predmeta
- dodjeljivanje predmeta profesoru
- pregled liste studenata
- dodavanje i editiranje studenata
- izrada/promjena upisnog lista za bilo kojeg studenta
- pregled liste profesora
- dodavanje i editiranje profesora
- pregled popisa studenata za svaki pojedinacni predmet (na svaki predmet dodati link „vidi popis studenata”)
- za administrator ulogu nije dozvoljeno koristiti Djangov admin sustav

Uloga profesor:
- autentikacija
- pregled liste predmeta prijavljenog profesora
- pregled popisa studenata na pojedinom kolegiju (kojem je prijavljeni profesor nositelj)
- mijenjanje statusa predmeta (po defaultu je samo upisan, a moze se promijeniti u „polozen” ili „izgubio potpis”. Predmet se moze ispisati sve dok mu status nije promijenjen u polozen/izgubio potpis)
- pregled studenata na svakom pojedinom predmetu prema sljedecim kriterijima:
1. studenti koji su izgubili potpis
2. studenti koji su dobili potpis, ali jos nisu polozili predmet
3. studenti koji su polozili predmet

Uloga student:
- autentikacija
- upis/ispis predmeta

Sve promjene u bazi vršiti preko POST zahtjeva. Obratiti pažnju na sigurnost aplikacije (kriptiranje lozinki, SQL injection i XSS). Strukturu baze koja je na slici nize treba prilagoditi potrebama ovog zadatka. Potrebno je dodati novu tablicu „uloge” u kojoj ce se
definirati uloge „admin”, „profesor” i „student” (u tablici korisnici izmijeniti stupac „uloga” iz
„enum” tipa podatka i napraviti relaciju na tablicu „uloge”). Tablica „korisnici” se razlikuje od Django-ve tablice User. Potrebno ju je prilagoditi (vidi predavanja). Takodjer je potrebno prosiriti tablicu „predmeti” sa stupcem koji definira nositelja kolegija. Taj stupac ce biti strani kljuc, a vezat ce se na tablicu korisnici. Na aplikacijskoj razini je nuzno voditi racuna kako se za nositelja kolegija moze postaviti samo korisnik koji ima ulogu profesor.
![image](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/b8b46479-dbd6-4915-b644-9754f8d25f38)



Na „upisnom listu“ svakog studenta se prikazuje lista neupisanih predmeta i lista
upisanih/položenih predmeta podijeljenih po semestrima (ovisno o statusu studenta). Izgled i funkcionalnosti upisnog lista su iste za studente i administratora (osim izbornika u vrhu stranice). Izbornik za studente će imati samo stavku „logout“ i prikazivati će se samo pripadajući upisni list. Izbornik za administratora će imati „logout“, „predmeti“, „studenti“ i „profesori” preko kojih će se pristupati ostalim prikazima. Profesor u izborniku na vrhu stranice ima stavke „predmeti” (prikaz predmeta kojima je on nositelj) i stavku „logout”. Odabirom svakog pojedinog predmeta ima uvid u studente koji su ih upisali i njihove statuse. Kod je potrebno izraditi u radnom okviru Django. Realizirati i organizirati kôd prema MVC (MVT) arhitekturi. Obavezno je imati strukturu koju je relativno lako proširiti sa manjim dodatnim funkcionalnostima (npr. dodati i prikazati zbroj upisanih ECTS bodova). 
Funkcionalnosti i sigurnost su glavne stavke, ali u ocjenu će ulaziti i upotrebljivost sučelja i organizacija kôda.

Primjer izgleda sucelja:
![image](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/ea561ddd-32f3-4edc-802c-15fec8f32387)  
Slika 1 Odabir studenata sa liste (za mentore). Link za svakog studenta vodi na njegov upisni list.

![image](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/8cbf8dba-75b6-48e3-b550-4fc83511732e)   
Slika 2 Pregled predmeta (za mentore). Linkovi omogućuju pregled i editiranje podataka o predmetu.

 ![image](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/829b070c-475e-4c5a-8007-66aa3470b8b1)

Slika 3 Upisni list (pogled mentora za redovnog studenta) za studenta red@oss.hr. Dugmad omogućuju promjenu upisa (upiši/ispiši/položeno).

Pravila.  
Obrana projekta se održava u sklopu ispita. Sastojati će se od pismenog ispita, u vidu jednog ili više zadataka (npr. dodati linkove koji vode na opise predmeta uz prikaz liste predmeta i sl.) kojeg je potrebno odraditi u zadanom vremenskom roku. Nakon pismenog ispita organizirati će se usmeni ispit. Na usmenom ispitu će svaki student prezentirati svoj projekt, te će trebati odgovarati na pitanja vezana uz kôd u projektu. Primjerice - pokazati kroz kôd kako se upiše novi predmet. Projekt je potrebno predati najkasnije tri radna dana prije planiranog ispitnog roka (ako je ispit u utorak-projekt je potrebno predati najkasnije do cetvrtka do 23.59 sati ili ako je ispit u petak projekt je potrebno predati najkasnije do utorka do 23.59 sati). Zakašnjeli projekti se automatizmom prebacuju na idući ispitni rok.
