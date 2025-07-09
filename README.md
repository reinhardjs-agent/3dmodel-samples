# 3D Model Samples

A collection of low-poly 3D models in glTF format, perfect for game development, prototyping, and learning.

## Contents

### Character Models
- **human_lowpoly.gltf** - Basic low-poly human character with simple geometric proportions
  - Location: `models/character/human_lowpoly.gltf`
  - Features: Head, torso, arms, and legs as separate geometric components
  - Vertex count: 48 vertices (very low poly for performance)

### Clothing & Wearables

#### Tops
- **basic_shirt.gltf** - Simple shirt/top that fits over the human character
  - Location: `models/clothing/tops/basic_shirt.gltf`
  - Features: Basic torso coverage with simple geometry

#### Bottoms  
- **basic_pants.gltf** - Basic pants with separated leg geometry
  - Location: `models/clothing/bottoms/basic_pants.gltf`
  - Features: Waist section with two separate leg pieces

#### Shoes
- **basic_shoes.gltf** - Simple footwear for left and right feet
  - Location: `models/clothing/shoes/basic_shoes.gltf`
  - Features: Two separate shoe objects with extended toe area

## Usage

These models are designed to be:
- **Low-poly**: Optimized for performance with minimal triangles
- **Modular**: Character and clothing are separate models that can be combined
- **glTF 2.0 compliant**: Compatible with modern 3D engines and viewers
- **Educational**: Simple geometry perfect for learning 3D modeling concepts

## File Format

All models are provided in glTF 2.0 format (.gltf) with embedded binary data for easy distribution and compatibility.

## Directory Structure

```
models/
├── character/
│   └── human_lowpoly.gltf
└── clothing/
    ├── tops/
    │   └── basic_shirt.gltf
    ├── bottoms/
    │   └── basic_pants.gltf
    └── shoes/
        └── basic_shoes.gltf
```

## Viewing the Models

You can view these models using:
- Online glTF viewers (e.g., gltf-viewer.donmccurdy.com)
- 3D modeling software (Blender, Maya, 3ds Max)
- Game engines (Unity, Unreal Engine, Godot)
- Web browsers with WebGL support