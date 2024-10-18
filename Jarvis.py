# Importera nödvändiga moduler
import tkinter as tk  # Använder Tkinter för att skapa ett enkelt användargränssnitt
from tkinter import scrolledtext, messagebox  # ScrolledText ger scrollbars för textfälten, messagebox för felmeddelanden
from langchain_ollama import OllamaLLM  # Importerar modellen som används för att AI:n ska fungera
from langchain_core.prompts import ChatPromptTemplate  # Behövs för att strukturera hur AI får prompts (frågor)

# Skapa en mall för chatbotens svar
# Här skriver jag en mall för hur varje fråga och svar ska skickas till modellen. Kontexten behövs så att AI:n kommer ihåg vad vi pratat om tidigare
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Initiera AI-modellen med Llama3
model = OllamaLLM(model="llama3")  # Här väljer jag att använda Llama3 som min modell
prompt = ChatPromptTemplate.from_template(template)  # Skapar en prompt baserat på mallen ovan
chain = prompt | model  # "Kedjar" ihop prompt och modell så att de kan arbeta tillsammans när jag kör konversationen

# Definiera en global kontextvariabel
context = ""  # Använder en variabel för att spara hela konversationens historik, så att AI:n vet vad som sagts tidigare

# Funktion för att hantera konversationen
def handle_conversation(user_input):
    global context  # Ser till att jag kan uppdatera och använda den globala kontexten
    try:
        # Här skickar jag användarens fråga och kontexten till modellen för att få ett svar
        result = chain.invoke({"context": context, "question": user_input})
        return result  # Returnerar AI:ns svar till användargränssnittet
    except Exception as e:
        # Om något går fel, visas ett felmeddelande
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return "An error occurred. Please try again."  # Returnerar ett enkelt felmeddelande

# Funktion för att skicka meddelanden från GUI
def send_message():
    global context  # Behöver global variabel för att uppdatera kontexten
    user_input = entry.get()  # Hämtar det användaren skrivit in
    if not user_input.strip():  # Om fältet är tomt, gör ingenting
        return
    # Lägger till användarens fråga i chatten
    chat_area.insert(tk.END, f"Jag: {user_input}\n", "user")
    entry.delete(0, tk.END)  # Tömmer inmatningsfältet efter att frågan skickats

    # Får AI:ns svar och uppdaterar kontexten
    bot_response = handle_conversation(user_input)  # Får ett svar från AI:n baserat på användarens fråga
    # Visar AI:ns svar i chatten
    chat_area.insert(tk.END, f"Jarvis: {bot_response}\n", "bot")
    context += f"\nUser: {user_input}\nAI: {bot_response}"  # Uppdaterar kontexten så AI:n kan hålla koll på samtalet

# Skapa ett snyggare GUI med Tkinter
def start_gui():
    global chat_area, entry  # Gör komponenterna globala så att de kan användas i andra funktioner

    # Skapa huvudfönstret
    root = tk.Tk()  # Här skapar jag själva fönstret för chatboten
    root.title("Jarvis Chatbot")  # Ger fönstret en titel
    root.geometry("500x600")  # Bestämmer storleken på fönstret
    root.config(bg="#2c3e50")  # Sätter en mörk bakgrundsfärg för att ge det ett snyggare utseende

    # Skapa en rubrik överst
    header_label = tk.Label(root, text="Jarvis AI Chatbot", font=("Helvetica", 18, "bold"), fg="white", bg="#2c3e50")
    header_label.pack(pady=10)  # Placerar rubriken och ger den lite utrymme runt om

    # Skapa ett textområde för att visa konversationen (med scrollbar)
    chat_area = scrolledtext.ScrolledText(root, height=20, width=60, wrap=tk.WORD, bg="#ecf0f1", fg="#2c3e50", font=("Helvetica", 12))
    chat_area.pack(padx=10, pady=10)  # Lägger till lite marginal runt textområdet
    chat_area.config(state=tk.NORMAL)  # Tillåter att text skrivs i fältet
    # Skapar olika stilar för användaren och AI:n för att skilja deras text åt
    chat_area.tag_config("user", foreground="#3498db", font=("Helvetica", 12,))  # Användarens text i blå
    chat_area.tag_config("bot", foreground="#e74c3c", font=("Helvetica", 12))  # Botens text i röd

    # Skapa en ram för inmatningsfältet och knappen
    entry_frame = tk.Frame(root, bg="#2c3e50")  # En ram för att hålla både textfältet och knappen
    entry_frame.pack(pady=10)  # Lägger till lite marginal runt ramen

    # Skapa ett textfält för användarens inmatning
    entry = tk.Entry(entry_frame, width=40, font=("Helvetica", 12))  # Ett textfält där användaren kan skriva sin fråga
    entry.grid(row=0, column=0, padx=5, pady=5)  # Lägger textfältet i layouten med lite utrymme runt om

    # Skapa en knapp för att skicka meddelanden
    send_button = tk.Button(entry_frame, text="Send", command=send_message, font=("Helvetica", 12), bg="#3498db", fg="black", activebackground="#2980b9")
    send_button.grid(row=0, column=1, padx=5)  # Lägger knappen bredvid textfältet

    # Starta GUI:t
    root.mainloop()  # Startar själva GUI:t och håller fönstret öppet så länge det används

# Starta programmet om denna fil körs direkt
if __name__ == "__main__":
    start_gui()  # Kör funktionen för att starta GUI:t
