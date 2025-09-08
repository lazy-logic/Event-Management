from nicegui import ui
from pages.create_event import show_create_event

@ui.page('/new_event')
def show_create_event_page():
    # show_create_event()

    with ui.column().classes('w-full min-h-screen bg-[#F8F8FA] rounded-2xl p-10 items-center'):
        
        # Page Title
        ui.label('Create Event').classes('text-3xl font-bold text-black mb-10')

        # Event Title
        event_title = ui.input(placeholder='Enter your event title').classes(
            'w-[816px] h-[46px] bg-white rounded-md mb-6'
        )

        # Event Venue
        event_venue = ui.input(placeholder='Enter your event venue').classes(
            'w-[816px] h-[46px] bg-white rounded-md mb-6'
        )

        # Start/End Time (two columns)
        with ui.row().classes('w-[816px] justify-between mb-6'):
            with ui.column().classes('w-[394px]'):
                ui.label('Start Time').classes('text-sm text-black self-start')
                start_time = ui.input().props('type=time').classes(
                    'w-full h-[46px] bg-white rounded-md'
                )
            with ui.column().classes('w-[394px]'):
                ui.label('End Time').classes('text-sm text-black self-start')
                end_time = ui.input().props('type=time').classes(
                    'w-full h-[46px] bg-white rounded-md'
                )

        # Start/End Date (two columns)
        with ui.row().classes('w-[816px] justify-between mb-6'):
            with ui.column().classes('w-[394px]'):
                ui.label('Start Date').classes('text-sm text-black self-start')
                start_date = ui.input().props('type=date').classes(
                    'w-full h-[46px] bg-white rounded-md'
                )
            with ui.column().classes('w-[394px]'):
                ui.label('End Date').classes('text-sm text-black self-start')
                end_date = ui.input().props('type=date').classes(
                    'w-full h-[46px] bg-white rounded-md'
                )

        # Start/End Date (two columns)
        with ui.row().classes('w-[816px] justify-between mb-6'):
            with ui.column().classes('w-[394px]'):
                ui.label('Start Date').classes('text-sm text-black self-start')
                start_date = ui.input().props('type=date').classes(
                    'w-full h-[46px] bg-white rounded-md'
                )
            with ui.column().classes('w-[394px]'):
                ui.label('End Date').classes('text-sm text-black self-start')
                end_date = ui.input().props('type=date').classes(
                    'w-full h-[46px] bg-white rounded-md'
                )

        # Title Event Description
        ui.label('Event Description').classes('text-3xl font-bold text-black mb-10')

                # Event Image Upload
        uploaded_file = ui.upload(auto_upload=True).props('accept="image/*"').classes(
            'hidden'  # hide the default blue uploader button
        )
        with ui.element('div').classes(
            'w-[813px] h-[254px] bg-[#ECECEC] hover:bg-[#DAD6F9] rounded-xl flex items-center justify-center mb-6 cursor-pointer border border-dashed border-gray-400'
        ).on ('click', lambda: uploaded_file.pick_files()):
            ui.label('Click or Drop Image Here').classes('text-gray-500')

        # Event Description
        event_description = ui.textarea(placeholder='Enter event description').classes(
            'w-[813px] h-[173px] bg-white rounded-md mb-6 shadow-md border border-gray-200 p-3'
        )


        # Submit Button
        def submit():
            details = {
                "title": event_title.value,
                "venue": event_venue.value,
                "start_time": start_time.value,
                "end_time": end_time.value,
                "start_date": start_date.value,
                "end_date": end_date.value,
                "description": event_description.value,
                "image": uploaded_file.value[0]['name'] if uploaded_file.value else None,
            }
            ui.notify(f'Event Created: {details}')

        ui.button('Create Event', on_click=submit).classes(
            'w-[813px] h-[49px] bg-deep-purple text-white rounded-md text-base'
        )
