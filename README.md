# Mesh Setup Tool  

A **Maya tool** designed for **character rigging setup**, but can be used for other purposes as well.  

![UI](https://i.imgur.com/SrZMbbZ.png)  


This tool allows you to set up meshes efficiently by applying various transformations and optimizations.  
Simply enter the **name** and **height**, select the desired **options**, and choose the **meshes** you want to modify. Then, click **Apply** to execute the selected operations.  
<br/>


## How to Use

1. Download the MeshSetupTool.py
2. Open Maya Script Editor (Windows - General Editors - Script Editor)
3. Add a new python script tab.
4. Drag the script(MeshSetupTool.py) to the Editor
5. Run the script!

<br/>



##  Features  

### - Apply Height  
- Scales all selected meshes proportionally to match the entered height.  

### - Move Mesh and Pivot to 0
- Uses the **bounding box** of all selected meshes to move them to the world origin 0,0,0.  
- Aligns their **pivot** to 0,0,0.  

### - Freeze All and Delete History  
- **Freezes transformations** (Translate, Rotate, Scale) to 0,0,0. 
- Apply **Delete by type - history** to optimize the meshes.  

### - Group Mesh  
- Groups all selected meshes under a structured hierarchy:

  
Name

 ├── mesh_grp
 
 │ ├── (Selected Meshes)

   
