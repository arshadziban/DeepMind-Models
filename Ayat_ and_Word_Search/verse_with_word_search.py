#import libraries
import streamlit as st
import pandas as pd

# Read dataset
quran_data = pd.read_excel('quran_dataset.xlsx')

# Giving unique Surah names in serial order based on SurahNo
surah_names = (
    quran_data[['SurahNo', 'SurahNameEnglish']]
    .drop_duplicates()
    .sort_values('SurahNo')
    .reset_index(drop=True)
)
surah_names_list = [f"{row['SurahNo']}. {row['SurahNameEnglish']}" for _, row in surah_names.iterrows()]

# Function to get a verse based on Surah name and verse number
def get_verse(surah_name, verse_number):
    surah_name = surah_name.split(". ", 1)[1] 
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

# Function to search for a word in English translation or Arabic text (case insensitive)
def search_word(query):
    query = query.lower()  # Convert the query to lowercase for case-insensitive comparison
    results = quran_data[
        quran_data['EnglishTranslation'].str.contains(query, case=False, na=False) | 
        quran_data['OrignalArabicText'].str.contains(query, case=False, na=False)
    ]
    return results[['SurahNameEnglish', 'AyahNo', 'EnglishTranslation', 'OrignalArabicText']]

# Streamlit ui
st.title("Quran Search Application")

# Surah name input with suggestions
surah_name = st.selectbox("Select or Enter Surah Name", surah_names_list)

# Verse number input
verse_number = st.number_input("Enter Verse Number", min_value=1, step=1)

# "Get Verse" button above the word search section
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

# Word search input
st.subheader("Search for a Word in the Quran")
query = st.text_input("Enter a word or phrase to search:")

# "Search Word" button below the word search input
if st.button("Search Word"):
    if query.strip():
        results = search_word(query)
        if not results.empty:
            st.write(f"Found {len(results)} results:")
            for _, row in results.iterrows():
                st.markdown(
                    f"- **Surah:** {row['SurahNameEnglish']}, **Ayah:** {row['AyahNo']}<br>"
                    f"<p style='font-size:18px; text-align:right; direction:rtl;'>{row['OrignalArabicText']}</p><br>"
                    f"**English Translation:** {row['EnglishTranslation']}",
                    unsafe_allow_html=True
                )
        else:
            st.warning("No results found for your search query.")
    else:
        st.warning("Please enter a word or phrase to search.")
