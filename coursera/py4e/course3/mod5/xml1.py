# xml1.py

"""
XML SCHEMA

• Description of the legal format of an XML document
• Expressed in terms of constraints on the structure and content of documents
• Often used to specify a 'contract' between systems - "My system will only
  accept xml that conforms to this particular Schema."
• If a particular piece of xml meets the specification of the Schema - it is
  said to "validate"

Example xml document:

<person>
    <lastname>Whiteside</lastname>
    <age>49</age>
    <dateborn>1976-12-25</dateborn>
</person>

Example xml schema contract:

<xs:complexType name="person">
    <xs:sequence>
        <xs:element name="lastname" type="xs:string"/>
        <xs:element name="age" type="xs:integer"/>
        <xs:element name="dateborn" type="xs:date"/>
    </xs:sequence>
</xs:complexType>

Many xml schema languages

• Document Type Definition (DTD)
    • http://en.wikipedia.org/wiki/Document_Type_Definition
• Standard Generalized Markup Language (ISO 8879:1986 SGML)
    • http://en.wikipedia.org/wiki/sgml
• XML Schema from W3C - (XSD)
    • http;//en.wikipedia.org/wiki/xml_schema_(w3c)


XSD XML Schema (W3C spec)
• We will focus on the  World Wide Web Consortium (W3C) version
• It is often called "W3C Schema" since "Schema" is considered generic
• More commonly it is called XSD since the file names end in .xsd


XSD STRUCTURE:

xs:complexType => xs:sequence => xs:element (can all be nested in each other)

XSD CONSTRAINTS

<xs:element name="person">
    <xs:complexType>
        <xs:sequence>
            <xs:elemment anme="full_name" type="xs:string"
                minOccurs="1" maxOccurs="1"/>
            <xs:element name="child_name" type="xs:string"
                minOccurs="0" maxOccurs="10"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>

<person>
    <full_name>Tove Refsnes</full_name>
    <child_name>Hege</child_name>
    <child_name>Stale</child_name>
    <child_name>Jim</child_name>
    <child_name>Borge</child_name>
</person>

XSD DATA TYPES:

<xs:element name="customer" type="xs:string"/>
<xs:element name="start" type="xs:date"/>
<xs:element name="startdate" type="xs:dateTime"/>
<xs:element name="prize" type="xs:decimal"/>
<xs:element name="weeks" type="xs:integer"/>

<customer>John Smith</customer>
<start>2026-03-28</start>
<startdate>2026-03-30T09:30:10Z</startdate>
<prize>999.50</prize>
<weeks>30</weeks>

"""
import xml.etree.ElementTree as et

data = '''<person>
    <name>Kevin</name>
    <phone type="intl">+1 734 303 4456</phone>
    <email hide="yes"/>
</person>'''

tree = et.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
