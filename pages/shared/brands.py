from nicegui import ui

def show():
    """Render the brands section"""
    with ui.column().classes('w-full items-center p-8'):
        # --- Heading ---
        ui.label("Join these brands").classes(
            "text-3xl font-bold text-gray-800 text-center mb-2")
        ui.label(
            "We've had the pleasure of working with industry-defining brands. "
            "These are just some of them."
        ).classes("text-base text-gray-800 text-center mb-8 opacity-80")

        # --- Brand Logos ---
        brands_data = [
            "/assets/brands/spotify.png",
            "/assets/brands/google.png",
            "/assets/brands/stripe.png",
            "/assets/brands/youtube.png",
            "/assets/brands/microsoft.png",
            "/assets/brands/uber.png",
            "/assets/brands/zoom.png",
            "/assets/brands/medium.png",
            "/assets/brands/grab.png",
            "/assets/brands/shopify.png",
        ]

        # Responsive centered grid
        with ui.element('div').classes(
            "grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 "
            "gap-10 justify-center items-center px-6 max-w-6xl mx-auto"
        ):
            for logo_url in brands_data:
                with ui.element('div').classes(
                    # Taller but still wide enough for long logos
                    "h-16 w-36 flex items-center justify-center"
                ):
                    ui.image(logo_url) \
                        .style("object-fit: contain; object-position: center;") \
                        .classes(
                            "max-h-full max-w-full opacity-80 hover:opacity-100 transition duration-300"
                        )

        # --- Optional separator ---
        ui.separator().classes("my-16")
