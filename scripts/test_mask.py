import numpy as np
from PIL import Image



def decompress_mask(compressed: str, shape: tuple):
    counts = []
    values = []
    i = 0
    
    while i < len(compressed):
        count_str = ''
        while i < len(compressed) and compressed[i].isdigit():
            count_str += compressed[i]
            i += 1
        count = int(count_str)
        counts.append(count)
        
        if compressed[i] == 'T':
            values.append(True)
        else:
            values.append(False)
        i += 1
    
    flat_mask = np.concatenate([np.full(count, value) for count, value in zip(counts, values)])
    
    mask = flat_mask.reshape(shape)
    
    return mask

original_shape = (640, 640)  

def save_mask_as_image(mask: np.ndarray, filename: str):
    mask_image = Image.fromarray((mask * 255).astype(np.uint8))  # Convert boolean mask to uint8
    mask_image.save(filename)

import sys , os
sys.path.append('/home/ubuntu/workdir/gs/NOTEBOOK/')
from run import run_func


def print_mask(mask_seg, file_name, method_type):
    
    remove_directory_path = '/home/ubuntu/workdir/gs/NOTEBOOK/mask/'
    files = os.listdir(remove_directory_path)

    for file_name_remove in files:
        
        file_path = os.path.join(remove_directory_path, file_name_remove)
        
        if os.path.isfile(file_path):  
            os.remove(file_path)
            print(f"Removed file: {file_path}")


    for idx, i in enumerate(mask_seg):
        compressed = i["segmentation"]
        decompressed_mask = decompress_mask(compressed, original_shape)

        if method_type == "click":
            save_mask_as_image(decompressed_mask, f"/home/ubuntu/workdir/gs/NOTEBOOK/mask/{file_name}_{idx}.png")
        else:
            save_mask_as_image(decompressed_mask, f"/home/ubuntu/workdir/gs/NOTEBOOK/mask/{file_name}_{1}.png")

    print(file_name)
    run_func(file_name)