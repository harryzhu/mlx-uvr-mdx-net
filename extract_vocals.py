import os
from mdxnet import *


if __name__ == "__main__":
    for root, dirs, files in os.walk("wav/_src", True):
        for f in files:
            if f[-4:].lower() != ".wav":
                continue
            fpath = os.path.join(root,f)
            print(f"extracting: {fpath}")
            separate_audio(fpath, output_dir="wav")

    
   


