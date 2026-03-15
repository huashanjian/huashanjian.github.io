---
title: "My CS Learning and Workflow: Harnessing LLMs, Obsidian, and Zotero"
date: 2025-05-08
---

In the fast-evolving field of Computer Science, continuous learning is the norm. Daily work and study expose us to information from diverse, fragmented sources: hundreds of pages of official documentation, concise technical blog posts, industry news scrolled on our phones. Building a personal workflow that integrates these fragments into a searchable knowledge base is essential.

After a period of practice and adjustment, I've refined a workflow centered around **Collect – Organize – Apply (COA)**, relying on three main tools: Large Language Models (LLMs), Obsidian, and Zotero. The goal is to master a few key tools and integrate them into daily routines, with one core objective: **to quickly find and effectively use knowledge when needed.**

## My Information Processing Philosophy: Prioritize Primary Sources, Leverage Secondary Information, and Build a Searchable Knowledge Network

Before constructing my workflow, I established several fundamental principles that guide how I filter, organize, and use information:

1. **Priority of Information Sources**: In CS, the quality of information sources is paramount. `Source code` and `official documentation` are usually the most accurate and up-to-date. Next are high-quality `academic papers` (especially from top conferences and classic works) and authoritative `English monographs`. Following these are reputable `English technical blogs` and `in-depth talks`. The principle: **the closer to the source, the less information distortion.**

2. **The Value of Secondary and Tertiary Information**: While primary sources are most reliable, excellent secondary and tertiary materials (reviews, high-quality tutorials, classic interpretations) often contain the author's deep thinking, structured organization (mind maps, flowcharts), and unique insights (analogies, abstractions). They help us grasp core content faster, but the ultimate goal is to internalize these understandings and quickly locate key information when needed.

3. **Building an Easily Searchable Knowledge Network**: Connections between knowledge points and clear organization are central. The purpose is to quickly and accurately access relevant content when solving specific problems or finding particular information.

4. **"Recursive" Learning: Deep Dives as Needed**: When encountering new problems or unfamiliar areas, I use existing knowledge nodes as springboards to dig deeper, quickly learning related unknown concepts. This is a problem-driven learning approach.

5. **Deep Tool Utilization, Focused on Practical Application**: Choose a few core tools and use their features thoroughly. The core value of tools lies in enhancing the efficiency of finding and applying knowledge, not in the tools themselves.

## My Core Workflow: COA (Collect - Organize - Apply)

My workflow revolves around three core stages:

### I. Collect: Precision Capture and Initial Processing

The goal of this stage is to efficiently bring valuable information into management with low friction, performing initial quality assessment and preprocessing.

* **Zotero: Standardized Management of Academic Literature and High-Quality Online Resources**
  * **Main Purpose**: Centralized management of academic papers, e-books, important reports, and valuable web articles.
  * **Key Uses**:
    * **Zotero Connector (Browser Plugin)**: One-click capture of paper metadata, PDFs, and webpage snapshots. For webpages, besides saving a snapshot, I also keep the original URL for traceability. For non-traditional resources like GitHub repositories, I create an entry, manually input key information, and link to the repository URL.
    * **Entry Management and Tagging**: Add custom tags to each entry (e.g., `#to-read`, `#core-concept`, `#project/ProjectX`, `#domain/database`). Zotero's tag system supports color-coding for visual differentiation.
    * **RSS Feed Integration**: Subscribe to RSS feeds of important journals, conferences, or influential tech blogs via Zotero's built-in feature or tools like Feedly. For Feedly, I periodically import filtered valuable articles using the "Save to Zotero" function.
    * **Collections**: Create dedicated collections for each course, research project, or major learning topic, facilitating categorized management and batch operations.

* **Obsidian: Markdown Storage for Daily Notes, Ideas, and Web Content**
  * **Main Purpose**: Recording fleeting ideas, meeting minutes, drafts of course notes, and clipping valuable web content. Obsidian serves as a "staging area" and "incubator" for knowledge.
  * **Key Uses**:
    * **Web Clipper Plugins**: Convert valuable web articles directly into Markdown format and save them to a designated "inbox" folder in Obsidian (e.g., `0_Inbox` or `ToProcess`). The high customizability of plugins like MarkDownload allows me to configure which elements to retain and how to format them, ensuring clean and consistent clipped content.

* **Large Language Models (LLMs): Intelligent Information Processing and Comprehension Aid**
  * **Main Purpose**: Quickly understanding unfamiliar concepts, translating foreign materials, initial information screening, and code assistance.
  * **Key Uses**:
    * **Quick Summarization and Translation**: For lengthy English documents or papers, I copy key paragraphs or the full text for the LLM to generate a summary or translation, helping me quickly assess their value and reading priority.
    * **Concept Explanation and Analogies**: For abstract or complex CS concepts, I ask the LLM to explain them in different ways, provide real-life analogies, or generate pseudocode to illustrate them.
    * **Code Snippet Interpretation and Generation**: When learning new APIs or algorithms, LLMs can help explain the logic of sample code, variable meanings, or generate initial implementations based on my requests (e.g., "Implement a quicksort function in Python with detailed comments"). I also use it to assist in translating code between programming languages.
    * **Conversational Exploration**: Engage in multi-turn dialogues with an LLM on a specific topic, delving deeper layer by layer to unearth related knowledge points. I organize and copy valuable conversation content into Obsidian.

### II. Organize: Structuring and Networking for "Rapid Retrieval"

The purpose of organizing is to structure and network the collected information. The core goal is to **optimize retrieval efficiency and contextual understanding**, enabling quick location and effective use when needed.

* **Obsidian: Building Your Searchable "Digital Brain"**
  * **Core Purpose**: The ultimate hub for knowledge consolidation, organization, and linking. All design choices prioritize future ease of search and application.
  * **Key Uses**:
    * **Bidirectional Linking**: This is key for rapid navigation and understanding context. Create separate notes for each core concept, technical term, project, or paper read, and organically connect them using `[[WikiLinks]]`. When looking up a concept, you can immediately see all directly related concepts and notes, forming a knowledge network.
    * **Strategic Use of Tags**: Tags are an important dimension for retrieval. I use hierarchical or thematic tags (e.g., `#technology/database/MySQL`, `#project/Alpha`, `#paper/to-read`, `#status/in-progress`) to quickly filter and locate relevant notes.
    * **MOCs (Maps of Content) as Indexes**: For a complex topic or important project, I create an MOC note, which serves as a "high-level index page" or "dashboard" for that topic. The MOC aggregates links to all relevant core notes, key resources, task lists, etc. When needing to systematically understand or find specific information within that topic, the MOC is an excellent starting point.

* **Zotero & Obsidian Synergy**:
  * **Linking Bibliographic Information**: Manage metadata and PDF files in Zotero. Using Zotero plugins, annotations and notes from literature can be exported as Markdown and stored in Obsidian. The exported Markdown file automatically includes a link to the Zotero entry (e.g., `zotero://select/library/items/ITEMKEY`), allowing a one-click jump back to Zotero to view the original text or complete metadata.
  * **Citations Plugin**: When writing content in Obsidian that requires formal citations (technical documents, research reports, blog posts), use the Citations plugin. This plugin requires the Better BibTeX plugin in Zotero to periodically export the library as a .bib file. Then, in Obsidian, you can quickly search and insert Pandoc-style citation markers, which can automatically generate a standard-formatted bibliography upon export.

* **LLMs: Assisting in Information Structuring & Refinement**
  * **Core Purpose**: To help transform scattered notes, conversation logs, or initially collected materials into more clearly structured note entries that are easier to retrieve in the future.
  * **Key Uses**:
    * **Information Point Extraction and Categorization Suggestions**: Input a raw note or LLM conversation log containing multiple knowledge points, and have the LLM help identify key information points and suggest appropriate tags or possible categorization methods for better organization in Obsidian.
    * **Generating Note Summaries or Keywords**: For longer notes, use an LLM to generate a brief summary or extract core keywords. These summaries and keywords can be added to the note's metadata area (e.g., Frontmatter), thereby optimizing Obsidian's internal search results and increasing the discoverability of relevant notes.

### III. Apply: Reviewing Through Application, Retrieving On-Demand

The value of knowledge is ultimately realized in its application. My "review" process occurs more often when I actually need to use this knowledge to solve problems, write documents, make technical decisions, or discuss with others. Powerful retrieval capabilities are the core foundation supporting this "just-in-time application-based review."

* **Obsidian: Your Instant Knowledge Extraction Engine**
  * **Core Purpose**: To quickly and accurately find the required information when needed. In this process of finding and applying, related knowledge points are naturally "reviewed" and consolidated.
  * **Key Uses**:
    * **Global Search**: Obsidian's global search is powerful, supporting multi-dimensional searches by keyword, tag, path, task status, etc., with extremely fast response times. This is my most frequently used method for finding information. I use search operators (e.g., `tag:#java file:ProjectA "specific error message" line:(onboarding)`) to pinpoint notes.
    * **Navigating via Links and Backlinks**: When dealing with a specific problem or learning a new technical point, I open the relevant core note. Through the links already established in the note, I can quickly jump to other related contextual information. Simultaneously, viewing the current note's **Backlinks Pane** shows me which other notes mention the current concept or topic. This is like the brain's associative thinking, helping me recall more related knowledge—a natural way to "review."
    * **MOCs as Starting Points for Searches**: When I'm fuzzy about the overall structure of a large knowledge topic, or need to find specific details within that topic, I first open the corresponding MOC note. An MOC is like a well-organized table of contents or entry page, guiding me quickly to the target note or related resources.
    * **Output-Driven Search and Organization**: When I need to write a technical proposal, prepare a presentation, write a blog post, or solve a complex engineering problem, I actively search and organize relevant notes in Obsidian. This process of "searching and organizing for output" is itself an efficient and targeted review and deepening of understanding. During this process, I might discover knowledge gaps, thereby driving new learning.

* **LLMs: Your Intelligent Q&A and Application Scenario Assistant**
  * **Core Purpose**: When you encounter specific problems and need to quickly extract and integrate information from your existing knowledge base (Obsidian notes), or need to expand thinking and generate solutions based on existing knowledge, LLMs can provide powerful assistance.
  * **Key Uses**:
    * **Q&A and Information Extraction Based on Note Content**: If I have extensive notes on a particular technology in Obsidian and encounter a specific application problem, I can copy relevant note snippets or key points to the LLM and ask: "Based on the above notes about [Technology X], how should I solve [specific problem Y]?" or "Please help me summarize the key considerations and configuration parameters for using [Technology X] in [scenario Z] from the following notes."
    * **Rapid Generation of Code Samples or Configuration Files**: When I need a code snippet for a specific function, or a configuration example for a tool, and my notes might only contain a description of the principle or partial fragments, I can combine the note content with a query to the LLM to generate more complete and practical code or configurations.
    * **Preliminary Discussion and Evaluation of Technical Solutions**: When conceptualizing a technical solution, I can feed relevant technical points, requirement constraints, and existing resource information from Obsidian to the LLM. It can help analyze the feasibility of the solution, provide comparisons of different approaches, point out potential technical risks, or recommend related best practices.

* **Zotero: Precisely Locating Academic and Authoritative Resources**
  * **Core Purpose**: When writing documents that require rigorous citation, conducting in-depth research, or needing to verify a technical argument, to quickly find relevant original literature and the annotations you've made on them.
  * **Key Uses**:
    * **Keyword and Tag Search**: Utilize Zotero's powerful search capabilities (including full-text search of PDF content if an index for the library has been built) to quickly locate target literature through keyword combinations, author, publication year, custom tags, etc.
    * **Directly Viewing Notes and Annotations**: After finding the target literature, open the PDF directly in Zotero to quickly browse highlights, underlines, and annotations made during previous readings. This rapidly recalls the core ideas of the literature and thoughts from that reading, often more efficiently than rereading the entire text.
    * **Seamless Integration with Obsidian Notes**: If the Zotero entry link is correctly recorded in an Obsidian literature note, you can one-click jump directly from the note in Obsidian to the corresponding entry in Zotero, and then view the original text or complete related metadata.

## Reflections on Tool Choices

I chose these three tools as the core of my personal knowledge management system because they each excel in different parts of the Collect-Organize-Apply process and can collaborate effectively. They also all support a local-first data management model, ensuring data sovereignty and control:

* **LLMs**: As an "intelligent accelerator" and "cognitive aid" for information processing, they significantly enhance efficiency in information acquisition, understanding, initial processing, and application stages.
* **Zotero**: As the "standardized foundation" for academic literature and high-quality online resources, it ensures the reliability of knowledge sources and professional management. Its data can be stored locally and synced via Zotero's cloud service or WebDAV with third-party cloud storage.
* **Obsidian**: As a personalized "knowledge hub" and "creativity workshop," its flexibility, powerful linking capabilities, and plain text Markdown foundation weave all information fragments into a unique knowledge network. Obsidian's core is local Markdown files, giving users complete data ownership and control.

This combination doesn't exclude other excellent tools. For example, when needing to draw complex diagrams, I might use Excalidraw or specialized drawing software; for code-intensive work, IDEs remain the main tool. But LLMs, Obsidian, and Zotero form the bedrock of my knowledge management workflow.

Furthermore, as times change and LLMs continuously evolve, I use the term "LLM" in this article rather than specific models. I have my own set of principles for choosing LLMs, but I won't elaborate on that here. The core idea is to **"see the gold after washing away the dross, returning to the authentic essence after discarding the superficial glamour."**

## Conclusion

For every learner and practitioner in the CS field, building a personal knowledge management system that can quickly respond to practical needs is as important as mastering a core programming language or a key technical framework. The practice I've shared, based on LLMs, Obsidian, and Zotero, focuses on efficiently finding, extracting, and applying information when needed, with "review" naturally integrated into these daily application scenarios.

The core philosophy is: **Prioritize high-quality information, build an easily searchable knowledge network, and use selected core tools to serve "just-in-time application."** This system is not static; it continuously iterates and optimizes as my understanding of these tools deepens and my work and study needs change.

I hope the experiences I've shared provide you with a practical and actionable perspective. The most important thing is not to copy my method entirely, but to understand the logic behind it, and in conjunction with your own learning habits and work scenarios, to boldly experiment, continuously adjust, and ultimately build a "knowledge engine" that truly suits you and can continuously empower your personal growth.
