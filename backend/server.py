from feed_manager import manage_feeds, save_updates
import json

def main():
    # Φορτώνουμε τα δεδομένα από το feeds.json με UTF-8 encoding
    with open('feeds.json', 'r', encoding='utf-8') as file:
        feeds_data = json.load(file)
    
    # === Κατηγοριοποίηση των feeds ===
    eu_feeds = []
    literary_feeds = []

    for feed in feeds_data:
        feed_url = feed.get('url', '')

        # Κατηγοριοποίηση με βάση το URL
        # === Ευρωπαϊκή Ένωση ===
        if ("europarl" in feed_url or 
            "consilium" in feed_url or 
            "europa" in feed_url):
            eu_feeds.append(feed)
        
        # === Λογοτεχνικά Περιοδικά ===
        elif ("vakxikon" in feed_url or "diastixo" in feed_url or 
              "tahomaliteraryreview" in feed_url or "theoffingmag" in feed_url):
            literary_feeds.append(feed)

    # === Εμφάνιση Επιλογών Κατηγοριοποιημένες ===
    print("\n=== Ευρωπαϊκή Ένωση ===")
    for idx, feed in enumerate(eu_feeds, start=1):
        print(f"{idx}. {feed['name']}")

    print("\n=== Λογοτεχνικά Περιοδικά ===")
    for idx, feed in enumerate(literary_feeds, start=len(eu_feeds) + 1):
        print(f"{idx}. {feed['name']}")

    # Ζητάμε από τον χρήστη να επιλέξει feed
    choice = input("\nΕισάγετε τον αριθμό της επιλογής σας: ")

    # Εύρεση του επιλεγμένου feed
    try:
        choice = int(choice) - 1
        
        # Έλεγχος αν η επιλογή ανήκει στην Ευρωπαϊκή Ένωση
        if choice < len(eu_feeds):
            selected_feed = eu_feeds[choice]
        else:
            # Αλλιώς είναι στην κατηγορία Λογοτεχνικά Περιοδικά
            literary_index = choice - len(eu_feeds)
            selected_feed = literary_feeds[literary_index]

        print(f"\nΕπιλέξατε το feed: {selected_feed['name']}")

        # Διαχείριση του feed μέσω του feed_manager.py
        feeds = manage_feeds([selected_feed])
        
        # Έλεγχος αν τα δεδομένα είναι κενά πριν την αποθήκευση
        if feeds:
            save_updates(feeds)
        else:
            print("Δεν βρέθηκαν δεδομένα για αποθήκευση.")
    
    except (ValueError, IndexError):
        print("Μη έγκυρη επιλογή!")

if __name__ == "__main__":
    main()
