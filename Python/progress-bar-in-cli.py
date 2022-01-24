#Custom Progress bar on the CLI itself.
#Just Like How 'pip install ...' has.

from tqdm import tqdm

for i in tqdm(range(1,101000101), desc="Dummy Loop For A Range"):
    ...
