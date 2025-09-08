from nicegui import ui

@ui.page('/signup')
def show_signup_page():
    # disable page scrolling
    ui.add_head_html('<style>body { overflow: hidden; }</style>')

    # Ensure the image CSS is available (use a reliable external image or local asset)
    image_url = 'https://cdn.pixabay.com/photo/2024/11/28/08/45/woman-9230049_1280.jpg'
    ui.add_head_html(f'''
        <style>
            /* background for right-side panel */
            .signup-right-bg {{
                background-image: url("{image_url}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                height: 100%;
            }}
            /* ensure the overall card does not overlap the image */
            .signup-left-card {{
                min-width: 360px;
                max-width: 520px;
            }}
        </style>
    ''')

    # Root row: explicit flex-row, gap and no overflow so columns won't overlap
    with ui.row().classes('w-full h-screen gap-8 overflow-hidden items-stretch'):
        # LEFT SIDE (form) - fixed-ish width so the right image has space
        with ui.element('div').classes(
            'w-2/5 min-w-[360px] flex items-center justify-center bg-transparent'
        ):
            with ui.row().classes("items-center gap-2 mb-8"):
                ui.icon("hub").classes("text-[#7848F4] text-3xl")
                ui.label("Event Hive").classes("text-2xl font-extrabold text-gray-900")

            with ui.card().classes('signup-left-card w-full p-8 rounded-2xl shadow-xl'):
                ui.label('Create Account').classes('text-3xl md:text-4xl font-extrabold mb-1 text-gray-900')
                ui.label('Join Event Hive today').classes('text-gray-500 mb-6')
                with ui.column().classes('w-full'):
                    ui.input(placeholder='Enter your email').props('outlined dense').classes('w-full mb-4')
                    ui.input(placeholder='Enter your password', password=True).props('outlined dense').classes('w-full mb-4')
                    ui.input(placeholder='Confirm password', password=True).props('outlined dense').classes('w-full mb-6')
                    ui.button(
                        'Sign Up', color='brand1',
                        on_click=lambda: ui.notify('Account created! 🎉')
                    ).classes(
                        'w-full py-3 rounded-lg bg-gradient-to-r from-indigo-500 to-purple-600 text-white font-semibold shadow-md'
                    )
                    ui.html(
                    '<p class="text-center text-gray-600 text-sm">'
                    'Already have an account? '
                    '<a href="/signin" class="text-[#7848F4] font-semibold hover:underline">Signin</a>'
                    '</p>'
                )
        # RIGHT SIDE (image) - takes remaining space; uses background-image to guarantee visibility
        with ui.element('div').classes('flex-1 relative min-w-[420px] h-full'):
            # background area that will always be visible and trimmed to container
            with ui.element('div').classes('signup-right-bg absolute inset-0'):
                # subtle overlay for text readability
                ui.element('div').classes('absolute inset-0 bg-gradient-to-r from-purple-600/55 to-indigo-600/55')
                # text overlay centered on the image
                with ui.column().classes('relative z-10 h-full items-center justify-center text-center p-6'):
                    ui.label('Welcome to Event Hive').classes('text-white text-2xl md:text-4xl font-extrabold mb-2')
                    ui.label('Discover and manage events effortlessly').classes('text-white text-base md:text-lg max-w-lg')

# If you run this file directly, you'll need ui.run() elsewhere in your main app file.
