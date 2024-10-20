# POLAR-yolo-conversion-and-train
Conversion of POLAR dataset (Posture-level Action Recognition Dataset) into YOLO format and training it on YOLO11 architecture

## Install [uv](https://docs.astral.sh/uv/getting-started/installation/#installing-uv):
### 1. For Linux:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
### 2. For Windows:
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Start working on the project
```
uv sync
```

## Download `hvnsh7rwz7-1.zip` dataset:
```
wget https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/hvnsh7rwz7-1.zip
```

## Extract `hvnsh7rwz7-1.zip` dataset:
```
unzip hvnsh7rwz7-1.zip -d hvnsh7rwz7-1
```

## Extract `annotations.zip` file:
```
unzip hvnsh7rwz7-1/Annotations/annotations.zip -d hvnsh7rwz7-1/Annotations/annotations
```

## Extract `JPEGImages.zip` to `converted_data` folder:
```
sudo apt install 7zip
7z x hvnsh7rwz7-1/JPEGImages/JPEGImages.zip -o./converted_data/
```

## Renaming `JPEGImages/` to `images/`
```
mv converted_data/JPEGImages/ converted_data/images/
```

## Convert data:
```
uv run scripts/convert.py
```

## Split data:
```
uv run scripts/split.py
```

## To run training script:
```
uv run scripts/train.py
```