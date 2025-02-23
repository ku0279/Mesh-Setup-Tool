from maya import cmds

class UI_Window(object):

    #constructor
    def __init__(self):
        
        self.window = "UI_Window"
        self.title = "Mesh Setup for Rigging"
        self.size = (400,200)
        
        #close old window is open
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)
            
        #create new window
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        
        cmds.columnLayout()
        
        cmds.text(self.title)
        cmds.separator(height=20)
        
        
        self.chaName = cmds.textFieldGrp(label = 'Name', text='Character')
        self.chaHeight = cmds.textFieldGrp(label = 'Height (cm)', text='160')
       
        cmds.separator(height=20)
        cmds.text('Select all of mesh and press Apply Button')
        
        
        global check1, check2, check3, check4
        
        check1 = cmds.checkBox(label='Apply Height',v=True)
        check2 = cmds.checkBox(label='Move mesh and pivot to 0',v=True)
        check3 = cmds.checkBox(label='Freeze all and Delete by history',v=True)
        check4 = cmds.checkBox(label='Group mesh',v=True)
        
        
        cmds.button(label = 'Apply', command = self.meshSetup)
        
        
        
        #display new window
        cmds.showWindow()
    
    
    
    
    
    
    #
    #Function
    #
    def meshSetup(self, *args):
        self.cha = cmds.ls(sl=1)
    
        if len(cha) > 0:
            
            if cmds.checkBox(check1, query=True, value=True):
                self.changeHeight()
            
            if cmds.checkBox(check2, query=True, value=True):
                self.moveToZero()
                
            if cmds.checkBox(check3, query=True, value=True):
                self.freezeDeleteHis()
                
            if cmds.checkBox(check4, query=True, value=True):
                self.groupMeshes()
           
            
            
        
        elif len(cha) == 0:
            cmds.warning("Select character mesh")
            return    



#Change Height of Character
    def changeHeight(self, *args):
        chaBoundBox = cmds.exactWorldBoundingBox(self.cha)
        min_y, max_y = chaBoundBox[1], chaBoundBox[4]
        current_height = max_y - min_y
        
        height = cmds.textFieldGrp(self.chaHeight, query=True, text=True)
        scale_factor = float(height) / current_height
        
        cmds.scale(scale_factor, scale_factor, scale_factor, self.cha, relative=True, pivot=(0, min_y, 0))



#Move and Setup Pivot to 0,0,0
    def moveToZero(self, *args):
  
        chaBoundBox = cmds.exactWorldBoundingBox(self.cha)
        min_x, min_y, min_z, max_x, max_y, max_z = chaBoundBox
                     
        center_x = (min_x + max_x)/2
        center_z = (min_z + max_z)/2
        
        #move to 0,0,0             
        cmds.move(-center_x, -min_y, -center_z, cha, relative =True)
        
        #pivot to 0,0,0
        for obj in cha:
                cmds.xform(obj, pivots=(0, 0, 0), worldSpace=True)
    

    
#Freeze all and Delete by History    
    def freezeDeleteHis(self, *args):
        for i in self.cha:
            # delete by History
            cmds.delete(i, constructionHistory = True)
            # Freeze All
            cmds.makeIdentity(i, apply=True)


#Group meshes
    def groupMeshes(self,*args):
        name = cmds.textFieldGrp(self.chaName, query=True, text=True)
        
        cmds.group(self.cha, n=name)
        meshGrp = cmds.group(cha, n='mesh_grp')



                
myWindow = UI_Window()

