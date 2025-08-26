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

def _delete(note_id: int, title: str):
    db.delete_note(note_id)
    st.toast(f"Notiz '{title}' gelöscht.")
    st.rerun()  # <- neuer Name statt experimental_rerun

notes = db.list_notes()
if notes:
    for n in notes:
        note_id, title, content, tags, folder, created = n
        with st.expander(f"📌 {title}  —  {created}"):
            st.write(content)
            if tags:
                st.caption(f"Tags: {tags}")
            if folder:
                st.caption(f"Ordner: {folder}")

            st.button(
                "🗑️ Löschen",
                key=f"del-{note_id}",
                on_click=_delete,
                args=(note_id, title),
            )
else:
    st.info("Noch keine Notizen vorhanden.")
