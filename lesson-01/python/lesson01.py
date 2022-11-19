"""Usage: `python3 lesson01.py --image="../images/python.jpg"`"""
from pathlib import Path

import click
import cv2


def display_gray_image(image: Path):
    """Open grayscale image and display it."""
    # read an image
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    # display in window
    cv2.imshow("My-Super-Image", img)
    cv2.waitKey(0)  # show untill press any key inside a window
    # delete all the windows created
    cv2.destroyAllWindows()


@click.command()
@click.option(
    "--image",
    type=click.Path(exists=True),
    help="Image filepath"
)
def display_gray_image_command(image: Path):
    display_gray_image(image)


if __name__ == "__main__":
    display_gray_image_command()
