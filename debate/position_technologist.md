# Position Paper: Academic Integrity and AI Fraud — A Technology Expert's Assessment

**Author perspective:** Senior AI researcher / ML systems architect — background in LLM internals, detection theory, and EdTech infrastructure. Think someone who has read arXiv:2301.10226 carefully and has also shipped production ML systems that affect millions of users.

**Date:** April 2026

---

## 1. Framing: Why Technical Rigor Matters Here

The conversation around AI and academic integrity has a problem: it is dominated by two groups who are not technically qualified to set the terms of debate. The first group is the integrity traditionalists, who treat AI detection as a solved problem and reach for Turnitin the way a carpenter reaches for a familiar hammer. The second group is the breathless AI optimists, who claim LLMs will revolutionize education while waving away the fraud problem as a footnote. Neither group has read the underlying papers. Neither group has thought carefully about what "detection" means as a statistical inference problem.

This paper is written from the perspective of someone who has. I will be precise about what current technology can and cannot do. I will be clear about what interventions I endorse and what I reject. I will not hand-wave.

The framing device I find most useful comes from Rose Luckin's *Machine Learning and Human Intelligence* (UCL IOE Press, 2018): Luckin distinguishes between the **algorithmic mind** (systematic, pattern-matching, accurately rule-following) and the **rational mind** (metacognitive, self-regulating, capable of directed motivation and genuine understanding). AI systems are extremely good at the former and structurally incapable of the latter. This distinction is not merely philosophical — it has direct engineering consequences for how we design both assessments and detection systems.

---

## 2. Technical State of the Art: What AI Detection Tools Actually Do

Let me be precise about the underlying mechanisms.

### 2.1 Perplexity-Based Detection

Tools like GPTZero (launched January 2, 2023, by Edward Tian, Princeton) and Turnitin AI Detection (launched April 2023) operate on a fundamentally simple signal: **perplexity and burstiness**. Perplexity measures how well a language model predicts each successive token given its context. LLMs, by design, generate text by sampling from high-probability distributions — their output is, on average, more predictable than human prose. Burstiness measures variance in sentence-level complexity; human writing has high variance (alternating complex and simple sentences), while LLM output tends toward uniform complexity.

This is the full technical story. The rest is feature engineering layered on top of these two signals.

### 2.2 The Liang et al. Finding: 61.3% False Positive Rate

In April 2023, Weixin Liang, Mert Yuksekgonul, Yining Mao, Eric Wu, and James Zou at Stanford HAI published arXiv:2304.02819 (later appearing in *Patterns*, Cell Press, doi:10.1016/j.patter.2023.100779). They tested seven popular AI detectors — including GPTZero, Turnitin, Copyleaks, Writer, ZeroGPT, Sapling, and Crossplag — against two corpora: TOEFL essays written by Chinese college students (legitimate human writing by non-native English speakers) and US 8th-grade student writing.

The result: **61.3% of TOEFL essays were flagged as AI-generated**. Only 1.5% of native-speaker essays received false positives. This is not a small rounding error. This is a systematic 40-fold disparity in false positive rates between native and non-native English writers.

The reason is mechanistically clear: ESL writers tend toward simpler, more uniform sentence structures, lower lexical diversity, and more predictable word choices — precisely the statistical fingerprint that perplexity-based detection interprets as AI authorship. The detector is not detecting AI; it is detecting non-native English proficiency.

This finding directly caused Vanderbilt University to disable Turnitin AI detection in 2023. Northwestern, Michigan State, and UT Austin followed. GPTZero's marketing claims a 0.24% false positive rate. The empirically measured rate on TOEFL essays is 250 times higher. This gap between vendor claims and empirical measurement is not a product liability edge case — it is the central fact that any serious institutional deployment must reckon with.

### 2.3 Turnitin's Real-World Performance

Turnitin claimed 98% accuracy at launch. The Washington Post's independent testing in 2023 found approximately 50% accuracy. The discrepancy between 98% and 50% is large enough that at least one of these numbers is not describing the same task. Turnitin's 98% figure likely reflects performance on clean, unedited AI output in a controlled evaluation set. The Washington Post's 50% figure likely reflects real-world conditions: human-edited AI content, AI-assisted (not AI-generated) writing, and the diversity of legitimate student prose.

Neither number is wrong; they are measuring different things. The problem is that Turnitin marketed the controlled evaluation figure to institutions making enforcement decisions under real-world conditions.

---

## 3. Why Detection Is Fundamentally Hard: A Statistical Argument

There is a deeper reason why AI detection tools fail, beyond the specific engineering choices made by GPTZero or Turnitin. It is a fundamental statistical argument.

**The detection task is to classify a text as human-written or AI-generated based on surface features.** The adversarial surface this creates is not merely practical — it is mathematical. Any classifier that uses statistical features of text to make this determination is exploiting the fact that the two distributions (human writing distribution and AI-generated text distribution) are imperfectly separated in feature space.

The problem: **these distributions are converging**. As LLMs are trained on more human text, they produce output that is statistically closer to human writing. As human writers are exposed to more AI-generated text (and often use AI for drafting and editing), their own writing moves toward patterns the model learned from AI. By 2025-2026, we are in a regime where the distributional overlap is substantial enough that reliable binary classification is not achievable with surface-level features.

### 3.1 Paraphrasing Attacks

Liang et al. also showed that a simple prompt instruction — "elevate the writing" — caused ChatGPT output to evade detection at greater than 90% success rate. This is a paraphrasing attack: the AI rewrites its own output to shift the perplexity distribution. An adversarially motivated student does not need to know anything about perplexity or burstiness to defeat detection. They need only know to ask the AI to rewrite its output in a different style.

More sophisticated attacks exist: translation chains (generate in English, translate to French, translate back), adversarial token substitution (replace high-probability tokens with synonyms), and deliberate introduction of grammatical errors. The arms race dynamic is real, and the asymmetry is unfavorable to detection: the defender must maintain high accuracy across all inputs; the attacker needs only find one evasion pathway.

### 3.2 Humanization Tools

Commercial products like Undetectable.ai, HIX.AI, and Quillbot are specifically engineered to defeat detection signals. They retrain against the outputs of GPTZero and Turnitin. This is the practical instantiation of the adversarial dynamic — tools explicitly designed to exploit the known weaknesses of detection classifiers. A student who knows about these tools has a systematic advantage over any detection system. The marginal cost of evasion approaches zero.

---

## 4. LLM Watermarking: The Right Idea, Facing the Wrong Incentives

If perplexity-based detection is fundamentally unreliable, the technically correct solution is **provenance-based verification**: embed a cryptographic signal in AI-generated text at generation time, enabling downstream verification without relying on surface statistical features.

Two serious academic schemes exist.

### 4.1 Kirchenbauer et al. — Green/Red Token Lists (arXiv:2301.10226, ICML 2023)

The University of Maryland team's approach (Kirchenbauer, Geiping, Wen, Kirchenbauer, Goldstein) is conceptually elegant. At generation time, the LLM applies a pseudorandom function seeded by the preceding token to partition the vocabulary into a "green list" (~50% of tokens) and a "red list." The decoding process is biased toward green-list tokens via a logit bias delta (typically 1.0–2.0). Detection requires only the same pseudorandom seed function and a z-score test on the green token fraction. Detection is achievable after approximately 200 tokens at p < 0.0001.

Critically, this approach does not require model access for detection — only the seed function. It has no false positive rate in the traditional sense: a human-written text cannot contain the watermark signal because no LLM applied the bias during generation.

The technical limitations are real: paraphrase attacks (copying into a second LLM) can remove the watermark by sampling from a fresh distribution; quality degrades at high delta values; multilingual texts see reduced effectiveness; short texts (under 200 tokens) have insufficient statistical power for detection.

### 4.2 Aaronson/OpenAI — Gumbel Softmax Distortion-Free Scheme

Scott Aaronson (UT Austin, then working at OpenAI) developed a complementary approach using Gumbel softmax noise sampling. The "distortion-free" property means the watermark does not change the statistical distribution of the output — only the specific token choices. This is theoretically superior: the output looks identical to an unwatermarked model's output from a distributional perspective, but the specific realization encodes a detectable signal.

In August 2023, Aaronson disclosed that he had built a functional watermarking system for OpenAI, but OpenAI chose not to deploy it. The stated reason: **competitive disadvantage**. If OpenAI watermarks its outputs but Google and Anthropic do not, then OpenAI's AI-generated text is uniquely identifiable while competitors' AI-generated text evades detection. This creates a perverse incentive structure where the responsible actor is penalized for transparency.

This is the collective action problem at the heart of watermarking. It is not a technical problem — the technology works. It is a market structure problem that requires regulatory intervention to resolve.

### 4.3 What Watermarking Can and Cannot Do

If universally deployed by all major commercial LLMs, watermarking would:
- Eliminate false positives against ESL writers (human text cannot contain the signal)
- Provide cryptographic-grade attribution rather than probabilistic inference
- Enable a "disclosure and attribution" framework for AI-assisted work in education

What watermarking cannot do, even under ideal deployment:
- Detect AI use when the LLM does not implement watermarking. Open-source models (Llama, Mistral, Qwen) cannot be forced to watermark — any student with a GPU can run an unwatermarked local model
- Survive heavy paraphrasing or translation attacks
- Detect the case where a student reads AI output and reproduces it from memory
- Prevent contract cheating by human ghost-writers

Google DeepMind's SynthID is deployed for AI-generated images and audio but as of 2025-2026 has not been extended to text at production scale. This remains the most concrete near-term candidate for a production watermarking deployment.

---

## 5. The Arms Race: Technical Escalation Analysis

The pattern of escalation in this domain follows a predictable dynamic: detection capability advances, evasion tools emerge within months, detection tools update, evasion tools update, repeat. This is the same dynamic as spam filtering, anti-virus detection, and content moderation.

The structural difference in the academic integrity context is that the stakes are asymmetric: a false accusation of fraud is a catastrophic harm to a student (grade penalty, misconduct proceedings, reputational damage, psychological harm). A missed detection of genuine fraud is a significant but recoverable institutional problem. This asymmetry means that systems operating at 50-60% accuracy with documented disparity in false positive rates across student populations should not be used for enforcement decisions.

The honest technical assessment is that the detection arms race currently favors evasion. The tools for evading detection are commercially available, cheap, and require no technical sophistication from users. The detection tools are expensive, institutionally deployed, and demonstrably producing systematic false positives against already-marginalized student populations. This is not a temporary lag that will be resolved by better detection algorithms — it reflects a fundamental mathematical constraint on the classification task.

---

## 6. What Actually Works Technically

Assessment redesign, not detection escalation, is the technically sound response to AI fraud. The following approaches address the problem at the source rather than through unreliable post-hoc inference.

### 6.1 Oral Defense / Spot Viva

Oral defense (viva voce) authenticates the **person** rather than the **product**. An LLM cannot sit in a room and answer follow-up questions. A student who submitted AI-generated work cannot explain the methodological choices, the reasoning chain, or the implications of their own submission under direct questioning by a competent examiner.

The "spot viva" model — randomly sampling 10–20% of written submissions for a 15–20 minute oral follow-up — is scalable. For a cohort of 300 students, 10% sampling requires approximately 10 hours of examiner time per assessment cycle. This is significant but not prohibitive.

Critically, oral defense has **no false positive rate** when the examiner is competent. The asymmetry is reversed relative to detection tools: it is harder for a cheating student to convincingly defend work they did not engage with than it is for an honest student to explain their own work. University of Western Ontario implemented oral exams at scale for an undergraduate business cohort of approximately 600 students in 2023–2024. Coursera launched an "AI-based Viva Exam" feature in June 2024.

Luckin's framework in *Machine Learning and Human Intelligence* provides the theoretical grounding for why oral defense works: it tests the **rational mind** — metacognitive knowledge, the ability to articulate relationships between concepts, self-regulated understanding — which is precisely what AI systems cannot replicate. Luckin writes that "AI systems cannot develop the accurate perceived self-efficacy that is needed to drive our education system." This is precisely what oral defense measures.

### 6.2 Process Verification

Document revision history (Google Docs activity tracking, version control timestamps, draft progression) is forensically interesting because it is difficult to fabricate retrospectively at scale. A student who submitted AI-generated text in a single paste event has a fundamentally different process fingerprint than a student who developed work through multiple editing sessions over days.

This is not a standalone detection mechanism — it requires contextual interpretation. But as one layer in a layered authentication system, it provides real information that pure product-based assessment does not.

### 6.3 Behavioral Biometrics and Metadata Analysis

Typing patterns, inter-keystroke timing, and interaction metadata can provide soft signals about whether a submission was typed or pasted. These signals are probabilistic and can be defeated by a sophisticated actor, but they raise the effort cost of fraud. Platforms like Century Tech have demonstrated that granular behavioral data (including mouse movements and keystrokes) can provide meaningful signals about learning engagement — the same data infrastructure could be applied to authentication.

### 6.4 Assessment Design for AI Resistance

Some assessment types are inherently more AI-resistant than others. Assignments requiring:
- Personal experience or situated knowledge ("describe a situation you encountered in your fieldwork")
- Real-time production ("complete this problem set during this supervised session")
- Synthesis of course-specific discussion ("apply the framework from Tuesday's lecture to the case study we analyzed in class")
- Local, contextual, or recent knowledge unavailable in LLM training data

...are systematically harder for AI to fulfill authentically. This is not about making assessments obscure; it is about aligning assessment design with what we actually want to measure.

---

## 7. What I Accept: Technically Credible Interventions

The following interventions have genuine technical merit and I endorse them:

**Oral defense and spot viva as primary authentication mechanisms for high-stakes work.** The technology here is human judgment and question design, not software. It is the most robust approach available and should be standard practice, not an exceptional measure.

**Process-based assessment — staged submissions, draft evidence, reflective journals.** These methods make the process of intellectual work visible, and visible processes are harder to fabricate than polished products.

**LLM watermarking advocacy at the policy level.** Institutions and governments should advocate for mandatory watermarking requirements for commercial LLM providers, framed under existing legal precedent (EU AI Act Article 50 on AI-generated content disclosure). This is the correct long-term technical solution. It requires regulatory coordination, not institutional unilateral action.

**AI detection tools as soft signals under a human-in-the-loop review process.** Used correctly — as one input among several that triggers a conversation with the student, never as standalone enforcement evidence — detection tools have a role. The required protocol: automated flag → instructor review → direct conversation with student → institutional decision. No grade penalty based on detection score alone.

**Bias auditing of any detection tool before institutional deployment.** This is technically straightforward: test the tool against a corpus of authentic writing from the specific student population before deployment. Any institution with a significant ESL population must audit ESL false positive rates specifically. This is due diligence, not optional.

**Assessment redesign as structural response.** Moving toward oral components, real-time production, and contextually situated tasks is the most durable response because it does not depend on the detection arms race reaching a favorable equilibrium.

---

## 8. What I Reject: Technically Illiterate Policies and Vendor Snake Oil

**Using AI detection tool scores as primary evidence in disciplinary proceedings.** Given documented false positive rates of 30–61% for ESL writers (Liang et al. 2023), mandating detection tools for enforcement decisions against ESL student populations constitutes foreseeable, systematic injustice. This is not an acceptable risk. Institutions that apply grade penalties or academic misconduct sanctions based solely on Turnitin AI Detection or GPTZero scores are operating below the evidentiary threshold that their own academic due process standards should require.

**Accepting vendor accuracy claims without independent audit.** Turnitin's claim of 98% accuracy versus the Washington Post's empirical finding of approximately 50% is the canonical case. A 48-point gap between vendor claim and independent measurement is not noise. Institutions that deploy tools based on vendor-provided accuracy figures without independent validation are not practicing institutional due diligence.

**Treating AI detection as a solved problem.** It is not. The academic literature (Liang et al. 2023; Weber-Wulff et al. 2023) is clear that current tools are unreliable, biased, and subject to trivial evasion. Administrators and policymakers who present detection deployment as a complete institutional response are not reading the evidence base.

**Mandating detection tools disproportionately affecting ESL students without accommodations or appeal processes.** For Vietnamese students writing in English on international programs, for Chinese graduate students writing dissertations in a second language, for any ESL population — deploying GPTZero or Turnitin AI Detection without explicit ESL-adjusted protocols and robust appeal mechanisms is discriminatory in effect, regardless of intent. The Liang et al. data make this foreseeable harm, not unintended consequence.

**Surveillance-as-integrity: continuous keystroke monitoring, always-on proctoring, behavioral monitoring with punishment rather than support as the default response.** Technologies that comprehensively monitor student behavior during assessment may reduce some forms of fraud at the cost of transforming the educational relationship from trust-based learning to adversarial surveillance. McCabe's 30-year longitudinal research demonstrates that honor-code cultures — built on trust, values communication, and community accountability — produce better long-term integrity outcomes than enforcement-first cultures. Surveillance architectures optimize for the wrong objective.

---

## 9. Red Lines: Technically Unacceptable Proposals

These are positions I will argue against under any framing:

**Red Line 1: Using tools with 60%+ ESL false positive rates as disciplinary evidence without explicit bias audit and ESL-specific accommodation.** This is not a matter of policy preference — it is a matter of evidentiary adequacy. An instrument with this false positive rate in the relevant population cannot meet the "reasonable grounds" threshold that academic misconduct proceedings are supposed to require.

**Red Line 2: Treating watermarking as currently deployable institutional policy.** Kirchenbauer et al. arXiv:2301.10226 (ICML 2023) and Aaronson's scheme exist in the research literature. Neither is deployed in production by any major LLM provider as of 2025-2026. Policies that reference watermarking as if it were currently operative are misrepresenting the technical landscape.

**Red Line 3: Blocking all AI use through technical restrictions as a substitute for assessment redesign.** Technical restrictions on AI access are security theater: any student with a smartphone has access to capable LLMs outside any institutional firewall. The correct response to capability proliferation is assessment design that makes AI substitution visible or irrelevant, not access restrictions that sophisticated users trivially bypass.

**Red Line 4: Applying any form of AI fraud sanction without first providing explicit AI use policy communication and AI literacy education.** Students cannot be held accountable to standards they were not clearly informed about. This is a basic principle of procedural justice, and it applies with particular force in a period when community norms around AI use are genuinely unsettled.

---

## 10. Future Technical Landscape: 2–5 Year Outlook

The 2–5 year horizon transforms several parameters of this problem.

**LLM capability will continue improving.** Models trained in 2027–2028 will produce output that is statistically even harder to distinguish from human writing. The distributional overlap problem discussed in Section 3 will worsen. Any detection approach that does not rely on provenance signals (watermarking) will become progressively less reliable as a function of model capability improvement.

**Open-source models will proliferate and become more capable.** Llama, Mistral, Qwen, and their successors are freely downloadable and can run on consumer hardware. No regulatory mandate for watermarking commercial LLMs will affect open-source models. By 2028, a motivated student will have access to locally-run, highly capable, uncheckable LLMs. This is not speculative — it is a direct extrapolation from the current trajectory of open-source model capability.

**Multi-modal generation will complicate assessment further.** Code generation, data analysis, image creation, and audio synthesis are all rapidly improving. Academic fraud is not limited to text essays. Assessment integrity frameworks built only around text detection are already incomplete.

**Watermarking may become a regulatory reality in some jurisdictions.** The EU AI Act's Article 50 disclosure requirements come into effect progressively through 2025–2026. China's Cyberspace Administration has already issued AI-generated content labeling requirements for Chinese AI providers. If major commercial LLMs are brought under mandatory watermarking requirements in key jurisdictions, this materially changes the detection landscape — though the open-source evasion problem remains.

**The correct policy response to this landscape:** Build assessment architectures that are robust to improvements in AI capability. Oral defense is not made less reliable by GPT-5 or GPT-6. Process verification is not defeated by better paraphrasing. Real-time production of contextually situated work is not undermined by more capable local models. The approaches that degrade gracefully in a world of improving AI are human-centered, process-oriented, and competency-testing — not statistical-inference-based detection.

---

## 11. Synthesis: A Technically Grounded Framework

Luckin's insight in *Machine Learning and Human Intelligence* is the right foundation: the goal of education is the development of human intelligence — specifically the **rational**, metacognitive, self-regulating capacities that AI cannot replicate. "AI systems cannot develop the accurate perceived self-efficacy that is needed to drive our education system." Assessment should measure these capacities directly.

When assessment is designed to measure genuine understanding, demonstrated in real time, by the specific person being evaluated, AI fraud becomes structurally difficult — not because AI capability is limited, but because the assessment task requires the human to show up and perform. Oral defense, real-time production, and situated knowledge testing are not anti-AI features; they are features of good assessment that happen to be AI-resistant.

The practical institutional framework I recommend:

1. **Tier 1 — Assessment Redesign:** All high-stakes assignments should include at least one component that requires real-time, situated, or oral demonstration of understanding. Spot viva sampling at 10–15% for large cohorts.

2. **Tier 2 — Process Evidence:** Require staged submissions with documented revision history for major written work. Not as surveillance, but as a normal part of academic work — just as scientists maintain lab notebooks.

3. **Tier 3 — Soft Detection, Human-in-the-Loop:** AI detection tools may be used as soft flags to trigger conversations, never as standalone enforcement. Require ESL bias audit before any institutional deployment. No grade consequences from detection scores alone.

4. **Tier 4 — Policy and Culture:** Explicit AI use policy communicated at the start of every course. AI literacy education as a prerequisite for AI use regulation. Honor-code culture development following McCabe's evidence base.

5. **Tier 5 — Long-Term Advocacy:** Advocate at institutional and government level for mandatory LLM watermarking requirements under data transparency regulations. Monitor Google SynthID and other production watermarking developments.

This is not a detection-escalation framework. It is a systems-design framework that builds authentication into the structure of learning rather than trying to recover it after-the-fact through unreliable inference.

---

## References

- Kirchenbauer, J., Geiping, J., Wen, Y., Kirchenbauer, M.S., Goldblum, M., & Goldstein, T. (2023). A watermark for large language models. *ICML 2023*. arXiv:2301.10226.
- Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J. (2023). GPT detectors are biased against non-native English writers. *Patterns (Cell Press)*. doi:10.1016/j.patter.2023.100779. arXiv:2304.02819.
- Luckin, R. (2018). *Machine Learning and Human Intelligence: The Future of Education for the 21st Century*. UCL IOE Press. ISBN 978-1-78277-251-4.
- Luckin, R., Holmes, W., Griffiths, M., & Corcier, L.B. (2016). *Intelligence Unleashed: An Argument for AI in Education*. Pearson / UCL Knowledge Lab.
- Aaronson, S. (2023). My OpenAI watermarking work. *Shtetl-Optimized* (blog), August 2023.
- Christ, M., Gunn, S., & Zamir, O. (2023). Undetectable watermarks for language models. arXiv:2306.09194.
- Eaton, S.E. (Ed.) (2024). *Second Handbook of Academic Integrity*. Springer.
- McCabe, D.L., Butterfield, K.D., & Treviño, L.K. (2012). *Cheating in College: Why Students Do It and What Educators Can Do about It*. Johns Hopkins University Press.
- EU Regulation 2024/1689 (EU AI Act), Articles 10 and 50.
- UNESCO (2023). *Guidance for Generative AI in Education and Research*. Paris: UNESCO.
- Weber-Wulff, D., et al. (2023). Testing of detection tools for AI-generated text. *International Journal for Educational Integrity*, 19(1), 26.
