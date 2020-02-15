
install webkit2png
Required for converting html to png. 

install imagemagick
Required for triming and setting transparent image. 

Create Python Virtual env
```
virtualenv -p python3 venv
source venv/bin/activate
```

```
pip install - r requirements.txt
```

```
$cd tools
python tools.py --verbose=True --do='text_to_img' --data=data.json --outDir=img
python tools.py --verbose=True --do='edge_detection' --inDir=img --outDir=out
python tools.py --verbose=True --do='trim' --inDir=out
python tools.py --verbose=True --do='set_transparent' --inDir=out
```