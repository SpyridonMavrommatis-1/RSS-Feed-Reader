# Συνάρτηση για την ανάλυση των δεδομένων από το RSS feed
def parse_feed(entries):
    parsed_data = []
    
    # Για κάθε είσοδο (entry) από το RSS feed
    for entry in entries:
        # Εξάγουμε τα απαραίτητα δεδομένα από κάθε entry
        title = entry.get('title', 'Χωρίς τίτλο')
        link = entry.get('link', '')
        published = entry.get('published', 'Χωρίς ημερομηνία')
        
        # Δημιουργούμε ένα λεξικό με τα δεδομένα του κάθε entry
        entry_data = {
            'title': title,
            'link': link,
            'published': published
        }
        
        # Προσθέτουμε το entry_data στη λίστα parsed_data
        parsed_data.append(entry_data)
    
    return parsed_data