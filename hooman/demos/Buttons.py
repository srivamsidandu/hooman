from hooman import Hooman

import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)

#the function that gets called when the button is clicked on
def button_clicked(): 
    if button2.y == 250:
        button2.y = 300
    else:
        button2.y = 250


grey_style = {
    'background_color':(200, 200, 200),
    'hover_background_color':(220, 220, 220),
    'curve':0.1,
    'padding_x':5,
    'padding_y':5,
    'font_size':15
    }
button1 = hapi.button(150, 150, "Click Me",
    grey_style
)

buttonx = hapi.button(150, 10, "Click Me",
    grey_style
)

button2 = hapi.button(150, 250, "No Click Me",
    {
    'background_color':(200, 200, 200),
    'hover_background_color':(220, 220, 220),
    'outline':hapi.outline({
            'color':(200, 200, 200), 
            'amount':5
            }),
    'curve':0.3,
    'action':button_clicked,
    'padding_x':40,
    'padding_y':10,
    'font_size':15
    })

def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False


hapi.handle_events = handle_events

clock = pygame.time.Clock()

while hapi.is_running:
    hapi.background(bg_col)

    if button1.update(): #if the button was clicked
        bg_col = (255, 0, 0) if bg_col == (255, 255, 255) else (255, 255, 255)
    
    # for i in range(5):
    #     x = hapi.button(10+i*80, hapi.mouseY(), "Click Me",
    #         grey_style
    #     )
    # don't use it for ui elements in loop lile the above
    # each element can also be individually
    # updated
    hapi.update_ui() 
    hapi.event_loop()

    hapi.flip_display()

    clock.tick(60)

pygame.quit()
