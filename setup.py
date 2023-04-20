import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding='utf8')

# This call to setup() does all the work
setup(
    name="yolov7",
    version="0.0.0",
    description="Fork of Python scripts performing object detection using the YOLOv7 model in ONNX",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jingyiyanlol/ONNX-YOLOv7-Predictor.git",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    packages=["yolov7"],
    include_package_data=True,
    install_requires=["opencv-python", "imread-from-url", "onnxruntime-gpu", "cap-from-youtube"],
)


