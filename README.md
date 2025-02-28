# Jarvis AI Chatbot

## Beskrivning
Jarvis AI Chatbot är en enkel chatbot byggd med Python och Tkinter för GUI samt OllamaLLM för AI-genererade svar. Programmet skapar en chattmiljö där användaren kan ställa frågor och få svar genererade av AI-modellen Llama3.

## Krav
För att köra denna chatbot behöver du ha följande bibliotek installerade:

- Tkinter (ingår i Python-standardbiblioteket)
- `langchain-ollama`
- `langchain-core`

## Installation
Följ dessa steg för att installera nödvändiga paket:

```sh
pip install langchain_ollama langchain_core
```

## Användning
Kör skriptet genom att exekvera följande kommando i terminalen:

```sh
python chatbot.py
```

Fönstergränssnittet startas och du kan börja chatta med AI:n.

## Funktioner
- En grafisk användargränssnitt byggt med Tkinter.
- AI-genererade svar baserade på konversationens kontext.
- Scrollbart textfält för konversationen.
- Färgkodade chattmeddelanden (blå för användaren, röd för AI:n).

## Kodstruktur
- **`template`**: En promptmall som används för att generera svar.
- **`model`**: AI-modellen Llama3.
- **`handle_conversation(user_input)`**: Funktion som skickar in data till modellen och returnerar AI:s svar.
- **`send_message()`**: Funktion som hanterar meddelanden och uppdaterar GUI.
- **`start_gui()`**: Funktion som skapar och startar användargränssnittet.

## Felsökning
Om du får ett felmeddelande, se till att:
- Alla bibliotek är korrekt installerade.
- Python är uppdaterat till en kompatibel version.
- Internetanslutning finns tillgänglig om AI-modellen kräver det.

