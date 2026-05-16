from time import sleep
from Loading import ft_tqdm

print("Testing ft_tqdm:")
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print("Done!")
