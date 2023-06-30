import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ImageConversionHandler(FileSystemEventHandler):
    def __init__(self, output_dir):
        super().__init__()
        self.output_dir = output_dir

    def on_created(self, event):
        if not event.is_directory and (event.src_path.endswith('.tif') or event.src_path.endswith('.tiff')):
            input_path = event.src_path
            output_path = os.path.join(self.output_dir, os.path.basename(input_path))
            output_path = os.path.splitext(output_path)[0] + '.jpg'

            try:
                with Image.open(input_path) as im:
                    im.save(output_path, 'JPEG')
                    print(f"Converted: {input_path} to {output_path}")
            except Exception as e:
                print(f"Error converting: {input_path}\n{str(e)}")

def convert_images(directory):
    if directory:
        for name in glob.glob(os.path.join(directory, '*.tif')):
            with Image.open(name) as im:
                name_without_extension = os.path.splitext(name)[0]
                output_name = name_without_extension + '.jpg'
                if os.path.exists(output_name):
                    print(f"Skipped: {output_name} already exists.")
                    continue
                try:
                    im.save(output_name, 'JPEG')
                    print(f"Converted: {name} to {output_name}")
                except Exception as e:
                    print(f"Error converting: {name}\n{str(e)}")

        for name in glob.glob(os.path.join(directory, '*.tiff')):
            with Image.open(name) as im:
                name_without_extension = os.path.splitext(name)[0]
                output_name = name_without_extension + '.jpg'
                if os.path.exists(output_name):
                    print(f"Skipped: {output_name} already exists.")
                    continue
                try:
                    im.save(output_name, 'JPEG')
                    print(f"Converted: {name} to {output_name}")
                except Exception as e:
                    print(f"Error converting: {name}\n{str(e)}")

def select_directory_and_convert():
    directory = filedialog.askdirectory(title="Select Directory")
    convert_images(directory)

def start_file_watcher(directory):
    global output_directory, event_handler, observer

    # Stop the existing observer if running
    stop_file_watcher()

    # Create a new observer and event handler
    output_directory = directory
    event_handler

# Watchdog file watcher
output_directory = None
event_handler = None
observer = None