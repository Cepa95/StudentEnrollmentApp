# StudentEnrollmentApp

OSS Split  
Marina Rodić, viši predavač  
Godina 2022./2023.  


Some functionalities:    
![cover](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/069617d9-833b-43f0-96d3-62d342bcad59)
![login](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/cf2b3f67-6ccf-43a7-8ee8-60cf70a95e33)
![home](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/c5852faa-094e-4541-86a1-afd5e5d883b5)
![add subject](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/f401ca9e-3dbe-434d-9193-160b593ba27b)
![add user](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/333a60c6-ac67-46e7-b200-c390dbe2edcc)
![subjects](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/30dad6e1-2b6c-43d0-8c4a-dc693eae6cdd)
![students](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/a1f796d1-9874-4bca-8d0b-0fc8aeab392f)
![enrollment list](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/698900c5-5c3a-46ca-afb8-1973a56d5d1b)
![remove user](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/43873fef-35d1-4c36-a5a3-a87684e9227b)
![student list](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/35d85372-202e-48ce-b290-b1aa4ea9de3d)
![enrolled subjects](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/7d6a6ca7-56b7-4690-b14b-5a4674b5ab3f)
![remove](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/e402fa0e-45fb-4874-bd7b-7cd0d6211294)
![enroll](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/61b84a4d-1476-4e69-a94f-3597844aab39)







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
![image](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/b2e2420e-4fb6-40e6-8ab4-e9f16ba1c3d9)  



Na „upisnom listu“ svakog studenta se prikazuje lista neupisanih predmeta i lista
upisanih/položenih predmeta podijeljenih po semestrima (ovisno o statusu studenta). Izgled i funkcionalnosti upisnog lista su iste za studente i administratora (osim izbornika u vrhu stranice). Izbornik za studente će imati samo stavku „logout“ i prikazivati će se samo pripadajući upisni list. Izbornik za administratora će imati „logout“, „predmeti“, „studenti“ i „profesori” preko kojih će se pristupati ostalim prikazima. Profesor u izborniku na vrhu stranice ima stavke „predmeti” (prikaz predmeta kojima je on nositelj) i stavku „logout”. Odabirom svakog pojedinog predmeta ima uvid u studente koji su ih upisali i njihove statuse. Kod je potrebno izraditi u radnom okviru Django. Realizirati i organizirati kôd prema MVC (MVT) arhitekturi. Obavezno je imati strukturu koju je relativno lako proširiti sa manjim dodatnim funkcionalnostima (npr. dodati i prikazati zbroj upisanih ECTS bodova). 
Funkcionalnosti i sigurnost su glavne stavke, ali u ocjenu će ulaziti i upotrebljivost sučelja i organizacija kôda.

Primjer izgleda sucelja:
![image](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/c469f4a8-4719-4269-8a62-73ed0ffeb648)  
Slika 1 Odabir studenata sa liste (za mentore). Link za svakog studenta vodi na njegov upisni list.

![image](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/8ceb146e-d675-40f6-a964-c85dc9468165)  
Slika 2 Pregled predmeta (za mentore). Linkovi omogućuju pregled i editiranje podataka o predmetu.

![image](https://github.com/Cepa95/StudentEnrollmentApp/assets/124800316/4b60fdd8-5526-473d-a8cf-04dd15b27c9d)  
Slika 3 Upisni list (pogled mentora za redovnog studenta) za studenta red@oss.hr. Dugmad omogućuju promjenu upisa (upiši/ispiši/položeno).

Pravila.  
Obrana projekta se održava u sklopu ispita. Sastojati će se od pismenog ispita, u vidu jednog ili više zadataka (npr. dodati linkove koji vode na opise predmeta uz prikaz liste predmeta i sl.) kojeg je potrebno odraditi u zadanom vremenskom roku. Nakon pismenog ispita organizirati će se usmeni ispit. Na usmenom ispitu će svaki student prezentirati svoj projekt, te će trebati odgovarati na pitanja vezana uz kôd u projektu. Primjerice - pokazati kroz kôd kako se upiše novi predmet. Projekt je potrebno predati najkasnije tri radna dana prije planiranog ispitnog roka (ako je ispit u utorak-projekt je potrebno predati najkasnije do cetvrtka do 23.59 sati ili ako je ispit u petak projekt je potrebno predati najkasnije do utorka do 23.59 sati). Zakašnjeli projekti se automatizmom prebacuju na idući ispitni rok.
