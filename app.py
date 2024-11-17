from functools import partial
from pathlib import Path

from shiny import reactive, req
from shiny.ui import page_navbar
from shiny.express import input, render, ui

from panel_a import panel_a
from panel_b import panel_b
from mod_markdown import markdown

static = Path(__file__).parent / "static"

ui.page_opts(
    title="Module Demo",  
    page_fn=partial(page_navbar, id="page"),  
)

with ui.nav_panel("Panel A"):  
    panel_a("main")

with ui.nav_panel("Panel B"):
    panel_b("main")

with ui.nav_panel("page 1"): 
    markdown("page1", static / "page1.md")

with ui.nav_panel("page 2"):
    markdown("page2", static / "page2.md")