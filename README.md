# 1qbit-matplotlib-style
Matplotlib style file following 1qbit's brand policies


### Use:
- Download the file 1qbit.mplstyle.  Put it somewhere.
- Add
``` python
import matplotlib.pyplot as plt
plt.style.use('~/1qbit.mplstyle')
```
to the top of your plotting scripts.


### Example:

```python 
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('~/1qbit.mplstyle')



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
