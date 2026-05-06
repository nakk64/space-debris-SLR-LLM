import os
import pandas as pd
import numpy as np
import hashlib
from tqdm.notebook import tqdm

class CRDProcessor:
    def __init__(self):
        self.file_hashes = set()
    
    def parse_file(self, file_path):
        # [Previous parse_crd implementation]
    
    def process_directory(self, root_dir):
        all_data = pd.DataFrame()
        for root, _, files in os.walk(root_dir):
            for file in tqdm(files, desc="Processing files"):
                if file.endswith(".fr2"):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'rb') as f:
                        file_hash = hashlib.md5(f.read()).hexdigest()
                    if file_hash not in self.file_hashes:
                        self.file_hashes.add(file_hash)
                        df = self.parse_file(file_path)
                        if not df.empty:
                            all_data = pd.concat([all_data, df])
        return all_data