# Visdom

```bash
python -m visdom.server -p 8097
```


## Line
### 1D-Line
```python
import visdom
import numpy as np

vis = visdom.Visdom()
window = vis.line(Y=np.zeros((1,1)), X=np.zeros((1,)))
for i, y in enumerate(np.random.normal(size=(1000, 1))):
    vis.line(Y=y, X=np.array([i]), win=window, update='append')
vis.close()
```


### 2D-Line
```python
```


