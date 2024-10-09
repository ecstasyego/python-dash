# Visdom

```bash
python -m visdom.server -p 8097
```


## Line
### One exploratory data dimension
data: `1d-array`
```python
import visdom
import numpy as np

vis = visdom.Visdom()
window = vis.line(Y=np.zeros((1,1)), X=np.zeros((1,)))
for i, y in enumerate(np.random.normal(size=(1000, ))): # data shape: 1d-array
    vis.line(Y=y[np.newaxis], X=np.array([i]), win=window, update='append') # Y: 1d-array, X: 1d-array
vis.close()
```

data shape: `2d-array`
```python
import visdom
import numpy as np

vis = visdom.Visdom()
window = vis.line(Y=np.zeros((1,1)), X=np.zeros((1,)))
for i, y in enumerate(np.random.normal(size=(1000, 1))): # data shape: 2d-array
    vis.line(Y=y, X=np.array([i]), win=window, update='append') # Y: 1d-array, X: 1d-array
vis.close()
```

### One more exploratory data dimension
```python
import visdom
import numpy as np

vis = visdom.Visdom()
window = vis.line(Y=np.zeros((1,5)), X=np.zeros((1,5)))
for i, y in enumerate(np.random.normal(size=(1000, 5))):
    vis.line(Y=y[np.newaxis, :], X=np.array([i]*5)[np.newaxis, :], win=window, update='append')
vis.close()
```


