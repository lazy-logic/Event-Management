from nicegui import ui

def show_header():
    """Renders the shared header component for the application."""
    
    
    with ui.header().classes('bg-white text-gray-800'):
        with ui.row().classes('w-full items-center justify-between px-4 py-2'):
            # Logo and Title
            with ui.row().classes('items-center gap-4 cursor-pointer') as logo:
                ui.colors(brand='#7848F4')
                ui.icon('hub', size='2.5rem').props('color=brand')
                ui.label('Event Hive').classes('text-2xl font-bold')
            logo.on('click', lambda: ui.navigate.to('/'))

            # Desktop Navigation
            with ui.row().classes('items-center gap-8 hidden md:flex').props('color=brand'):
                ui.button('Home', on_click=lambda: ui.navigate.to('/')).props('color=brand text-lg')
                ui.button('Colleges', on_click=lambda: ui.navigate.to('/college')).props('flat text-lg text-deep-purple-')
                ui.button('Events', on_click=lambda: ui.navigate.to('/event')).props('flat text-lg')
                ui.button('Contact', on_click=lambda: ui.navigate.to('/contact')).props('flat text-lg')

            # Auth Buttons
            with ui.row().classes('items-center gap-2 md:flex'):
             ui.colors(brand='#7848F4')
             ui.button('Sign In', on_click=lambda: ui.navigate.to('/signin')).classes('text-deep-purple-700').props('flat color=deep-purple-7')
             ui.button('Sign Up', on_click=lambda: ui.navigate.to('/signup')).props('color=brand text-white')

            # Mobile Menu
            with ui.element('div').classes('md:hidden'):
                with ui.button(icon='menu').props('flat round'):
                    with ui.menu() as menu:
                        ui.menu_item('Home', on_click=lambda: ui.navigate.to('/'))
                        ui.menu_item('Colleges', on_click=lambda: ui.navigate.to('/college'))
                        ui.menu_item('Events', on_click=lambda: ui.navigate.to('/event'))
                        ui.menu_item('Contact', on_click=lambda: ui.navigate.to('/contact'))
                        ui.separator()
                        ui.menu_item('Sign In', on_click=lambda: ui.navigate.to('/signin'))
                        ui.menu_item('Sign Up', on_click=lambda: ui.navigate.to('/signup'))
                menu.anchor = 'top right'
                menu.offset = (0, 10)