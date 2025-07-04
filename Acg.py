import streamlit as st
import pandas as pd
from Andhra_details import andhra_show
from Karnataka_details import karnataka_show
import warnings
warnings.filterwarnings("ignore")
def acg_show():
    session_state = st.session_state
    if 'page' not in session_state:
        session_state.page = None 
    st.subheader('General Election to Assembly Constituencies: Trends & Results June-2024')

    andh = ['TDP', 'JnP', 'YSRCP', 'BJP']
    wandh = [135, 21, 11, 8]

    kar = ['BJP', 'INC', 'JD(S)', 'Others']
    wkar = [104, 78, 37, 5]

    col1, col2 = st.columns([2, 2])

    # Add a new row for the prediction button
    col_pred = st.container()
    with col_pred:
        prediction_button = st.button("Election Prediction", use_container_width=True, type="primary")
        if prediction_button:
            session_state.page = 'Prediction'

    with col1:
        st.markdown(f"""
            <div style="background-color: teal; border: solid 2px teal; border-radius: 10px; overflow: hidden;max-height:700px; max-width: 700px; margin: 0 auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                <div style="background-color: white; color: teal; font-size:20.4px; font-weight:500; text-align: center; padding: 10px; border-bottom: solid 2px teal;font-weight: bolder;">
                    Andhra Pradesh
                </div>
                <div style="padding: 20px; color: white; display: flex; justify-content: space-between; align-items: center;">
                    <p style="margin: 10px 0; font-size: 1.2em;">Assembly Constituency</p>
                    <p style="background-color: grey; color: white; padding: 10px; font-size: 1.5em; border-radius: 5px; margin: 0;">175</p>
                </div>
                <p style="font-size:12px; color:white; padding-left:15px">Status of Top Five Parties</p>
                <div style="background-color: white; padding: 20px; border-radius: 5px; margin-top: 20px;text-align: center;">
                    <table style="width: 100%; color:black; border-collapse: collapse;">
                        <tr style="text-align: center; padding: 8px; background-color: teal; color: white;">
                            <th style="text-align: center; padding: 12px;">Parties</th>
                            <th style="text-align: center; padding: 12px;">Leading/Won</th>
                        </tr>
                        <tr style="background-color: #f2f2f2;">
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;">{andh[0]}</td>
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;">{wandh[0]}</td>
                        </tr>
                        <tr>
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;">{andh[1]}</td>
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;">{wandh[1]}</td>
                        </tr>
                        <tr style="background-color: #f2f2f2;">
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;">{andh[2]}</td>
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;">{wandh[2]}</td>
                        </tr>
                        <tr>
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;">{andh[3]}</td>
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;">{wandh[3]}</td>
                        </tr>
                         <tr>
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;"></td>
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;"></td>
                        </tr>
                        <tr>
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;"></td>
                        </tr>
                    </table>
                </div>
            </div>
        """, unsafe_allow_html=True)

        andhra_button = st.button("Andhra Pradesh",use_container_width=True,type="primary")
        if andhra_button:
            session_state.page = 'Andhra Pradesh'

    with col2:
        st.markdown(f"""
            <div style="background-color: #1a237e; border: solid 2px #1a237e; border-radius: 10px; overflow: hidden;max-height:700px; max-width: 700px; margin: 0 auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                <div style="background-color:white; font-size:20.4px; font-weight:500; color: #1a237e; text-align: center; padding: 10px; border-bottom: solid 2px #1a237e;font-weight: bolder;">
                    Karnataka
                </div>
                <div style="padding: 20px; color: white; display: flex; justify-content: space-between; align-items: center;">
                    <p style="margin: 10px 0; font-size: 1.2em;">Assembly Constituency</p>
                    <p style="background-color: grey; color: white; padding: 10px; font-size: 1.5em; border-radius: 5px; margin: 0;">224</p>
                </div>
                <p style="font-size:12px; color:white; padding-left:15px">Status of Top Four Parties</p>
                <div style="background-color: white; padding: 20px; border-radius: 5px; margin-top: 20px;text-align: center;">
                    <table style="width: 100%; color:black; border-collapse: collapse;">
                        <tr style="text-align: center; padding: 8px; background-color: #1a237e; color: white;">
                            <th style="text-align: center; padding: 12px;">Parties</th>
                            <th style="text-align: center; padding: 12px;">Leading/Won</th>
                        </tr>
                        <tr style="background-color: #f2f2f2;">
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;">{kar[0]}</td>
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;">{wkar[0]}</td>
                        </tr>
                        <tr>
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;">{kar[1]}</td>
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;">{wkar[1]}</td>
                        </tr>
                        <tr style="background-color: #f2f2f2;">
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;">{kar[2]}</td>
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;">{wkar[2]}</td>
                        </tr>
                        <tr>
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;">{kar[3]}</td>
                            <td style="text-align: center; font-size:13.6px; font-weight:600; padding: 12px;">{wkar[3]}</td>
                        </tr>
                    </table>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
        karnataka_button = st.button("Karnataka",use_container_width=True,type="primary")
        if karnataka_button:
            session_state.page = 'Karnataka'

    if session_state.page == 'Andhra Pradesh':
        andhra_show()
    elif session_state.page == 'Karnataka':
        karnataka_show()
    elif session_state.page == 'Prediction':
        st.subheader('Election Prediction')
        # --- Prediction Form ---
        st.write('Enter details to predict election outcome:')
        # Example party list (replace with actual unique parties from your data)
        party_list = [
            'Bharatiya Janata Party',
            'Indian National Congress',
            'Janata Dal  (Secular)',
            'Bahujan Samaj Party',
            'Independent',
            'Others'
        ]
        party = st.selectbox('Party', party_list)
        percent_votes = st.number_input('% of Votes', min_value=0.0, max_value=100.0, value=50.0, step=0.1)
        if st.button('Predict'):
            # Dummy prediction logic (replace with model inference)
            if percent_votes > 40:
                st.success(f'Prediction: {party} is likely to WIN!')
            else:
                st.warning(f'Prediction: {party} is likely to LOSE.')
warnings.resetwarnings()
