import streamlit as st
from datetime import datetime


# -----------------------------------------------------------------------------
# 1. CONFIGURATION
# -----------------------------------------------------------------------------


st.set_page_config(
   page_title="One message every day",
   page_icon="🎄",
   layout="centered"
)


# Start Date: December 17th (Change this to change when Day 1 unlocks)
current_year = datetime.now().year
START_DATE = datetime(current_year, 12, 21)


# --- YOUR MESSAGES HERE ---
# Replace the text inside the quotes with your real messages later.
DAILY_MESSAGES = [
   "So che questo Natale e' diverso.. quindi facciamo si che sia diverso. La magia comincia adesso.. Se presti attenzione sentirai che sono li con te",
   "Adesso e' il mio momento per un trucco di magia. Prendi il mazzo che e' sul tavolo. Lo hai preso? Scorri il mazzo e... manca la carta che hai scelto. L'ho fatta apparire in un luogo che vicino questa data l'anno scorso ha ricordato come non vendoci per molto tempo siamo stati vicini. Il mio trucco non e' riuscito finche' non la trovi.  Suggerimento: scopriamo chi siamo solo vivendo, non prima ",
   "Questi giorni il letto puo' essere un po' piu' freddo e ho pensato a qualcosa per farti dormire meglio. Ti suggerisco di andare da qualche parte a Londra. Dove? C'e' un metodo infallibile per decidere",
   "Se presti attenzione mi sentirai vicina. Pensaci intensamente, potresti volere maggiore potenza neurale",
   "Buon Natale! Trovera il nastro della sorpresa in un posto con altre cose mie, dovrai attendere  ancora qualche giorno per poterlo scartare",
   "Now it's up to you. Make the magic happen. Show me a magic trick I haven't seen to unlock. You have 24 hours",
   "Date?",
   "Non vedo l'ora di vederti, a presto"
]


# -----------------------------------------------------------------------------
# 2. DESIGN & CSS
# -----------------------------------------------------------------------------


st.markdown("""
<style>
   /* IMPORT FONTS */
   @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lato:wght@300;400&display=swap');


   /* --- BACKGROUND --- */
   .stApp {
       background-color: #0f1c15;
       background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
                         url("https://images.unsplash.com/photo-1512474932049-78ac69ede12c?q=80&w=1920&auto=format&fit=crop");
       background-size: cover;
       background-attachment: fixed;
       background-position: center;
   }


   /* --- HEADER TYPOGRAPHY --- */
   .special-header {
       text-align: center;
       margin-bottom: 40px;
       animation: fadeIn 2s ease-in;
   }
  
   .top-label {
       font-family: 'Lato', sans-serif;
       font-size: 14px;
       color: #d4af37; /* Gold */
       text-transform: uppercase;
       letter-spacing: 3px;
       margin-bottom: 10px;
       display: flex;
       justify-content: center;
       align-items: center;
       gap: 10px;
   }


   .main-title {
       font-family: 'Playfair Display', serif;
       font-size: 3.5rem; /* Adjusted for better visibility */
       font-weight: 700;
       color: #ffffff !important;
       margin: 0;
       line-height: 1.1;
       text-shadow: 0 4px 10px rgba(0,0,0,0.5);
   }


   .subtitle {
       font-family: 'Playfair Display', serif;
       font-size: 1.2rem;
       color: #ccc;
       font-weight: 400;
       margin-top: 15px;
       font-style: italic;
   }


   .divider {
       width: 6px;
       height: 6px;
       background-color: #d4af37;
       border-radius: 50%;
       margin: 20px auto;
       box-shadow: 0 0 10px #d4af37;
   }


   /* --- LUXURY CELLS (BUTTONS) --- */
   div.stButton > button {
       width: 100%;
       height: 150px;
       background: linear-gradient(145deg, #2e1015 0%, #1a0505 100%);
       border: 1px solid rgba(212, 175, 55, 0.2);
       border-radius: 8px;
       color: #8c6b6b;
       font-family: 'Playfair Display', serif;
       font-size: 18px;
       transition: all 0.4s ease;
       white-space: pre-wrap;
       display: flex;
       flex-direction: column;
       justify-content: center;
       align-items: center;
       line-height: 1.5;
   }


   div.stButton > button:hover {
       border-color: #d4af37;
       transform: translateY(-2px);
       color: #d4af37;
   }


   /* Styles specifically for the button when it's active/focused */
   div.stButton > button:active, div.stButton > button:focus {
       background: linear-gradient(145deg, #3d151c 0%, #290a0a 100%);
       border-color: #d4af37;
       color: #d4af37;
   }


   /* --- ANIMATIONS --- */
   @keyframes fadeIn {
       from { opacity: 0; transform: translateY(20px); }
       to { opacity: 1; transform: translateY(0); }
   }


</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 3. LOGIC
# -----------------------------------------------------------------------------


def calculate_unlocked_day():
   today = datetime.now()
   d_today = datetime(today.year, today.month, today.day)
   d_start = datetime(START_DATE.year, START_DATE.month, START_DATE.day)
   diff_days = (d_today - d_start).days
  
   # If before start date, return 0. Otherwise return days passed + 1
   if diff_days < 0:
       return 0
   return min(diff_days + 1, 8)


if 'opened_days' not in st.session_state:
   st.session_state.opened_days = set()


current_unlocked_day = calculate_unlocked_day()


# -----------------------------------------------------------------------------
# 4. HEADER LAYOUT
# -----------------------------------------------------------------------------


st.markdown("""
   <div class="special-header">
       <div class="top-label">
           <span>✨</span> A SPECIAL COUNTDOWN <span>✨</span>
       </div>
       <h1 class="main-title">One message every day</h1>
       <p class="subtitle"> until we're together again</p>
       <div class="divider"></div>
   </div>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 5. DIALOG & GRID
# -----------------------------------------------------------------------------


# We use the @st.dialog decorator to create a modal popup
@st.dialog("From Angela to Gabriele 💌")
def show_message(day_num, message_text):
   # We inject specific styling HERE to ensure the text is visible inside the modal
   st.markdown(f"""
       <div style='
           background-color: #1a0505;
           padding: 20px;
           border-radius: 10px;
           border: 1px solid #d4af37;
           text-align: center;
           color: #eebb88;
       '>
           <h2 style='
               font-family: "Playfair Display", serif;
               margin-bottom: 10px;
               color: #d4af37;
           '>Day {day_num}</h2>
           <hr style='border-color: rgba(212, 175, 55, 0.3); margin-bottom: 20px;'>
           <p style='
               font-size: 1.3rem;
               font-style: italic;
               line-height: 1.6;
               color: #-ff;
           '>
               "{message_text}"
           </p>
       </div>
   """, unsafe_allow_html=True)




# The Grid Layout
days = list(range(1, 9))


with st.container():
   # Loop through days in chunks of 4 (4 columns wide)
   for i in range(0, len(days), 4):
       cols = st.columns(4)
       row_days = days[i:i+4]
      
       for idx, day in enumerate(row_days):
           with cols[idx]:
               is_unlocked = day <= current_unlocked_day
               is_opened = day in st.session_state.opened_days
              
               # Determine Label
               if not is_unlocked:
                   label = f"\n{day}\n\n🔒 Locked"
               elif is_opened:
                   label = f"\n{day}\n\n♥ Opened"
               else:
                   label = f"\n{day}\n\n✨ Open Me"
              
               # Render Button
               if st.button(label, key=f"btn_{day}", disabled=not is_unlocked):
                   st.session_state.opened_days.add(day)
                   # Trigger the modal
                   show_message(day, DAILY_MESSAGES[day-1])


# -----------------------------------------------------------------------------
# 6. FOOTER
# -----------------------------------------------------------------------------


st.markdown("""
   <div style="text-align: center; margin-top: 60px; color: rgba(255,255,255,0.4); font-family: 'Playfair Display', serif;">
       <p>See you soon</p>
           <p>Angela 🤍</p>
   </div>
""", unsafe_allow_html=True)


