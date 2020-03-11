# make request to dict.cc to get html
# make multithreaded request
# parse with beautifulsoup4
# store in datastructure
# make that data struct available to CLI
# 

import requests
from bs4 import BeautifulSoup

SUPPORTED_LANGUAGES = {
    "en": "english",
    "de": "german",
    "es": "spanish"
}

class Dictionary(object):
    @classmethod
    def translate(cls, word, from_language, to_language, num_of_translations=3):
        # multithread just for practice if second language ;) 
        
        html_body = cls._get_raw_response(word, from_language, to_language)
        translations = cls._parse_response(html_body)
        return translations[:num_of_translations]
    
    @classmethod
    def _get_raw_response(cls, word, from_language, to_language):
        
        response = requests.get(
            url="https://" + from_language.lower() + to_language.lower() + ".dict.cc",
            params={"s": word.encode("utf-8")},
            headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0'}
        )
        
        return response.content.decode("utf-8")
       
    
    # return a list of tuples of translation pairs
    @classmethod
    def _parse_response(cls, html_response):
        
         # use html parser, can also be changed to xml parser
        soup = BeautifulSoup(html_response, "html.parser")

        # <td> is a standard html cell, <tr> is a row
        # feel very inefficient; TODO: find a python way of doing this better
        translations = []
        translationPair = [None, None]
        for td in soup.findAll("td", class_="td7nl"):
            if translationPair[0] == None:
                translationPair[0] = ' '.join([a.getText() for a in td.findAll("a")])
            elif translationPair[1] == None:
                translationPair[1] = ' '.join([a.getText() for a in td.findAll("a")])
            else:
                translations.append((translationPair[0], translationPair[1]))
                translationPair = [None, None]
        
        return translations





