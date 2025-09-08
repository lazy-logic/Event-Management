from nicegui import ui


# from pages.create_event import show_create_event
from pages.shared import header
from pages.shared import footer
from pages.shared import brands
from pages.shared.college import show_college_page 
from pages.blogs import show_blogs_page


# ----------------- HOME PAGE -----------------
@ui.page("/home")
def show_home_page():

    ui.add_head_html('''
            <style>
                body { 
                    overflow-x: hidden; /* disable left-right scrolling */
                }
                .no-overflow {
                    max-width: 100vw; 
                    overflow-x: hidden;
                    margin: 0;
                    margin-left: 0px;
                    margin-right: auto;
                    padding: 0;
                    box-sizing: none;
                }
            </style>
        ''')

    ui.colors(
        brand='#7848F4',   # your main purple
        primary='#7848F4', # optional: also set as primary
        brand1='#31089A',
        secondary='#26a69a',
        accent = '#9c27b0',
        dark = '#1d1d1d',
        dark_page= '#121212',
        positive= '#21ba45',
        negative = '#c10015',
        info='#7848F4',
        warning= '#f2c037',
    )
    

    # ---------------- NAVBAR ----------------
    header.show_header()

    # ---------------- HERO SECTION ----------------
        # with ui.element("div").style("background-image: url(/assets/hero.jpg)").classes("h-screen w-screen flex flex-col bg-cover bg-center justify-center items-center"):
    with ui.element("div").classes(
        "relative bg-cover w-screen h-screen bg-center flex flex-col items-center justify-center text-center scroll-smooth"
    ).style(
        'background-image: url("assets/img/background2.jpg");'
    ):
        ui.element("div").classes("absolute inset-0 bg-black/50")
        ui.label("MADE FOR THOSE").classes(
            "text-white text-4xl md:text-6xl font-extrabold z-10 animate-fadeInDown mt-10"
        )
        ui.label("WHO DO").classes(
            "text-white text-4xl md:text-6xl font-extrabold z-10 animate-fadeInDown mt-10"
        )
        ui.label("Discover, create and join events effortlessly").classes(
            "text-white text-lg md:text-2xl mt-4 z-10 animate-fadeInUp"
        )
        # search bar
        # ---------------- SEARCH BAR ----------------
        with ui.row().classes(
            "absolute -bottom-10 bg-[#10107B] rounded-xl shadow-lg p-4 w-11/12 md:w-3/4 "
            "justify-around space-x-4 z-20 animate-fadeInUp"
        ):

            # Event type select
            ui.select(
                ["Select event type", "Conference", "Workshop", "Concert"],
                value="Select event type",
                with_input=True,
            ).props("outlined dense").classes("w-1/4 bg-white rounded-lg text-gray-700")

            # Location select
            ui.select(
                ["Select location", "Accra", "London", "New York"],
                value="Select location",
                with_input=True,
            ).props("outlined dense").classes("w-1/4 bg-white rounded-lg text-gray-700")

            # Date/time input
            ui.input(label="Choose date and time").props("outlined dense").classes(
                "w-1/4 bg-white rounded-lg text-gray-700"
            )

            # Search button
            ui.button(icon="search", color='brand1').classes("bg-purple-600 text-white rounded-sm p-3 hover:bg-indigo-700 "
                "hover:scale-105 transition-all shadow-lg"
            )

    ui.element("div").style("height: 20px")  # Spacer to prevent content overlap

    # ---------------- UPCOMING EVENTS ----------------
    # Upcoming Events title and filters in a single row, spaced apart
    with ui.row().classes(
        "w-full px-[100px] mr-auto mt-20 justify-between items-center"
    ):
        # Left-aligned title
        with ui.row().classes("items-baseline"):
            ui.label("Upcoming").classes(
                "font-roboto text-[30px] font-bold leading-[42px] text-black"
            )
            ui.label("Events").classes(
                "font-roboto text-[30px] font-bold leading-[42px] text-[#7848F4] ml-2"
            )
        # Right-aligned filters
        with ui.row().classes("space-x-4"):
            # Event Type Filter
            ui.select(
                ["All Types", "Conference", "Workshop", "Concert"],
                value="All Types",
            ).props("outlined dense").classes(
                "w-[140px] h-[40px] bg-[rgba(104,124,148,0.05)] rounded-md text-[12px] text-[#131315]"
            )

            # Location Filter
            ui.select(
                ["All Locations", "Accra", "London", "New York"],
                value="All Locations",
            ).props("outlined dense").classes(
                "w-[140px] h-[40px] bg-[rgba(104,124,148,0.05)] rounded-md text-[12px] text-[#131315]"
            )

            # Date Filter
            ui.select(
                ["Any Date", "Today", "This Week", "This Month"],
                value="Any Date",
            ).props("outlined dense").classes(
                "w-[140px] h-[40px] bg-[rgba(104,124,148,0.05)] rounded-md text-[12px] text-[#131315]"
            )
    # Separator below the row
    ui.separator().classes("my-6 bg-gray-300 h-[1px] w-full")

    # Event cards data

    event_images = [
        "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?auto=format&fit=crop&w=400&q=80",
        "https://images.unsplash.com/photo-1556740749-887f6717d7e4?auto=format&fit=crop&w=400&q=80",
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=400&q=80",
        "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=400&q=80",
        "https://images.unsplash.com/photo-1496307042754-b4aa456c4a2d?auto=format&fit=crop&w=400&q=80",
        "https://images.unsplash.com/photo-1487014679447-9f8336841d58?auto=format&fit=crop&w=400&q=80",
    ]

    # Grid layout for events
    with ui.row().classes(
        "grid grid-cols-1 md:grid-cols-3 lg:grid-cols-3 gap-8 px-[120px] mt-10"
    ):
        for i, img_url in enumerate(event_images):
            with ui.card().classes(
                "relative w-[320px] h-[400px] bg-white shadow-[0px_-8px_80px_rgba(0,0,0,0.07),0px_-2.9px_29.2px_rgba(0,0,0,0.05),0px_-1.4px_14.1px_rgba(0,0,0,0.04),0px_-0.7px_6.9px_rgba(0,0,0,0.03),0px_-0.27px_2.7px_rgba(0,0,0,0.02)] rounded-lg overflow-hidden hover:scale-105 transition duration-300 animate-fadeInUp"
            ):
                # Event Image
                with ui.element("div").classes("relative h-[240px] w-full"):
                    ui.image(img_url).classes("h-full w-full object-cover rounded-md")

                    # FREE Tag
                    with ui.element("div").classes(
                        "absolute top-5 left-5 bg-white text-[#7848F4] text-[10px] font-roboto rounded px-2 py-1 shadow"
                    ):
                        ui.label("FREE")

                # Event Info
                with ui.element("div").classes("absolute left-5 right-5 top-[275px]"):
                    ui.label(f"Event {i+1} - Bestseller Book Bootcamp").classes(
                        "text-[16px] leading-[19px] font-roboto text-black"
                    )

                # Date
                with ui.element("div").classes("absolute left-5 right-5 bottom-[57px]"):
                    ui.label("Saturday, March 18 | 9:30PM").classes(
                        "text-[12px] leading-[14px] font-roboto text-[#7848F4]"
                    )

                # Location
                with ui.element("div").classes("absolute left-5 right-5 bottom-[21px]"):
                    ui.label("ONLINE EVENT • Attend anywhere").classes(
                        "text-[12px] leading-[14px] font-roboto text-[#7E7E7E]"
                    )

    # Load more button
    ui.button("Load more...", color="brand").classes(
        "mx-auto mt-8 hover:bg-indigo-700 text-white px-6 py-2  shadow transition duration-300"
    )

    # ---------------- CREATE EVENT CTA ----------------
    ui.separator().classes("my-20")
    

    # ---------------- BRANDS ----------------

    # Use shared brands section
    brands.show()

    # COLLEGE SECTION
    show_college_page()
    
    
    # ---------------- BLOGS ----------------
    show_blogs_page()
    

# ---------------- RUN APP ----------------
ui.run(title="Event Hive", reload=True)
