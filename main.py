import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable GPU
from multiprocessing import shared_memory
import re
import sys

print(sys.path)
import numpy as np
import signal
from typing import List
import posix_ipc
from posix_ipc import Semaphore, O_CREAT


from threading import Thread
from queue import Queue, Empty

import time
import tensorflow as tf
tf.random.set_seed(1234)

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
  tf.config.experimental.set_memory_growth(gpu, True)

from tensorflow.keras.datasets import mnist

# cmd.Env = append(os.Environ(), "PYTHONUNBUFFERED=1")

from tensorflow.keras.utils import to_categorical
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from tensorflow.keras.initializers import GlorotUniform
initializer = GlorotUniform(seed=1234)

import math

import json
import platform
import warnings
import logging


# ——————————————————————————————————————————————————————————————
#  Semaphore & Shared‑Memory Setup
# ——————————————————————————————————————————————————————————————
def load_config(file="config.json"):
    """Load configuration from a JSON file."""
    with open(file, "r") as f:
        content = f.read()
        # Replace JavaScript-style booleans and null with Python-compatible values
    content = (
        content.replace("true", "True")
        .replace("false", "False")
        .replace("null", "None")
    )
    try:
        config = eval(content)
    except SyntaxError as e:
        raise ValueError(f"Failed to parse the JSON file: {file}. Error: {e}")
    logger.info(f"Loaded config: {config}")
    return config


