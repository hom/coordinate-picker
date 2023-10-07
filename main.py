import sys
import json
from fastkml import kml

def main():
    argv = sys.argv
    if not argv or len(argv) < 2:
        raise("缺少文件路径参数")
    
    file_path = argv[1]

    with open(file_path, 'rb') as f:
        kml_document = f.read()
    
    k = kml.KML()
    k.from_string(kml_document)
    features = list(k.features())
    for document in features:
        print(document.name)
        for document_feature in list(document.features()):
            print(document_feature.name)
            if document_feature.geometry.geom_type == 'Polygon':
                coordinates = []
                for coord in document_feature.geometry.exterior.coords:
                    x, y, _ = coord
                    coordinates.append({"x": x, "y": y})
                print(json.dumps(coordinates))
            elif document_feature.geometry.geom_type == 'Point':
                print(f"经度：{document_feature.geometry.x}")
                print(f"纬度：{document_feature.geometry.y}")

if __name__ == "__main__":
    main()