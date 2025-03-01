from PIL import Image



def color(image, color):
    image = image.convert("RGBA")

    color = hex_to_rgb(color)

    # Get the data of the image (each pixel is a tuple of RGBA)
    data = image.getdata()

    # Define the color you want to change (e.g., changing white to red)
    new_data = []
    for item in data:
        # Change all white (also shades of white)
        if item[3]!=0:
            new_data.append((color[0], color[1],color[2], item[3]))  # Red color with the same alpha
        else:
            new_data.append(item)  # Keep other colors unchanged

    # Update the image with new data
    image.putdata(new_data)
    return image


def hex_to_rgb(hex_color):
    # Remove the "#" if present
    hex_color = hex_color.lstrip("#")
    
    # Convert the hex to RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    return (r, g, b)
