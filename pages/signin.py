from nicegui import ui

@ui.page('/signin')
def show_signin_page():
    # disable page scrolling
    ui.add_head_html('<style>body { overflow: hidden; }</style>')

    # reuse the same background image from signup
    image_url = 'https://cdn.pixabay.com/photo/2024/11/28/08/45/woman-9230049_1280.jpg'
    ui.add_head_html(f'''
        <style>
            .signin-left-bg {{
                background-image: url("{image_url}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                height: 100%;
            }}
            .signin-right-card {{
                min-width: 360px;
                max-width: 480px;
            }}
        </style>
    ''')

    # Root container
    with ui.row().classes('w-full h-screen gap-8 overflow-hidden items-stretch'):
        # LEFT SIDE (background image with overlay)
        with ui.element('div').classes('flex-1 relative min-w-[420px] h-full'):
            with ui.element('div').classes('signin-left-bg absolute inset-0'):
                ui.element('div').classes('absolute inset-0 bg-gradient-to-r from-purple-600/55 to-indigo-600/55')
                with ui.column().classes('relative z-10 h-full items-center justify-center text-center p-6'):
                    ui.label('Welcome Back to Event Hive').classes('text-white text-2xl md:text-4xl font-extrabold mb-3')
                    ui.label('Manage your events with ease').classes('text-white text-base md:text-lg max-w-md')

        # RIGHT SIDE (form)
        with ui.element('div').classes(
            'w-2/5 min-w-[360px] flex items-center justify-center bg-transparent'
        ):
            with ui.row().classes("items-center gap-2 mb-8"):
                ui.icon("hub").classes("text-[#7848F4] text-3xl")
                ui.label("Event Hive").classes("text-2xl font-extrabold text-gray-900")

            with ui.card().classes('signin-right-card w-full p-8 rounded-2xl shadow-xl'):
                ui.label('Welcome Back').classes('text-3xl md:text-4xl font-extrabold mb-2 text-gray-900')
                ui.label('Log in to continue').classes('text-gray-500 mb-6 text-center')

                with ui.column().classes('w-full'):
                    ui.input(placeholder='Enter your email').props('outlined dense').classes('w-full mb-4')
                    ui.input(placeholder='Enter your password', password=True).props('outlined dense').classes('w-full mb-6')

                    ui.button(
                        'Login',color='brand1',
                        on_click=lambda: ui.notify('Login successful! ✅')
                    ).classes(
                        'w-full py-3 rounded-lg bg-gradient-to-r from-indigo-500 to-purple-600 text-white font-semibold shadow-md mb-4'
                    )

                    ui.html(
                        '<p class="text-center text-gray-600 text-sm">'
                        'Don’t have an account? '
                        '<a href="/signup" class="text-[#7848F4] font-semibold hover:underline">Sign up</a>'
                        '</p>'
                    )
