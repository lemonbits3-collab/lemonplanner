import streamlit as st
import notizen_db as db

st.set_page_config(page_title="Notizen · LemonPlanner", page_icon="📝", layout="wide")

st.title("📝 Notizen")

# --- Formular zum Anlegen ---
with st.form("note_form", clear_on_submit=True):
    st.subheader("Neue Notiz erstellen")
    title = st.text_input("Titel")
    content = st.text_area("Inhalt")
    tags = st.text_input("Tags (optional, komma-getrennt)")
    folder = st.text_input("Ordner (optional)")
    submitted = st.form_submit_button("Speichern")

    if submitted and title.strip() and content.strip():
        db.add_note(title, content, tags, folder)
        st.success(f"Notiz '{title}' gespeichert!")

st.write("---")

# --- Notizen anzeigen ---
st.subheader("Gespeicherte Notizen")

notes = db.list_notes()
if notes:
    for n in notes:
        with st.expander(f"📌 {n[1]}  —  {n[5]}"):
            st.write(n[2])  # Inhalt
            if n[3]:
                st.caption(f"Tags: {n[3]}")
            if n[4]:
                st.caption(f"Ordner: {n[4]}")
            # Löschen
            if st.button("🗑️ Löschen", key=f"del{n[0]}"):
                db.delete_note(n[0])
                st.warning(f"Notiz '{n[1]}' gelöscht.")
                st.experimental_rerun()
else:
    st.info("Noch keine Notizen vorhanden.")
