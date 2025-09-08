from nicegui import ui
  
@ui.page('/signup')
def show_signup_page():
    with ui.row().classes('w-full h-screen'):  # full width & height
        # LEFT SIDE (Sign Up form)
        with ui.element('div').classes(
            'flex-1 flex flex-col justify-center items-center bg-white p-10 rounded-l-2xl shadow-lg'
        ):
            ui.label('Sign Up Page').classes('text-3xl font-bold mb-6 text-gray-800')
            ui.button('Back to Home', on_click=lambda: ui.navigate.to('/home'))
            ui.input(label='Email').classes('w-80 mb-4')
            ui.input(label='Password', password=True).classes('w-80 mb-6')
            ui.button('Sign Up').classes('bg-green hover:bg-blue-600 text-white px-6 py-2 rounded-lg shadow')

        # RIGHT SIDE (Image)
        with ui.element('div').classes(
            'flex-1 flex items-center justify-center bg-gradient-to-r from-blue-400 to-blue-600 rounded-r-2xl'
        ):
            ui.image('https://cdn.pixabay.com/photo/2022/11/14/14/13/lake-7591750_1280.jpg').classes(
                'object-cover w-full h-half rounded-r-2xl'
            )