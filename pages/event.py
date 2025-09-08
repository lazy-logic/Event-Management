from nicegui import ui

def show_event_page():
    # Render header at the top level
  from nicegui import ui
import random

# Some random Unsplash image categories for variety
HERO_IMAGES = [
    "https://cdn.pixabay.com/photo/2025/08/13/13/02/landscape-9772229_1280.jpg",
    "https://cdn.pixabay.com/photo/2025/08/22/01/18/rabbit-9788945_1280.jpg",
   ]

MAP_IMAGES = [
    "https://cdn.pixabay.com/photo/2024/01/22/22/09/map-8526430_1280.jpg",
    "https://cdn.pixabay.com/photo/2018/05/08/13/56/globe-3383088_1280.jpg",

]

@ui.page('/event')
def show_event_page():
    hero_image = random.choice(HERO_IMAGES)
    map_image = random.choice(MAP_IMAGES)

    # === PAGE CONTAINER ===
    with ui.element('div').classes(
        'max-w-[1320px] mx-auto mt-[40px] bg-white rounded-[10px] shadow-lg overflow-hidden'
    ):
        # === HERO SECTION ===
        with ui.element('div').classes(
            f"relative h-[600px] bg-[url('{hero_image}')] bg-cover bg-center rounded-t-[10px] overflow-hidden"
        ):
            # Overlay
            ui.element('div').classes('absolute inset-0 bg-black/60')

            # Back Button
            with ui.element('a').classes(
                'absolute top-[30px] left-[30px] flex items-center gap-2 px-4 py-2 '
                'bg-[#7848F4] text-white rounded shadow-md cursor-pointer hover:bg-[#6937d9]'
            ):
                ui.icon('arrow_back').classes('text-white')
                ui.label('Back').classes('text-white text-[16px]')

            # HERO TEXT
            with ui.element('div').classes(
                'absolute top-[150px] left-[60px] max-w-[600px] flex flex-col gap-6'
            ):
                ui.label('Dream world wide in Jakarta').classes(
                    'text-[64px] font-bold text-white leading-tight drop-shadow-lg'
                )
                ui.label('IIIT Sonepat').classes(
                    'text-[36px] font-bold text-white drop-shadow'
                )
                ui.label(
                    'DesignHub organized a 3D Modeling Workshop using Blender on 16th February '
                    'at 5 PM. The workshop taught participants the magic of creating stunning 3D models '
                    'and animations using Blender. It was suitable for both beginners and experienced users. '
                    'The event was followed by a blender-render competition, which added to the excitement.'
                ).classes('text-white text-[16px] leading-relaxed max-w-[550px]')
                # View Map link
                with ui.element('div').classes(
                    'flex items-center gap-2 text-white mt-2 underline cursor-pointer'
                ):
                    ui.icon('place')
                    ui.label('View map').classes('text-[18px]')

            # EVENT INFO CARD (Right Side)
            with ui.element('div').classes(
                'absolute top-[140px] right-[60px] w-[385px] bg-white rounded-[10px] shadow-xl p-6 flex flex-col gap-6'
            ):
                ui.label('Date & Time').classes('text-[24px] font-bold text-black')
                ui.separator().classes('bg-gray-200')
                ui.label('Saturday, March 18 2023, 9.30PM').classes('text-[#7E7E7E] text-[18px]')
                ui.label('Add to calendar').classes('text-[#7848F4] text-[16px] cursor-pointer')
                ui.separator().classes('bg-gray-200')

                # Signup Buttons
                with ui.element('div').classes('flex flex-col gap-3 mt-2'):
                    ui.button('Book Now', color='brand').classes(
                        'w-full text-white rounded-[5px] py-3 hover:bg-[#6937d9]'
                    )
                    ui.button('Program Promoter', color='grey').classes(
                        'w-full text-white rounded-[5px] py-3 hover:bg-[#a0a0a0]'
                    )

                ui.label('No Refunds').classes('text-center text-[#7E7E7E] text-[16px] mt-2')

        # === MAIN CONTENT BELOW HERO ===
        with ui.element('section').classes(
            'p-10 bg-[#FAFAFA] grid grid-cols-1 md:grid-cols-3 gap-[40px]'
        ):
            # LEFT COLUMN
            with ui.element('div').classes('md:col-span-2 flex flex-col gap-[40px]'):
                # Description
                with ui.element('div').classes('flex flex-col gap-4'):
                    ui.label('Description').classes('text-[28px] font-bold text-black')
                    ui.label(
                        'This workshop introduced participants to the world of 3D modeling. '
                        'It was designed for both beginners and advanced learners, covering everything '
                        'from the basics of Blender to rendering competitions.'
                    ).classes('text-[#7E7E7E] text-[18px] leading-relaxed')

                # Hours
                    with ui.element('div').classes('flex flex-col gap-4'):
                     ui.label('Hours').classes('text-[28px] font-bold text-black')

                with ui.element('div').classes('flex items-center gap-2 text-[18px]'):
                    ui.label('Weekdays hour:').classes('text-[#7E7E7E]')
                    ui.label('7PM - 10PM').classes('text-[#7848F4] font-semibold')

                with ui.element('div').classes('flex items-center gap-2 text-[18px]'):
                    ui.label('Sunday hour:').classes('text-[#7E7E7E]')
                    ui.label('7PM - 10PM').classes('text-[#7848F4] font-semibold')

                # Organizer Contact
                with ui.element('div').classes('flex flex-col gap-4'):
                    ui.label('Organizer Contact').classes('text-[28px] font-bold text-black')
                    ui.label(
                        'Please go to www.sneakypeeks.com and refer the FAQ section for more detail.'
                    ).classes('text-[#7E7E7E] text-[18px] leading-relaxed')

            # RIGHT SIDEBAR
            with ui.element('div').classes('flex flex-col gap-[40px]'):
                # Location
                with ui.element('div').classes(
                    'flex flex-col gap-4 bg-white p-4 rounded-[10px] shadow'
                ):
                    ui.label('Event Location').classes('text-[24px] font-bold text-black')
                    ui.element('div').classes(
                        f"w-full h-[220px] rounded-[10px] bg-[url('{map_image}')] bg-cover"
                    )
                    ui.label('Dream world wide in Jakarta').classes(
                        'text-[20px] font-semibold text-black'
                    )
                    ui.label(
                        'Dummy location model by RSU... generates more realistic dummy locations.'
                    ).classes('text-[#7E7E7E] text-[16px] leading-relaxed')

                # Tags
                with ui.element('div').classes(
                    'flex flex-col gap-3 bg-white p-4 rounded-[10px] shadow'
                ):
                    ui.label('Tags').classes('text-[24px] font-bold text-black')
                    with ui.element('div').classes('flex flex-wrap gap-2'):
                        for tag in ['Design', '3D', 'Workshop', 'Blender',]:
                            ui.label(tag).classes(
                                'px-4 py-1.5 bg-[#F8F8FA] rounded text-[14px]'
                            )

                # Share
                with ui.element('div').classes(
                'flex flex-col gap-3 bg-white p-4 rounded-[10px] shadow'
            ):
                    ui.label('Share with friends').classes('text-[24px] font-bold text-black')

                with ui.element('div').classes('flex gap-4'):
                    with ui.element('a').props('href=https://facebook.com target=_blank'):
                        ui.icon('fa-brands fa-facebook-f').classes('text-[#1877F2] text-[28px]')
                    with ui.element('a').props('href=https://linkedin.com target=_blank'):
                        ui.icon('fa-brands fa-linkedin-in').classes('text-[#0A66C2] text-[28px]')
                    with ui.element('a').props('href=https://twitter.com target=_blank'):
                        ui.icon('fa-brands fa-twitter').classes('text-[#1DA1F2] text-[28px]')
                    with ui.element('a').props('href=https://wa.me/123456789 target=_blank'):
                        ui.icon('fa-brands fa-whatsapp').classes('text-[#25D366] text-[28px]')
