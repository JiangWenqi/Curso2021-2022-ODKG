# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lqwpdoBkarKM_WEcZLWqoGyo8l_3MS9b

**Task 07: Querying RDF(s)**
"""

# !pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")


print("TASK 7.1: List all subclasses of Person with SPARQL")
# TO DO

from rdflib.plugins.sparql import prepareQuery

NS = Namespace("http://somewhere#")
 
q1 = prepareQuery('''
  SELECT ?Subclass WHERE{
    ?Subclass rdfs:subClassOf+ ns:Person
  }
  ''',
  initNs = { "ns": NS}
)
# Visualize the results

for r in g.query(q1):
    print(r.Subclass)

print("TASK 7.1: List all subclasses of Person with RDFLib")
#with RDFLib
list = []
def allSubClasses(r):
  for s,p,o in g.triples((None, RDFS.subClassOf, r)):
    list.append(s)
    allSubClasses(s)
    return list

subclasses = allSubClasses(NS.Person)

for s in subclasses:
  print(s)

print("TASK 7.2: List all individuals of Person with SPARQL (remember the subClasses)")

# TO DO
q2 = prepareQuery('''
  SELECT ?individuals WHERE{
    ?individuals rdf:type/rdfs:subClassOf* ns:Person
  }
  ''',
  initNs = {"ns": NS}
)
# Visualize the results
for r in g.query(q2):
    print(r.individuals)
    
 
print("TASK 7.2: List all individuals of Person with RDFLib (remember the subClasses)")
#with RDFLib
subclasses.append(NS.Person)
individuals = []
for i in subclasses:
  for s,p,o in g.triples((None, RDF.type, i)):
    individuals.append(s)

for s in individuals:    
  print(s)



print("TASK 7.3: List all individuals of Person and all their properties including their class with SPARQL")

# TO DO
q3 = prepareQuery('''
  SELECT ?individuals ?p ?o WHERE{
    ?individuals rdf:type/rdfs:subClassOf* ns:Person.
    ?individuals ?p ?o
  }
  ''',
  initNs = {"ns": NS}
)
# Visualize the results
for r in g.query(q3):
    print(r.individuals, r.p, r.o)

print("TASK 7.3: List all individuals of Person and all their properties including their class with RDFLib")

#with RDFLib
for i in individuals:
  for s,p,o in g.triples((i, None, None)):
    print(s,p,o)
    