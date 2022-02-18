#PyCmdblock  
*how to mek minecraft commands?*
## Usage
Using:
```python
from pycmdblock import commands
from pycmdblock.target_selector import Target

commands.tellraw(
        Target()
            .all_player()
            .distance(10)
            .gamemode("c")
            .team(False)
            .volume(commands.Volume(x=0, y=0, z=0, dx=10, dy=10, dz=10))
            .tag(False),
        commands.conv("&a&lHello World!")
    )
```
should give the following output:
```
tellraw @a[distance=10,gamemode=creative,team=,x=0,y=0,z=0,dx=10,dy=10,dz=10,tag=] {"text": "Hello World!", "color": "green", "bold": true}
```
## FAQ
1. Why the "fluent design"? Isn't it "un-pythonic"?   
yes. but this way it is easier to look at. You can still use normal syntax though.
2. It's lacking *feature x*!  
You can implement it yourself. Make a pull request.
