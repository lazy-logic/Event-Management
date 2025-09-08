from nicegui import ui

def render_header():
    with ui.header().classes('bg-white shadow-md fixed top-0 left-0 w-full z-50'):
        with ui.row().classes('container mx-auto flex items-center justify-between px-6 py-4'):
            ui.label('EventHive').classes('text-2xl font-bold text-indigo-600')
            with ui.row().classes('space-x-6'):
                ui.link('Home', '/').classes('text-gray-700 hover:text-indigo-600')
                ui.link('Events', '/event').classes('text-gray-700 hover:text-indigo-600')
                ui.link('Colleges', '/college').classes('text-gray-700 hover:text-indigo-600')
                ui.link('Contact', '/contact').classes('text-gray-700 hover:text-indigo-600')
                ui.button('Sign In', on_click=lambda: ui.navigate.to('/signin')).classes(
                    'bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700'
                )

def render_footer():
    with ui.footer().classes('bg-gray-900 text-white py-6 mt-16'):
        with ui.column().classes('container mx-auto text-center'):
            ui.label('© 2025 EventHive. All rights reserved.').classes('text-gray-400 text-sm')
            with ui.row().classes('justify-center space-x-6 mt-4'):
                ui.link('Privacy Policy', '/privacy').classes('text-gray-400 hover:text-white text-sm')
                ui.link('Terms of Service', '/terms').classes('text-gray-400 hover:text-white text-sm')
                ui.link('Contact Us', '/contact').classes('text-gray-400 hover:text-white text-sm')
