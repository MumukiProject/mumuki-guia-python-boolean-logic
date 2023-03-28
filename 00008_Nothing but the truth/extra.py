light_colors = ["white", "beige", "pink", "yellow", "skyblue"]

def is_light_tone(color):
  return color in light_colors
  
def has_contrast(font_color, background_color):
  return is_light_tone(font_color) != is_light_tone(background_color)  