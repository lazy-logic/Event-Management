from nicegui import ui

def show_home_page():
    ui.label('Home Page')
    with ui.row():
        ui.button('Go to Sign In', on_click=lambda: ui.set_page('signin'))
        ui.button('Go to Sign Up', on_click=lambda: ui.set_page('signup'))
    with ui.row():
        ui.link('College', "/college")
        ui.link('Event', "/event")