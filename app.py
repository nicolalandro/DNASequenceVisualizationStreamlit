import streamlit as st
from streamlit_seqviz import streamlit_seqviz

st.subheader("DNA Sequence Vistualization Test")
st.markdown("This is a demo for [streamlit_seqviz](https://gitlab.com/nicolalandro/streamlit-seqviz) library that is lib for DNA sequence visualization.")
streamlit_seqviz(
    name = "J23100",
    seq = "TTGACGGCTAGCTCAGTCCTAGGTACAGTGCTAGC",
    annotations = [{ "name": "promoter", "start": 0, "end": 30, "direction": 1 }],
    style =  { "height": "100vh", "width": "100vw" },
    highlights = [{ "start": 0, "end": 10 }],
    enzymes = [
        "EcoRI",
        "PstI",
        {
            "name": "Cas9",
            "rseq": "NGG", # recognition sequence
            "fcut": 0, # cut index on FWD strand, relative to start of rseq
            "rcut": 1, # cut index on REV strand, relative to start of rseq
            "color": "#D7E5F0", # color to highlight recognition site with
            "range": {
                "start": 4,
                "end": 8,
            },
        },
    ],
)