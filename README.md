# Human Knowledge Markdown (HKM)

Human Knowledge Markdown (HKM) is a practical approach to knowledge management that seamlessly integrates freeform notes with powerful knowledge structuring capabilities. It extends beyond simple metadata fields to incorporate capabilities typically found in formal knowledge management systems, but in a more flexible and intuitive manner.

HKM enhances traditional note-taking by allowing for a spectrum of structured information, from simple metadata fields to complex semantic relationships, enabling more effective organization, retrieval, and analysis of knowledge. Moreover, its design allows AI models to directly interpret and leverage the underlying knowledge structure, facilitating deeper understanding and more sophisticated processing of the notes' content.

## Key Features

- **Unified Knowledge Representation**: HKM bridges multiple knowledge paradigms, including:
  - Unstructured text (Markdown)
  - Structured data (YAML)
  - Knowledge graphs
  - Topic maps
  - Formal ontologies

- **Flexible Knowledge Modeling**: Embraces a bottom-up approach, allowing unconstrained expression of knowledge while enabling organic emergence of knowledge structures.

- **Semantic Richness**: Goes beyond simple key-value pairs to represent complex relationships, hierarchies, and semantic context.

- **AI-Friendly Format**: Designed for direct interpretation by AI language models, enhancing capabilities in knowledge extraction, reasoning, and generation.

- **Extensible Framework**: Built on a core set of primitives that can be extended for domain-specific knowledge modeling.

- **Interoperability**: Compatible with existing knowledge representation standards, facilitating integration with other systems.

## How It Works

HKM uses YAML frontmatter in Markdown files to represent structured knowledge, while allowing freeform content in the Markdown body. This approach enables:

1. Capturing structured metadata about knowledge artifacts
2. Representing complex relationships between entities
3. Organizing knowledge into topics and hierarchies
4. Maintaining human-readability while enabling sophisticated machine processing

## Getting Started

To start using HKM:

1. Familiarize yourself with the [core concepts and primitives](./docs/HKM%20Technical%20Specification%20and%20Architecture.md#3-foundational-primitives).
2. Review the [HKM schema files](./hkm/) to understand the available entity types and relationships.
3. Create your first HKM document using a text editor that supports Markdown with YAML frontmatter.

Example HKM document:

```yaml
---
name: Introduction to HKM
is_a: note
author: Your Name
topics:
  - Knowledge Management
  - Markdown
---

# Introduction to Human Knowledge Markdown

HKM is a flexible knowledge representation format that combines the simplicity of Markdown with the power of formal knowledge systems...

## Key Benefits

1. Intuitive knowledge capture with rich semantic structure
2. Seamless integration of unstructured and structured information
3. Enhanced knowledge discovery and reasoning capabilities
```

## Documentation

- [Technical Specification and Architecture](./docs/HKM%20Technical%20Specification%20and%20Architecture.md)
- [Design Decisions and Rationale](./docs/HKM%20Design%20Decisions%20and%20Rationale.md)
- [Philosophical Framework and Principles](./docs/HKM%20Philosophical%20Framework%20and%20Principles.md)

## Tools

- [compile_hkm_package.py](./tools/compile_hkm_package.py): A utility for compiling individual YAML definition files into a single HKM schema package.

## Contributing

HKM is an open-source project, and contributions are welcome. Whether you're interested in extending the core definitions, creating domain-specific packages, or improving tooling, your input can help shape the future of knowledge representation.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](./LICENSE) file for details.