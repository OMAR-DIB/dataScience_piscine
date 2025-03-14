
def ft_tqdm(lst: range) -> None:
    '''
    progress bar like tqdm nut in static way
    '''
    total = len(lst)
    if total == 0:
        return
    last_index = total - 1

    for value in lst:
        percent = int((value / last_index) * 378)
        bar = '█' * (percent//2)
        bar += ' ' * ((100//2) - len(bar))
        text = f"{value+1}/{total}"
        print(f"\r100%|{bar}| {text}", end="",)
        yield
    print()

# from time import sleep
# from tqdm import tqdm
# for elem in ft_tqdm(range(333)):
# 	sleep(0.005)
# print()
# for elem in tqdm(range(333)):
# 	sleep(0.005)
# print()
