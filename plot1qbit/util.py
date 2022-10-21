import matplotlib.pyplot as plt
import gif



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


