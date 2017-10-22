# mustache-AOT-compiler
compiles mustache documents AOT to static .html files  
somewhat like jekyll, but decomplicated and stupidly easy to use.

## the basics
the module contains one major function that does all the work  
    `compile(dirPath, layoutName, outputDir, globalData)`  
**dirPath** is the directory where the layout and views are located  
all source files must have .mustache extension  
**views** are the indivual files that get rendered inside of the **layout**  
**layoutPath** is the path to the layout. if its in the views  
**outputDir** defaults to the current directory  
**globalData** defaults to {}  
 it can be used for data that can be acessed and rendered in the layout/views but needs to be broken out for easy editing  
it could include:  
1. linktext/href pairs for a navbar
2. copywright year
3. contact information
4. other things that could be broken out for the construction of themes
## basic layout.mustache
layouts/layout.mustache:  
```html
<html>  
  <head>
    <title>{{title}}</title>
  </head>
  <body>
    {{{body}}}
  </body>
</html>
```
the title property is reserved and will allways be the name of the file without the .mustache extension  
similarly with body it will be the contents of the file but the difference is the body is surounded by 3 mustaches({)
instead of 2. the difference is that 2 will escape html, but 3 won't.
## a basic view and the comilation result
views/view.mustache  
```html
<h1>this is the view page!</h1>
<p>its great to have some content</p>
```
asuming we also have the previus example of views/layout.mustache we could call `compile('views', 'layouts/layout.mustache')`
and we would get the file view.html in our current directory  
```html
<html>  
  <head>
    <title>view</title>
  </head>
  <body>
    <h1>this is the view page!</h1>
    <p>its great to have some content</p>
  </body>
</html>
```
## using globaldata
say we have a copyright year but we dont want to go digging through our html file to update it  
we could instead setup our layout to uses a parameter from global data  
layouts/copyLayout.mustache
```html
<html>  
  <head>
    <title>{{title}}</title>
  </head>
  <body>
    {{{body}}}
    <div id="footer">&copy; {{copyrightYear}} Author McOwnerson</div>
  </body>
</html>
```
then calling 
```python
data={'copyrightYear':'2017'}
compile('views', 'layouts/copyLayout.mustache', globalData=data)
```
would give you a file in the current directory called view.html
```html
<html>  
  <head>
    <title>view</title>
  </head>
  <body>
    <h1>this is the view page!</h1>
    <p>its great to have some content</p>
    <div id="footer">&copy; 2017 Author McOwnerson</div>
  </body>
</html>
```
