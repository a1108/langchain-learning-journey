import os
import re
from dotenv import load_dotenv
from supabase import create_client
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.chat_history import BaseChatMessageHistory

from langchain_core.messages import (
    message_to_dict,
    messages_from_dict,
)
from langchain_core.runnables.history import RunnableWithMessageHistory

# ==========================================
# 1. SUPABASE & ENVIRONMENT CONFIGURATION
# ==========================================
load_dotenv()

supabase = create_client(
    os.environ["SUPABASE_URL"],
    os.environ["SUPABASE_SECRET_KEY"]
)

USERS_TABLE = "users"
HISTORY_TABLE = "chat_history"


# ==========================================
# 2. LOAD USERS
# ==========================================
def load_users():
    response = (
        supabase
        .table(USERS_TABLE)
        .select("username, profile")
        .execute()
    )
    users = {}
    for row in response.data:
        users[row["username"]] = row["profile"]
    return users


# ==========================================
# 3. SAVE USERS
# ==========================================
def save_users(users):
    rows = []
    for username, profile in users.items():
        rows.append({
            "username": username,
            "profile": profile
        })
    if rows:
        supabase.table(USERS_TABLE).upsert(rows, on_conflict="username").execute()


# ==========================================
# 4. USER SIGNUP
# ==========================================
def signup(users):
    print("\n--- SIGNUP ---")
    name = input("Enter Name: ").strip()
    username = input("Enter Username: ").strip().lower()
    password = input("Enter Password: ")

    if not name or not username or not password:
        print("All fields are required")
        return

    if not re.fullmatch(r"[a-z0-9_]+", username):
        print("Use only letters, numbers and underscores")
        return

    if username in users:
        print("Username already exists")
        return

    users[username] = {
        "name": name,
        "password": password
    }
    save_users(users)
    print("Signup Successful!")


# ==========================================
# 5. USER LOGIN
# ==========================================
def login(users):
    print("\n--- LOGIN ---")
    username = input("Enter Username: ").strip().lower()
    password = input("Enter Password: ")

    if username not in users:
        print("Invalid Username")
        return None

    if users[username]["password"] == password:
        print("Login Successful!")
        print("Welcome", users[username]["name"])
        return username

    print("Incorrect Password")
    return None


# ==========================================
# 6. SUPABASE DATABASE CHAT HISTORY
# ==========================================
class SupabaseChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id):
        self.session_id = session_id

    @property
    def messages(self):
        response = (
            supabase
            .table(HISTORY_TABLE)
            .select("messages")
            .eq("session_id", self.session_id)
            .execute()
        )
        if not response.data:
            return []
        data = response.data[0]["messages"]
        if not data:
            return []
        return messages_from_dict(data)

    def add_messages(self, messages):
        all_messages = self.messages + messages
        data = [message_to_dict(message) for message in all_messages]
        (
            supabase
            .table(HISTORY_TABLE)
            .upsert(
                {
                    "session_id": self.session_id,
                    "messages": data
                },
                on_conflict="session_id"
            )
            .execute()
        )

    def clear(self):
        (
            supabase
            .table(HISTORY_TABLE)
            .upsert(
                {
                    "session_id": self.session_id,
                    "messages": []
                },
                on_conflict="session_id"
            )
            .execute()
        )


# ==========================================
# 7. CREATE GEMINI MODEL
# ==========================================
# Replaced ChatOpenAI with ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)


# ==========================================
# 8. CREATE PROMPT
# ==========================================
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful AI assistant. Answer in simple English. The user's name is {name}."
    ),
    MessagesPlaceholder("history"),
    ("human", "{question}")
])


# ==========================================
# 9. CREATE LCEL CHAIN
# ==========================================
chain = prompt | llm


# ==========================================
# 10. GET SESSION HISTORY
# ==========================================
def get_session_history(session_id):
    return SupabaseChatMessageHistory(session_id)


# ==========================================
# 11. CREATE CHATBOT WITH HISTORY
# ==========================================
chatbot = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)


# ==========================================
# 12. LOAD REGISTERED USERS & START APP
# ==========================================
users = load_users()
current_user = None

print("\nMULTI-USER AI CHATBOT")
print("SUPABASE JSONB DATABASE (GEMINI POWERED)")

while True:
    if current_user is None:
        print("\n1. Signup")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter Choice: ").strip()

        if choice == "1":
            signup(users)
        elif choice == "2":
            current_user = login(users)
        elif choice == "3":
            break
        else:
            print("Invalid Choice")
    else:
        question = input(f"\n{current_user}: ").strip()

        if question.lower() == "logout":
            print("Logged Out")
            current_user = None
        elif question.lower() == "exit":
            break
        elif question:
            name = users[current_user]["name"]
            try:
                response = chatbot.invoke(
                    {
                        "name": name,
                        "question": question
                    },
                    config={
                        "configurable": {
                            "session_id": current_user
                        }
                    }
                )
                print("\nAI:", response.text)
            except Exception as error:
                print("Error:", error)

print("\nProgram Ended")