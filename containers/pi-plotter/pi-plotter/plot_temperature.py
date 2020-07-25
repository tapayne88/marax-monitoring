import matplotlib.pyplot as plt
import io
from PIL import Image, ImageDraw, ImageFont

print("running")

plt.plot([1,2,3,4,5])

with io.BytesIO() as file:
    plt.savefig(file)
    file.seek(0)
    img = Image.open(file)
    img.save("figure1.png")
