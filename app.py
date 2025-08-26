# app.py
import streamlit as st
from datetime import datetime

# ---- Grundkonfiguration ----
st.set_page_config(
    page_title="LemonPlanner",
    page_icon="🍋",
    layout="centered",
)

# ---- Heutiges Datum (Deutsch) ----
WOCHENTAGE = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"]
heute = datetime.now()
datum = f"{WOCHENTAGE[heute.weekday()]}, {heute.day:02d}.{heute.month:02d}.{heute.year}"

# ---- Dark Theme Styling ----
st.markdown("""
<style>
:root { --bg:#0f1115; --panel:#171923; --text:#e7e7e7; --muted:#b6b6c1; --border:#2a2f3a; }
html, body, [data-testid="stAppViewContainer"] { background: var(--bg); color: var(--text); }
h1,h2,h3 { color: var(--text); }
.hero { text-align:center; margin-top: 0.5rem; margin-bottom: 2rem; }
.hero-title { font-size: 2.2rem; font-weight: 800; }
.hero-sub { color: var(--muted); font-size: 1rem; }
.hero-date { margin-top: .5rem; font-weight: 600; color: #d6d6dc; }
.card {
  background: var(--panel); border:1px solid var(--border);
  border-radius: 16px; padding: 22px; text-align:center;
  transition: transform .12s ease-out, border-color .12s ease-out;
}
.card:hover { transform: translateY(-3px); border-color:#3a4252; }
.card-icon { font-size: 36px; margin-bottom: 10px; }
.card-title { font-weight: 800; font-size: 1.2rem; }
.card-desc { color: var(--muted); margin-top:6px; min-height: 42px; }
.footer { text-align:center; color:var(--muted); margin-top: 12px; }
</style>
""", unsafe_allow_html=True)

# ---- Hero Section ----
st.markdown(f"""
<div class="hero">
  <div class="hero-title">📂 LemonPlanner – dein Raum für Gedanken & Pläne</div>
  <div class="hero-sub">Alles übersichtlich und nur einen Klick entfernt.</div>
  <div class="hero-date">Heute ist: {datum}</div>
</div>
""", unsafe_allow_html=True)

# ---- Karten nebeneinander ----
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
      <div class="card-icon">📝</div>
      <div class="card-title">Notizen</div>
      <div class="card-desc">Sammle Gedanken & Ideen.</div>
    </div>
    """, unsafe_allow_html=True)
    st.button("Öffnen", key="btn_notes")

with col2:
    st.markdown("""
    <div class="card">
      <div class="card-icon">✅</div>
      <div class="card-title">Aufgaben</div>
      <div class="card-desc">Kommt bald.</div>
    </div>
    """, unsafe_allow_html=True)
    st.button("Bald verfügbar", key="btn_tasks", disabled=True)

with col3:
    st.markdown("""
    <div class="card">
      <div class="card-icon">📅</div>
      <div class="card-title">Kalender</div>
      <div class="card-desc">Kommt bald.</div>
    </div>
    """, unsafe_allow_html=True)
    st.button("Bald verfügbar", key="btn_calendar", disabled=True)

# ---- Footer ----
st.markdown('<div class="footer">MVP · Fokus auf Übersicht</div>', unsafe_allow_html=True)
