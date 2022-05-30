
# Image-to-image Constellation Outlining

This project employs image-to-image conversion networks to try and convert constellation images into their corresponding object outline image (Figure A). 

![FigureA](images/figureA.png)

Beside outlining, we also aim to determine at which point the outline is too difficult to find, given increasingly difficult constellations (Figure B).

![FigureB](images/figureB.png)

The conversion networks we use are [pix2pix and cycleGAN](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix).

## Data

The data originates from [Constellation Datasets](https://osf.io/qf5tz/) provided by Tarun Khajuria

## pix2pix

Our first approach is to use pix2pix, which requires training data to be structured in a paired manner, where the input and output is combined together. The combination can be done by calling pix2pix's script:`python datasets/combine_A_and_B.py --fold_A /path/to/data/A --fold_B /path/to/data/B --fold_AB /path/to/data`

However, before this, creating `fold_A` and `fold_B` can be done by running our `pix2pix/scripts/restructure_all_difficulties.py` script.
The script requires you to have placed the unstructured data in the `unstructured_data` folder. By default the folder should be called `Constellations_All_003`, but change it as required. This will create several folds for `fold_A`, enabling separate training for multiple constellation difficulty levels. Both folds will include their own training and hold-out validation and test sets.

## Cycle_gan

The second approach is to use cycle_gan. Comparing to the pix2pix, it requires a different structure for training and testing the model. The dataset must contain 2 directories to host images from domain A `/path/to/data/trainA` and from domain B `path/to/data/trainB`. Similarly for testing purposes to create hold-out test datasets at `/path/to/data/testA` and `/path/to/data/testB` to test the model on unseen images.

This can be achieved by using our script: `python cycle_gan/scripts/restructure_cyclegan.py`. Similarly to the pix2pix, the script requires you to have placed the unstructured data in the `unstructured_data` folder. This will create several folds for each difficulty level allowing the training for different constallation difficulty levels.

