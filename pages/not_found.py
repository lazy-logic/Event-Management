from nicegui import ui
from pages.shared.header import show_header
from pages.shared.footer import show_footer

# ✅ Universal 404 page (catch-all)

def not_found_page():
    show_header()

    # Load Themify icons
    ui.add_head_html(
        '<link href="https://cdn.jsdelivr.net/themify-icons/0.1.2/css/themify-icons.css" rel="stylesheet" />'
    )

    with ui.element('div').classes(
        'w-full min-h-screen bg-[#F8F8FA] flex flex-col items-center rounded-2xl relative'
    ):
        # Illustration
        ui.image("assets/img/404.png").classes('w-[722px] h-[392px] mt-12')

        # Heading + Message
        ui.label('Oops!').classes('text-3xl font-bold mt-8')
        ui.label('We can’t seem to find the page you are looking for').classes(
            'text-xl text-gray-500 text-center mt-2'
        )

        # Back Button
        ui.button('Back to Homepage', on_click=lambda: ui.open('/')).classes(
            'mt-10 bg-deep-purple text-white px-10 py-3 rounded-full text-lg font-bold'
        )

        # Follow Us Section
        with ui.column().classes('mt-16 items-center justify-center'):
            ui.label('Follow us on').classes('text-lg text-black mb-4')

            with ui.row().classes('gap-6 justify-center'):
                for icon, url in [
                    ('ti-instagram', 'https://instagram.com'),
                    ('ti-facebook', 'https://facebook.com'),
                    ('ti-linkedin', 'https://linkedin.com'),
                    ('ti-twitter', 'https://twitter.com'),
                    ('ti-youtube', 'https://youtube.com'),
                ]:
                    with ui.element('div').classes(
                        'w-16 h-16 bg-[#7848F4]/10 rounded-2xl flex items-center justify-center cursor-pointer hover:scale-110 transition'
                    ):
                        ui.html(f'<i class="{icon} text-2xl text-[#7848F4]"></i>').on(
                            'click', lambda e, url=url: ui.open(url)
                        )
    ui.html("") # Spacer to prevent content overlap

   