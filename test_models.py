#!/usr/bin/env python3
"""
Simple test script to validate all glTF files in the repository.
Checks JSON structure, required fields, and basic geometry data.
"""

import json
import os
import sys

def test_gltf_file(file_path):
    """Test a single glTF file for basic validity"""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Check required glTF 2.0 fields
        required_top_level = ['asset', 'scene', 'scenes', 'nodes', 'meshes', 'accessors', 'bufferViews', 'buffers']
        missing_fields = [field for field in required_top_level if field not in data]
        if missing_fields:
            return False, f"Missing required fields: {missing_fields}"
        
        # Check asset version
        if data['asset']['version'] != '2.0':
            return False, f"Invalid glTF version: {data['asset']['version']}"
        
        # Check that we have at least one mesh
        if len(data['meshes']) == 0:
            return False, "No meshes found"
        
        # Check that we have vertices (position accessor)
        has_position = False
        for mesh in data['meshes']:
            for primitive in mesh['primitives']:
                if 'POSITION' in primitive.get('attributes', {}):
                    has_position = True
                    break
            if has_position:
                break
        
        if not has_position:
            return False, "No position attributes found in meshes"
        
        # Check buffer data exists
        for buffer in data['buffers']:
            if 'uri' not in buffer or not buffer['uri'].startswith('data:'):
                return False, "Buffer data not embedded"
        
        return True, "Valid glTF 2.0 file"
        
    except json.JSONDecodeError as e:
        return False, f"JSON parse error: {e}"
    except Exception as e:
        return False, f"Unexpected error: {e}"

def run_tests():
    """Run tests on all glTF files"""
    base_path = "/home/runner/work/3dmodel-samples/3dmodel-samples/models"
    
    if not os.path.exists(base_path):
        print("❌ Models directory not found")
        return False
    
    # Find all glTF files
    gltf_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.gltf'):
                gltf_files.append(os.path.join(root, file))
    
    if not gltf_files:
        print("❌ No glTF files found")
        return False
    
    print(f"Testing {len(gltf_files)} glTF files...\n")
    
    all_passed = True
    for gltf_file in gltf_files:
        rel_path = os.path.relpath(gltf_file, "/home/runner/work/3dmodel-samples/3dmodel-samples")
        success, message = test_gltf_file(gltf_file)
        
        if success:
            print(f"✅ {rel_path}: {message}")
        else:
            print(f"❌ {rel_path}: {message}")
            all_passed = False
    
    print(f"\n{'✅ All tests passed!' if all_passed else '❌ Some tests failed!'}")
    return all_passed

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)