import xml.etree.ElementTree as ET

def convert_coverage(input_file="coverage.xml", output_file="sonar-coverage.xml"):
    # Parse the original coverage file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Force version="1.0" (SonarQube requirement)
    root.attrib["version"] = "1.0"

    # Remove unsupported attributes (if present)
    for attr in ["timestamp", "complexity", "branches-covered", "branches-valid"]:
        if attr in root.attrib:
            del root.attrib[attr]

    # Save the modified XML
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"Converted {input_file} to SonarQube-compatible {output_file}")

if __name__ == "__main__":
    convert_coverage()