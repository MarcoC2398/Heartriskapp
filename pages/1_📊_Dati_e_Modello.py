import streamlit as st

st.title("📊 Dati & Modello — Panoramica")
st.write(
    """
    In questa pagina verranno mostrati:
    - il dataset utilizzato (anteprima e descrizione colonne),
    - i passaggi di **pre‑processing** (pulizia, encoding, scaling),
    - il **modello** scelto per la classificazione (baseline).

    """
)

import streamlit as st
from ml import train_logistic_regression_model


st.write(
    "Fare clic sul pulsante per addestrare una regressione logistica binaria sul dataset cardiaco OpenML.. "
    "Il modello addestrato verrà memorizzato (stato della sessione) e utilizzato dalla pagina del simulatore.."
)

train_button_clicked = st.button("Train model")

if train_button_clicked:
    try:
        st.info("⏳ Formazione in corso... La prima volta potrebbero volerci alcuni secondi (download del set di dati).")
        trained_model = train_logistic_regression_model()
        st.session_state["model"] = trained_model  # store for other pages
        st.success("✅ Modello addestrato e memorizzato nella memoria.")
        st.caption("LogisticRegression with default settings. No preprocessing, no pipeline.")
    except Exception as error:
        st.error(f"Formazione fallita. Dettagli: {error}")

# Status indicator (so students know if a model is available)
if "model" in st.session_state:
    st.success("Un modello addestrato è disponibile in memoria e pronto per l'uso nella pagina Simulatore.")
else:
    st.warning("Nessun modello in memoria. Fare clic su "Addestra modello" per crearne uno..")


