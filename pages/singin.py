from nicegui import ui

@ui.page('/signin')
def show_signin_page():
    ui.label('Sign In Page')
    ui.button('Back to Events', on_click=lambda: ui.navigate.to('/event'))
    ui.input(label='Username', placeholder='Enter your username')
    ui.button('Sign In', on_click=lambda: ui.notify('Sign In clicked'))
    ui.input(label='Password', placeholder='Enter your password', password=True)
    ui.button('Sign In', on_click=lambda: ui.notify('Sign In clicked'))
