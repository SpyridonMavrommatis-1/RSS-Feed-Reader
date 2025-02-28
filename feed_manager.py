import feedparser
import csv

# Συνάρτηση για τη διαχείριση των feeds
def manage_feeds(feeds_data):
    feeds = []

    # === DEBUGGING ===
    print("Τύπος feeds_data:", type(feeds_data))
    print("Περιεχόμενο feeds_data:", feeds_data)

    # Λίστες με λέξεις-κλειδιά για κάθε κατηγορία
    literary_keywords = ["vakxikon", "diastixo", "tahomaliteraryreview", "theoffingmag"]
    eu_keywords = ["europarl", "consilium", "europa"]

    # Διαχειριζόμαστε κάθε feed ξεχωριστά
    for feed in feeds_data:  
        print("Τύπος feed:", type(feed))
        print("Περιεχόμενο feed:", feed)

        # Παίρνουμε το URL του feed
        feed_url = feed.get('url')  
        print("URL feed:", feed_url)

        # Έλεγχος αν το URL είναι έγκυρο
        if not feed_url:
            print("Το feed δεν έχει έγκυρο URL.")
            continue
        
        # Χρησιμοποιούμε το feedparser για να αναλύσουμε το feed
        parsed_feed = feedparser.parse(feed_url)

        # Έλεγχος για σφάλματα κατά την ανάλυση του feed
        if parsed_feed.bozo:
            print(f"Σφάλμα κατά την ανάλυση του feed: {feed['url']}")
            continue

        # Δυναμική κατηγοριοποίηση με λίστες λέξεων-κλειδιών
        if any(keyword in feed_url for keyword in literary_keywords):
            category = "Λογοτεχνικά Περιοδικά"
        elif any(keyword in feed_url for keyword in eu_keywords):
            category = "Ευρωπαϊκή Ένωση"
        else:
            category = "General"

        # Προσθέτουμε τα δεδομένα στη λίστα
        feeds.append({
            'category': category,
            'name': feed.get('name', 'Άγνωστο Όνομα'),
            'url': feed_url,
            'entries': parsed_feed.entries
        })

    print("Περιεχόμενο feeds στο τέλος του manage_feeds:", feeds)
    return feeds

# Συνάρτηση για την αποθήκευση των δεδομένων σε CSV
def save_updates(parsed_data):
    print(f"Αποθηκεύονται τα δεδομένα: {parsed_data}")
    
    # Χρησιμοποιούμε UTF-8-SIG για σωστή εμφάνιση ελληνικών χαρακτήρων
    with open('updates.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['Category', 'Feed Name', 'Title', 'Link', 'Published Date'])

        for feed in parsed_data:
            category = feed['category']
            name = feed['name']

            for entry in feed['entries']:
                # Εξαγωγή δεδομένων από κάθε entry
                title = entry.get('title', 'Χωρίς τίτλο')
                link = entry.get('link', '')
                published = entry.get('published', 'Χωρίς ημερομηνία')

                # Διασφαλίζουμε ότι οι τίτλοι δεν κόβονται λόγω ειδικών χαρακτήρων
                writer.writerow([category, name, title.strip(), link.strip(), published.strip()])

    print("Τα αποτελέσματα αποθηκεύτηκαν επιτυχώς στο updates.csv!")  
