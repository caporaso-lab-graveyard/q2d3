# q2ui-q2d3

This is a prototype that illustrates how to use the QIIME 2 SDK to build an interface. This is based on the earlier [q2d2](https://github.com/gregcaporaso/q2d2) prototype. As this is a prototype, you shouldn't rely on any of the code in this package.

## Interface demo
These instructions cover how to install and use the q2d3 (experimental) interface of [QIIME 2](https://github.com/biocore/qiime2).

### Installation

To run these steps, you'll first need to install [Miniconda](http://conda.pydata.org/miniconda.html) if you don't already have it installed.

Then...

```bash
conda create -n q2d3 python=3.5 jupyter scikit-bio -c biocore
```

```bash
source activate q2d3
```

```bash
pip install https://github.com/biocore/qiime2/archive/master.zip https://github.com/qiime2-plugins/feature-table/archive/master.zip https://github.com/qiime2-plugins/diversity/archive/master.zip https://github.com/gregcaporaso/q2ui-q2d3/archive/master.zip
```

```bash
git clone https://github.com/gregcaporaso/q2ui-q2d3.git
```

```bash
cd q2ui-q2d3/demo/analysis-dir
```

### Launch the server
```bash
q2d3 serve
```

### Stop the server
To stop the server, enter control-C.

### Import a new artifact (this will be automated soon, see [#31](https://github.com/biocore/qiime2/issues/31))

Change to the raw data directory (you may need to first change out of the ``analysis-dir`` directory) and then launch the IPython terminal:

```bash
cd q2ui-q2d3/demo/raw-data-dir
ipython
```

Then, run the following commands

```python
from feature_table.artifact_types import FeatureTable, Frequency

import biom
biom_path = "./otu-table.tsv"
table = biom.load_table(biom_path)

from qiime.sdk import Artifact
Artifact.save(table, FeatureTable[Frequency], None, "./example-table.qtf")
```

You can then exit the IPython terminal, and inspect the resulting artifact after untaring it with the following command:

```bash
tar -xvf example-table.qtf
```
