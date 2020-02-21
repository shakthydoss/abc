
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

Install Genie tool
remove any .egg-info in tools directory.
cd tools 
rm -rf *.egg-info 
cd ../
```
pip uninstall tools
pip install -e tools/
```

```
$cd tools
genie --verbose=True --do='text_to_img' --data=data.json --outDir=img
genie --verbose=True --do='edge_detection' --inDir=img --outDir=out
genie --verbose=True --do='trim' --inDir=out
genie --verbose=True --do='set_transparent' --inDir=out
```