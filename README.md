# 1qbit-matplotlib-style
Matplotlib style file following [1QBit](http://www.1qbit.com)'s brand policies.

_Note that this is nowhere near complete.  There are plot types that are not accounted for.  Please feel free to make a pull request with updates._


## Use:
Install this package, e.g. 
```bash
pip install plot1qbit
```

Import the `plot1qbit` package prior to plotting, but after importing matplotlib.

### Font

1QBit's brand font is Brandon Text.  This is a commercial font and thus cannot be distributed.  If you have Brandon Text installed on your computer through some other means, this package will pick it up and use it.  You may need to delete your matplotlib cache first though:
```bash 
rm -r $HOME/.cache/matplotlib
```
If you're an employee of 1QBit, a zip file containing these fonts can be found in the company Google Drive.



## Example:

```python 
import numpy as np
import matplotlib.pyplot as plt
import plot1qbit


fig, axs = plt.subplots(1,2,figsize=(10,5))
xs = np.linspace(0,5*np.pi, num=100)
axs[0].imshow(np.random.rand(64,64))
axs[0].set_title("Image plotting")
for c in range(6):
    axs[1].plot(xs, np.sin(xs - 0.3*c), label=f"c={c}")
axs[1].legend()
axs[1].set_title("Example plot")
axs[1].set_ylabel("vertical axis")
axs[1].set_xlabel("horizontal axis")

plt.tight_layout()
fig.show()
```

![example](https://raw.githubusercontent.com/millskyle/1qbit-matplotlib-style/master/example.png)
