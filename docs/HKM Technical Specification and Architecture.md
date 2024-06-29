# Human Knowledge Markdown (HKM): Technical Specification and Architecture

## 1. Introduction

Human Knowledge Markdown (HKM) is a flexible, extensible framework for representing and organizing knowledge. It bridges multiple paradigms including data serialization formats, knowledge graphs, topic maps, and formal ontologies. 

HKM works by combining YAML frontmatter with Markdown content in a single file, creating a flexible knowledge container. This allows users to store structured data in the YAML section and freeform notes in the Markdown section:

```yaml
---
name: Example HKM Document
is_a: note
author: John Doe
topics:
  - HKM
  - Knowledge Representation
---

# HKM Example

This is a freeform Markdown section where users can add detailed notes, explanations, or any unstructured content.
```

Unlike simple data serialization formats, HKM goes beyond mere structured data representation. It provides a semantic layer that captures the meaning and relationships of the knowledge being represented. This is achieved through a carefully designed set of primitives and relationships that model how humans naturally think about and organize knowledge. As a result, HKM documents are not just data containers, but rich, interconnected knowledge artifacts that can be easily understood by both humans and machines.

HKM is also designed with AI integration in mind. Its structured yet flexible format makes it ideal for AI language models to process, understand, and generate. AI can be used to create new HKM documents, extract structured HKM data from unstructured text, or even extend the HKM language itself by defining new types of entities and relationships. This AI-friendly design makes HKM a powerful tool for knowledge management in the age of artificial intelligence.

This document provides a comprehensive technical specification and architectural overview of HKM, aimed at developers and knowledge workers who may want to implement, use, or extend the language.

## 2. Core Concepts

Human Knowledge Markdown is built on three fundamental levels of knowledge representation, all deriving from a common `entity`:

1. **Attributes**: The most granular level, representing individual characteristics or properties.
2. **Things**: Distinct objects, concepts, or notions that can be subjects of knowledge. These are intended as flexible containers for any entity: people, places, events, books, etc.
3. **Topics**: Broader areas of knowledge that can encompass multiple things and serve as organizational units. Topics are used to organize more conceptual information in the form of notes.

These levels form a flexible hierarchy that allows for bottom-up knowledge modeling while maintaining the ability to represent complex relationships and structures.

## 3. Foundational Primitives

Human Knowledge Markdown defines a set of core primitives that serve as the building blocks for all knowledge representation within the system. These primitives are self-defining, creating a circular yet flexible foundation that allows for extensibility and adaptation.

### 3.1 Entity

The `entity` primitive is the root of all representational units in HKM. It denotes the existence of a distinct concept, construct, or individuated thing, whether abstract or concrete.

Key characteristics:
- Serves as the base class for all other primitives
- Defines core attributes like `name`, `description`, `aliases`, and `predicates`
- Allows for flexible extension through subclassing

### 3.2 Attribute

An `attribute` represents a characteristic, quality, or piece of information associated with an entity.

Key characteristics:
- Subclass of `entity`
- Can be used to define properties of other entities
- Includes specialized types like `name`, `description`, and `identifier`

### 3.3 Relationship

A `relationship` is a specialized type of attribute that represents an associative connection between entities.

Key characteristics:
- Subclass of `attribute`
- Defines connections between entities
- Includes core types like `is_a`, `subclass_of`, and `related_to`

### 3.4 Thing

A `thing` represents a distinct object, concept, or notion that can be considered a subject of knowledge.

Key characteristics:
- Subclass of `entity`, `relationship`, and `note`
- Serves as a flexible container for representing instantiated knowledge
- Can be used to model both abstract concepts and concrete objects

### 3.5 Topic

A `topic` is a fundamental unit for organizing knowledge, representing abstract conceptual components, concrete entities that are subjects of discourse, or areas of knowledge and understanding.

Key characteristics:
- Subclass of `entity` and `note`
- Serves as a high-level organizational unit
- Can encompass multiple `thing` instances and other `topic`s

### 3.6 Aliases

Aliases in HKM serve a dual purpose:

1. They provide alternative linguistic representations for entities, enhancing findability and natural language processing.
2. They can be flexibly used as attribute names when referencing entities, allowing for more intuitive and context-specific knowledge representation.

For example, an entity of type "person" might have aliases like "individual" or "human". These aliases can then be used interchangeably when referencing the entity in other HKM documents, providing flexibility in how knowledge is expressed and linked.

## 4. Knowledge Representation Model

HKM uses a flexible entity-attribute-relationship model for knowledge representation. This model allows for:

- Bottom-up knowledge modeling
- Flexible schema of entity types and relationships
- Gradual formalization of knowledge structures

### 4.1 Entity Schema and Packages

In HKM, individual entities are defined in YAML files. For example, the `entity` primitive is defined in `src/core/entity.yaml`:

```yaml
name: entity
description: The primordial representational unit denoting the existence of a distinct concept, construct or individuated thing, whether abstract or concrete.
is_a: entity
attributes:
  - name
  - description
  - aliases
  - predicates
```

These individual entity definitions are then "compiled" into a simple YAML list of entities to create packages or libraries that are easier to use and distribute. We refer to these as HKM schema files

### 4.2 HKM Schema Structure

Entities in HKM are defined using a consistent structure:

```yaml
- name: entity_name
  description: Textual description of the entity
  is_a: parent_class
  subclass_of: higher_level_class
  attributes:
    - attribute1
    - attribute2
  predicates:
    - predicate1
    - predicate2
  aliases:
    - alias1
    - alias2
```

This structure allows for clear definition of entity characteristics while maintaining flexibility in knowledge representation.

### 4.3 Inheritance and Type System

HKM uses the `subclass_of` relationship to define type hierarchies. This allows for:

- Creation of specialized entity types
- Inheritance of attributes and relationships from parent classes
- Flexible modeling of complex concepts through multiple inheritance

### 4.4 Relationship Representation

Relationships in HKM are represented as attributes with special semantics. They can be defined using natural language predicates, allowing for intuitive knowledge modeling.

## 5. Serialization and Syntax

HKM uses YAML as its primary serialization format for entity definitions and structured data representation. Definitions are stored in YAML files (.yaml) to differentiate them from their usage inside markdown files.

### 5.1 YAML Structure

#### Individual Entity Files

HKM entities are typically defined in individual YAML files. Here are two example entity definitions:

1. `person.yaml`:
```yaml
name: person
description: A human being, representing an individual with a distinct identity.
is_a: subclass_of
subclass_of: thing
attributes:
  - birth_date
  - gender
predicates:
  - is_a_person
aliases:
  - human
```

2. `organization.yaml`:
```yaml
name: organization
description: A structured group of people with a particular purpose, such as a business, government agency, non-profit, or other collective entity.
is_a: subclass_of
subclass_of: thing
attributes:
  - industry
predicates:
  - is_organization
aliases:
  - business
```

#### Packaged Entity List

These individual entity definitions are then combined into a single YAML file to create a package or library. This packaged list might look like this:

```yaml
- name: person
  description: A human being, representing an individual with a distinct identity.
  is_a: subclass_of
  subclass_of: thing
  attributes:
    - birth_date
    - gender
  predicates:
    - is_a_person
  aliases:
    - human

- name: organization
  description: A structured group of people with a particular purpose, such as a business, government agency, non-profit, or other collective entity.
  is_a: subclass_of
  subclass_of: thing
  attributes:
    - industry
  predicates:
    - is_organization
  aliases:
    - business
```

This packaged list combines multiple entity definitions into a single YAML file, making it easier to distribute and use a set of related entities as a cohesive library or package.

## 6. Usage in Markdown Knowledge Artifacts

In Human Knowledge Markdown, a knowledge artifact is any document or file that captures and represents a piece of knowledge. This can range from notes and articles to structured representations of entities or concepts. Knowledge artifacts in HKM typically combine YAML frontmatter for structured data with Markdown content for freeform information.

### 6.1 Notes

HKM knowledge artifacts combine YAML frontmatter with Markdown content, allowing for rich, freeform knowledge representation. Here's an example of a note-type knowledge artifact:

```yaml
---
name: HKM Usage Example
is_a: note
author: Jane Smith
topics:
  - Knowledge Management
  - HKM
created: 2023-06-15
---

# HKM in Practice

This Markdown section allows for detailed explanations and freeform content.

## Key Benefits

- Flexible knowledge representation
- Combines structured and unstructured data
- Easy to read and write for humans and machines
```

### 6.2 Representing Things

HKM can also be used to represent "things" in a more structured, database-like manner. Here's an example of a knowledge artifact representing a person:

```yaml
---
name: John Doe
is_a: person
birth_date: 1985-03-15
gender: male
occupation: Software Engineer
email: john.doe@example.com
skills:
  - Python
  - JavaScript
  - Machine Learning
affiliations:
  - name: Tech Innovators Inc.
    role: Senior Developer
    start_date: 2018-01-01
---

# John Doe

John is a skilled software engineer with a passion for machine learning and web technologies. He has been a key contributor to several open-source projects and is known for his expertise in Python and JavaScript.

## Notable Projects

1. Developed a machine learning algorithm for predictive maintenance in industrial equipment.
2. Led the frontend team in creating a responsive web application for real-time data visualization.

## Publications

- Doe, J., & Smith, A. (2022). "Advances in Applied Machine Learning for IoT Devices." Journal of Internet of Things, 15(3), 45-62.
```

This example shows how HKM can be used to represent structured data about a person (in the YAML frontmatter) along with additional unstructured information in the Markdown section.

### 6.3 Using Defined Attributes and Relationships

When creating HKM documents, users are encouraged to use the attributes and relationships defined in the HKM core and any additional packages they're using. However, users can also add custom attributes and relationships to suit their specific needs:

```yaml
---
title: My Custom HKM Document
author: John Doe
topics:
  - Custom Knowledge
custom_attribute: This is a user-defined attribute
custom_relationship:
  - Related Item 1
  - Related Item 2
---

# Custom HKM Usage

This document demonstrates how users can add custom attributes and relationships to standard HKM structures.

## Extended Usage

While HKM provides a set of core attributes and relationships, its flexibility allows for domain-specific extensions, enabling rich and varied knowledge representation.
```

These examples demonstrate the versatility of HKM in representing different types of knowledge artifacts, from freeform notes to structured entity representations, while allowing for customization to meet specific needs.

### 6.4 Flexible Usage of Common Entities

Common entities in HKM, such as person, datetime, and location, can be used both as standalone knowledge artifacts and as attributes within other entities. This dual nature allows for rich, detailed representation when needed, and simpler attribute-style usage in other contexts.

For example, a "person" entity could be a full HKM document:

```yaml
---
name: John Doe
is_a: person
birth_date: 1985-03-15
occupation: Software Engineer
---

Detailed biography and information about John Doe...
```

Or it could be used as an attribute in another entity:

```yaml
---
name: Project X
is_a: project
lead_developer: 
  name: John Doe
  role: Software Engineer
---

Project details...
```

This flexibility allows HKM to adapt to various levels of detail and complexity in knowledge representation.

## 7. Extensibility and Customization

Human Knowledge Markdown is designed to be highly extensible, allowing for domain-specific customizations and extensions.

### 7.1 Custom Entity Types

New entity types can be defined by subclassing existing primitives:

```yaml
- name: custom_entity
  is_a: subclass_of
  subclass_of: thing
  attributes:
    - custom_attribute1
    - custom_attribute2
```

### 7.2 Domain-Specific Packages

HKM supports the creation of domain-specific packages that extend the core primitives with specialized entities and relationships.

## 8. Interoperability

Human Knowledge Markdown is designed to interoperate with existing knowledge representation standards and technologies. However, it's important to note that much work still needs to be done in this area. The following examples illustrate potential interoperability approaches:

### 8.1 Mapping to Formal Ontologies

HKM constructs can be mapped to formal ontologies like OWL or schema.org. For example:

```yaml
name: Person
is_a: subclass_of
subclass_of: thing
owl_equivalent_class: schema:Person
attributes:
- name
- birthDate
```

This definition could be mapped to the schema.org Person class, allowing for integration with existing semantic web technologies.

### 8.2 Knowledge Graph Compatibility

The entity-attribute-relationship model of HKM is compatible with graph database structures. For instance, an HKM relationship:

```yaml
- name: John
  knows:
    - Jane
```

Could be represented as a graph edge: `(John)-[KNOWS]->(Jane)`

### 8.3 Topic Map Alignment

HKM's topic-based organization aligns with topic map concepts. For example:

```yaml
- name: Programming
  subclass_of: topic
  related_topics:
    - Computer Science
    - Software Engineering
```

This could be represented as a topic with associations in a topic map structure.

#### 8.3.1 Self-Organizing Topic Map Algorithm
HKM provides a powerful framework for organizing knowledge through topic mapping. A key feature is the Self-Organizing Topic Map Algorithm, which enables the construction of coherent topic structures from large collections of unstructured notes.

1. **Initial Topic Extraction**
   - Use an AI language model to analyze the content of each note
   - Extract potential topics based on semantic analysis, entity recognition, and keyword extraction
   - Assign a confidence score to each extracted topic based on relevance to the note content

2. **Topic Clustering and Pruning**
   - Aggregate the extracted topics across all notes into a master list
   - Use clustering algorithms (e.g., K-Means, DBSCAN) to group similar topics together
   - Identify and remove redundant or near-duplicate topics within each cluster
   - Optionally, use word vector models (e.g., Word2Vec, GloVe) to enhance semantic similarity calculations

3. **Human-Guided Topic Curation**
   - Present the clustered topics to human curators for review
   - Allow curators to merge, split, rename, or remove topics as needed
   - Facilitate collaborative discussion and resolution of conflicts or ambiguities
   - Capture human-provided topic descriptions and relationships

4. **Topic Hierarchy Construction**
   - Use the curated topics as input to a hierarchy construction algorithm
   - Employ techniques like subsumption analysis, semantic similarity, and co-occurrence patterns
   - Identify potential parent-child relationships and construct an initial topic hierarchy
   - Utilize any existing ontologies or taxonomies as a base structure, if available

5. **Topic Relationship Modeling**
   - Analyze the topic hierarchy and note content to identify cross-cutting relationships
   - Model these relationships as links between different branches of the hierarchy
   - Construct a topic graph representing both hierarchical and associative relationships

6. **Note Re-Tagging**
   - Use the constructed topic graph as a reference model
   - Re-analyze each note's content against the graph
   - Assign the most relevant topics (hierarchical and associative) to each note
   - Utilize AI techniques like semantic similarity, topic modeling, and classification

7. **Human Validation and Refinement**
   - Provide interfaces for human experts to review the note-topic assignments
   - Allow for manual corrections, additions, or removals of assigned topics
   - Capture human feedback and use it to refine the topic graph and AI models

8. **Iterative Convergence**
   - Feed the human-validated note-topic assignments back into the algorithm
   - Repeat steps 2-7, using the updated data to further refine the topic structure
   - Continue iterating until the topic graph and note assignments stabilize

This algorithm leverages both AI capabilities and human expertise to create a robust, self-organizing knowledge structure that can handle large volumes of unstructured information.

### 8.4 Schema.org Alignment

HKM entities can be aligned with Schema.org types to enhance web discoverability. For example:

```yaml
name: Person
is_a: subclass_of
subclass_of: thing
schema_org_type: schema:Person
attributes:
  - name
  - birthDate
  - gender
```

This alignment allows HKM data to be easily translated into Schema.org-compatible formats for use in structured data on the web.

## 9. AI Integration

Human Knowledge Markdown is designed to be used directly with AI Language Models (LLMs). The language is structured so that AI models can directly understand the meaning through the semantic definitions reinforced by the entity definitions.AI can be used with HKM in several ways:

1. **Entity Definition**: AI can create new entity definitions based on natural language descriptions. For example:

   Prompt: "Create an HKM entity definition for a 'Recipe' that includes attributes for ingredients, instructions, and cooking time."

   AI-generated response:
   ```yaml
   name: recipe
   is_a: subclass_of
   subclass_of: thing
   attributes:
     - ingredients
     - instructions
     - cooking_time
   predicates:
     - is_recipe_for
     - has_ingredient
     - requires_time
   aliases:
     - dish
     - meal
   ```

2. **Structured Data Extraction**: AI can extract structured HKM data from unstructured text. For instance, given a paragraph about a person, AI could generate an HKM-formatted representation of that person.

3. **Knowledge Base Expansion**: AI can suggest new relationships or attributes for existing entities based on analysis of the current knowledge base and external information sources.

4. **Natural Language Querying**: AI can interpret natural language queries and translate them into formal queries against the HKM knowledge base.

## 10. Implementation Considerations

### 10.1 Parsing and Processing

Implementations of HKM should consider:
- Efficient YAML parsing
- Handling of circular definitions
- Resolution of inheritance hierarchies

### 10.2 Validation

HKM implementations should provide validation mechanisms for:
- Entity structure compliance
- Relationship consistency
- Inheritance validity

### 10.3 Query and Traversal

While specific query languages are not part of the core HKM specification, implementations should consider efficient mechanisms for:
- Entity lookup
- Relationship traversal
- Attribute querying

## 11. Future Directions

The Human Knowledge Markdown specification is designed to evolve. Additional areas for future research and development include:
- Enhanced interoperability with AI and machine learning systems
- Cardinality constraints for relationships and attributes
- Additional relationship characteristics (transitivity, symmetry, etc.)
- Data types and value constraints for attribute values
- Support for reification and higher-order constructs
- Advanced querying capabilities, including a dedicated query language for HKM
- Inference engines for deriving new knowledge from existing HKM data
- Tools for visual editing and navigation of HKM knowledge bases

## 12. Contributing

Human Knowledge Markdown is an open-source project, and contributions are welcome. The source code is available at https://github.com/digitalreplica/human-knowledge-markdown under an Apache 2.0 license. Users are free to use, adapt, and contribute back to the project.

We encourage contributions in several areas:
- Extending core definitions and creating new entity types
- Developing domain-specific packages
- Improving interoperability with other knowledge representation systems
- Creating tools and libraries for working with HKM

It is hoped that with more contributors, natural "best-in-breed" libraries will emerge to help standardize knowledge representation across large groups of people.

## 13. Conclusion

Human Knowledge Markdown provides a flexible, extensible framework for knowledge representation that bridges multiple paradigms. By combining the strengths of data serialization formats, knowledge graphs, topic maps, and formal ontologies, HKM offers a powerful tool for capturing and organizing human knowledge in a machine-processable form. Its design facilitates both human readability and AI processing, making it a versatile choice for modern knowledge management needs.

## Addendum: Human Knowledge Markdown Development Process

Human Knowledge Markdown was developed through an iterative process of human-AI collaboration, consisting of multiple dialogue sessions between a single human researcher and an AI language model.

Key aspects of the process:

1. Sessions: Each development session was a single dialogue between the human researcher and the AI. The human provided direction, critical analysis, and domain expertise, while the AI offered rapid prototyping, systematic analysis, and diverse perspective generation.

2. Knowledge Delta Accumulation: After each session, the ai articulated the "knowledge delta" - new insights, decisions, or refinements made during the dialogue. This delta was documented and integrated into the evolving HKM framework.

3. Cross-Session Context: While AI interactions are stateless, the accumulation of knowledge deltas allowed context to be carried across sessions. The human researcher used this accumulated knowledge to inform and guide subsequent dialogues.

4. Iterative Refinement: Each session built upon previous ones, allowing for continuous refinement of HKM's core concepts, structures, and principles.

This approach enabled the organic evolution of HKM, grounded in practical application and responsive to emerging insights. It leveraged the complementary strengths of human expertise and AI capabilities to create a flexible, robust knowledge representation framework.