# HKMD Design Decisions and Rationale

## 1. Foundational Principles

### 1.1 Bottom-Up Knowledge Modeling
- Decision: Adopt a bottom-up approach to knowledge modeling.
- Rationale: Allows for unconstrained, natural expression of knowledge, aligning with how humans typically think and communicate.
- Implications: Requires flexible structures that can accommodate diverse knowledge representations.

### 1.2 Balancing Flexibility and Structure
- Decision: Strike a balance between unconstrained knowledge authoring and providing semantic rigor.
- Rationale: Enables intuitive knowledge capture while still allowing for machine-processable representations.
- Implications: Necessitates careful design of core primitives and extension mechanisms.

## 2. Knowledge Representation Model

### 2.1 Entity-Attribute-Relationship Model
- Decision: Adopt an entity-attribute-relationship model as the foundation for HKMD.
- Rationale: Provides a flexible yet powerful framework for representing diverse knowledge structures.
- Implications: Influences the design of core primitives and how knowledge is structured in HKMD documents.

### 2.2 Unification of Topics and Entities
- Decision: Represent both conceptual topics and concrete entities using the same "topic" construct.
- Rationale: Simplifies the knowledge model and avoids the need for separate hierarchies or representations.
- Implications: Enables a more intuitive organization of knowledge, allowing seamless navigation between abstract concepts and specific instances.

### 2.3 Primordial "thing" Entity
- Decision: Define a primordial "thing" entity as the core contextual container for representing instantiated objects, concepts, and notions.
- Rationale: Provides a flexible, broad container that avoids rigid ontological classifications from the outset.
- Implications: Allows for representing any kind of instantiated concept, whether physical or abstract, aligning with HKMD's goal of unconstrained knowledge modeling.

## 3. Linguistic Integration

### 3.1 Natural Language Grounding
- Decision: Ground HKMD constructs in natural language semantics.
- Rationale: Enhances intuitiveness and accessibility for human users while maintaining machine-processability.
- Implications: Requires mechanisms for capturing linguistic variations and mapping them to formal structures.

### 3.2 Aliases and Predicates
- Decision: Introduce "aliases" and "predicates" as core concepts in entity definitions.
- Rationale: Allows capturing multiple linguistic forms for entities and relationships, enhancing flexibility in knowledge expression.
- Implications: Enables more intuitive and context-specific knowledge representation across all entity types.

### 3.3 Flexible Usage of Aliases
- Decision: Allow aliases to be used flexibly as attribute names when referencing entities.
- Rationale: Enhances the natural language feel of HKMD documents and allows for more intuitive knowledge authoring.
- Implications: Requires clear guidelines for alias definition and usage to maintain consistency.

## 4. Inheritance and Type System

### 4.1 Subclass Relationship
- Decision: Adopt "subclass_of" as the primary mechanism for defining type hierarchies.
- Rationale: Aligns with established knowledge representation standards and enables clear inheritance structures.
- Implications: Facilitates the creation of rich, hierarchical knowledge models.

### 4.2 Multiple Inheritance
- Decision: Allow entities to subclass or instantiate multiple parent classes.
- Rationale: Provides flexibility in modeling complex concepts that may belong to multiple categories.
- Implications: Requires careful consideration of property inheritance and potential conflicts.

### 4.3 Inheritance as Knowledge Modeling Mechanism
- Decision: Position inheritance as a crucial mechanism for enabling modular, extensible knowledge modeling.
- Rationale: Allows for building up rich hierarchies of increasingly specialized entity types through composition of shared relationship primitives.
- Implications: Enables a modular, scalable approach to knowledge modeling aligned with HKMD principles.

## 5. Core Primitives

### 5.1 Selection of Fundamental Entities
- Decision: Define entity, attribute, relationship, thing, topic, and note as core primitives.
- Rationale: Provides a minimal yet comprehensive set of building blocks for knowledge representation.
- Implications: Influences the entire HKMD framework and how knowledge is structured and manipulated.

### 5.2 Evolution from 'Property' to 'Attribute'
- Decision: Adopt "attribute" as the fundamental concept representing characteristics of entities, replacing the initial notion of "property".
- Rationale: Better aligns with the broader scope of entity characteristics in HKMD's flexible modeling approach.
- Implications: Affects the definition and usage of entity characteristics throughout the HKMD framework.

### 5.3 Relationship as Specialized Attribute
- Decision: Define "relationship" as a specialized type of "attribute" where the value represents an associative connection between entities.
- Rationale: Unifies the concept of entity characteristics while distinguishing associative connections.
- Implications: Simplifies the core model while maintaining the ability to represent complex inter-entity relationships.

## 6. Extensibility and Customization

### 6.1 Layered Architecture
- Decision: Adopt a layered architecture with core primitives, common entities, and domain-specific extensions.
- Rationale: Provides a clear structure for extending HKMD while maintaining a stable core.
- Implications: Facilitates the development of domain-specific knowledge models without compromising the fundamental HKMD framework.

### 6.2 Separation of Ontological Constructs
- Decision: Move formal ontological constructs (e.g., part_of, has_part) into a separate ontology package.
- Rationale: Keeps the core HKMD model lean while allowing for more formal ontological work when needed.
- Implications: Maintains HKMD's flexibility while providing a path for integration with more formal ontological systems.

## 7. Serialization and Syntax

### 7.1 YAML as Primary Format
- Decision: Use YAML as the primary serialization format for HKMD.
- Rationale: YAML provides a good balance of human readability and machine parseability, aligning with HKMD's goals.
- Implications: Influences the syntax and structure of HKMD documents and affects tooling development.

### 7.2 Integration with Markdown
- Decision: Combine YAML frontmatter with Markdown content in HKMD documents.
- Rationale: Allows for structured metadata alongside freeform textual content, enhancing expressiveness.
- Implications: Requires clear guidelines for integrating YAML and Markdown sections in HKMD documents.

### 7.3 Naming Conventions
- Decision: Adopt underscore-delimited phrases for relationship and attribute names.
- Rationale: Enhances readability while avoiding potential conflicts with other syntax elements.
- Implications: Establishes a consistent naming convention across HKMD documents and definitions.

## 8. Ontological Considerations

### 8.1 Relationship to Formal Ontologies
- Decision: Design HKMD to be mappable to formal ontologies while maintaining its flexible core.
- Rationale: Enables interoperability with existing ontological systems without sacrificing HKMD's unique strengths.
- Implications: Requires careful design of mapping mechanisms and consideration of ontological principles in HKMD's structure.

### 8.2 Handling of Specialized Ontological Constructs
- Decision: Include specialized ontological constructs (e.g., part_of, has_part) in a separate package rather than the core.
- Rationale: Maintains the lean, flexible nature of core HKMD while providing options for more formal ontological modeling.
- Implications: Allows HKMD to cater to both informal and formal knowledge modeling needs.

## 9. Scalability and Performance

### 9.1 Large-Scale Knowledge Base Considerations
- Decision: Design HKMD with potential for large-scale knowledge bases in mind.
- Rationale: Ensures HKMD can handle substantial amounts of knowledge as it grows.
- Implications: Influences decisions on indexing, querying, and storage mechanisms for HKMD data.

### 9.2 Query and Inference Considerations
- Decision: Defer implementation of complex query and inference mechanisms to future development.
- Rationale: Focuses initial development on core knowledge representation capabilities.
- Implications: Requires consideration of how future query and inference capabilities will integrate with the core HKMD model.

## 10. Tooling and Implementation

### 10.1 Tooling Considerations
- Decision: Design HKMD with future tool development in mind.
- Rationale: Ensures the HKMD specification is implementable and user-friendly.
- Implications: Influences decisions on syntax, structure, and extension mechanisms to facilitate tool development.

### 10.2 Compatibility and Integration
- Decision: Consider compatibility with existing knowledge management and semantic web technologies.
- Rationale: Enhances HKMD's potential for adoption and integration with existing systems.
- Implications: Requires careful design decisions to balance HKMD's unique features with compatibility concerns.
