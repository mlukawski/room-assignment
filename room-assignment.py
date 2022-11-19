import streamlit as st
import math

st.subheader("Please adjust session parameters:")
st.slider(label="Participants per room", min_value=1, max_value=15,step=1, key="ppr")
st.slider(label="Number of facilitators", min_value=1, max_value=10,step=1, key="nof")
st.number_input(label="Number of participants: ", min_value=1, value=50, key="nop")

no_of_rooms = int(round(st.session_state["nop"]/st.session_state["ppr"],0))
rooms_per_facilitator = no_of_rooms / st.session_state["nof"]


st.subheader(f"Create {no_of_rooms} breakout rooms.")

for i in range(st.session_state["nof"]):
    facilitator_number = i + 1
    facilitator = st.text_input(label=f"Facilitator {facilitator_number}:",
                                placeholder="Type in facilitator's name")

    first_room = math.floor((facilitator_number * rooms_per_facilitator) - rooms_per_facilitator + 1)
    last_room = math.floor(facilitator_number * rooms_per_facilitator)
    st.subheader(f"Rooms {first_room} - {last_room}")

