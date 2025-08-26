# app.py
# LemonPlanner – Startseite (MVP Dashboard)
import streamlit as st
from datetime import datetime, date

# ---------- Basic Page Config ----------
st.set_page_config(
    page_title="LemonPlanner",
    page_icon="📂",
    layout="centered",
)

# ---------- Small helper to format German date ----------
GERMAN_WEEKDAYS = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
def german_date(d: date) -> str:
    wd = GERMAN_WEEKDAYS[d.weekday()]
    return f"{wd}, {d:%d.%m.%Y}"

# ---------- Minimal Dark Styling + Card Layout ----------
st.markdown("""
<style>
:root { --bg:#0f1115; --panel:#171923; --text:#e7e7e7; --muted:#b6b6c1; --accent:#ffd54f; --border:#2a2f3a; }
html, body, [data-testid="stAppViewContainer"] { background: var(--bg); color: var(--text); }
h1, h2, h3, h4, h5, h6 { color: var(--text); }
.lemon-hero { text-align:center; margin-top: 0.5rem; margin-bottom: 2rem; }
.lemon-title { font-size: 2.2rem; font-weight: 800; line-height:1.2; }
.lemon-sub { color: var(--muted); font-size: 1rem; }
.lemon-date { margin-top: .5rem; font-weight: 600; color: #d6d6dc; }

.lemon-row { display:flex; gap: 24px; justify-content:center; flex-wrap:wrap; margin: 28px 0; }
.card {
  width: 320px; background: var(--panel); border:1px solid var(--border);
  border-radius: 16px; padding: 22px; box-shadow: 0 6px 20px rgba(0,0,0,.25);
  transition: transform .12s ease-out, border-color .12s ease-out, box-shadow .12s ease-out;
}
.card:hover { transform: translateY(-3px); border-color:#3a4252; box-shadow: 0 10px 26px rgba(0,0,0,.35); }
.card-icon { font-size: 36px; line-height: 1; margin-bottom: 10px; }
.card-title { font-weight: 800; font-size: 1.2rem; display:flex; align-items:center; gap:.5rem; }
.card-desc { color: var(--muted); margin-top:6px; min-height: 42px; }
.card-btn {
  margin-top: 14px; display:inline-block; padding:10px 14px; border-radius: 12px;
  border:1px solid #3a4252; color: var(--text); text-decoration:none; background:#1d2230;
}
.card-btn:hover { border-color:#55607a; background:#232a3b; }
.lemon-footer { text-align:center; color:var(--muted); margin-top: 12px; }
.lemon-badge { background: #2a2f3a; padding: 3px 10px; border-radius: 999px; border: 1px solid #3a4252; }
</style>
""", unsafe_allow_html=True)

# ---------- Session nav ----------
if "page" not in st.session_state:
    st.session_state.page = "home"

def go(page: str):
    st.session_state.page = page

# ---------- HOME ----------
if st.session_state.page == "home":
    st.markdown(f"""
    <div class="lemon-hero">
      <div class="lemon-title">📂 LemonPlanner – dein Raum für Gedanken &amp; Pläne</div>
      <div class="lemon-sub">Willkommen! Starte entspannt – alles ist übersichtlich und nur einen Klick entfernt.</div>
      <div class="lemon-date">Heute ist: <span class="lemon-badge">{german_date(datetime.now().date())}</span></div>
    </div>
    """, unsafe_allow_html=True)

    # Cards row
    st.markdown('<div class="lemon-row">', unsafe_allow_html=True)

    # --- Card: Notizen ---
    with st.container():
        st.markdown("""
        <div class="card">
          <div class="card-icon">📝</div>
          <div class="card-title">Notizen</div>
          <div class="card-desc">Schnell festhalten, ordnen und später wiederfinden.</div>
          <span id="btn-notes"></span>
        </div>
        """, unsafe_allow_html=True)
        # Real button (uses Streamlit to change state)
        if st.button("Öffnen", key="open_notes"):
            go("notes")

    # --- Card: Aufgaben ---
    with st.container():
        st.markdown("""
        <div class="card">
          <div class="card-icon">✅</div>
          <div class="card-title">Aufgaben</div>
          <div class="card-desc">Kommt als Nächstes – Schritt für Schritt.</div>
          <span id="btn-tasks"></span>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Bald verfügbar", key="open_tasks", disabled=True):
            pass

    # --- Card: Kalender ---
    with st.container():
        st.markdown("""
        <div class="card">
          <div class="card-icon">📅</div>
          <div class="card-title">Kalender</div>
          <div class="card-desc">Bauen wir später ein.</div>
          <span id="btn-cal"></span>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Bald verfügbar ", key="open_calendar", disabled=True):
            pass

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="lemon-footer">MVP · Fokus auf Ruhe &amp; <b>Übersicht</b></div>', unsafe_allow_html=True)

# ---------- PLACEHOLDER PAGES ----------
elif st.session_state.page == "notes":
    st.page_link("app.py", label="← Zurück zur Startseite", icon="↩️")
    st.title("📝 Notizen (MVP)")
    st.info("Hier kommt Phase 1 rein: CRUD, Tags/Ordner, Anhänge, Suche.")
    # Tiny placeholder example so die Navigation „lebt“:
    title = st.text_input("Titel", "")
    content = st.text_area("Inhalt", height=180, placeholder="Schreib deine Gedanken hier rein…")
    cols = st.columns([1,1,1])
    with cols[0]:
        st.button("Speichern (Stub)", use_container_width=True)
    with cols[1]:
        st.button("Löschen (Stub)", use_container_width=True)
    with cols[2]:
        if st.button("Zur Startseite", use_container_width=True):
            go("home")
