# Chain of Thought as a Research Methodology

A deep research synthesis covering chain-of-thought reasoning in both the AI/LLM sense and the broader intellectual/academic sense. This document provides actionable techniques for developing ideas through structured thinking.

---

## 1. Chain of Thought in Research: Breaking Problems into Sequential Steps

### The Core Idea

Chain of thought (CoT) reasoning is the practice of decomposing complex problems into intermediate steps, solving each step individually, and building toward a final conclusion. This is not merely an AI technique -- it is a fundamental mode of human cognition that has deep roots in intellectual history.

### Historical Roots

**Descartes' Method (1637):** In *Discourse on Method*, Descartes established rules for reasoning that centered on creating "a long chain of inferences." He insisted that philosophers should leave nothing out of the chain of reasoning and should repeatedly review the chain of relationships between all parts of a problem, making it easy to understand how any single part relates to others. This is arguably the first formal articulation of chain-of-thought reasoning as methodology.

**Peirce's Critique:** Charles Sanders Peirce rejected Descartes' "single chain of argumentation" in favor of a more community-based, fallibilistic epistemology. Peirce argued that "all our cognitions are hypothetical and fallible," suggesting that reasoning chains should be treated as provisional rather than certain. This tension -- between linear certainty and provisional exploration -- remains central to how we use CoT today.

### Practical Application

A research chain of thought follows this general pattern:

1. **Identify the problem** -- What specifically are you trying to understand?
2. **Decompose** -- What are the sub-questions that must be answered first?
3. **Sequence** -- In what order must these sub-questions be addressed?
4. **Solve incrementally** -- Work through each step, documenting your reasoning
5. **Synthesize** -- Combine the intermediate findings into a coherent answer
6. **Verify** -- Does the conclusion hold when you trace back through the chain?

### When Sequential Reasoning Works Best

- Arithmetic and logical problems with clear dependencies
- Causal analysis (A causes B causes C)
- Legal reasoning and case analysis
- Debugging (systematic elimination)
- Mathematical proofs
- Policy analysis (if X then Y)

---

## 2. Socratic Method and Dialectical Thinking

### The Socratic Method

The Socratic method is a form of argumentative dialogue in which one probes a conversation partner's position through questioning until the partner either reaches a conclusion independently or their reasoning breaks down, revealing inconsistencies.

**Core process:**

1. **Start with a claim** -- The interlocutor states what they believe
2. **Question assumptions** -- "What do you mean by X?" / "How do you know that?"
3. **Seek counterexamples** -- "Can you think of a case where that isn't true?"
4. **Expose contradictions** -- Show where the reasoning is inconsistent
5. **Refine or abandon** -- The interlocutor modifies their position or admits ignorance

Socrates believed that the first step to knowledge was recognition of one's ignorance. The method is designed to reveal that what appears to be knowledge is often unexamined assumption.

### Dialectical Thinking

The dialectical process builds on Socratic questioning with a more structured framework:

- **Thesis:** A clear statement or proposition
- **Antithesis:** A strong counter-argument
- **Critical analysis:** Examining strengths and weaknesses of both positions
- **Synthesis:** Reconciling the opposing views into a more nuanced position

### Practical Self-Questioning Protocol for Research

You can apply the Socratic method to your own thinking by asking yourself:

1. What exactly is my claim?
2. What evidence supports it?
3. What assumptions am I making that I haven't examined?
4. What would someone who disagrees say?
5. Can I find a counterexample to my claim?
6. If my claim is wrong, what would be true instead?
7. How would I test whether my claim is correct?

This self-interrogation is one of the most powerful techniques for developing rigorous research questions from vague intuitions.

---

## 3. Structuring a Research Chain of Thought

### From Question to Conclusion: A Complete Framework

**Phase 1: Problem Identification**
- Start with a broad area of interest or a personal observation
- Ask "What puzzles me about this?" or "What doesn't work as expected?"
- Write down everything you think you know about it (Feynman technique)

**Phase 2: Literature Immersion**
- Read initial literature to understand the scope
- Look for unexplored or underexplored areas in existing research
- Identify competing theories and frameworks
- Note gaps, contradictions, and unresolved questions

**Phase 3: Question Refinement**
- Transform vague interest into specific, testable questions
- Apply the FINERMAPS criteria: Feasible, Interesting, Novel, Ethical, Relevant, Manageable, Appropriate, Potential value, Publishability, Systematic

**Example transformation:**
- Vague: "What is the impact of technology on education?"
- Specific: "How does the use of tablets in elementary classrooms affect student engagement and learning outcomes?"

**Phase 4: Hypothesis Development**
- Propose tentative answers to your refined question
- Each hypothesis should be falsifiable
- Build a conceptual model that represents your hypothesis, illustrating how the system is expected to behave

**Phase 5: Evidence Gathering**
- Design methods to test your hypothesis
- Collect data systematically
- Document your reasoning at every step

**Phase 6: Synthesis**
- Integrate findings across all evidence sources
- Go beyond summarizing individual sources -- generate understanding of what the body of research offers collectively
- Identify where evidence converges and diverges

**Phase 7: Conclusion and Iteration**
- State what you found and what confidence level you have
- Identify limitations and open questions
- The conclusion often becomes the starting point for the next chain

### The "PICO" Framework (for structured questions)

Originally from evidence-based medicine, broadly applicable:
- **P**opulation: Who/what are you studying?
- **I**ntervention: What action or variable are you examining?
- **C**omparison: What are you comparing it against?
- **O**utcome: What effect are you measuring?

---

## 4. Chain of Thought Prompting with AI

### The Original CoT Research

Chain-of-thought prompting was formalized by Jason Wei et al. (2022) in the paper "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." The key finding: generating a series of intermediate reasoning steps significantly improves LLMs' ability to perform complex reasoning. This works because the model is forced to show its work rather than jumping to a conclusion.

### Current State (2025-2026)

The landscape has shifted significantly:

- **Reasoning-native models** (Claude's extended thinking, OpenAI's o-series) now include step-by-step reasoning as a built-in capability
- **Manual CoT prompting** is still useful but less critical than it was in 2023
- **Extended thinking** (Claude) and **adaptive thinking** automate the process, with the model deciding when and how much to reason
- The new pattern is **Role-Context-Constraint-Format (RCCF)** rather than manually asking for step-by-step reasoning

### Practical Techniques for Research with AI

**Basic CoT prompt:**
```
Think through this step by step before giving your answer:
[your question]
```

**Structured research prompt with XML tags (Claude-optimized):**
```xml
<context>
I am researching [topic]. Here is what I know so far:
[your current understanding]
</context>

<task>
Analyze [specific aspect]. Consider:
1. What evidence supports this?
2. What evidence contradicts this?
3. What assumptions am I making?
4. What alternative explanations exist?
</task>

<format>
Structure your response as:
- Current evidence assessment
- Competing hypotheses
- Gaps in the evidence
- Recommended next steps
</format>
```

**Self-correction chain (multi-pass):**
1. Generate a draft analysis
2. Have Claude review it against specific criteria
3. Have Claude refine based on the review
This mirrors the academic peer-review process.

**Competing hypotheses prompt:**
```
Search for this information in a structured way. As you gather data,
develop several competing hypotheses. Track your confidence levels.
Regularly self-critique your approach and plan. Update a hypothesis
tree or research notes file.
```

### When NOT to Use Manual CoT

- Simple factual lookups
- Tasks that modern reasoning models handle natively
- When you need speed over depth
- When the model is already producing high-quality output without it

---

## 5. Thinking in Writing

### Paul Graham: "Putting Ideas into Words"

Graham's central argument: writing is not merely the transcription of pre-formed ideas -- writing IS the thinking process itself. Key claims:

- "Half the ideas that end up in an essay will be ones you thought of while you were writing it"
- When you try to put ideas into words, a missing idea creates a sort of vacuum that draws it out of you
- There is "a kind of thinking that can only be done by writing"
- Writing is stricter than conversation because it demands "a single, optimal sequence of words" without tone or gesture to fill gaps
- "No one who hasn't written about a topic has fully formed ideas about it"

**Practical implication:** If you want to develop an idea, write about it. Don't wait until the idea is "ready" -- the writing itself is what makes it ready.

### The Feynman Technique

Named after physicist Richard Feynman, this is a four-step process for deep understanding:

1. **Teach it to a child:** Write everything you know about a subject as if explaining to a 12-year-old. Use simple language, no jargon. "If you can't clearly and simply define the words and terms you are using, you don't really know what you're talking about."
2. **Identify gaps:** Where does your explanation struggle or feel unclear? Return to source materials to fill these knowledge holes.
3. **Organize and simplify:** Arrange your notes into a coherent narrative. Read it aloud. Iterate until it flows naturally.
4. **Transmit (optional):** Share with someone unfamiliar. Their questions deepen your understanding further.

### Rubber Duck Debugging

From *The Pragmatic Programmer* by Andy Hunt and Dave Thomas: the act of explaining a problem step by step -- even to an inanimate object -- forces you to build a clear mental model, which often reveals the solution.

**Why it works:** When you verbalize something, your brain has to construct a coherent narrative. The gaps between what you think you know and what you can actually articulate become visible.

### The Common Thread

All three approaches share one principle: **externalizing thought through language creates clearer thinking and deeper understanding.** The medium forces precision. You cannot hide behind vague intuitions when you must commit words to paper (or screen).

### Practical Writing-as-Thinking Workflow

1. **Freewrite for 10 minutes** on your topic (no editing, no judgment)
2. **Read what you wrote** and identify the one sentence that surprised you
3. **Expand that sentence** into a paragraph, forcing yourself to be specific
4. **Challenge every claim** in the paragraph: How do I know this? What's my evidence?
5. **Rewrite** incorporating the challenges
6. **Repeat** until you've reached genuine clarity

---

## 6. Mind Mapping vs. Linear Chains

### Linear Thinking

Linear thinking processes information in logical, ordered steps: A leads to B, which leads to C. It activates the brain's left hemisphere, particularly the prefrontal cortex responsible for analytical reasoning and logical sequencing.

**Best for:**
- Well-defined problems with clear steps
- Sequential processes and procedures
- Mathematical derivations
- Cause-and-effect analysis
- Implementation planning
- Writing final drafts

### Mind Mapping

Mind mapping reflects how neurons actually connect -- in radiant, associative networks. A central concept branches outward, with related ideas forming sub-branches. This activates right-hemisphere areas involved in spatial relationships and creative connections.

**Best for:**
- Open-ended exploration with multiple possible directions
- Brainstorming and ideation
- Understanding relationships between disparate concepts
- Literature review organization
- Early-stage research when the question isn't yet clear
- Studying and memorizing complex topics

### Research Evidence

- Mind mapping improves learning by 10-15% compared to conventional study techniques
- Memory improvements of up to 32% compared to lists
- The combination of visual and verbal processing strengthens encoding

### The Hybrid Approach (Recommended)

The most effective problem-solvers switch between approaches:

1. **Start with a mind map** to capture the big picture and all associations
2. **Identify clusters** of related ideas in the map
3. **Convert clusters to linear chains** for deeper analysis
4. **Return to the map** when you get stuck or need new connections
5. **End with linear writing** to produce the final output

### Decision Framework

Ask yourself: "Am I solving a well-defined problem with clear steps (use linear), or exploring an open-ended challenge with multiple possible solutions (use mind mapping)?"

---

## 7. Academic Research Methodologies

### Systematic Literature Review (SLR)

A rigorous, reproducible method for finding and synthesizing all relevant research on a question.

**Steps:**
1. Define research question (using PICO or similar framework)
2. Develop search strategy (databases, keywords, inclusion/exclusion criteria)
3. Search systematically across multiple databases
4. Screen titles and abstracts
5. Full-text review of remaining papers
6. Quality assessment of included studies
7. Data extraction
8. Synthesis (narrative, meta-analysis, or thematic)
9. Report findings following PRISMA guidelines

**When to use:** When you need comprehensive, unbiased coverage of existing evidence on a specific question.

### Grounded Theory

Theory generation from data through an inductive approach. The researcher develops theory that is "grounded" in systematically collected and analyzed data.

**Key processes:**
- **Open coding:** Break data into discrete concepts
- **Axial coding:** Relate codes to each other, finding categories and subcategories
- **Selective coding:** Identify a core category that integrates all others
- **Constant comparison:** Continuously compare new data against emerging theory
- **Theoretical sampling:** Let emerging theory guide what data to collect next
- **Memo writing:** Document your analytical thinking throughout

**When to use:** When there's no existing theory to test, or when existing theories don't adequately explain the phenomenon.

### Thematic Analysis

Identifying, analyzing, and reporting patterns (themes) within data. Known for its flexibility.

**Steps (Braun & Clarke's 6-phase process):**
1. Familiarization with the data
2. Generating initial codes
3. Searching for themes
4. Reviewing themes
5. Defining and naming themes
6. Producing the report

**Key distinction from Grounded Theory:** Thematic analysis is not tied to theory generation. It can be used within any epistemological framework (realist, constructionist, critical). Grounded theory is explicitly linked to generating new theory.

### Thematic Synthesis (for systematic reviews of qualitative research)

Combines systematic review rigor with thematic analysis:
1. Line-by-line coding of primary study findings
2. Development of "descriptive themes"
3. Generation of "analytical themes" (going beyond what primary studies reported)

---

## 8. Tools and Techniques

### Concept Mapping

Visual representation of relationships between concepts. Unlike mind maps (which radiate from a center), concept maps can have multiple hubs and cross-links.

**How to create:**
1. List key concepts
2. Rank from most general to most specific
3. Connect with labeled arrows showing relationships ("causes," "requires," "contradicts")
4. Add cross-links between different branches
5. Review and revise

**Tools:** CmapTools, draw.io, Miro, even pen and paper

### Argument Mapping

Visual representation of argument structure using the Toulmin model or similar framework.

**Toulmin Model components:**
- **Claim:** What you're arguing
- **Grounds (Data):** Evidence supporting the claim
- **Warrant:** The reasoning that connects data to claim (why does this evidence support this claim?)
- **Backing:** Support for the warrant itself
- **Qualifier:** Degree of certainty ("probably," "in most cases")
- **Rebuttal:** Conditions under which the claim might not hold

**Practical steps for argument mapping:**
1. Identify the core claim
2. List all supporting evidence (grounds)
3. Make the warrant explicit -- why does this evidence support this claim?
4. Identify potential rebuttals
5. Assess whether the warrant needs additional backing
6. Add qualifiers based on strength of evidence

**Tools:** Rationale (argumentation software), MindMup, Kialo, or manual diagramming

### Research Logs

A written record of what you did, why, and what you learned.

**Structure for a research log entry:**
- Date and time
- What question am I working on?
- What did I do? (methods, sources consulted)
- What did I find?
- What surprised me?
- What questions emerged?
- What should I do next?

**Why it matters:** Research logs create an audit trail of your thinking, making it possible to retrace your reasoning chain. They also surface patterns you wouldn't notice otherwise.

### SWOT Analysis for Research Positions

- **Strengths:** What evidence strongly supports this position?
- **Weaknesses:** Where is the evidence thin or contradictory?
- **Opportunities:** What unexplored angles could strengthen this?
- **Threats:** What findings could undermine this position?

---

## 9. Obsidian + Chain of Thought: Externalized Reasoning Chains

### The Zettelkasten Method in Obsidian

The Zettelkasten ("slip box") method, developed by sociologist Niklas Luhmann (who published over 70 books and 400 articles using it), focuses on connections between atomic ideas rather than organizing by topic.

**Core principles:**
- **One note, one idea** (atomic notes)
- **Rewrite in your own words** (forces understanding, like the Feynman technique)
- **Link abundantly** -- every note should link to related notes
- **Let structure emerge** from links rather than imposing it top-down

### Practical Obsidian Workflow for Research

**Step 1: Capture (Literature Notes)**
- When reading a source, create a literature note
- Summarize key findings in your own words
- Tag with `#toread`, `#processing`, or `#processed`

**Step 2: Distill (Atomic/Permanent Notes)**
- Extract individual ideas from literature notes
- Each permanent note = one idea, stated clearly
- Link back to the source note
- Link to related permanent notes
- Example: Reading about CoT prompting, you create separate notes for "CoT improves arithmetic reasoning," "CoT only works at scale (100B+ parameters)," "Zero-shot CoT uses 'Let's think step by step'"

**Step 3: Connect (Maps of Content)**
- Create MOC notes that serve as hubs
- A MOC links to all relevant atomic notes on a theme
- MOCs are not fixed -- they evolve as you add notes
- Example: `[[Research Methodology MOC]]` links to notes on grounded theory, thematic analysis, systematic reviews, etc.

**Step 4: Develop (Reasoning Chains)**
- Create "argument notes" that link atomic notes in sequence
- Structure: Claim note -> Evidence note 1 -> Evidence note 2 -> Warrant note -> Conclusion note
- This creates an externalized chain of thought that you can revisit and refine

**Step 5: Produce (Output)**
- When writing a paper or essay, your MOCs serve as outlines
- The atomic notes provide pre-written building blocks
- The links show you which ideas connect and where gaps remain

### Obsidian Plugins for Research

- **Dataview:** Dynamic queries across your vault (auto-updating MOCs)
- **Templater:** Consistent note structures
- **Citations/Zotero integration:** Academic reference management
- **Canvas:** Visual arrangement of notes (like a digital corkboard)
- **Graph view:** Visualize connections across your entire vault

### Example: Building a Research Chain in Obsidian

Starting with a vague idea "I think education technology isn't being used well":

```
[[EdTech Observations]] (fleeting note)
  -> links to [[Literature: Cuban 2001 - Oversold and Underused]]
  -> links to [[Literature: Selwyn 2016 - Digital Skepticism]]
  -> leads to atomic note [[EdTech adoption often prioritizes tools over pedagogy]]
  -> links to [[Teachers lack training in pedagogical integration of tech]]
  -> links to [[Technology determinism in education policy]]
  -> these converge in [[MOC: EdTech Implementation Gaps]]
  -> which generates research question:
     [[RQ: How do teachers' pedagogical beliefs mediate their adoption of educational technology?]]
```

Each note in this chain is a reasoning step. The links are the logical connections. The entire chain is inspectable, revisitable, and modifiable.

---

## 10. Practical Examples: From Vague Idea to Research Question

### Example 1: Personal Observation to Research Question

**Starting point:** "Students seem bored in class"

**Step 1 -- Freewrite (5 minutes):**
"I notice that when the teacher lectures for more than 20 minutes, students start checking phones. But when there's a discussion, they seem more engaged. Is it the format? The topic? The time of day? Some students are always engaged regardless. What makes them different?"

**Step 2 -- Identify the surprise:**
"Some students are always engaged regardless." This is interesting -- what's different about them?

**Step 3 -- Preliminary literature search:**
Discover concepts like "intrinsic motivation," "self-determination theory," "student engagement," "autonomy-supportive teaching"

**Step 4 -- Apply Socratic questioning:**
- What do I mean by "bored"? -> Disengaged, not paying attention, not participating
- How do I know they're bored vs. processing internally? -> I don't. I'm inferring from behavior.
- What assumptions am I making? -> That visible participation = engagement. That lecture = boring.
- What would someone who disagrees say? -> "Some students learn best by listening quietly."

**Step 5 -- Narrow using PICO:**
- P: Undergraduate students in lecture-based courses
- I: Autonomy-supportive teaching practices (choice, rationale, acknowledgment)
- C: Traditional lecture without autonomy support
- O: Self-reported engagement and behavioral indicators

**Step 6 -- Final research question:**
"How do autonomy-supportive teaching practices affect undergraduate student engagement in lecture-based university courses?"

### Example 2: Theoretical Interest to Research Question

**Starting point:** "Chain of thought seems important for both AI and humans"

**Step 1 -- Mind map the territory:**
Central concept: "Chain of Thought." Branches: AI prompting, Socratic method, writing as thinking, Descartes' method, problem decomposition, metacognition, scaffolding in education, think-alouds in reading

**Step 2 -- Identify an interesting cluster:**
Three branches converge: "think-alouds in reading," "scaffolding in education," and "AI CoT prompting." They all involve making invisible reasoning visible.

**Step 3 -- Literature dive:**
Find that think-aloud protocols have decades of research in reading comprehension. Find that CoT prompting was inspired by showing worked examples. Find that Vygotsky's scaffolding theory emphasizes making expert thinking visible.

**Step 4 -- Apply the Toulmin model:**
- Claim: Making reasoning visible improves learning
- Grounds: Think-aloud research, CoT prompting results, scaffolding theory
- Warrant: Learners need models of expert reasoning to develop their own
- Rebuttal: Some research shows that excessive scaffolding creates dependency
- Qualifier: "In many cases" rather than "always"

**Step 5 -- Refine:**
"Under what conditions does making reasoning processes visible (through think-alouds, worked examples, or AI-generated chains of thought) improve vs. hinder independent reasoning ability in university students?"

### Example 3: Applied Problem to Research Design

**Starting point:** "I want to use AI in my research but I don't know if it helps"

**Step 1 -- Define "helps":**
Faster literature review? Better question formulation? More comprehensive analysis? Reduced bias? Write down all possible meanings.

**Step 2 -- Pick one and go deep:**
"Does using AI-generated chain-of-thought prompts help students develop better research questions?"

**Step 3 -- Design a chain of evidence:**
1. Define what a "good" research question looks like (use FINERMAPS criteria)
2. Have two groups: one develops questions with AI CoT assistance, one without
3. Blind evaluation of resulting questions by faculty
4. Interview participants about their reasoning process
5. Compare quality scores and reasoning patterns

**Step 4 -- Anticipate objections:**
- "Maybe the AI just writes the question for them" -> Design the intervention so AI asks probing questions rather than generating questions
- "Novelty effect" -> Use a longer intervention period
- "Self-selection bias" -> Random assignment

---

## Summary: A Meta-Chain of Thought

The chain of thought through this entire document follows its own logic:

1. **What is chain of thought?** (Definition and history)
2. **How do we question our own thinking?** (Socratic method)
3. **How do we structure the reasoning?** (Research framework)
4. **How do we use AI as a reasoning partner?** (CoT prompting)
5. **How does externalizing thought create clarity?** (Writing as thinking)
6. **When should we branch vs. go linear?** (Mind mapping vs. chains)
7. **What formal methods exist?** (Academic methodologies)
8. **What tools help us?** (Argument mapping, Toulmin, research logs)
9. **How do we build persistent reasoning systems?** (Obsidian + Zettelkasten)
10. **What does it look like in practice?** (Worked examples)

Each section builds on the previous ones. The entire document is itself a chain of thought about chains of thought.

---

## Sources

- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (Wei et al., 2022)](https://arxiv.org/abs/2201.11903)
- [What is Chain of Thought (CoT) Prompting? -- IBM](https://www.ibm.com/think/topics/chain-of-thoughts)
- [Google Research: Language Models Perform Reasoning via Chain of Thought](https://research.google/blog/language-models-perform-reasoning-via-chain-of-thought/)
- [Chain-of-Thought Prompting -- Prompt Engineering Guide](https://www.promptingguide.ai/techniques/cot)
- [Socratic Method -- Wikipedia](https://en.wikipedia.org/wiki/Socratic_method)
- [The Socratic Method: Fostering Critical Thinking -- Colorado State University](https://tilt.colostate.edu/the-socratic-method/)
- [Dialectic -- Wikipedia](https://en.wikipedia.org/wiki/Dialectic)
- [Putting Ideas into Words -- Paul Graham](https://paulgraham.com/words.html)
- [The Feynman Learning Technique -- Farnam Street](https://fs.blog/feynman-learning-technique/)
- [Writing is a Thinking Tool -- Ness Labs](https://nesslabs.com/writing-thinking-tool)
- [The Feynman Technique, Rubber Duck Debugging, and Pseudocode](https://medium.com/@enriquecoscarelli/the-feynman-technique-rubber-duck-debugging-and-pseudocode-d1a385573c6f)
- [Mind Thinking: Mind Mapping vs Linear Approaches -- Ahead App](https://ahead-app.com/blog/mindfulness/mind-thinking-mind-mapping-vs-linear-approaches-for-better-problem-solving)
- [Linear vs. Non-Linear Thinking -- Mind-Map.com](https://mind-map.com/whats-wrong-with-lists/)
- [Mastering Argument Mapping -- Number Analytics](https://www.numberanalytics.com/blog/ultimate-guide-argument-mapping)
- [Toulmin Argument -- Purdue OWL](https://owl.purdue.edu/owl/general_writing/academic_writing/historical_perspectives_on_argumentation/toulmin_argument.html)
- [Grounded Theory Research: A Design Framework for Novice Researchers](https://pmc.ncbi.nlm.nih.gov/articles/PMC6322175/)
- [Thematic Analysis vs. Grounded Theory -- ATLAS.ti](https://atlasti.com/guides/thematic-analysis/thematic-analysis-grounded-theory)
- [Methods for Thematic Synthesis of Qualitative Research in Systematic Reviews](https://pmc.ncbi.nlm.nih.gov/articles/PMC2478656/)
- [How to Organize Research Notes with Obsidian -- Obsibrain](https://www.obsibrain.com/blog/how-to-organize-research-notes)
- [Getting Started with Zettelkasten in Obsidian](https://obsidian.rocks/getting-started-with-zettelkasten-in-obsidian/)
- [Maps of Content (MoC): The Complete Guide for PKM](https://www.dsebastien.net/2022-05-15-maps-of-content/)
- [Formulation of Research Question -- Stepwise Approach (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6322175/)
- [From Ideas to Studies: How to Get Ideas and Sharpen Them (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5846748/)
- [Writing Strong Research Questions -- Scribbr](https://www.scribbr.com/research-process/research-questions/)
- [Descartes' Method -- Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/descartes-method/)
- [Claude Prompt Engineering: Chain of Thought](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-of-thought)
- [Reflective Journals and Learning Logs -- Northern Illinois University](https://www.niu.edu/citl/resources/guides/instructional-guide/reflective-journals-and-learning-logs.shtml)
- [Reflexive Journals in Qualitative Research -- Quirkos](https://www.quirkos.com/blog/post/reflexive-journals-in-qualitative-research/)
