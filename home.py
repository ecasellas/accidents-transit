import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title = 'Accidents de trànsit a Catalunya')

st.title("Accidents de trànsit a Catalunya")

st.markdown("En aquesta pàgina web trobareu una visió general sobre la problemàtica dels accidents de trànsit "
            "a Catalunya entre el 2010 i el 2021. A través de gràfics interactius es desglossarà informació "
            "sobre els tipus d'accidents, la mortalitat d'aquests, i les unitats implicades.") 

tab1, tab2, tab3 = st.tabs(["Unitats", "Mortalitat", "Tipus"])

with tab1:
   st.markdown("""Les unitats en un accident de trànsit fan referència a tots els tipus de vehicles implicats, que s'agrupen
               en vehicles lleugers, vehicles pesants, motocicletes, ciclomotors i bicicletes. També, sense oblidar els
               vianants.  
               Les gràfiques mostren l'evolució de les unitats implicades al llarg del període considerat, així
                com el nombre d'unitats implicades desglossat per tipus. A més, es mostra la distribució espacial per
               comarques de la proporció de cada tipus d'unitat en els accidents de trànsit.""")
   tab11, tab12, tab13 = st.tabs(["Evolució", "Dades", "Mapa"])
   with tab11:
    st.markdown("""##### Idees generals""")
    st.write("- El vehicle lleuger és el tipus d'unitat amb un nombre més elevat d'implicació en accidents de trànsit.")
    st.write("- La pandèmia de la COVID-19 té una clara influència en la reducció d'unitats implicades el 2020.")
    st.write("- La implicació dels ciclomotors ha patit un descens suau, però continuat, des del 2010.")

    components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16386577"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
   with tab12:
      components.html("""<div class="flourish-embed flourish-pictogram" data-src="visualisation/16385382"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=550)
   with tab13:
      st.markdown("""##### Idees generals""")
      st.write("- El Ripollès presenta la proporció més elevada d'accidents on hi ha implicades bicicletes.")
      st.write("- A les Garrigues, en un 1 de cada 3 accidents hi intervé un vehicle pesant.")
      st.write("- Al Solsonès, en un 40% d'accidents hi intervenen motocicletes.")

      components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/16410010"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=850)
      with st.expander("Dades representades"):
         st.write("""
            El gràfic mostra la distribució espacial per comarca del percentatge de cada tipus d'unitat 
            en el total d'accidents occorreguts entre 2011 i 2021.
            """)
         st.write("Per exemple, per a la unitat *Bicicletes* s'ha dividit el nombre d'unitats de bicicleta d'una comarca en concret entre el nombre total d'unitats implicades en els accidents.")

with tab2:
   st.markdown("""La mortalitat en un accident de trànsit fa referència a la proporció de víctimes mortes enfront 
               de totes les vícitmes implicades. Aquest índex, que hem derivat de les dades originals, pot ser un 
               indicador de la violència dels accidents. Les dades classifiquen les víctimes en ferits lleus, ferits
               greus i morts.  
               Les gràfiques mostren la proporció de cada tipus de víctima, el mapa de mortalitat per comarca i la
               influència de la velocitat de la via on té lloc l'accident i la mortalitat.
               """)


   tab21, tab22, tab23 = st.tabs(["Víctimes", "Mapa", "Velocitat"])
   with tab21:
    components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16412103"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
   with tab22:
      st.markdown("""##### Idees generals""")
      st.write("- Les comarques de la Depressió Central concentren els accidents amb una mortalitat més elevada.El Ripollès presenta la proporció més elevada d'accidents on hi ha implicades bicicletes.")
      st.write("- Del sud del país, el Baix Ebre concentra la mortalitat més elevada.")
      st.write("- Al Pirineu la mortalitat es dispara al Ripollès.")
      components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/16411969"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=850)
   with tab23:
      st.write("La velocitat màxima permesa de la via on té lloc l'accident té una influència clara en la mortalitat dels accidents.")
      st.write("Cal tenir en compte, que la velocitat de les unitats implicades pot superar, de llarg, la màxima permesa de la via.")
      components.html("""<div class="flourish-embed flourish-scatter" data-src="visualisation/16422643"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=850)

with tab3:
   st.write("Els accidents poden ocórrer en moltes circumstàncies, les dades emprades els classifica en cinc tipus diferents. A més, poden estar influenciats per agents externs, com ara l'hora o el dia de la setmana, i les condicions meteorològiques, entre d'altres.")

   tab31, tab32, tab33 = st.tabs(["Tipus", "Influències condicions", "Influències temporals"])

   with tab31:
      components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16423526"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=850)
   with tab32:
      st.write("En la gran majoria d'accidents no s'hi recullen influències externes, però d'entre els accidents que n'inclouen, la figura en mostra la proporció.")
      components.html("""<div class="flourish-embed flourish-bubble-chart" data-src="visualisation/16423444"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=850)
   with tab33:
      components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16423650"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
      components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/16423674"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=850)