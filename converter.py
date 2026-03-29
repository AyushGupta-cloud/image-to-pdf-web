from PIL import Image

def images_to_pdf(image_paths, output_pdf):
    images = []

    for file in image_paths:
        img = Image.open(file)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        images.append(img)

    if images:
        images[0].save(output_pdf, save_all=True, append_images=images[1:])