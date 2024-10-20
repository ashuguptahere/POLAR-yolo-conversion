import splitfolders

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .1, .1)`.
splitfolders.ratio(
    "converted_data",
    output="dataset",
    seed=1337,
    ratio=(0.8, 0.1, 0.1),
    group_prefix=None,
    move=False,
)  # default values