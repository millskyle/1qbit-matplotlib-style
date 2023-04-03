import matplotlib.pyplot as plt
import gif
import numpy as np

class ImageGrid():

    """Simple method to hold an NxM grid of sx x sy images.

    Example:

            N=5
            M=4

            digits_img = ImgArray(N, M, 8, 8)

            counter = 0

            for i in range(N):
                for j in range(M):
                    digits_img.insert(i, j, np.ones((8,8))*counter)
                    counter += 1

            plt.imshow(digits_img.img)

    """

    def __init__(self, N, M, sx, sy, negative_space_value=np.nan):
        self.Nx = N
        self.Ny = M
        self.sx = sx
        self.sy = sy

        self._img = np.zeros((N*sx + N + 1, M*sy + M + 1)) + negative_space_value

    def insert(self, i, j, data):
        assert data.shape[0] == self.sx, f"Unexpected width. Got {data.shape[0]}. Expected {self.sx}."
        assert data.shape[1] == self.sy, f"Unexpected height. Got {data.shape[1]}. Expected {self.sy}."
        self._img[1+i*(self.sx+1):1+i*(self.sx+1)+self.sx, 1+j*(self.sy+1):1+j*(self.sy+1)+self.sy] = data

    def get(self):
        return self._img

    @property
    def img(self):
        return self.get()



def plot_to_gif(func, ts, gif_params={"duration":50, "unit":'ms', "between":'frames'}, gif_filename=None, return_image=True):
    
    if gif_filename is None:
        import inspect
        this_func_name = inspect.stack()[0][3]
        passed_func_name = inspect.stack()[1].code_context[0].replace(f"{this_func_name}(","").split(",")[0].replace("func=","")
        gif_filename=f"{passed_func_name}.gif"
    print(f"Constructing {gif_filename}")
    
    @gif.frame
    def __plot(t_):
        func(t_)
   
    try:
        from tqdm.notebook import tqdm
        frames = [__plot(t) for t in tqdm(ts)]
    except:
        frames = [__plot(t) for t in ts]

    gif.save(frames, gif_filename, **gif_params)
    if return_image:
        from IPython.display import Image
        return Image(gif_filename)
    else:
        return gif_filename


