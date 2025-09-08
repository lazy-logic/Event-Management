from nicegui import ui

def show_blogs_page():
    """Render a blogs section similar to the upcoming events style."""

    blogs = [
        {
            'title': 'Blog 1 - Event Insights',
            'date': 'March 18, 2023',
            'excerpt': 'Learn how events are shaping industries.',
            'image': '/assets/blogs/blog1.jpg',
        },
        {
            'title': 'Blog 2 - Event Insights',
            'date': 'March 18, 2023',
            'excerpt': 'Learn how events are shaping industries.',
            'image': '/assets/blogs/blog2.jpg',
        },
        {
            'title': 'Blog 3 - Event Insights',
            'date': 'March 18, 2023',
            'excerpt': 'Learn how events are shaping industries.',
            'image': '/assets/blogs/blog3.jpg',
        },
    ]

    with ui.column().classes('w-full px-6 sm:px-12 lg:px-24 py-12 gap-8 items-start'):
        # Left-aligned title with two colors
        ui.html('''
            <h2 style="
                font-family: 'Roboto', sans-serif;
                font-weight: 700;
                font-size: 36px;
                line-height: 42px;
                margin: 0;
                spacing: 0;
            ">
                Our <span style="color:#7848F4;">Blogs</span>
            </h2>
        ''')

        # Grid for 3 blog cards (aligned in a row like upcoming events)
        with ui.row().classes('w-full gap-8 mt-6 flex-wrap justify-start'):
            for blog in blogs:
                with ui.column().classes('w-full sm:w-80 shadow-xl rounded-2xl flex flex-col'):
                    ui.image(blog['image']).classes('w-full h-64 object-contain rounded-t-1xl')
                    with ui.column().classes('flex-1 p-4 gap-2 items-start'):
                        ui.label(blog['title']).classes('text-l font-bold')
                        ui.label(blog['date']).classes('text-deep-purple')
                        ui.label(blog['excerpt']).classes('text-gray-600')
                       