# I made this project to calculate the cost of my house.

First I began with an spreadsheet but this is good how a starting point but when you advance is very limited an confuse
I ever thinked in how easy was to do the backend in python but I get bored when though in the UI, I hate build UIs. Then I realized that what I want is only for me no for clients and pandas printing capabilities are suffice to me.

Then I did it. After I was looking for an application for 3D modeling of the house, and found blender. Blender is python also, then I build a little interface with my programa and voila with a pair of clicks I got the cost of my house.

After that success I thougth I can get the bill of materials also, then I build it.

Now, I want to give you this work as a little contribution to this world of Python and Blender and other open source projects that have given me so much. 

I would appreciate if you can give some ideas or made changes or contributions.

# How it works

Give a look at the file casa.py

An object of class Obra is what you need to fill. You fill with different elements like wall, column, beam, ceiling, floor, etc.

Each one of this elements need a name and quantity. And for columns and beams the section area and the number of varillas.

I name this elements apus (spanish analisis de precios unitarios or unitary price analysis). They are defined in apus.py. You can define yours inheriting Apu class.

Each apu has several materials. They are defined in mp.py. You can define yours, only need to add several properties to your clases (look mp.py)

# In blender

Give a look at the file blender.py

I build my blender projects with cubes. Wall, beam, column, floor, ceiling, all are cubes. In this script I recognize the type of element by its material

In this script I fill the obra Obra class object with each of the cubes of my blender draw, classifing then according its material. You can modify it.

# what's next

I want to translate to english all the code, the variables, functions and class names

# contact

senenbotello@gmail.com
