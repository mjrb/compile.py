# 
import pystache
renderer=pystache.Renderer()

def file2json(dirPath, fileName, data):
    filePath=dirPath+'/'+fileName
    title=fileName.replace('.mustache', '')
    outputName=fileName.replace('.mustache', '.html')
    fileContents=renderer.render_path(filePath, data)
    return {'title':title, 'body':fileContents, 'outputName':outputName}

def render (dirPath, layoutPath, pageData):
    layoutLocation=layoutPath
    return renderer.render_path(layoutLocation, pageData)

# builds json array from files to build
def getFiles(dirPath, layoutPath, globalData):
    from os import listdir
    viewNames=listdir(dirPath)
    files=list(map((lambda fileName:file2json(dirPath, fileName, globalData)),viewNames))
    return files

def compile(dirPath, layoutPath, outputDir='.', globalData={}):
    files=getFiles(dirPath, layoutPath, globalData)
    
    def renderFunc(pageData):
        pageData.update(globalData)
        return render(dirPath, layoutPath, pageData)
    
    renderedFiles=list(map(renderFunc, files))

    for i in range(0, len(files)):
        name=outputDir+'/'+files[i]['outputName']
        content=renderedFiles[i]
        file=open(name, 'w')
        file.write(content)

# example compilation
#compile('views', 'layouts/layout.mustache')
#compile('views', 'layouts/copyLayout.mustache', globalData={'copyrightYear':'2017'})

