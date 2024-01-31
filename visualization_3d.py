import pyvista as pv
pv.start_xvfb()
import streamlit as st
import tempfile
from stpyvista import stpyvista

path_to_stl = 'assets/lungs.stl'

st.set_page_config(page_icon="🧊", layout="wide")

plotter = pv.Plotter(border=False, window_size=[1000, 1000])
plotter.background_color = "#000000"

reader = pv.STLReader(path_to_stl)

mesh = reader.read()
plotter.add_mesh(mesh, color="#ffc800")
plotter.view_isometric()

stpyvista(plotter, key="my_stl")