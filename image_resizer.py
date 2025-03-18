from PIL import Image

def resize_image(image_path, output_path, size):
    image = Image.open(image_path)
    image = image.resize(size)
    image.save(output_path)
    print(f"✅ Image saved as {output_path}")

# Example usage
resize_image("input.jpg", "output.jpg", (300, 300))
