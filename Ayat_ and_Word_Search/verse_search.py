#import libraries
import streamlit as st
import pandas as pd

# Read dataset
quran_data = pd.read_excel('quran_dataset.xlsx')

# Get unique Surah names in serial order based on SurahNo
surah_names = (
    quran_data[['SurahNo', 'SurahNameEnglish']]
    .drop_duplicates()
    .sort_values('SurahNo')
    .reset_index(drop=True)['SurahNameEnglish']
    .tolist()
)

# Function to get a verse based on Surah name and verse number
def get_verse(surah_name, verse_number):
    row = quran_data[
        (quran_data['SurahNameEnglish'].str.lower() == surah_name.lower()) & 
        (quran_data['AyahNo'] == verse_number)
    ]
    if not row.empty:
        return row[['Juz', 'JuzNameArabic', 'JuzNameEnglish', 'SurahNo', 'SurahNameArabic',
                    'SurahNameEnglish', 'SurahMeaning', 'WebLink', 'Classification', 'AyahNo',
                    'EnglishTranslation', 'OrignalArabicText', 'ArabicText', 'ArabicWordCount', 
                    'ArabicLetterCount']].to_dict('records')[0]
    else:
        return None

# Streamlit UI
st.title("Quran Search Application")

# Surah name input with suggestions
surah_name = st.selectbox("Select or Enter Surah Name", surah_names)

# Verse number input
verse_number = st.number_input("Enter Verse Number", min_value=1, step=1)

# Button to fetch verse
if st.button("Get Verse"):
    verse = get_verse(surah_name, verse_number)
    if verse:
        st.write(f"Surah: {verse['SurahNameEnglish']} ({verse['SurahNameArabic']}) - Meaning: {verse['SurahMeaning']}")
        st.write(f"Juz: {verse['Juz']}")
        st.write(f"Classification: {verse['Classification']}")
        st.write(f"Surah Number: {verse['SurahNo']}")
        st.write(f"Ayah: {verse['AyahNo']}")
        st.markdown(
            f"<p style='font-size:24px; text-align:right; direction:rtl;'>{verse['OrignalArabicText']}</p>",
            unsafe_allow_html=True
        )
        st.write(f"English Translation: {verse['EnglishTranslation']}")
        st.write(f"Arabic Word Count: {verse['ArabicWordCount']}")
        st.write(f"Arabic Letter Count: {verse['ArabicLetterCount']}")
        st.write(f"Web Link: [Learn More]({verse['WebLink']})")
    else:
        st.error("Verse not found. Please check the Surah name and verse number.")


