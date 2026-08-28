import os
from openai import OpenAI
from elevenlabs.client import ElevenLabs

# Initialisierung der APIs (Nutzt Umgebungsvariablen für Sicherheit)
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
eleven_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

def generate_sales_pitch(product_name, target_audience):
    """Nutzt GPT, um ein psychologisch optimiertes Verkaufsskript zu schreiben."""
    prompt = f"Schreibe ein kurzes, überzeugendes 30-sekündiges Verkaufsskript für das Produkt '{product_name}'. Zielgruppe ist '{target_audience}'. Der Ton soll professionell, dynamisch und einladend sein. Maximal 3 Sätze."
    
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices.message.content

def convert_pitch_to_speech(text, output_filename="sales_pitch.mp3"):
    """Konvertiert das Skript mit ElevenLabs in eine emotionale KI-Stimme."""
    print("Generiere Audio mit ElevenLabs...")
    
    # Nutzt die Standard-Stimme 'Rachel' (oder jede andere gültige Voice_ID)
    audio_generator = eleven_client.generate(
        text=text,
        voice="Rachel",
        model="eleven_multilingual_v2"
    )
    
    # Audio-Stream als Datei speichern
    with open(output_filename, "wb") as f:
        for chunk in audio_generator:
            f.write(chunk)
    print(f"Erfolgreich gespeichert als {output_filename}")

if __name__ == "__main__":
    # Beispiel-Daten für den Sales-Pitch
    PRODUCT = "ElevenLabs Enterprise Voice Solutions"
    AUDIENCE = "Abteilungsleiter im Kundenservice von DAX-Unternehmen"
    
    print(f"Erstelle Pitch für {PRODUCT}...")
    script = generate_sales_pitch(PRODUCT, AUDIENCE)
    print(f"\nGeneriertes Skript:\n{script}\n")
    
    # Hinweis: Für den echten Lauf werden API-Keys benötigt
    try:
        convert_pitch_to_speech(script)
    except Exception as e:
        print(f"\n[Hinweis] ElevenLabs-Generierung übersprungen (Keys nicht gesetzt): {e}")
