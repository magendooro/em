import streamlit as st
'''
# Ecommerce Platform Development

Engineering Maturity Quiz
'''

questions = [
    "Ca developer nou, am un proces simplu si automatizat de a putea porni dezvoltarea pe calculatorul meu",
    "Folosesc un sistem de versionare, am un flux de tipul gitflow prestabilit pe care il cunosc si il urmez cand fac modificari sau dezvoltari noi",
    "Am un proces de code review",    
    "Am standarde de securitate (pe care le pot rula local sau in CI) si am un sistem de verificare a securitatii",
    "Am pipelines care executa o serie de procese pentru asigurarea calitatii si securitatii codului scris/adaugat in proiect",
    "Nu pot trece mai departe in flux, daca nu sunt respectate standardele",    
    "Am mecanisme de testare automata pentru asigurarea calitatii si integritatii",
    "Am un proces clar de QA",    
    "Am procese automate pentru a face deployment pe QA, Stage, Productie",
    "Am procese clare legat de aprobari si notificarea stakeholderilor",
    "Am un proces clar de management de proiecte",    
    "Am la dispozitie o platforma prin care pot sa vad metrici si loguri ale tuturor componentelor platformei, agregate intr-un singur loc",
    "In caz ca apar probleme dupa un release nou, pot face “rollback” in productie",
    "Am un proces clar de integrare a componentelor in platforma"    
]
i=0
score = 0
q_answer_list = []
for q in questions:
    q_answer = st.radio(q,('Nu', 'Partial', 'Da'))    
    q_answer_list.append(q_answer)     

for qa in q_answer_list:
    if qa == 'Nu':
        score = score + 0
    elif qa == 'Partial':
        score = score + 1
    elif qa == 'Da':
        score = score + 2

if st.button('Calculeaza scor'):
    st.text("Scor: "+str(score))  
    if score == 28:
        st.text("Este o platforma de succes - fluxurile de dezvoltare sunt bine puse la punct")
    elif score > 20:
        st.text("Este o platforma de succes")
    elif score >= 14:
        st.text("Este o platforma de nivel mediu. Nu se potriveste pentru businessuri mature sau care necesita stabilitate.")
    elif score >= 0:
        st.text("Este o platforma riscant de folosit")
else:
    st.write('Calculez scorul? (apasa butonul)')

st.markdown("[Inspirat de: Dezvoltarea platformei unui magazin online](https://florinelchis.medium.com/dezvoltarea-platformei-unui-magazin-online-4bd9a396e2a0)", unsafe_allow_html=True)
st.markdown("[Contact](mailto:florinel.chis@gmail.com)", unsafe_allow_html=True)
       
