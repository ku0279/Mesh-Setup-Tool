# Mesh Setup Tool  

A **Maya tool** designed for **character rigging setup**, but can be used for other purposes as well.  

![UI](https://i.imgur.com/SrZMbbZ.png)  


This tool allows you to set up meshes efficiently by applying various transformations and optimizations.  
Simply enter the **name** and **height**, select the desired **options**, and choose the **meshes** you want to modify. Then, click **Apply** to execute the selected operations.  


##  Features  

### - Apply Height  
Scales all selected meshes proportionally to match the entered height.  

### - Move Mesh and Pivot to (0,0,0)  
- Uses the **bounding box** of all selected meshes to move them to the world origin 0,0,0.  
- Aligns their **pivot** to 0,0,0.  

### - Freeze All and Delete History  
- **Freezes transformations** (Translate, Rotate, Scale) to 0,0,0. 
- **Deletes construction history** to optimize the meshes.  

### - Group Mesh  
- Groups all selected meshes under a structured hierarchy:

  
Name

 ├── mesh_grp
 
 │ ├── (Selected Meshes)

   
