#!/usr/bin/python3
"""
Module documentation
"""
import xml.etree.ElementTree as ET
"""
Serialization with XML
"""


def serialize_to_xml(dictionary, filename):
    """
    Function documentation
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        key_element = ET.SubElement(root, "child_element")
        key_element.set("key", key)
        key_element.text = value
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Function documentation
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    new_dict = {}

    for x in root:
        key = x.get("key")
        value = x.text
        new_dict[key] = value
    return new_dict
