from shiny.express import module, ui

@module
def markdown(input, output, session, path):
    with open(path) as f:
        md = f.read()

    ui.markdown(md)