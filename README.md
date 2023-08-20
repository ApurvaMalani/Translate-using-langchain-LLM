# Translate-using-langchain-LLM

Given a demo script document, generate its localized version. The localized version is expected to satisfy following objectives:
1. Translate the language of the demo script to the language specified by the user.
2. Use names from the country specified by the user in the demo script.

**Guidelines for Localization**
1. While using names of people from a country, please ensure that the same names are localized correctly for all their occurrences. 
  For instance, if Alex Smith is to be changed to Rahul Sharma (considering the user has chosen the country to be India), then all occurrences of 
  Alex and Alex Smith must be replaced with Rahul and Rahul Sharma in the document.
2. The input will be a demo script DOCX file and the output will be a localized demo script DOCX file.
