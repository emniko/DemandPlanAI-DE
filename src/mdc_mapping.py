mdc_to_fachabteilung = {
    "Prä-MDC": {
        "Fachabteilung": ["3600"],  # Intensivmedizin
        "Sekundär": []
    },
    "01 – Nervensystem": {
        "Fachabteilung": ["2800"],  # Neurologie
        "Sekundär": ["1700"]  # Neurochirurgie
    },
    "02 – Augen": {
        "Fachabteilung": ["2700"],  # Augenheilkunde
        "Sekundär": []
    },
    "03 – Ohren, Mund, Hals": {
        "Fachabteilung": ["2600"],  # HNO
        "Sekundär": []
    },
    "04 – Atmungsorgane": {
        "Fachabteilung": ["0800", "1400"],  # Pneumologie, Lungen- und Bronchialheilkunde
        "Sekundär": ["2000"]  # Thoraxchirurgie
    },
    "05 – Kreislaufsystem": {
        "Fachabteilung": ["0300"],  # Kardiologie
        "Sekundär": ["2100"]  # Herzchirurgie
    },
    "06 – Verdauungsorgane": {
        "Fachabteilung": ["0700"],  # Gastroenterologie
        "Sekundär": ["1500"]  # Allgemeine Chirurgie (Viszeralchirurgie)
    },
    "07 – Hepatobiliäres System & Pankreas": {
        "Fachabteilung": ["0700"],  # Gastroenterologie
        "Sekundär": ["0100"]  # Innere Medizin
    },
    "08 – Muskel-Skelett-System & Bindegewebe": {
        "Fachabteilung": ["2300"],  # Orthopädie
        "Sekundär": ["1600"]  # Unfallchirurgie
    },
    "09 – Haut, Unterhaut, Mamma": {
        "Fachabteilung": ["3400"],  # Dermatologie
        "Sekundär": ["1900"]  # Plastische Chirurgie (Senologie)
    },
    "10 – Endokrine & Stoffwechselkrankheiten": {
        "Fachabteilung": ["0600"],  # Endokrinologie
        "Sekundär": []  # Diabetologie is part of Endokrinologie
    },
    "11 – Harnorgane": {
        "Fachabteilung": ["2200"],  # Urologie
        "Sekundär": ["0400"]  # Nephrologie
    },
    "12 – Männliche Geschlechtsorgane": {
        "Fachabteilung": ["2200"],  # Urologie
        "Sekundär": ["0100"]  # Innere Medizin
    },
    "13 – Weibliche Geschlechtsorgane": {
        "Fachabteilung": ["2400"],  # Frauenheilkunde und Geburtshilfe
        "Sekundär": []
    },
    "14 – Schwangerschaft & Geburt": {
        "Fachabteilung": ["2400"],  # Frauenheilkunde und Geburtshilfe
        "Sekundär": ["2500"]  # Geburtshilfe
    },
    "15 – Neugeborene": {
        "Fachabteilung": ["1000"],  # Pädiatrie
        "Sekundär": ["1200"]  # Neonatologie
    },
    "16 – Blut, Immunsystem": {
        "Fachabteilung": ["0500"],  # Hämatologie und Onkologie
        "Sekundär": []
    },
    "17 – Neubildungen": {
        "Fachabteilung": ["0500"],  # Hämatologie und Onkologie
        "Sekundär": []
    },
    "18A – HIV": {
        "Fachabteilung": ["3700"],  # Sonstige (Infektiologie)
        "Sekundär": []
    },
    "18B – Infektiöse Krankheiten": {
        "Fachabteilung": ["3700"],  # Sonstige (Infektiologie/Tropenmedizin)
        "Sekundär": []
    },
    "19 – Psychische Krankheiten": {
        "Fachabteilung": ["2900"],  # Allgemeine Psychiatrie
        "Sekundär": ["3100"]  # Psychosomatik
    },
    "20 – Alkohol/Drogen": {
        "Fachabteilung": ["8500"],  # Entwöhnungsbehandlungen
        "Sekundär": ["2900"]  # Psychiatrie
    },
    "21A – Polytrauma": {
        "Fachabteilung": ["1600"],  # Unfallchirurgie
        "Sekundär": ["3600"]  # Intensivmedizin
    },
    "21B – Verletzungen/Vergiftungen": {
        "Fachabteilung": ["1600"],  # Unfallchirurgie
        "Sekundär": ["3700"]  # Toxikologie (Sonstige)
    },
    "22 – Verbrennungen": {
        "Fachabteilung": ["1900"],  # Plastische Chirurgie
        "Sekundär": ["3600"]  # Intensivmedizin
    },
    "23 – Sozialmedizin": {
        "Fachabteilung": ["8200", "8600", "8800"],  # Prävention, Rehabilitation
        "Sekundär": ["3700"]  # Sonstige
    },
    "24 – Sonstige DRGs": {
        "Fachabteilung": ["3700"],  # Sonstige
        "Sekundär": []
    },
    "-1 – Fehler-DRGs": {
        "Fachabteilung": ["0000", "3700"],  # Keine Zuordnung / Sonstige
        "Sekundär": []
    },
    "Unknown": {
        "Fachabteilung": ["0000"],  # Keine Zuordnung
        "Sekundär": []
    }
}