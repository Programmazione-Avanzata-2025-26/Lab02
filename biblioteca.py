import csv
def carica_da_file(file_path):
    """Carica i libri dal file"""
    # TODO

    import csv

    dizionario=dict() # dizionario vuoto2


    try:
        with open(file_path) as csvfile:
            libri= csv.reader(csvfile) # leggo con lo strumento del csv
            lista=(list(libri)) # aggiungo i libri letti uno per uno in una lista

        for el in range(0,len(lista)):
            sezione=int(lista[el][-1]) #prende le singole liste contenenti un singolo libro
                                      # e prende l'ultimo elemento, ovvero la sezione

            if sezione not in dizionario:
                dizionario[sezione]=[]
            dizionario[sezione].append(lista[el]) #aggiunge alla lista i singoli libri
            dizionario= dict(sorted(dizionario.items()))#gli ordina nel dizionario in base alla sezione

    except FileNotFoundError:
        print(f"Il file digitato non è stato trovato:{file_path},\n riprova")

    return dizionario


def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    # TODO
    new_book= [] # aggiungo il libro inserito in input
    new_book.append(titolo)
    new_book.append(autore)
    new_book.append(anno)
    new_book.append(pagine)
    new_book.append(sezione)
    if sezione <= max(biblioteca.keys()): #se la sezione esiste
        trovato= False
        for keys, list in biblioteca.items(): # itero su chiave valore, il valore è una lista di liste
            for el in list: # prendo le singole liste dalla lista complessiva
                if el[0].lower()== new_book[0].lower(): #prende il titolo del nuovo libro
                                                        # e lo confronto con i titoli presdenti nel dizionario
                    trovato = True #cambio valore per uscire dal ciclo
                    break

            if trovato:
                break

        if trovato:
            print("il libro è già presente nel data base")
        else: # se non trova il libro vuol dire che non è presente nel data base
            biblioteca[sezione].append(new_book)# lo aggiungo al dizionario

            with open(file_path, mode="a", newline="") as csvfile: # modifico il file aggiungendo il new_book
                #"a" in modalità append, aggiungo. newline="" evita di far mettere in automatico l'acapo
                AddFile = csv.writer(csvfile)
                AddFile.writerow(new_book)
                csvfile.close()

            return new_book,print(f"è stato aggiunto:{new_book}")
    else:
        print("non esiste la sezione")



def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO
    trovato= False
    for  chiave, lista_liste in biblioteca.items(): # itero su chaive valore, di liste di liste
        for lista in lista_liste: #cerco le singole liste
            for i in range(len(lista)):
                if lista[0].lower() == titolo.lower(): #confronto i titoli
                    # .lower perché così confronto tutto in minuscolo
                    trovato = True
                    return lista

    if trovato == False: #se non trovo il libro
        print("Il libro non è presente nel data base")



def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
    if sezione in biblioteca: # se la sezione è nelle chiavi della biblioteca
        biblioteca[sezione]= sorted(biblioteca[sezione])#ordina la lista in ordine crescente
        print(f"la sezione {sezione} è stata ordinata, il nuovo ordine è:{biblioteca[sezione]}")
    else:#se non lo trova
        print(f"non esiste la sezione {sezione} digitata")



def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

