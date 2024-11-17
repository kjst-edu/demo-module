from shiny.express import module, render, ui

@module
def panel_a(input, output, session):
    
    ui.input_slider("val", "Slider label", min=0, max=100, value=50)

    @render.text
    def slider_val():
        return f"Slider value: {input.val()}"