Verantwoording
Bij het maken van de opdrachten is gebruik gemaakt van Google, Stackoverflow en ChatGPT. Bij het maken van de eerste opdracht is gebruik gemaakt van de externe Python libraries Pandas, Matplotlib en Numpy. Bij opdracht twee zijn de externe Python libraries, Flask en Flask_Restful gebruikt. Voor het maken van opdracht drie is een lokale SQL database opgezet, de queries voor het aanmaken van deze tabel is bijgevoegd. 

Opzet
Code voor de respectievelijke opdrachten bevindt zich in de mappen 1, 2 en 3. De data die bij de opdracht is aangeraden bevindt zich, al dan niet verrijkt, in de map "data". Tussentijdse exports van data welke is gecleaned of getransformeerd bevinden zich in de "cleaned_output" map. Visuele weergaven van resultaten bevinden zich in de map "results".

1.
Er is een matig tot niet bestaande correlatie tussen GDP per land tegenover de gemiddelde leeftijd waarop een respondent zegt te zijn begonnen met programmeren. Op de plot is visueel niet een trend te onderschijden. Ook is er een correlatiecoëfficient geconstateerd van -0.11 wat erop duidt dat er geen duidelijke correlatie is te onderschijden.

Om de resultaten van opdracht te verkrijgen kan 1/main.py worden gerund. De correlatiecoëfficient wordt geprint. De plot verschijnt in results. De unittest voor de correlatiecoëfficient kan worden gerund door 1/unit_test.py te runnen.

2.
De microservice kan worden gerund op een lokale server door 2/webservice.py te runnen. Ga vervolgens naar http://127.0.0.1:5000/countries/NL bijvoorbeeld. In plaat van NL kan een andere ISO code worden ingevoerd waarmee de data wordt opgehaald.

Om een api te kunnen scalen zou je gebruik kunnen maken van load balancing of van caching. Load balancing zou eraan kunnen bijdragen dat een enkele server niet overbelast raakt als er veel requests worden gedaan aan de api. Caching kan ervoor zorgen dat er uberhaupt minder requests hoeven worden gedaan, aangezien er al eerder bekeken data kan worden weergegeven in plaats van een nieuwe call naar de api.

3. 
Het eindresultaat is te genereren met de query in 3/count_popular_languages_per_country.sql.#   t e c h n i c a l _ i n t e r v i e w  
 