import streamlit as st
import requests
from bs4 import BeautifulSoup

# UI Text

"""
# BroNews
"""
st.markdown("News for Bros by Bros.")
video_url = st.text_input("_:red[Enter an Article URL:]_")
st.markdown("_Created by [Adam Gilani](https://twitter.com/adamgilani) and [Brendan Arias](google.com)_")



# Iterate through each word in article's text

def Bronews():
    # Make the request and store the response.
    response = requests.get(video_url)

    # Parse the HTML content of the website.
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the text from the website and print it.
    article_text = " "
    for p in soup.find_all("p"):
        article_text += p.text + '/n'

    # Split text into a list of words
    article_text = article_text.split()

    # Use lists of pronouns to compare to text to replace with Bro
    upper_singular_pronouns = ['I', 'Me', 'My', 'Mine', 'You', 'You', 'Your', 'Yours', 'He', 'Him', 'His', 'His', 'She',
                               'Her', 'Her', 'Hers', 'It', 'It', 'Its', 'We', 'Us', 'Our', 'Ours', 'You', 'You', 'Your',
                               'Yours', 'They', 'Them', 'Their', 'Theirs', 'Myself', 'Yourself', 'Himself', 'Herself',
                               'Itself', 'Ourselves', 'Yourselves', 'Themselves']
    lower_singular_pronouns = ['me', 'my', 'mine', 'you', 'your', 'yours', 'he', 'him', 'him', 'his', 'she', 'her', 'hers',
                               'it', 'its', 'we', 'us', 'our', 'you', 'your', 'yours', 'they', 'them', 'their', 'theirs',
                               'myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'yourselves',
                               'themselves']
    name_list = []
    new_text = "So basically bro..."
    
    for word in article_text:
        # If word is an uppercase singular pronoun, change it to "Bro" then add it to new text list
        if word in upper_singular_pronouns:
            word = "Bro"
            new_text += word
            new_text += " "
        # If word is a lowercase singular pronoun, change it to "bro" then add it to new text list
        elif word in lower_singular_pronouns:
            word = "bro"
            new_text += word
            new_text += " "
        # If word is possessive, add to name list, then replace with possessive Bro or "Bro's" and add to new text list
        elif word[0].isupper() and word[-1] == 's' and word[-2] == "’":
            name_list += word.split("’s")
            word = "Bro's"
            new_text += word
            new_text += " "
        # Else if word is none of the above, just add it to our new text list
        else:
            new_text += word
            new_text += ' '
    # Turn New Text Back into
    new_text = new_text.split(" ")

    # Make name list a set to get rid of duplicates, and remove empty instances
    name_list = list(set(name_list))
    if '' in name_list:
        name_list.remove(' ')
    
    new_name_list = ""
    for name in name_list:
        new_name_list += name + "." + "/"
        new_name_list += name + "," + "/"
        new_name_list += name + ";" + "/"
        new_name_list += name + "!" + "/"
        new_name_list += name + ":" + "/"
        new_name_list += name + "?" + "/"
    new_name_list = new_name_list.split("/")

    newer_text = ""
    for target in new_text:
        if target:
            punctuation = target[-1]
            if target in new_name_list:
                new_word = "Bro"
                new_word += punctuation
                newer_text += new_word
                newer_text += ' '
            elif target in name_list:
                newer_text += "Bro "
            else:
                newer_text += target
                newer_text += " "
        else:
            newer_text += target
            newer_text += " "
            
    newer_text = newer_text.split("/n")
    
    return newer_text

if video_url:
    # Text generation spinner
    with st.spinner("Please wait while your Bro News is being generated..."):
        # Generate the summarization text
        summary = Bronews()
    # Feed the summarization text to the app
    for paragraph in summary:
        st.write(paragraph + "\n")

