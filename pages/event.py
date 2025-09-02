from nicegui import ui

@ui.page('/event')
def show_event_page():
    ui.label('Event Page')
    ui.button('Go to Sign In', on_click=lambda: ui.navigate.to('/signin'))
    ui.button('Go to Sign Up', on_click=lambda: ui.navigate.to('/signup'))