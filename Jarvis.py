import tkinter as tk 
from tkinter import scrolledtext, messagebox 
from langchain_ollama import OllamaLLM 
from langchain_core.prompts import ChatPromptTemplate  


template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3") 
prompt = ChatPromptTemplate.from_template(template) 


context = ""  

def handle_conversation(user_input):
    global context  
    try:
        result = chain.invoke({"context": context, "question": user_input})
        return result  
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return "An error occurred. Please try again." 

def send_message():
    global context 
    user_input = entry.get() 
    if not user_input.strip(): 
        return
    chat_area.insert(tk.END, f"Jag: {user_input}\n", "user")
    entry.delete(0, tk.END)  

    bot_response = handle_conversation(user_input) 
    chat_area.insert(tk.END, f"Jarvis: {bot_response}\n", "bot")
    context += f"\nUser: {user_input}\nAI: {bot_response}" 
def start_gui():
    global chat_area, entry 

    root = tk.Tk() 
    root.title("Jarvis Chatbot")  
    root.geometry("500x600")  
    root.config(bg="#2c3e50")  

    header_label = tk.Label(root, text="Jarvis AI Chatbot", font=("Helvetica", 18, "bold"), fg="white", bg="#2c3e50")
    header_label.pack(pady=10)  
    chat_area = scrolledtext.ScrolledText(root, height=20, width=60, wrap=tk.WORD, bg="#ecf0f1", fg="#2c3e50", font=("Helvetica", 12))
    chat_area.pack(padx=10, pady=10)  
    chat_area.config(state=tk.NORMAL) 
    chat_area.tag_config("user", foreground="#3498db", font=("Helvetica", 12,))  
    chat_area.tag_config("bot", foreground="#e74c3c", font=("Helvetica", 12)) 

    entry_frame = tk.Frame(root, bg="#2c3e50") 
    entry_frame.pack(pady=10) 

    entry = tk.Entry(entry_frame, width=40, font=("Helvetica", 12))  
    entry.grid(row=0, column=0, padx=5, pady=5)  

    send_button = tk.Button(entry_frame, text="Send", command=send_message, font=("Helvetica", 12), bg="#3498db", fg="black", activebackground="#2980b9")
    send_button.grid(row=0, column=1, padx=5) 

    root.mainloop()  
if __name__ == "__main__":
    start_gui()  
