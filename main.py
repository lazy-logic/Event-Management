from nicegui import app, ui

# Import pages
from pages.blogs import show_blogs_page
from pages.home import show_home_page
from pages.signup import show_signup_page
from pages.signin import show_signin_page
from pages.shared.college import show_college_page
from pages.event import show_event_page
from pages.contact import contact_page
from pages.not_found import not_found_page
from pages.shared.header import show_header
from pages.shared.footer import show_footer
import pages.home
from pathlib import Path
from pages.new_event import show_create_event_page


# Serve static files from the 'assets' directory
assets_dir = Path(__file__).parent / 'assets'
app.add_static_files('/assets', str(assets_dir))

ui.colors(
    brand='#7848F4',   # your main purple
    primary='#7848F4', # optional: also set as primary
    brand1='#31089A',
    secondary='#7848F4',
    accent = '#9c27b0',
    dark = '#1d1d1d',
    dark_page= '#121212',
    positive= '#21ba45',
    negative = '#c10015',
    info='#7848F4',
    warning= '#f2c037',
)
        

@ui.page("/")
def _home():
    show_header()
    show_home_page()
    show_footer()


@ui.page("/signup")
def _signup():
    show_signup_page()


@ui.page("/signin")
def _signin():
    show_signin_page()


@ui.page("/college")
def _college():
    show_header()
    show_college_page()
    show_footer()


@ui.page("/event")
def _event():
    show_header()
    show_event_page()
    show_blogs_page()
    show_blogs_page()
    show_footer()


@ui.page("/contact")
def _contact():
    show_header()
    contact_page()
    show_footer()   


@ui.page("create_event")
def _create_event():
    # TODO: Implement the create event page
    pass

@ui.page("/not_found")
def _not_found():
    show_header()
    not_found_page()
    show_footer()
   
 
@ui.page("/blogs")
def _blogs():
    show_blogs_page()
    
    
@ui.page("/new_event")
def _new_event():
    show_header()
    show_create_event_page()


